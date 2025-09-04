from dataclasses import dataclass, asdict
from typing import Optional, List

@dataclass
class Flight:
    hex: str
    callsign: str
    altitude_ft: Optional[int]
    squawk: str
    registration: str
    type: str
    alt_geom: Optional[int]
    gs: Optional[float]
    ias: Optional[float]
    tas: Optional[float]
    mach: Optional[float]
    wd: Optional[int]
    ws: Optional[int]
    oat: Optional[int]
    tat: Optional[int]
    roll: Optional[float]
    mag_heading: Optional[float]
    true_heading: Optional[float]
    baro_rate: Optional[int]
    geom_rate: Optional[int]
    emergency: str
    category: str
    nav_qnh: Optional[int]
    nav_altitude_mcp: Optional[int]
    nav_altitude_fms: Optional[int]
    nav_modes: Optional[List[str]]
    lat: Optional[float]
    lon: Optional[float]
    nic: Optional[int]
    rc: Optional[int]
    seen_pos: Optional[float]
    version: Optional[int]
    nic_baro: Optional[int]
    nac_p: Optional[int]
    nac_v: Optional[int]
    sil: Optional[int]
    sil_type: str
    gva: Optional[int]
    sda: Optional[int]
    alert: Optional[bool]
    spi: Optional[bool]
    mlat: Optional[List[str]]
    tisb: Optional[List[str]]
    messages: Optional[int]
    seen: Optional[float]
    rssi: Optional[float]
    dst: Optional[float]
    dir: Optional[float]

    @staticmethod
    def from_api(ac: dict) -> "Flight":
        """Create a Flight object from raw API data."""
        return Flight(
            hex=ac.get("hex", "N/A"),
            callsign=ac.get("flight", "N/A").strip(),
            altitude_ft=ac.get("alt_baro"),
            squawk=ac.get("squawk", "N/A"),
            registration=ac.get("r", "Unknown"),
            type=ac.get("t", "Unknown"),
            alt_geom=ac.get("alt_geom"),
            gs=ac.get("gs"),
            ias=ac.get("ias"),
            tas=ac.get("tas"),
            mach=ac.get("mach"),
            wd=ac.get("wd"),
            ws=ac.get("ws"),
            oat=ac.get("oat"),
            tat=ac.get("tat"),
            roll=ac.get("roll"),
            mag_heading=ac.get("mag_heading"),
            true_heading=ac.get("true_heading"),
            baro_rate=ac.get("baro_rate"),
            geom_rate=ac.get("geom_rate"),
            emergency=ac.get("emergency", "Unknown"),
            category=ac.get("category", "Unknown"),
            nav_qnh=ac.get("nav_qnh"),
            nav_altitude_mcp=ac.get("nav_altitude_mcp"),
            nav_altitude_fms=ac.get("nav_altitude_fms"),
            nav_modes=ac.get("nav_modes"),
            lat=ac.get("lat"),
            lon=ac.get("lon"),
            nic=ac.get("nic"),
            rc=ac.get("rc"),
            seen_pos=ac.get("seen_pos"),
            version=ac.get("version"),
            nic_baro=ac.get("nic_baro"),
            nac_p=ac.get("nac_p"),
            nac_v=ac.get("nac_v"),
            sil=ac.get("sil"),
            sil_type=ac.get("sil_type", "Unknown"),
            gva=ac.get("gva"),
            sda=ac.get("sda"),
            alert=ac.get("alert"),
            spi=ac.get("spi"),
            mlat=ac.get("mlat"),
            tisb=ac.get("tisb"),
            messages=ac.get("messages"),
            seen=ac.get("seen"),
            rssi=ac.get("rssi"),
            dst=ac.get("dst"),
            dir=ac.get("dir"),
        )

    def to_dict(self) -> dict:
        """Convert Flight object into JSON-friendly dict."""
        return asdict(self)
