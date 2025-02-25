# ==================================================================================

# チップの位置を更新してから読み込む。

# ==================================================================================

from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    tip_rack_p300 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 3)
    well_plate_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', 5)
 
    # 最初のチップがある位置を設定する  
    right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack_p300])
    right_pipette.starting_tip = tip_rack_p300['H9']

# 1
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['C1'])
    right_pipette.dispense(20, well_plate_384['B13'])
    right_pipette.dispense(20, well_plate_384['B17'])
    right_pipette.dispense(20, well_plate_384['B21'])
    right_pipette.drop_tip()

# 2
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['C2'])
    right_pipette.dispense(20, well_plate_384['C15'])
    right_pipette.dispense(20, well_plate_384['C19'])
    right_pipette.dispense(20, well_plate_384['C23'])
    right_pipette.drop_tip()

# 3
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['C3'])
    right_pipette.dispense(20, well_plate_384['E13'])
    right_pipette.dispense(20, well_plate_384['E17'])
    right_pipette.dispense(20, well_plate_384['E21'])
    right_pipette.drop_tip()

# 4
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['C4'])
    right_pipette.dispense(20, well_plate_384['F15'])
    right_pipette.dispense(20, well_plate_384['F19'])
    right_pipette.dispense(20, well_plate_384['F23'])
    right_pipette.drop_tip()

# 5
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['C5'])
    right_pipette.dispense(20, well_plate_384['H13'])
    right_pipette.dispense(20, well_plate_384['H17'])
    right_pipette.dispense(20, well_plate_384['H21'])
    right_pipette.drop_tip()

# 6
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['C6'])
    right_pipette.dispense(20, well_plate_384['I15'])
    right_pipette.dispense(20, well_plate_384['I19'])
    right_pipette.dispense(20, well_plate_384['I23'])
    right_pipette.drop_tip()

# 7
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['D1'])
    right_pipette.dispense(20, well_plate_384['K13'])
    right_pipette.dispense(20, well_plate_384['K17'])
    right_pipette.dispense(20, well_plate_384['K21'])
    right_pipette.drop_tip()

# 8
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['D2'])
    right_pipette.dispense(20, well_plate_384['L15'])
    right_pipette.dispense(20, well_plate_384['L19'])
    right_pipette.dispense(20, well_plate_384['L23'])
    right_pipette.drop_tip()

# 9
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['D3'])
    right_pipette.dispense(20, well_plate_384['N13'])
    right_pipette.dispense(20, well_plate_384['N17'])
    right_pipette.dispense(20, well_plate_384['N21'])
    right_pipette.drop_tip()

# 10
    right_pipette.pick_up_tip()
    right_pipette.aspirate(60, tube_rack['D4'])
    right_pipette.dispense(20, well_plate_384['O15'])
    right_pipette.dispense(20, well_plate_384['O19'])
    right_pipette.dispense(20, well_plate_384['O23'])
    right_pipette.drop_tip()

# milliQ
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(60, tube_rack['D5'])
    # right_pipette.dispense(20, well_plate_384['O4'])
    # right_pipette.dispense(20, well_plate_384['O7'])
    # right_pipette.dispense(20, well_plate_384['O10'])
    # right_pipette.drop_tip()