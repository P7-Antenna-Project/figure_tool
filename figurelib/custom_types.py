from dataclasses import dataclass
from typing import Tuple

# Dataclasses
TXSymbolType = Tuple[int, int, int]
SymbolAtLocationType = Tuple[int, TXSymbolType]
MissedSymbolAtLocationType = Tuple[int, str]

@dataclass
class SingleRunResults:
    count: int
    offset: int
    correct_symbols_at_location: list[SymbolAtLocationType]
    incorrect_symbols_at_location: list[SymbolAtLocationType]
    false_positives_at_location: list[SymbolAtLocationType]
    false_negatives_at_location: list[SymbolAtLocationType]
    missed_decodings: list[MissedSymbolAtLocationType]
    tx_syms: list[TXSymbolType]
    snr: float
    doppler: float
    has_packet_error: bool
    off_by_ones: int


@dataclass
class EGCResults:
    run_results: list[SingleRunResults]
    egc: int


@dataclass
class SNRResults:
    egc_results: list[EGCResults]
    snr: float
    theta_min: float


@dataclass
class SimulationResults:
    snr_results: list[SNRResults]