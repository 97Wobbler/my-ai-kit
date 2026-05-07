---
name: noethers-theorem
display_name: Noether's Theorem
class: model
underlying_class: native
domain: physics
source: Emmy Noether, "Invariante Variationsprobleme," Nachrichten der Königlichen Gesellschaft der Wissenschaften zu Göttingen, 1918
best_for:
  - Predicting conserved quantities in a physical system from its symmetries
  - Understanding why energy, momentum, and angular momentum are conserved
  - Identifying new conservation laws in unfamiliar Lagrangians
one_liner: "Every continuous symmetry of a system corresponds to a conserved quantity."
---

# Noether's Theorem

## Overview

Noether's Theorem claims that every continuous symmetry of a physical system's
action (its Lagrangian or Hamiltonian) corresponds to exactly one conserved
quantity. The theorem is deeply explanatory: it reveals *why* conservation laws
exist and *how to construct* them from first principles. Rather than treating
energy, momentum, and angular momentum as independent postulates, Noether's
Theorem shows they are mathematical consequences of translational and rotational
symmetry. The theorem is predictive — given a Lagrangian and its symmetries, you
can read off what is conserved. It applies to classical mechanics, field theory,
and quantum mechanics.

## Core Variables and Relationships

**The core claim:** If the action S = ∫ L(φ, ∂φ) d⁴x is invariant under a
continuous symmetry transformation φ(x) → φ(x) + εξ(x) (where ε is an
infinitesimal parameter and ξ is the generator), then there exists a conserved
current j^μ such that ∂_μ j^μ = 0. The conserved charge is Q = ∫ j⁰ d³x.

Key variables and their relationships:

1. **Symmetry type and generator ξ** → determines the form of the
   transformation.
   - Spacetime symmetries (translation, rotation, Lorentz boost)
   - Internal symmetries (phase rotations, flavor transformations, gauge
     symmetries)
   - Continuous (Lie group) vs. discrete symmetries; only continuous
     symmetries yield local conservation laws via Noether

2. **Lagrangian or action S** → determines what is conserved when the
   symmetry holds.
   - L depends on fields φ and their derivatives ∂_μφ
   - Kinetic terms (∂_μφ ∂^μφ) and potential terms V(φ) both constrain
     symmetries

3. **Action invariance** — the Lagrangian is invariant under the symmetry:
   L(φ', ∂φ') = L(φ, ∂φ) + total derivative.
   - If L is not invariant, the symmetry is broken and the conserved
     quantity vanishes (in the broken phase)

4. **Conserved current j^μ** — constructed directly from L and ξ:
   - j^μ = (∂L / ∂(∂_μφ_i)) · ξ^i (plus similar terms for all fields)
   - Conservation law: ∂_μ j^μ = 0 (continuity equation)

5. **Conserved charge Q** — the spatial integral of j⁰.
   - Time-independent: dQ/dt = 0
   - Physical interpretation depends on the symmetry:
     - Spacetime translation (time) → energy
     - Spacetime translation (space) → momentum
     - Rotation → angular momentum
     - Phase rotation → particle number, electric charge

The theorem is **universal**: the form of the conserved quantity depends only
on the symmetry, not on the details of the potential or coupling constants.

## Key Predictions

- **Energy is conserved in any system whose Lagrangian is independent of
  time.** This is not an assumption; it is a prediction from time-translation
  symmetry. If the Lagrangian explicitly depends on time (e.g., time-varying
  external field), energy is not conserved.

- **Momentum is conserved in any system invariant under spatial translation.**
  A uniform external field breaks translational symmetry and causes momentum
  to be non-conserved; a bound potential that depends on absolute position
  also breaks it.

- **Angular momentum is conserved in any rotationally invariant system.**
  The theorem predicts both orbital angular momentum (from spatial rotation)
  and spin angular momentum (from internal rotations of spinor fields), from
  the same principle.

- **Electric charge is conserved because the Lagrangian of the Standard Model
  is invariant under local U(1) phase rotations φ → e^{iα}φ.** The conserved
  current is the electromagnetic current j^μ. If the symmetry were broken
  (e.g., at very high energies in grand unified theories), charge conservation
  would fail — a testable prediction.

- **Broken symmetries give rise to non-conserved quantities with slow decay.**
  If a symmetry is approximate (nearly conserved) because the Lagrangian has
  a small symmetry-breaking term, the current is nearly conserved, and the
  associated charge decays only via the symmetry-breaking interaction. Example:
  strangeness in weak interactions, where the lifetime of strange particles is
  anomalously long because strangeness is conserved in the strong interaction.

- **In field theories with gauge symmetries, Noether's theorem predicts the
  existence of massless particles (gauge bosons).** The gauge symmetry implies
  a conserved current, and in a quantum field theory, massless particles are
  the excitations of the associated field.

## Application Procedure

Instantiate the theorem against a concrete physical system to predict what is
conserved.

1. **Define the system and write its Lagrangian (or Hamiltonian) explicitly.**
   What are the degrees of freedom φ? Do they depend on space, time, or both?
   What are the kinetic and potential terms? Write L or H in detail, not
   schematically.

2. **Identify the continuous symmetries of L.**
   - Spacetime symmetries: Is L invariant under time translation? Spatial
     translation? Rotation? Lorentz boost? (Test: does L change if you shift
     the origin or rotate the coordinates?)
   - Internal symmetries: Is L invariant under phase rotations of a complex
     field? Gauge transformations? (Test: does L change if you rotate the
     internal space without touching spacetime?)
   - Write down the generator ξ for each symmetry — the infinitesimal
     transformation that leaves L invariant.

3. **For each symmetry, construct the conserved current j^μ.**
   - Use the formula: j^μ = (∂L / ∂(∂_μφ)) · ξ
   - Verify that ∂_μ j^μ = 0 (this is automatic if the symmetry holds).

4. **Compute the conserved charge Q = ∫ j⁰ d³x.**
   - This integral often reduces to a simple physical quantity (energy,
     momentum, angular momentum, particle number) once you interpret j⁰.
   - Check dimensions: does Q have the right units?

5. **Predict the physical consequence.**
   - Is Q conserved in the system? Will dQ/dt = 0?
   - If the symmetry is exact, Q is exactly conserved. If the symmetry is
     approximate (small symmetry-breaking terms in L), Q is nearly conserved
     and decays on a slow timescale.

6. **Check boundary conditions** (see below). If any apply, flag that
   Noether's prediction may be incomplete or require modification.

## Boundary Conditions

Noether's Theorem applies rigorously to systems described by a Lagrangian
with continuous symmetries. It breaks down or requires modification when:

- **The system has a boundary or is finite in size.** Noether's derivation
  assumes spacetime is infinite and fields vanish at infinity. In finite
  systems (e.g., a particle in a box), edge effects and boundary conditions
  can modify the conserved currents. For localized systems, use a modified
  version (Noether's theorem for systems with boundaries) that includes
  surface terms.

- **Symmetries are spontaneously broken.** If the Lagrangian is symmetric
  but the ground state is not, the conserved current still exists
  mathematically, but its spatial integral (the charge Q) is not an
  eigenvalue of the Hamiltonian — the system does not have a sharp value of
  Q. Example: in a ferromagnet, rotational symmetry of the Lagrangian is
  broken by the ground state, so angular momentum is not a good quantum
  number. The theorem holds; the interpretation changes.

- **Anomalies occur at the quantum level.** In quantum field theory, a
  classical symmetry of the Lagrangian can be broken by quantum loop effects.
  The conserved current is then anomalous: ∂_μ j^μ ≠ 0 even though the
  classical Lagrangian is symmetric. Example: the axial current in QCD is
  anomalous at one loop (related to the strong CP problem). Noether's theorem
  predicts the classical current; quantum field theory must determine if
  anomalies modify it.

- **The Lagrangian is not known or is emergent.** In condensed-matter systems,
  the microscopic Lagrangian is often complicated or not fully known.
  Effective low-energy Lagrangians may have symmetries not present in the
  fundamental theory, leading to emergent conservation laws. Conversely, an
  effective description may hide breaking of a fundamental symmetry. Use
  Noether's theorem on the effective Lagrangian, but check against
  experiments or microscopic simulations.

- **Gauge fixing breaks manifest symmetry.** In gauge theories, the
  Lagrangian has a gauge symmetry, but gauge fixing (e.g., Coulomb gauge in
  electromagnetism) breaks manifest invariance. The conserved quantities still
  exist (they are gauge-invariant), but they are not obvious from the
  gauge-fixed Lagrangian. Use the covariant formulation to apply Noether
  directly.

- **Time-dependent or nonconservative systems.** If the Lagrangian explicitly
  depends on time (e.g., a driven oscillator), time-translation symmetry is
  broken and energy is not conserved. If dissipation or friction is present,
  the system is not Lagrangian and Noether's theorem does not apply — use
  irreversible thermodynamics instead.

## Output Format

```
## Noether Analysis: <system name>

**System:** <brief description of the physical system>
**Lagrangian (or Hamiltonian):** <L or H, written explicitly>

### Continuous symmetries
| Symmetry | Generator ξ | Invariance check | Notes |
|---|---|---|---|
| <spacetime/internal> | <explicit form> | <L invariant? yes/no> | <classical or emergent> |

### Conserved currents and charges
| Symmetry | Conserved current j^μ | Conserved charge Q | Physical interpretation |
|---|---|---|---|
| ... | ... | ... | ... |

### Predictions
- Q₁ is [exactly/approximately] conserved because [symmetry is exact/approximate]
- If [symmetry condition] holds, then [consequence on observable]
- If [symmetry] is broken, then [conserved quantity decays / changes]

### Symmetry-breaking check
<is any symmetry broken in this system, classically or at the quantum level?>

### Boundary-condition notes
<which of the boundary conditions above apply and how they affect the predictions>

### Confidence: high | medium | low
<reasoning: Lagrangian clarity + whether symmetries are manifest or emergent +
quantum vs. classical domain + any anomalies or boundary effects>
```
