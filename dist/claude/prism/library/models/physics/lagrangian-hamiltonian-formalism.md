---
name: lagrangian-hamiltonian-formalism
display_name: Lagrangian/Hamiltonian Formalism
class: model
underlying_class: native
domain: physics
source: Joseph-Louis Lagrange, Mécanique Analytique (1788); William Rowan Hamilton, "On a General Method in Dynamics" (1834)
best_for:
  - Deriving equations of motion for complex mechanical systems without choosing coordinates first
  - Identifying conserved quantities and symmetries in physical systems
  - Transitioning between classical and quantum mechanics
one_liner: "Coordinate-independent mechanics that derives equations of motion from symmetry and action minimization."
---

# Lagrangian/Hamiltonian Formalism

## Overview

The Lagrangian and Hamiltonian formalisms claim that the dynamics of any
mechanical system — classical or quantum, constrained or unconstrained — can
be derived from a single scalar function (the Lagrangian L or Hamiltonian H)
without ever explicitly choosing coordinates. The central insight is
**geometric and variational**: the system evolves along paths that extremize
(usually minimize) the action integral ∫L dt, and conserved quantities
emerge directly from symmetries in L or H via Noether's theorem. The
formalism is both predictive — it generates the correct equations of motion
— and explanatory: it reveals why certain quantities (energy, momentum,
angular momentum) are conserved, and what symmetries (time translation,
spatial translation, rotation) are responsible. Unlike Newtonian F = ma,
which is tied to Cartesian coordinates, the Lagrangian approach works in any
generalized coordinates and scales cleanly to quantum mechanics.

## Core Variables and Relationships

The key entities and how they relate:

1. **Lagrangian L(q, q̇, t)** — a scalar function of generalized
   coordinates q, their time derivatives q̇, and time t.
   - Typically L = T − V (kinetic energy minus potential energy).
   - Invariant under coordinate transformations: if q → q'(q, t), then L
     transforms such that the equations of motion are unchanged.
   - The choice of L is not unique; L and L + d(f)/dt produce the same
     equations of motion.

2. **Action S** — the time integral of L over a path in configuration
   space:
   - S[path] = ∫ L(q(t), q̇(t), t) dt
   - **Hamilton's principle**: the *actual* path satisfies δS = 0
     (extremal, usually minimal action). Virtual paths nearby have higher
     or equal action.
   - Leads directly to the **Euler-Lagrange equations**:
     d/dt(∂L/∂q̇ᵢ) − ∂L/∂qᵢ = 0

3. **Generalized momentum pᵢ** — defined as pᵢ = ∂L/∂q̇ᵢ.
   - Not always m·v; depends on the structure of L.
   - Conserved if ∂L/∂qᵢ = 0 (cyclic coordinate or ignorable coordinate).

4. **Hamiltonian H(p, q, t)** — a Legendre transform of L.
   - H = ∑ pᵢq̇ᵢ − L
   - Usually H = T + V (kinetic plus potential energy, when L = T − V).
   - Generates equations of motion via **Hamilton's equations**:
     dqᵢ/dt = ∂H/∂pᵢ,  dpᵢ/dt = −∂H/∂qᵢ
   - Symmetric in q and p; reveals the *phase-space* structure of
     dynamics.

5. **Noether's theorem** — the bridge between symmetry and conservation.
   - For every continuous symmetry of L (i.e., a transformation q → q + εξ
     that leaves L unchanged), there is a conserved quantity.
   - Time translation symmetry (∂L/∂t = 0) → energy conservation.
   - Spatial translation symmetry (L independent of absolute position) →
     linear momentum conservation.
   - Rotational symmetry (L unchanged under rotations) → angular momentum
     conservation.

6. **Phase space** — the (q, p) space in which H naturally lives.
   - The Hamiltonian formalism makes it clear that dynamics is a flow in
     phase space, not configuration space alone.
   - Preserves volume in phase space (Liouville's theorem) — essential for
     statistical mechanics.
   - Canonical transformations (q, p) → (Q, P) leave H's structure
     unchanged; solutions in one set of canonical coordinates map to
     solutions in another.

## Key Predictions

- **A system with no explicit time-dependence in L will conserve energy.**
  Not because you imposed a conservation law, but as a mathematical
  consequence of Noether's theorem. The system *must* have constant H if
  ∂H/∂t = 0.

- **A coordinate that does not appear in L is "cyclic" and its conjugate
  momentum is conserved.** A satellite in a spherically symmetric
  gravitational potential has cyclic angular coordinates (φ); its angular
  momentum L_z is automatically conserved without invoking any separate
  principle.

- **Small perturbations to a Hamiltonian system can be analyzed via
  canonical perturbation theory**, revealing action-angle variables and
  resonances. This is the foundation of celestial mechanics stability
  analysis and explains why some orbits are chaotic while others are
  stable.

- **The Hamiltonian formalism reproduces Lagrangian predictions but also
  reveals the phase-space geometry** — separatrix structures, Lyapunov
  exponents, and KAM tori — that the Lagrangian view obscures.

- **Quantization is a direct rewrite**: the classical Poisson bracket
  {A, B} in the Hamiltonian formalism becomes the commutator −iℏ[Â, B̂] in
  quantum mechanics. Constraints and symmetries in the classical
  formulation often *automatically* carry over to the quantum case.

## Application Procedure

Instantiate the formalism against a concrete mechanical system.

1. **Identify the system and its degrees of freedom.** What are the
   bodies, the constraints, and the generalized coordinates q that
   fully specify the configuration? Count n = number of q's. Write the
   configuration space explicitly (e.g., "two pendulums linked by a
   spring" → q = (θ₁, θ₂)).

2. **Write the kinetic and potential energies in the chosen coordinates.**
   - T = T(q, q̇) — account for constraint-reduced speeds.
   - V = V(q) — typically does not depend on q̇.
   - Form L = T − V.

3. **Identify any symmetries of L.**
   - Does L depend explicitly on time? (Affects energy conservation.)
   - Are there cyclic coordinates? (Affects momentum conservation.)
   - Are there rotational or translational symmetries?
   - Use Noether's theorem to identify what is conserved.

4. **Compute the Euler-Lagrange equations** (or equivalently, the
   Hamiltonian equations).
   - For each coordinate qᵢ, compute d/dt(∂L/∂q̇ᵢ) − ∂L/∂qᵢ = 0.
   - This produces n coupled ODEs in second order.
   - Solve if possible; if not, set up for numerical integration or use
     qualitative/perturbative methods.

5. **Convert to Hamiltonian form if needed.**
   - Compute pᵢ = ∂L/∂q̇ᵢ (solve for q̇ᵢ in terms of pᵢ if necessary).
   - Form H = ∑ pᵢq̇ᵢ − L, express as H(q, p).
   - Write Hamilton's equations and analyze phase-space dynamics.

6. **Extract conserved quantities.**
   - From symmetries (via Noether): energy if ∂L/∂t = 0; linear/angular
     momentum if translationally or rotationally invariant.
   - From cyclic coordinates: pᵢ = const if qᵢ does not appear in L.
   - Use these to reduce dimensionality or simplify the solution.

7. **Check boundary conditions** (below). If any apply, note what
   assumptions of the formalism may be violated.

## Boundary Conditions

The Lagrangian/Hamiltonian formalism assumes a finite-dimensional
configuration space and holonomic constraints. It breaks down or requires
extension when:

- **Non-holonomic constraints** (constraints on velocities, not just
  coordinates — e.g., rolling without slipping, or magnetic forces
  perpendicular to velocity). The formalism requires modification; the
  usual Lagrange equations do not apply directly. Must add constraint
  forces or use Lagrange multipliers in a modified form.

- **Dissipative forces** (friction, air resistance). The standard
  formalism assumes conservative forces derivable from a potential. For
  small dissipation, add a dissipation function; for large dissipation,
  the extremal action principle breaks down and you must work with
  equations of motion directly or use a generalized potential.

- **Velocity-dependent potential** (Lorentz force in electromagnetism).
  The formalism adapts — use V(q, q̇) = −q·φ + q̇·A in the Lagrangian —
  but this is less transparent than the conservative case and Noether's
  theorem must be applied carefully.

- **Singular or degenerate Lagrangian** (when ∂²L/∂q̇ᵢ∂q̇ⱼ is singular or
  nearly so). The transformation to Hamiltonian form fails or requires
  Dirac constraint analysis. Common in gauge theories and systems with
  degeneracies.

- **Infinite-dimensional systems** (fields, continua). The formalism
  extends — replace q → φ(x, t) and L → density ℒ(φ, ∂_μ φ) — but
  functional calculus and PDE techniques dominate; the finite-dimensional
  intuition can mislead.

- **Systems with explicit nonlinearity at very high amplitude.** While
  the formalism is formally valid, integrability is rare and perturbation
  theory or numerical methods become necessary. The qualitative insight
  from symmetries and conservation laws may still hold, but quantitative
  prediction requires computation.

## Output Format

```
## Lagrangian/Hamiltonian Analysis: <system name>

**System:** <description of bodies, constraints, degrees of freedom>
**Configuration space:** <list generalized coordinates q>
**Time-dependence:** <L explicitly time-dependent? H? Why?>

### Lagrangian and symmetries
- L(q, q̇) = <expression>
- T = <kinetic energy>
- V = <potential energy>
- Cyclic coordinates: <list, if any>
- Symmetries: <time translation? rotational? translational?>

### Conserved quantities (Noether)
| Symmetry | Conserved quantity | Formula |
|---|---|---|
| ... | ... | ... |

### Equations of motion
- Euler-Lagrange form: <2nd-order ODE or system>
- Hamiltonian form: Hamilton's equations in (q, p) space

### Phase-space structure (if Hamiltonian form used)
- H(q, p) = <expression>
- Dimensionality of phase space: 2n
- Fixed points / separatrices / integrable regions: <qualitative description>

### Reduction via conservation laws
- Independent variables after using conservation: <which remain free?>
- Effective reduced Hamiltonian or Lagrangian: <if simplification is substantial>

### Boundary-condition check
<which boundary conditions apply; what modifications or complementary
analysis is required?>

### Confidence: high | medium | low
<reasoning: holonomic or not, conservative or not, integrable or not,
small or large amplitude>
```
---
