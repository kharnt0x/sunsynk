"""Sunsynk high voltage hybrid 3-phase inverter sensor definitions."""
# pylint: disable=duplicate-code
from sunsynk import AMPS, CELSIUS, KWH, VOLT, WATT
from sunsynk.rwsensors import (
    NumberRWSensor,
    SelectRWSensor,
    SwitchRWSensor,
    SystemTimeRWSensor,
    TimeRWSensor,
)
from sunsynk.sensors import (
    BinarySensor,
    HVFaultSensor,
    InverterStateSensor,
    MathSensor,
    SDStatusSensor,
    Sensor,
    SensorDefinitions,
    SerialSensor,
    TempSensor,
)

SENSORS = SensorDefinitions()

##########
# Battery
##########
SENSORS += (
    Sensor(586, "Battery 1 temperature", CELSIUS, 0.1),
    Sensor(587, "Battery 1 voltage", VOLT, 0.1),
    Sensor(588, "Battery 1 SOC", "%"),
    Sensor(590, "Battery 1 power", WATT, -10),
    Sensor(591, "Battery 1 current", AMPS, -0.01),
    Sensor(589, "Battery 2 SOC", "%"), #correct
    Sensor(593, "Battery 2 voltage", VOLT, 0.1), #correct
    Sensor(594, "Battery 2 current", AMPS, -0.01), #correct
    Sensor(595, "Battery 2 power", WATT, -10), #correct
    Sensor(596, "Battery 2 temperature", CELSIUS, 0.1), #correct I think
)

#################
# Inverter Power
#################
SENSORS += (
    Sensor(636, "Inverter power", WATT, -1),
    Sensor(633, "Inverter L1 power", WATT, -1),
    Sensor(634, "Inverter L2 power", WATT, -1),
    Sensor(635, "Inverter L3 power", WATT, -1),
    Sensor(627, "Inverter voltage", VOLT, 0.1),
    Sensor(638, "Inverter frequency", "Hz", 0.01),
)

#############
# Grid Power
#############
SENSORS += (
    Sensor(609, "Grid frequency", "Hz", 0.01),
    Sensor(625, "Grid power", WATT, -1),  # gridTotalPac
    Sensor(622, "Grid L1 power", WATT, -1),  # aPower
    Sensor(623, "Grid L2 power", WATT, -1),  # bPower
    Sensor(624, "Grid L3 power", WATT, -1),  # cPower
    Sensor(598, "Grid L1 voltage", VOLT, 0.1),  # aLineVolt
    Sensor(599, "Grid L2 voltage", VOLT, 0.1),  # bLineVolt
    Sensor(600, "Grid L3 voltage", VOLT, 0.1),  # cLineVolt
    MathSensor(
        (610, 611, 612), "Grid current", AMPS, factors=(0.01, 0.01, 0.01)
    ),  # iac1,iac2,iac3
    Sensor(619, "Grid CT power", WATT, -1),  # totalPower
    Sensor(616, "Grid CT L1 power", WATT, -1),  # aPower
    Sensor(617, "Grid CT L2 power", WATT, -1),  # bPower
    Sensor(618, "Grid CT L3 power", WATT, -1),  # cPower
)

#############
# Load Power
#############
SENSORS += (
    Sensor(653, "Load power", WATT, -1),
    Sensor(650, "Load L1 power", WATT, -1),
    Sensor(651, "Load L2 power", WATT, -1),
    Sensor(652, "Load L3 power", WATT, -1),
    Sensor(644, "Load L1 voltage", VOLT, 0.1),
    Sensor(645, "Load L2 voltage", VOLT, 0.1),
    Sensor(646, "Load L3 voltage", VOLT, 0.1),
)

#
################
# Solar Power
################
SENSORS += (
    MathSensor((672, 673, 674, 675), "PV power", WATT, factors=(10, 10, 10, 10)),  # pv1 power,pv2 power
)
################
# MPPT 1 Solar Power
################
SENSORS += (
    Sensor(672, "PV1 power", WATT, 10),
    Sensor(676, "PV1 voltage", VOLT, 0.1),
    Sensor(677, "PV1 current", AMPS, 0.1),
)

################
# MPPT2 Solar Power
################
SENSORS += (
    Sensor(673, "PV2 power", WATT, 10),
    Sensor(678, "PV2 voltage", VOLT, 0.1),
    Sensor(679, "PV2 current", AMPS, 0.1),
)

################
# MPPT3 Solar Power
################
SENSORS += (
    Sensor(674, "PV3 power", WATT, 10),
    Sensor(680, "PV3 voltage", VOLT, 0.1),
    Sensor(681, "PV3 current", AMPS, 0.1),
)

################
# MPPT4 Solar Power
################
SENSORS += (
    Sensor(675, "PV4 power", WATT, 10),
    Sensor(682, "PV4 voltage", VOLT, 0.1),
    Sensor(683, "PV4 current", AMPS, 0.1),
)


###################
# Power on Outputs (aka GEN - which has multiple modes on the deye 3 Phase )
###################
SENSORS += (
    Sensor(667, "Gen power", WATT, -1),
    Sensor(664, "Gen L1 power", WATT, -1),
    Sensor(665, "Gen L2 power", WATT, -1),
    Sensor(666, "Gen L3 power", WATT, -1),
)

###################
# Energy
###################
SENSORS += (
    Sensor(502, "Day Active Energy", KWH, -0.1),
    Sensor(514, "Day Battery Charge", KWH, 0.1),
    Sensor(515, "Day Battery discharge", KWH, 0.1),
    Sensor(521, "Day Grid Export", KWH, 0.1),
    Sensor(520, "Day Grid Import", KWH, 0.1),
    Sensor(536, "Day Gen Energy", KWH, 0.1),
    Sensor(526, "Day Load Energy", KWH, 0.1),  # I guess "used" = load?
    Sensor(529, "Day PV Energy", KWH, 0.1),
    Sensor((506, 507), "Total Active Energy", KWH, 0.1),  # signed?
    Sensor((516, 517), "Total Battery Charge", KWH, 0.1),
    Sensor((518, 519), "Total Battery Discharge", KWH, 0.1),
    Sensor((524, 525), "Total Grid Export", KWH, 0.1),
    Sensor((522, 523), "Total Grid Import", KWH, 0.1),
    Sensor((527, 528), "Total Load Energy", KWH, 0.1),
    Sensor((534, 535), "Total PV Energy", KWH, 0.1),
)

##########
# General
##########
RATED_POWER = Sensor((20, 21), "Rated power", WATT, 0.1)
SENSORS += RATED_POWER

SENSORS += (
    Sensor(
        0, "Device Type"
    ),  # {2: "Inverter", 3: "Hybrid Inverter", 4: "Micro Inverter", 5: "3 Phase Hybrid Inverter" }),
    HVFaultSensor((555, 556, 557, 558), "Fault"),
    InverterStateSensor(500, "Overall state"),
    SDStatusSensor(0, "SD Status", ""),  # type: ignore
    SerialSensor((3, 4, 5, 6, 7), "Serial"),
    TempSensor(540, "DC transformer temperature", CELSIUS, 0.1),
    TempSensor(541, "Radiator temperature", CELSIUS, 0.1),
    Sensor(
        552, "Grid Connected Status"
    ),  # Bit 0 = INV Relay, 1 = Undef, 2 = Grid relay, 3 = Gen relay, 4 = Grid give, 5, Dry contact
    BinarySensor(194, "Grid Connected", bitmask=1 << 2),
    SystemTimeRWSensor((62, 63, 64), "Date Time", unit=""),
)


###########
# Settings
###########
SENSORS += (
    NumberRWSensor(128, "Grid Charge Battery current", AMPS, max=210),
    SwitchRWSensor(130, "Grid Charge enabled"),
    NumberRWSensor(127, "Grid Charge Start Battery SOC", "%"),
    NumberRWSensor(128, "Grid Charge Amps", AMPS),
    SwitchRWSensor(146, "Use Timer", on=255),
    SwitchRWSensor(145, "Solar Export"),
    NumberRWSensor(143, "Export Limit power", WATT, max=RATED_POWER),
    NumberRWSensor(108, "Battery Max Charge current", AMPS, max=210),
    NumberRWSensor(109, "Battery Max Discharge current", AMPS, max=210),
    NumberRWSensor(102, "Battery Capacity current", "Ah", max=2000),
)

# Additional optional sensors
SENSORS += (
    NumberRWSensor(
        103, "Battery low voltage", VOLT, -0.1
    ),  # interesting perhaps not available in menu. default 4500 (45V)
    SelectRWSensor(
        133,
        "Generator Port Usage",
        options={0: "Generator", 1: "Smartload", 2: "Micro Inverter"},
    ),
    SelectRWSensor(129, "Generator Charge enabled", options={0: "Off", 1: "On"}),
    NumberRWSensor(124, "Generator Charge Start Battery SOC", "%"),
    NumberRWSensor(125, "Generator Charge Battery current", AMPS),
    SelectRWSensor(112, "Battery Wake Up", options={0: "On", 1: "Off"}), #according to docs, 0 is enabled for this one
    NumberRWSensor(113, "Battery Resistance", "mΩ", max=6000),
    NumberRWSensor(114, "Battery Charge Efficiency", "%", 0.1),
    NumberRWSensor(104, "System Zero Export power", WATT, -1),
    NumberRWSensor(105, "Battery Equalization Days", "days", -1),
    NumberRWSensor(106, "Battery Equalization Hours", "h", -1),  # 1 = 0.5 hours
    
)

# Absolute min and max voltage based on Deye inverter
MIN_VOLT = 41
MAX_VOLT = 60

BATTERY_EQUALIZATION_VOLT = NumberRWSensor(
    99, "Battery Equalization voltage", VOLT, 0.01, min=MIN_VOLT, max=MAX_VOLT
)
BATTERY_ABSORPTION_VOLT = NumberRWSensor(
    100, "Battery Absorption voltage", VOLT, 0.01, min=MIN_VOLT, max=MAX_VOLT
)
BATTERY_FLOAT_VOLT = NumberRWSensor(
    101, "Battery Float voltage", VOLT, 0.01, min=MIN_VOLT, max=MAX_VOLT
)

BATTERY_MODE = SelectRWSensor(111, "Battery Type", options={0: "Use Battery Voltage", 1: "Lithium (Use BMS)", 2: "No Battery"}), 

BATTERY_SHUTDOWN_CAP = NumberRWSensor(115, "Battery Shutdown Capacity", "%")
BATTERY_RESTART_CAP = NumberRWSensor(116, "Battery Restart Capacity", "%")
BATTERY_LOW_CAP = NumberRWSensor(
    117,
    "Battery Low Capacity",
    "%",
    min=BATTERY_SHUTDOWN_CAP,
    max=BATTERY_RESTART_CAP,
)
BATTERY_SHUTDOWN_CAP.max = BATTERY_LOW_CAP
BATTERY_RESTART_CAP.min = BATTERY_LOW_CAP

BATTERY_SHUTDOWN_VOLT = NumberRWSensor(
    118, "Battery Shutdown voltage", VOLT, 0.01, min=MIN_VOLT
)
BATTERY_LOW_VOLT = NumberRWSensor(
    120, "Battery Low voltage", VOLT, 0.01, min=BATTERY_SHUTDOWN_VOLT, max=MAX_VOLT
)
BATTERY_RESTART_VOLT = NumberRWSensor(
    119, "Battery Restart voltage", VOLT, 0.01, max=MAX_VOLT
)
BATTERY_SHUTDOWN_VOLT.max = BATTERY_LOW_VOLT
BATTERY_RESTART_VOLT.min = BATTERY_LOW_VOLT

SENSORS += (
    BATTERY_MODE,
    BATTERY_EQUALIZATION_VOLT,
    BATTERY_ABSORPTION_VOLT,
    BATTERY_FLOAT_VOLT,
    BATTERY_SHUTDOWN_CAP,
    BATTERY_RESTART_CAP,
    BATTERY_LOW_CAP,
    BATTERY_SHUTDOWN_VOLT,
    BATTERY_RESTART_VOLT,
    BATTERY_LOW_VOLT,
)

#################
# System program
#################

SENSORS += SwitchRWSensor(141, "Priority Load")

SENSORS += SelectRWSensor(
    142,
    "Load Limit",
    options={0: "Allow Export", 1: "Zero Export To Non Essential", 2: "Zero Export To Grid CT"},
)

PROG1_TIME = TimeRWSensor(148, "Prog1 Time")
PROG2_TIME = TimeRWSensor(149, "Prog2 Time", min=PROG1_TIME)
PROG3_TIME = TimeRWSensor(150, "Prog3 Time", min=PROG2_TIME)
PROG4_TIME = TimeRWSensor(151, "Prog4 Time", min=PROG3_TIME)
PROG5_TIME = TimeRWSensor(152, "Prog5 Time", min=PROG4_TIME)
PROG6_TIME = TimeRWSensor(153, "Prog6 Time", min=PROG5_TIME)
PROG1_TIME.min = PROG6_TIME
PROG1_TIME.max = PROG2_TIME
PROG2_TIME.max = PROG3_TIME
PROG3_TIME.max = PROG4_TIME
PROG4_TIME.max = PROG5_TIME
PROG5_TIME.max = PROG6_TIME
PROG6_TIME.max = PROG1_TIME

PROG_CHARGE_OPTIONS = {
    0: "Off",
    1: "Grid Only",
    2: "Gen Only",
    3: "Grid and Gen",
}

SENSORS += (
    PROG1_TIME,
    PROG2_TIME,
    PROG3_TIME,
    PROG4_TIME,
    PROG5_TIME,
    PROG6_TIME,
    NumberRWSensor(154, "Prog1 power", WATT, 10, max=RATED_POWER),
    NumberRWSensor(155, "Prog2 power", WATT, 10, max=RATED_POWER),
    NumberRWSensor(156, "Prog3 power", WATT, 10, max=RATED_POWER),
    NumberRWSensor(157, "Prog4 power", WATT, 10, max=RATED_POWER),
    NumberRWSensor(158, "Prog5 power", WATT, 10, max=RATED_POWER),
    NumberRWSensor(159, "Prog6 power", WATT, 10, max=RATED_POWER),
    NumberRWSensor(166, "Prog1 Capacity", "%", min=BATTERY_LOW_CAP),
    NumberRWSensor(167, "Prog2 Capacity", "%", min=BATTERY_LOW_CAP),
    NumberRWSensor(168, "Prog3 Capacity", "%", min=BATTERY_LOW_CAP),
    NumberRWSensor(169, "Prog4 Capacity", "%", min=BATTERY_LOW_CAP),
    NumberRWSensor(170, "Prog5 Capacity", "%", min=BATTERY_LOW_CAP),
    NumberRWSensor(171, "Prog6 Capacity", "%", min=BATTERY_LOW_CAP),
    SelectRWSensor(172, "Prog1 charge", options=PROG_CHARGE_OPTIONS),
    SelectRWSensor(173, "Prog2 charge", options=PROG_CHARGE_OPTIONS),
    SelectRWSensor(174, "Prog3 charge", options=PROG_CHARGE_OPTIONS),
    SelectRWSensor(175, "Prog4 charge", options=PROG_CHARGE_OPTIONS),
    SelectRWSensor(176, "Prog5 charge", options=PROG_CHARGE_OPTIONS),
    SelectRWSensor(177, "Prog6 charge", options=PROG_CHARGE_OPTIONS),
)

SENSORS += (
    SelectRWSensor(146, "Prog Time Of Use Enabled", options={0: "off", 1: "on"}, bitmask=0x01),
    SelectRWSensor(146, "Prog Monday Enabled", options={0: "off", 2: "on"}, bitmask=0x02),
    SelectRWSensor(146, "Prog Tuesday Enabled", options={0: "off", 4: "on"}, bitmask=0x04),
    SelectRWSensor(146, "Prog Wednesday Enabled", options={0: "off", 8: "on"}, bitmask=0x08),
    SelectRWSensor(146, "Prog Thursday Enabled", options={0: "off", 16: "on"}, bitmask=0x10),
    SelectRWSensor(146, "Prog Friday Enabled", options={0: "off", 32: "on"}, bitmask=0x20),
    SelectRWSensor(146, "Prog Saturday Enabled", options={0: "off", 64: "on"}, bitmask=0x40),
    SelectRWSensor(146, "Prog Sunday Enabled", options={0: "off", 128: "on"}, bitmask=0x80),
)


SENSORS += (
    NumberRWSensor(
        160,
        "Prog1 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLT,
        max=BATTERY_FLOAT_VOLT,
    ),
    NumberRWSensor(
        161,
        "Prog2 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLT,
        max=BATTERY_FLOAT_VOLT,
    ),
    NumberRWSensor(
        162,
        "Prog3 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLT,
        max=BATTERY_FLOAT_VOLT,
    ),
    NumberRWSensor(
        163,
        "Prog4 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLT,
        max=BATTERY_FLOAT_VOLT,
    ),
    NumberRWSensor(
        164,
        "Prog5 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLT,
        max=BATTERY_FLOAT_VOLT,
    ),
    NumberRWSensor(
        165,
        "Prog6 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLT,
        max=BATTERY_FLOAT_VOLT,
    ),
)

SENSORS += (
    NumberRWSensor(131, "Generator AC Couple Frz High", "Hz", 0.01),
    NumberRWSensor(135, "Generator Off", "%"),
    NumberRWSensor(137, "Generator On", "%"),
)

SENSORS.deprecated.update(
    {
        "priority_mode": "priority_load",
        "Battery temperature": "Battery 1 temperature",
        "Battery voltage": "Battery 1 voltage",
        "Battery SOC": "Battery 1 SOC",
        "Battery power": "Battery 1 power",
        "Battery current": "Battery 1 current",
    }
)
