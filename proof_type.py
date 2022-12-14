"""
sphinx_proof.proof_type
~~~~~~~~~~~~~~~~~~~~~~~

List of proof-type directives

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""

from .directive import ElementDirective


class TheoremDirective(ElementDirective):
    """A custom theorem directive."""

    name = "theorem"


class LemmaDirective(ElementDirective):
    """A custom lemma directive."""

    name = "lemma"


class DefinitionDirective(ElementDirective):
    """A custom definition directive."""

    name = "definition"


class RemarkDirective(ElementDirective):
    """A custom remark directive."""

    name = "remark"


class ConjectureDirective(ElementDirective):
    """A custom conjecture directive."""

    name = "conjecture"


class CorollaryDirective(ElementDirective):
    """A custom corollary directive."""

    name = "corollary"


class AlgorithmDirective(ElementDirective):
    """A custom algorithm directive."""

    name = "algorithm"


class CriterionDirective(ElementDirective):
    """A custom criteria directive."""

    name = "criterion"


class AxiomDirective(ElementDirective):
    """A custom axiom directive."""

    name = "axiom"


class ExampleDirective(ElementDirective):
    """A custom example directive."""

    name = "example"


class PropertyDirective(ElementDirective):
    """A custom property directive."""

    name = "property"


class ObservationDirective(ElementDirective):
    """A custom observation directive."""

    name = "observation"


class PropositionDirective(ElementDirective):
    """A custom proposition directive."""

    name = "proposition"


PROOF_TYPES = {
    "axioma": AxiomDirective,
    "teorema": TheoremDirective,
    "lema": LemmaDirective,
    "algoritmo": AlgorithmDirective,
    "definición": DefinitionDirective,
    "remark": RemarkDirective,
    "conjecture": ConjectureDirective,
    "corollary": CorollaryDirective,
    "criterion": CriterionDirective,
    "ejemplo": ExampleDirective,
    "property": PropertyDirective,
    "observation": ObservationDirective,
    "proposición": PropositionDirective,
}
