"use strict";
const data=JSON.parse(document.getElementById("folio-data").textContent);
const report=document.getElementById("report-view"), materials=document.getElementById("materials-view"), evidence=document.getElementById("evidence-view"), preview=document.getElementById("preview");
const sources=new Map(data.sources.map(s=>[s.id,s])), items=new Map(data.evidence.map(e=>[e.id,e]));
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
let reportScroll=0;
document.getElementById("review-status").textContent=data.review;
for(const finding of data.findings){const note=document.createElement('p');note.className='trace';note.textContent=`Review ${finding.status}: ${finding.reason}`;document.getElementById('review-status').after(note);}
function safeLink(url){try{const parsed=new URL(url);return ["https:","http:"].includes(parsed.protocol)?url:""}catch{return ""}}
function availability(s){const url=safeLink(s.shared_url);return url?`<p><a href="${esc(url)}" rel="noopener noreferrer">Shared original</a> · recipient permissions apply</p>`:"<p class=trace>Original not attached. Locate or request it using the document identity and position.</p>"}
function route(){
  preview.hidden=true;
  const parts=location.hash.replace(/^#/,"").split("/");
  report.hidden=parts[0]!=="report"&&parts[0]!=="";
  materials.hidden=parts[0]!=="materials";
  evidence.hidden=parts[0]!=="evidence";
  document.getElementById("report-tab").setAttribute("aria-current",!report.hidden?"page":"false");
  document.getElementById("materials-tab").setAttribute("aria-current",!materials.hidden?"page":"false");
  if(!report.hidden){requestAnimationFrame(()=>scrollTo(0,reportScroll));return}
  if(parts[0]==="evidence"){
    const item=items.get(parts[1]);
    if(!item){evidence.innerHTML="<p>Evidence not found.</p><a href='#report'>Return to report</a>";return}
    const source=sources.get(item.source), unit=item.kind==="quote"?item.unit:item.kind==="calculation"?item.units[0]:(item.result.matched_units[0]||item.result.population_units[0]||"");
    const units=item.kind==="aggregate"?item.result.population_units:item.kind==="calculation"?item.units:[];
    const rowLinks=source.included&&units.length?`<p class=trace>Referenced units: ${units.map(id=>`<a href="#materials/${source.id}/${id}">${esc(id)}</a>`).join(' · ')}</p>`:"";
    evidence.innerHTML=`<div class=actions><a href="#report">Return to report · 본문으로</a></div><h2>Evidence ${esc(item.number||item.id)}</h2><p class=trace>${esc(item.trace)}</p><blockquote>${esc(item.display_text)}</blockquote>${item.context?`<p>${esc(item.context)}</p>`:""}${source.included?`<a href="#materials/${source.id}/${unit}">View original context · 원문 보기</a>`:availability(source)}${rowLinks}`;
    return;
  }
  if(parts[0]==="materials"){
    if(!parts[1]){
      materials.innerHTML=`<h2>Materials · 자료</h2>${data.sources.map(s=>`<article><a href="#materials/${s.id}">${esc(s.title)}</a><p class=trace>${esc(s.origin)} · ${s.included?`${s.units.length} recorded units included`:"Original not embedded"}</p></article>`).join("")||"<p>No materials supplied.</p>"}`;
      return;
    }
    const source=sources.get(parts[1]);
    if(!source){materials.innerHTML="<p>Material not found.</p>";return}
    materials.innerHTML=`<div class=actions><a href="#report">Return to report · 본문으로</a><a href="#materials">All materials</a></div><h2>${esc(source.title)}</h2><p class=trace>${esc(source.origin)} · ${source.included?"Recorded source snapshot included; see units below":"Original not embedded"}</p>${source.coverage?`<p class=trace>${esc(source.coverage)}</p>`:""}${source.included?source.units.map(u=>`<article id="unit-${u.id}" class="${u.id===parts[2]?"target":""}"><small>${esc(u.locator)}</small><div>${esc(u.text)}</div></article>`).join(""):availability(source)}`;
    if(parts[2])requestAnimationFrame(()=>document.getElementById("unit-"+parts[2])?.scrollIntoView());
  }
}
document.addEventListener("click",event=>{if(event.target.closest(".citation"))reportScroll=scrollY;});
document.addEventListener("mouseover",event=>{const link=event.target.closest(".citation");if(link){const item=items.get(link.dataset.evidence);preview.textContent=item?item.trace+"\n\n"+item.display_text:"";preview.hidden=!item;}});
document.addEventListener("mouseout",event=>{if(event.target.closest(".citation"))preview.hidden=true;});
document.addEventListener("focusin",event=>{const link=event.target.closest(".citation");if(link){const item=items.get(link.dataset.evidence);preview.textContent=item?item.trace+"\n\n"+item.display_text:"";preview.hidden=!item;}});
document.addEventListener("focusout",()=>preview.hidden=true);
window.addEventListener("hashchange",route);route();
