# '0x03' == 'Door type'
# '0x00' == 'Door Status and LCP Firmware versions'
# '0x10' == 'MCP Status & MCP Firmware Versions'
# '0x1E' == 'Door Switch Mode'
# '0x11' == 'Door Errors'
# {'0x01', '0x68'} == 'System Cycle count'
# '0x03' == 'Door/Motor Cycle count'
# '0x09' == 'Clear cycle count'
# {0x01, 0x81}, {0x01, 0x83}, {0x01, 0x85}, {0x01, 0x87} == 'Active door ID'
# {0x01, 0x8B}, {0x01, 0x8D}, {0x01, 0x8F}, {0x01, 0x91} == 'Original door ID'
import pandas as pd
import sys,json

# input_json = {
#                 "Metadata": {
#                     "ConfigVerNo": "cof123",
#                     "DoorType": {
#                         "Type": "String"
#                     },
#                     "FirmwareVersionRange": {
#                         "LowVersion": "String",
#                         "HighVersion": "String"
#                     },
#                     "endpoint_ciu_cloud" : {
#                         "AWS_HOSTNAME" : "ar72sxipi1awa.iot.us-east-2.amazonaws.com"
#                     },
#                     "Device_profile_id":"dev_123"
#                 },
#                 "DataCommandGroup": [
#                     {
#                         "ID": "0xF0",
#                         "Name": "Door Error",
#                         "PollTime": "1000, // in milliseconds",
#                         "TransmitTime": "10000, //Max time the CIU will wait. If no transmission till that time, then there will be a force transmission",
#                         "Active": "Y",
#                         "Priority": 1,
#                         "TransmitOnChange": "Y",
#                         "List": ["0x01", "0x02"],
#                         "Commands": [
#                             {"ID": "0x01", "Active": "Y", "Cmd": ["0x11", "0x01", "0x00", "$List"]},
#                             # {"ID": "0x02", "Active": "Y", "Cmd": ["0x11", "0x11", "0x00", "$List"]},
#                             {"ID": "0x03", "Active": "Y", "Cmd": ["0x11", "0x11", "0x01", "$List"]},
#                             {"ID": "0x04", "Active": "Y", "Cmd": ["0x11", "0x02", "0x00", "$List"]},
#                             {"ID": "0x05", "Active": "Y", "Cmd": ["0x11", "0x12", "0x00", "$List"]},
#                             {"ID": "0x06", "Active": "Y", "Cmd": ["0x11", "0x12", "0x01", "$List"]},
#                             {"ID": "0x07", "Active": "Y", "Cmd": ["0x03", "0x00", "0x00", "0x00"]},
#                             {"ID": "0x08", "Active": "Y", "Cmd": ["0x00", "0x00", "0x00", "0x00"]},
#                             {"ID": "0x09", "Active": "Y", "Cmd": ["0x10", "0x00", "0x00", "0x00"]},
#                             # {"ID": "0x10", "Active": "Y", "Cmd": ["0x10", "0x01", "0x00", "0x00"]},
#                             {"ID": "0x11", "Active": "Y", "Cmd": ["0x1E", "0x00", "0x00", "0x00"]},
#                             {"ID": "0x12", "Active": "Y", "Cmd": ["0x01", "0x68", "0x00", "0x00"]},
#                             {"ID": "0x13", "Active": "Y", "Cmd": ["0x01", "0x6A", "0x00", "0x00"]},
#                             {"ID": "0x14", "Active": "Y", "Cmd": ["0x03", "0x7C", "0x00", "0x00"]},
#                             {"ID": "0x15", "Active": "Y", "Cmd": ["0x03", "0x7D", "0x00", "0x00"]},
#                             {"ID": "0x16", "Active": "Y", "Cmd": ["0x03", "0x7E", "0x00", "0x00"]},
#                             {"ID": "0x17", "Active": "Y", "Cmd": ["0x03", "0x7F", "0x00", "0x00"]},
#                             {"ID": "0x18", "Active": "Y", "Cmd": ["0x03", "0x6C", "0x00", "0x00"]},
#                             {"ID": "0x19", "Active": "Y", "Cmd": ["0x03", "0x6D", "0x00", "0x00"]},
#                             {"ID": "0x20", "Active": "Y", "Cmd": ["0x03", "0x6E", "0x00", "0x00"]},
#                             {"ID": "0x21", "Active": "Y", "Cmd": ["0x03", "0x6F", "0x00", "0x00"]},
#                             {"ID": "0x22", "Active": "Y", "Cmd": ["0x01", "0x81", "0x00", "0x00"]},
#                             {"ID": "0x23", "Active": "Y", "Cmd": ["0x01", "0x83", "0x00", "0x00"]},
#                             {"ID": "0x24", "Active": "Y", "Cmd": ["0x01", "0x85", "0x00", "0x00"]},
#                             {"ID": "0x25", "Active": "Y", "Cmd": ["0x01", "0x87", "0x00", "0x00"]},
#                             {"ID": "0x26", "Active": "Y", "Cmd": ["0x01", "0x8B", "0x00", "0x00"]},
#                             {"ID": "0x27", "Active": "Y", "Cmd": ["0x01", "0x8D", "0x00", "0x00"]},
#                             {"ID": "0x28", "Active": "Y", "Cmd": ["0x01", "0x8F", "0x00", "0x00"]},
#                             {"ID": "0x29", "Active": "Y", "Cmd": ["0x01", "0x91", "0x00", "0x00"]},

#                         ]
#                     },
#                     {
#                         "ID": "0xF1",
#                         "Name": "Door Error",
#                         "PollTime": "1000, // in milliseconds",
#                         "TransmitTime": 10000,
#                         "Active": "Y",
#                         "Priority": 1,
#                         "TransmitOnChange": "Y",
#                         "List": ["0x03", "0x04"],
#                         "Commands": [
#                             {"ID": "0x01", "Active": "Y", "Cmd": ["0x11", "0x01", "0x00", "$List"]},
#                             {"ID": "0x02", "Active": "Y", "Cmd": ["0x11", "0x11", "0x00", "$List"]},
#                             {"ID": "0x03", "Active": "Y", "Cmd": ["0x11", "0x11", "0x01", "$List"]},
#                             {"ID": "0x04", "Active": "Y", "Cmd": ["0x11", "0x02", "0x00", "$List"]},
#                             {"ID": "0x05", "Active": "Y", "Cmd": ["0x11", "0x12", "0x00", "$List"]},
#                             {"ID": "0x06", "Active": "Y", "Cmd": ["0x11", "0x12", "0x01", "$List"]}
#                         ]
#                     }
#                 ]
#             }

# response_json = {
#     "Metadata": {
#                     "ConfigVerNo": "cof123",
#                     "DoorType": {
#                         "Type": "String"
#                     },
#                     "FirmwareVersionRange": {
#                         "LowVersion": "String",
#                         "HighVersion": "String"
#                     },
#                     "endpoint_ciu_cloud" : {
#                         "AWS_HOSTNAME" : "ar72sxipi1awa.iot.us-east-2.amazonaws.com"
#                     },
#                     "Device_profile_id":"dev_123"
#                 },
#     "DataCommandGroup": [
#         {
#             "ID": "0xF0",
#             "Responses": [
#                 {"ID": "0x01", "Res": ['0x11', '0x46', '0x76', '0x01']},
#                 # {"ID": "0x02", "Res": ['0x11', '0x24', '0x12', '0x01']},
#                 {"ID": "0x03", "Res": ['0x11', '0x41', '0x14', '0x01']},
#                 {"ID": "0x04", "Res": ['0x11', '0x34', '0x41', '0x01']},
#                 {"ID": "0x05", "Res": ['0x11', '0x75', '0x11', '0x01']},
#                 {"ID": "0x06", "Res": ['0x11', '0x17', '0x23', '0x01']},
#                 {"ID": "0x07", "Res": ['0x00', '0x03', '0x00', '0x02']},
#                 {"ID": "0x08", "Res": ["0x00", "0x00", "0x00", "0x01"]},
#                 {"ID": "0x09", "Res": ["0x00", "0x10", "0x00", "0x01"]},
#                 # {"ID": "0x10", "Res": ["0x00", "0x10", "0x00", "0x00"]},
#                 {"ID": "0x11", "Res": ["0x00", "0x1E", "0x00", "0x03"]},
#                 {"ID": "0x12", "Res": ["0x00", "0x68", "0x03", "0x01"]},
#                 {"ID": "0x13", "Res": ["0x00", "0x6A", "0x02", "0x00"]},
#                 {"ID": "0x14", "Res": ["0x00", "0x7C", "0x00", "0x01"]},
#                 {"ID": "0x15", "Res": ["0x00", "0x7D", "0x00", "0x03"]},
#                 {"ID": "0x16", "Res": ["0x00", "0x7E", "0x03", "0x45"]},
#                 {"ID": "0x17", "Res": ["0x00", "0x7F", "0x02", "0x63"]},
#                 {"ID": "0x18", "Res": ["0x00", "0x6C", "0x32", "0x31"]},
#                 {"ID": "0x19", "Res": ["0x00", "0x6D", "0x10", "0x03"]},
#                 {"ID": "0x20", "Res": ["0x00", "0x6E", "0x03", "0x15"]},
#                 {"ID": "0x21", "Res": ["0x00", "0x6F", "0x02", "0x23"]},
#                 {"ID": "0x22", "Res": ["0x00", "0x81", "0x00", "0x01"]},
#                 {"ID": "0x23", "Res": ["0x00", "0x83", "0x00", "0x00"]},
#                 {"ID": "0x24", "Res": ["0x00", "0x85", "0x00", "0x00"]},
#                 {"ID": "0x25", "Res": ["0x00", "0x87", "0x00", "0x00"]},
#                 {"ID": "0x26", "Res": ["0x00", "0x8B", "0x00", "0x01"]},
#                 {"ID": "0x27", "Res": ["0x00", "0x8D", "0x00", "0x00"]},
#                 {"ID": "0x28", "Res": ["0x00", "0x8F", "0x00", "0x00"]},
#                 {"ID": "0x29", "Res": ["0x00", "0x91", "0x00", "0x00"]},
#                 {"ID": "0x01", "Res": ['0x11', '0x23', '0x76', '0x02']},
#                 # {"ID": "0x02", "Res": ['0x11', '0x24', '0x47', '0x02']},
#                 {"ID": "0x03", "Res": ['0x11', '0x96', '0x14', '0x02']},
#                 {"ID": "0x04", "Res": ['0x11', '0x34', '0x12', '0x02']},
#                 {"ID": "0x05", "Res": ['0x11', '0x43', '0x11', '0x02']},
#                 {"ID": "0x06", "Res": ['0x11', '0x17', '0x51', '0x02']},
#             ]
#         },
#         {
#             "ID": "0xF1",
#             "Responses": [
#                 {"ID": "0x01", "Res": ['0x11', '0x16', '0x26', '0x03']},
#                 {"ID": "0x02", "Res": ['0x11', '0x44', '0x02', '0x03']},
#                 {"ID": "0x03", "Res": ['0x11', '0x01', '0x34', '0x03']},
#                 {"ID": "0x04", "Res": ['0x11', '0x24', '0x11', '0x03']},
#                 {"ID": "0x05", "Res": ['0x11', '0x25', '0x41', '0x03']},
#                 {"ID": "0x06", "Res": ['0x11', '0x47', '0x23', '0x03']},
#                 {"ID": "0x01", "Res": ['0x11', '0x53', '0x16', '0x04']},
#                 {"ID": "0x02", "Res": ['0x11', '0x04', '0x41', '0x04']},
#                 {"ID": "0x03", "Res": ['0x11', '0x66', '0x04', '0x04']},
#                 {"ID": "0x04", "Res": ['0x11', '0x14', '0x72', '0x04']},
#                 {"ID": "0x05", "Res": ['0x11', '0x41', '0x41', '0x04']},
#                 {"ID": "0x06", "Res": ['0x11', '0x13', '0x51', '0x04']},
#             ]
#         }
#     ]
# }

# Function to interpret door errors
'''
'Door_Error': [
                {'DataCmdID': '0xF0', 'CmdID': '0x01', 'byte0_ids': '0x11', 'byte1_ids': '0x01', 'Cmds': ['0x11', '0x01', '0x00', '$List'], 'Res': ['0x11', '0x46', '0x76', '0x01']},
                {'DataCmdID': '0xF0', 'CmdID': '0x04', 'byte0_ids': '0x11', 'byte1_ids': '0x02', 'Cmds': ['0x11', '0x02', '0x00', '$List'], 'Res': ['0x11', '0x34', '0x41', '0x01']},
                {'DataCmdID': '0xF0', 'CmdID': '0x02', 'byte0_ids': '0x11', 'byte1_ids': '0x11', 'Cmds': ['0x11', '0x11', '0x00', '$List'], 'Res': ['0x11', '0x24', '0x12', '0x01']},
                {'DataCmdID': '0xF0', 'CmdID': '0x03', 'byte0_ids': '0x11', 'byte1_ids': '0x11', 'Cmds': ['0x11', '0x11', '0x01', '$List'], 'Res': ['0x11', '0x41', '0x14', '0x01']},
                {'DataCmdID': '0xF0', 'CmdID': '0x05', 'byte0_ids': '0x11', 'byte1_ids': '0x12', 'Cmds': ['0x11', '0x12', '0x00', '$List'], 'Res': ['0x11', '0x75', '0x11', '0x01']},
                {'DataCmdID': '0xF0', 'CmdID': '0x06', 'byte0_ids': '0x11', 'byte1_ids': '0x12', 'Cmds': ['0x11', '0x12', '0x01', '$List'], 'Res': ['0x11', '0x17', '0x23', '0x01']}
            ]
'''
def InterpretDoorErrorResponse(Door_Error):
    try:
        door_error = []
        error_type_list = []
        if Door_Error:

            # Getting unique list of error types
            for i in Door_Error:
                error_type = i['Res'][3]
                if len(error_type_list)==0:
                    error_type_list.append(error_type)
                if len(error_type_list)!=0 and error_type not in error_type_list:
                    error_type_list.append(error_type)

            # Sorting door error response based on unique error type
            error_res_dict = {}
            for i in error_type_list:
                error_res_list = []
                for j in Door_Error:
                    if j['Res'][3] == i:
                        error_res_list.append(j)
                error_res_dict[i] = error_res_list

            # Interpreting door error for each error type with respect to left door and right door
            for x,y in error_res_dict.items():
                LD_cum_count = None
                RD_cum_count = None
                LD_occ_count_1 = None
                LD_occ_count_2 = None
                RD_occ_count_1 = None
                RD_occ_count_2 = None

                for i in y:

                    # Checking left door commands for cumulative count
                    if i['Cmds'][1] == '0x01':
                        if i['Cmds'][2] == '0x00':
                            byte1 = i['Res'][1]
                            byte0 = i['Res'][2]
                            LD_cum_count = int(byte1, 16) << 8 | int(byte0, 16)

                    # Checking right door commands for cumulative count
                    elif i['Cmds'][1] == '0x02':
                        if i['Cmds'][2] == '0x00':
                            byte1 = i['Res'][1]
                            byte0 = i['Res'][2]
                            RD_cum_count = int(byte1, 16) << 8 | int(byte0, 16)

                    # Checking left door commands for cyclic occurrence count
                    elif i['Cmds'][1] == '0x11':
                        if i['Cmds'][2] == '0x00':
                            byte1 = i['Res'][1]
                            byte0 = i['Res'][2]
                            LD_occ_count_1 = int(byte1, 16) << 8 | int(byte0, 16)
                        elif i['Cmds'][2] == '0x01':
                            byte3 = i['Res'][1]
                            byte2 = i['Res'][2]
                            LD_occ_count_2 = int(byte3, 16) << 8 | int(byte2, 16)

                    # Checking right door commands for cyclic occurrence count
                    elif i['Cmds'][1] == '0x12':
                        if i['Cmds'][2] == '0x00':
                            byte1 = i['Res'][1]
                            byte0 = i['Res'][2]
                            RD_occ_count_1 = int(byte1, 16) << 8 | int(byte0, 16)
                        elif i['Cmds'][2] == '0x01':
                            byte3 = i['Res'][1]
                            byte2 = i['Res'][2]
                            RD_occ_count_2 = int(byte3, 16) << 8 | int(byte2, 16)

                # Checking if any byte missing if yes then ignoring the corresponding response
                Error = {}
                Error['ErrorType'] = int(x, 16)
                if LD_cum_count is not None:
                    Error['left_door_cumulative_count'] = LD_cum_count
                if LD_occ_count_1 is not None and LD_occ_count_2 is not None:
                    Error['left_door_occurrence_count'] = LD_occ_count_2 << 16 | LD_occ_count_1
                if RD_cum_count is not None:
                    Error['right_door_cumulative_count'] = RD_cum_count
                if RD_occ_count_1 is not None and RD_occ_count_2 is not None:
                    Error['right_door_occurrence_count'] = RD_occ_count_2 << 16 | RD_occ_count_1

                door_error.append(Error)

        return door_error
    except Exception as e:
        print(e)

# Function to interpret Door status value and LCP Firmware Version
'''
'Door_Status': [{'DataCmdID': '0xF0', 'CmdID': '0x08', 'byte0_ids': '0x00', 'byte1_ids': '0x00', 'Cmds': ['0x00', '0x00', '0x00', '0x00'], 'Res': ['0x00', '0x00', '0x00', '0x01']}]
'''
def InterpretDoorStatusResponse(Door_Status):

    try:
        door_status = []

        # Checking condition to get DOOR STATUS value and lcp firmware version
        if Door_Status:
            for i in Door_Status:
                status = {}
                byte1 = i['Res'][1]
                status_value = int(byte1, 16)
                high_byte = i['Res'][2]
                low_byte = i['Res'][3]
                lcp_firm_version = int(high_byte, 16) << 8 | int(low_byte, 16)

                # Assigning interpreted status value and lcp firmware version
                status['status_value'] = status_value
                status['lcp_firm_version'] = lcp_firm_version
                door_status.append(status)

        return door_status
    except Exception as e:
        print(e)

# Function to interpret Motor status value and MCP Firmware Version
'''
'Motor_Status': [   
                    {'DataCmdID': '0xF0', 'CmdID': '0x09', 'byte0_ids': '0x10', 'byte1_ids': '0x00', 'Cmds': ['0x10', '0x00', '0x00', '0x00'], 'Res': ['0x00', '0x10', '0x00', '0x01']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x10', 'byte0_ids': '0x10', 'byte1_ids': '0x01', 'Cmds': ['0x10', '0x01', '0x00', '0x00'], 'Res': ['0x00', '0x10', '0x00', '0x00']}
                ]
'''
def InterpretMotorStatusResponse(Motor_Status):
    try:
        motor_status = []
        if Motor_Status:
            m_s = {}
            mcp_firm_ver_1 = None
            mcp_firm_ver_2 = None
            for i in Motor_Status:
                byte1 = i['Res'][1]
                status_value = int(byte1, 16)

                # Checking condition for first command
                if i['Cmds'][1] == '0x00':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    mcp_firm_ver_1 = int(high_byte, 16) << 8 | int(low_byte, 16)

                # Checking condition for second command
                elif i['Cmds'][1] == '0x01':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    mcp_firm_ver_2 = int(high_byte, 16) << 8 | int(low_byte, 16)

            # Checking if any byte missing to interpret MCP firmware version
            if mcp_firm_ver_1 is not None and mcp_firm_ver_2 is not None:
                mcp_firm_version = mcp_firm_ver_2 << 16 | mcp_firm_ver_1
                m_s['status_value'] = status_value
                m_s['mcp_firm_version'] = mcp_firm_version
                motor_status.append(m_s)

        return motor_status
    except Exception as e:
        print(e)

# Function to interpret door switch mode
'''
'Door_Switch_Mode': [{'DataCmdID': '0xF0', 'CmdID': '0x11', 'byte0_ids': '0x1E', 'byte1_ids': '0x00', 'Cmds': ['0x1E', '0x00', '0x00', '0x00'], 'Res': ['0x00', '0x1E', '0x00', '0x03']}]
'''
def InterpretDoorSwitchModeResponse(Door_Switch_Mode):

    try:
        door_switch_mode = []

        # Checking condition to get Door switch mode value
        if Door_Switch_Mode:
            for i in Door_Switch_Mode:
                status = {}
                byte3 = i['Res'][3]
                switch_mode_value = int(byte3, 16)
                status['switch_mode_value'] = switch_mode_value
                door_switch_mode.append(status)

        return door_switch_mode
    except Exception as e:
        print(e)

# Function to interpret System cycle count
'''
'sys_cycle_count': [
                    {'DataCmdID': '0xF0', 'CmdID': '0x12', 'byte0_ids': '0x01', 'byte1_ids': '0x68', 'Cmds': ['0x01', '0x68', '0x00', '0x00'], 'Res': ['0x00', '0x68', '0x03', '0x01']}, 
                    {'DataCmdID': '0xF0', 'CmdID': '0x13', 'byte0_ids': '0x01', 'byte1_ids': '0x6A', 'Cmds': ['0x01', '0x6A', '0x00', '0x00'], 'Res': ['0x00', '0x6A', '0x02', '0x00']}
                ]
'''
def getSystemCycleCount(sys_cycle_count):
    try:
        if sys_cycle_count:
            for i in sys_cycle_count:

                # Checcking condition for first command
                if i['byte1_ids']=='0x68':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    sys_cycle_count_1 = int(high_byte, 16) << 8 | int(low_byte, 16)

                # Checking condition for second command
                elif i['byte1_ids']=='0x6A':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    sys_cycle_count_2 = int(high_byte, 16) << 8 | int(low_byte, 16)

            # Interpreting responses to get system cycle count
            system_cyc_count = sys_cycle_count_2 << 16 | sys_cycle_count_1

        return system_cyc_count
    except Exception as e:
        print(e)

# Interpreting Motor 1/ Door 1 system cycle count
'''
'motor1Response': [
                    {'DataCmdID': '0xF0', 'CmdID': '0x14', 'byte0_ids': '0x03', 'byte1_ids': '0x7C', 'Cmds': ['0x03', '0x7C', '0x00', '0x00'], 'Res': ['0x00', '0x7C', '0x00', '0x01']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x15', 'byte0_ids': '0x03', 'byte1_ids': '0x7D', 'Cmds': ['0x03', '0x7D', '0x00', '0x00'], 'Res': ['0x00', '0x7D', '0x00', '0x03']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x16', 'byte0_ids': '0x03', 'byte1_ids': '0x7E', 'Cmds': ['0x03', '0x7E', '0x00', '0x00'], 'Res': ['0x00', '0x7E', '0x03', '0x45']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x17', 'byte0_ids': '0x03', 'byte1_ids': '0x7F', 'Cmds': ['0x03', '0x7F', '0x00', '0x00'], 'Res': ['0x00', '0x7F', '0x02', '0x63']}
                ]
'''
def InterpretMotorOneResponse(motor1Response):
    try:
        if motor1Response:
            for i in motor1Response:

                # Checcking condition for all four commands to interpret motor1/door1 system cycle count
                if i['byte1_ids'] == '0x7C':
                    res1 = i['Res'][3]
                elif i['byte1_ids'] == '0x7D':
                    res2 = i['Res'][3]
                elif i['byte1_ids'] == '0x7E':
                    res3 = i['Res'][3]
                elif i['byte1_ids'] == '0x7F':
                    res4 = i['Res'][3]

            # Interpreting the motor1/door1 system cycle count using the given formula
            motor1_sys_cyc_count = 1000000 * int(res1, 16) + 10000 * int(res2, 16) + 100 * int(res3, 16) + int(res4, 16)

        return motor1_sys_cyc_count
    except Exception as e:
        print(e)

# Interpreting Motor 2/ Door 2 system cycle count
'''
'motor2Response':[
                    {'DataCmdID': '0xF0', 'CmdID': '0x18', 'byte0_ids': '0x03', 'byte1_ids': '0x6C', 'Cmds': ['0x03', '0x6C', '0x00', '0x00'], 'Res': ['0x00', '0x6C', '0x32', '0x31']}, 
                    {'DataCmdID': '0xF0', 'CmdID': '0x19', 'byte0_ids': '0x03', 'byte1_ids': '0x6D', 'Cmds': ['0x03', '0x6D', '0x00', '0x00'], 'Res': ['0x00', '0x6D', '0x10', '0x03']}, 
                    {'DataCmdID': '0xF0', 'CmdID': '0x20', 'byte0_ids': '0x03', 'byte1_ids': '0x6E', 'Cmds': ['0x03', '0x6E', '0x00', '0x00'], 'Res': ['0x00', '0x6E', '0x03', '0x15']}, 
                    {'DataCmdID': '0xF0', 'CmdID': '0x21', 'byte0_ids': '0x03', 'byte1_ids': '0x6F', 'Cmds': ['0x03', '0x6F', '0x00', '0x00'], 'Res': ['0x00', '0x6F', '0x02', '0x23']},
                ]
'''
def InterpretMotorTwoResponse(motor2Response):
    try:
        if motor2Response:
            for i in motor2Response:

                # Checcking condition for all four commands to interpret motor2/door2 system cycle count
                if i['byte1_ids'] == '0x6C':
                    res1 = i['Res'][3]
                elif i['byte1_ids'] == '0x6D':
                    res2 = i['Res'][3]
                elif i['byte1_ids'] == '0x6E':
                    res3 = i['Res'][3]
                elif i['byte1_ids'] == '0x6F':
                    res4 = i['Res'][3]

            # Interpreting the motor2/door2 system cycle count using the given formula
            motor2_sys_cyc_count = 1000000 * int(res1, 16) + 10000 * int(res2, 16) + 100 * int(res3, 16) + int(res4, 16)

        return motor2_sys_cyc_count
    except Exception as e:
        print(e)

# Function to interpret one byte response to get door type, motor1/door1 system cycle count and motor2/door2 system cycle count
'''
'OneByteResponse': [{'DataCmdID': '0xF0', 'CmdID': '0x07', 'byte0_ids': '0x03', 'byte1_ids': '0x00', 'Cmds': ['0x03', '0x00', '0x00', '0x00'],  'Res': ['0x00', '0x03', '0x00', '0x02']},  ............................]
'''
def InterpretOneByteResponse(OneByteResponse):
    try:
        one_byte_response = []
        if OneByteResponse:
            one_byte_res = {}
            motor1Response = []
            motor2Response = []

            # Iterating through the OneByteResponse
            for i in OneByteResponse:

                # Checking if byte1 is '0x00' to interpret door type
                if i['byte1_ids'] == '0x00':
                    byte3 = i['Res'][3]
                    door_type_id = int(byte3, 16)

                # Checking motor1/door1 commands to interpret motor1/door1 system cycle count
                elif i['byte1_ids'] == '0x7C':
                    motor1Response.append(i)
                elif i['byte1_ids'] == '0x7D':
                    motor1Response.append(i)
                elif i['byte1_ids'] == '0x7E':
                    motor1Response.append(i)
                elif i['byte1_ids'] == '0x7F':
                    motor1Response.append(i)

                # Checking motor2/door2 all commands to interpret motor2/door2 system cycle count
                elif i['byte1_ids'] == '0x6C':
                    motor2Response.append(i)
                elif i['byte1_ids'] == '0x6D':
                    motor2Response.append(i)
                elif i['byte1_ids'] == '0x6E':
                    motor2Response.append(i)
                elif i['byte1_ids'] == '0x6F':
                    motor2Response.append(i)

            # Checking condition for door type
            if door_type_id:
                one_byte_res['door_type'] = door_type_id

            # Checking condition for motor1Response and calling the function InterpretMotorOneResponse
            if len(motor1Response) == 4:
                motor1_res = InterpretMotorOneResponse(motor1Response)
                one_byte_res['motor1_sys_cyc_count'] = motor1_res

            # Checking condition for motor2Response and calling the function InterpretMotorTwoResponse
            if len(motor2Response) == 4:
                motor2_res = InterpretMotorTwoResponse(motor2Response)
                one_byte_res['motor2_sys_cyc_count'] = motor2_res

            if one_byte_res:
                one_byte_response.append(one_byte_res)

        return one_byte_response
    except Exception as e:
        print(e)

# Function to interpret Active Door ID
'''
'active_door': [
                {'DataCmdID': '0xF0', 'CmdID': '0x22', 'byte0_ids': '0x01', 'byte1_ids': '0x81', 'Cmds': ['0x01', '0x81', '0x00', '0x00'], 'Res': ['0x00', '0x81', '0x00', '0x01']},
                {'DataCmdID': '0xF0', 'CmdID': '0x23', 'byte0_ids': '0x01', 'byte1_ids': '0x83', 'Cmds': ['0x01', '0x83', '0x00', '0x00'], 'Res': ['0x00', '0x83', '0x00', '0x00']},
                {'DataCmdID': '0xF0', 'CmdID': '0x24', 'byte0_ids': '0x01', 'byte1_ids': '0x85', 'Cmds': ['0x01', '0x85', '0x00', '0x00'], 'Res': ['0x00', '0x85', '0x00', '0x00']},
                {'DataCmdID': '0xF0', 'CmdID': '0x25', 'byte0_ids': '0x01', 'byte1_ids': '0x87', 'Cmds': ['0x01', '0x87', '0x00', '0x00'], 'Res': ['0x00', '0x87', '0x00', '0x00']}
            ]
'''
def getActiveDoorID(active_door):
    try:
        if active_door:
            for i in active_door:

                # Checcking condition for all four commands to interpret Active Door ID
                if i['byte1_ids'] == '0x81':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    active_res1 = int(high_byte, 16) << 8 | int(low_byte, 16)
                elif i['byte1_ids'] == '0x83':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    active_res2 = int(high_byte, 16) << 8 | int(low_byte, 16)
                elif i['byte1_ids'] == '0x85':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    active_res3 = int(high_byte, 16) << 8 | int(low_byte, 16)
                elif i['byte1_ids'] == '0x87':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    active_res4 = int(high_byte, 16) << 8 | int(low_byte, 16)

            # Interpreting responses to get ACTIVE DOOR ID
            Active_Door_ID = (active_res4 << 16 | active_res3) << 32 | (active_res2 << 16 | active_res1)

        return Active_Door_ID
    except Exception as e:
        print(e)

# Function to interpret Original Door ID
'''
'original_door': [
                    {'DataCmdID': '0xF0', 'CmdID': '0x26', 'byte0_ids': '0x01', 'byte1_ids': '0x8B', 'Cmds': ['0x01', '0x8B', '0x00', '0x00'], 'Res': ['0x00', '0x8B', '0x00', '0x01']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x27', 'byte0_ids': '0x01', 'byte1_ids': '0x8D', 'Cmds': ['0x01', '0x8D', '0x00', '0x00'], 'Res': ['0x00', '0x8D', '0x00', '0x00']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x28', 'byte0_ids': '0x01', 'byte1_ids': '0x8F', 'Cmds': ['0x01', '0x8F', '0x00', '0x00'], 'Res': ['0x00', '0x8F', '0x00', '0x00']},
                    {'DataCmdID': '0xF0', 'CmdID': '0x29', 'byte0_ids': '0x01', 'byte1_ids': '0x91', 'Cmds': ['0x01', '0x91', '0x00', '0x00'], 'Res': ['0x00', '0x91', '0x00', '0x00']}
                ]
'''
def getOriginalDoorID(original_door):
    try:
        if original_door:
            for i in original_door:

                # Checcking condition for all four commands to interpret Original Door ID
                if i['byte1_ids'] == '0x8B':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    original_res1 = int(high_byte, 16) << 8 | int(low_byte, 16)
                elif i['byte1_ids'] == '0x8D':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    original_res2 = int(high_byte, 16) << 8 | int(low_byte, 16)
                elif i['byte1_ids'] == '0x8F':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    original_res3 = int(high_byte, 16) << 8 | int(low_byte, 16)
                elif i['byte1_ids'] == '0x91':
                    high_byte = i['Res'][2]
                    low_byte = i['Res'][3]
                    original_res4 = int(high_byte, 16) << 8 | int(low_byte, 16)

            # Interpreting responses to get ORIGINAL DOOR ID
            Original_Door_ID = (original_res4 << 16 | original_res3) << 32 | (original_res2 << 16 | original_res1)

        return Original_Door_ID
    except Exception as e:
        print(e)

# Function to interpret two byte response for system cycle count, active door id and original door id
'''
'twoByteResponse': [{'DataCmdID': '0xF0', 'CmdID': '0x12', 'byte0_ids': '0x01', 'byte1_ids': '0x68', 'Cmds': ['0x01', '0x68', '0x00', '0x00'], 'Res': ['0x00', '0x68', '0x03', '0x01']}, ...................................]
'''
def InterpretTwoByteResponse(twoByteResponse):
    try:
        two_byte_res = []
        if twoByteResponse:
            two_byte_response = {}
            system_cycle_count = []
            active_door = []
            original_door = []

            # Iterating through the two byte response
            for i in twoByteResponse:

                # To Check condition for system cycle count commands
                if i['byte1_ids'] == '0x68':
                    system_cycle_count.append(i)
                elif i['byte1_ids'] == '0x6A':
                    system_cycle_count.append(i)

                # To Check condition for Active door ID commands
                elif i['byte1_ids'] == '0x81':
                    active_door.append(i)
                elif i['byte1_ids'] == '0x83':
                    active_door.append(i)
                elif i['byte1_ids'] == '0x85':
                    active_door.append(i)
                elif i['byte1_ids'] == '0x87':
                    active_door.append(i)

                # To Check condition for Original door ID commands
                elif i['byte1_ids'] == '0x8B':
                    original_door.append(i)
                elif i['byte1_ids'] == '0x8D':
                    original_door.append(i)
                elif i['byte1_ids'] == '0x8F':
                    original_door.append(i)
                elif i['byte1_ids'] == '0x91':
                    original_door.append(i)

            # Checking condition for system cycle count and call the function to interpret  system cycle count
            if len(system_cycle_count)==2:
                sys_cycle_count = getSystemCycleCount(system_cycle_count)
                two_byte_response['system_cycle_count'] = sys_cycle_count

            # Checking condition for active door and call the function to interpret active door id
            if len(active_door)==4:
                active_door_id = getActiveDoorID(active_door)
                two_byte_response['active_door_id'] = active_door_id

            # Checking condition for original door and call the function to interpret original door id
            if len(original_door)==4:
                original_door_id = getOriginalDoorID(original_door)
                two_byte_response['original_door_id'] = original_door_id

            if two_byte_response:
                two_byte_res.append(two_byte_response)

        return two_byte_res
    except Exception as e:
        print(e)

''' Intermediate function to check condition on key and call the 
    the respective function '''
'''
'parent_dict': {
                '0x11': [{'DataCmdID': '0xF0', 'CmdID': '0x01', 'byte0_ids': '0x11', 'byte1_ids': '0x01', 'Cmds': ['0x11', '0x01', '0x00', '$List'],  'Res': ['0x11', '0x46', '0x76',  '0x01']}, ............................]
                
                '0x03': [{'DataCmdID': '0xF0', 'CmdID': '0x07', 'byte0_ids': '0x03', 'byte1_ids': '0x00', 'Cmds': ['0x03', '0x00', '0x00', '0x00'],  'Res': ['0x00', '0x03', '0x00', '0x02']},  ............................]
                
                '0x00': [{'DataCmdID': '0xF0', 'CmdID': '0x08', 'byte0_ids': '0x00', 'byte1_ids': '0x00', 'Cmds': ['0x00', '0x00', '0x00', '0x00'], 'Res': ['0x00', '0x00', '0x00', '0x01']}],
                
                '0x10': [{'DataCmdID': '0xF0', 'CmdID': '0x09', 'byte0_ids': '0x10', 'byte1_ids': '0x00', 'Cmds': ['0x10', '0x00', '0x00', '0x00'], 'Res': ['0x00', '0x10', '0x00', '0x01']},
                        {'DataCmdID': '0xF0', 'CmdID': '0x10', 'byte0_ids': '0x10', 'byte1_ids': '0x01', 'Cmds': ['0x10', '0x01', '0x00', '0x00'], 'Res': ['0x00', '0x10', '0x00', '0x00']}],
                
                '0x1E': [{'DataCmdID': '0xF0', 'CmdID': '0x11', 'byte0_ids': '0x1E', 'byte1_ids': '0x00', 'Cmds': ['0x1E', '0x00', '0x00', '0x00'], 'Res': ['0x00', '0x1E', '0x00', '0x03']}],
                
                '0x01': [{'DataCmdID': '0xF0', 'CmdID': '0x12', 'byte0_ids': '0x01', 'byte1_ids': '0x68', 'Cmds': ['0x01', '0x68', '0x00', '0x00'], 'Res': ['0x00', '0x68', '0x03', '0x01']}, ...................................]
            }
'''
def dcu_cmd_function_call(parent_dict):
    try:
        response = []
        if parent_dict:

            for x,y in parent_dict.items():

                # Checking condition for DOOR ERROR and calling the corresponding DOOR ERROR function
                if x == '0x11':
                    door_error = {}
                    d_e = InterpretDoorErrorResponse(y)
                    door_error[x] = d_e
                    response.append(door_error)

                # Checking condition for DOOR STATUS and calling the corresponding DOOR STATUS function
                elif x == '0x00':
                    door_status = {}
                    d_s = InterpretDoorStatusResponse(y)
                    door_status[x] = d_s
                    response.append(door_status)

                # Checking condition for MOTOR STATUS and calling the corresponding MOTOR STATUS function
                elif x == '0x10':
                    motor_status = {}
                    m_s = InterpretMotorStatusResponse(y)
                    motor_status[x] = m_s
                    response.append(motor_status)

                # Checking condition for DOOR SWITCH MODE and calling the corresponding DOOR SWITCH MODE function
                elif x == '0x1E':
                    motor_status = {}
                    m_s = InterpretDoorSwitchModeResponse(y)
                    motor_status[x] = m_s
                    response.append(motor_status)

                # Checking condition for TWO BYTE RESPONSE and calling the corresponding TWO BYTE RESPONSE FUNCTION
                # to interpret SYSTEM CYCLE COUNT, ACTIVE DOOR ID and ORIGINAL DOOR ID
                elif x == '0x01':
                    two_byte_res = {}
                    s_c = InterpretTwoByteResponse(y)
                    two_byte_res[x] = s_c
                    response.append(two_byte_res)

                # Checking condition for ONE BYTE RESPONSE and calling the corresponding ONE BYTE FUNCTION
                # to interpret DOOR TYPE, MOTOR1 SYSTEM CYCLE COUNT and MOTOR2 SYSTEM CYCLE COUNT
                elif x == '0x03':
                    one_byte_res = {}
                    d_t = InterpretOneByteResponse(y)
                    one_byte_res[x] = d_t
                    response.append(one_byte_res)

        return response
    except Exception as e:
        print(e)

''' Main Function to get input json and response json.
    Check the input json confi version with response json.
    if version matches go ahead and segregate the json as per respective byte0 and byte1 value from the command groups.
    After creating sorted dictionary call the function  'dcu_cmd_function_call' '''
def dcu_command_parser(input_json, response_json):

    try:
        Result = []
        input_command_grps = input_json['DataCommandGroup']
        response_command_grps = response_json['DataCommandGroup']
        input_conf_ver_no = input_json['Metadata']['ConfigVerNo']
        res_conf_ver_no = response_json['Metadata']['ConfigVerNo']
        input_dev_pro_id = input_json['Metadata']['Device_profile_id']
        res_dev_pro_id = response_json['Metadata']['Device_profile_id']

        # Checking input json and response json have same version no. and device profile id

        if input_conf_ver_no==res_conf_ver_no and input_dev_pro_id==res_dev_pro_id:
            for i in input_command_grps:
                for j in response_command_grps:

                    # Checking input command group id matched with response command group id
                    if i['ID'] == j['ID']:
                        datacmdres = {}
                        datacmdid = i['ID']
                        commands = i['Commands']
                        Responses = j['Responses']

                        DataCmdID = []
                        CmdID = []
                        Cmds = []
                        Res = []
                        byte0_ids = []
                        byte1_ids = []

                        # Creating list for data command group id, command id, byte0 id, byte1 id, commands and response
                        for p in Responses:
                            DataCmdID.append(datacmdid)
                            for q in commands:
                                if q['ID'] == p['ID']:
                                    CmdID.append(q['ID'])
                                    Cmds.append(q['Cmd'])
                                    Res.append(p['Res'])
                                    byte0_ids.append(q['Cmd'][0])
                                    byte1_ids.append(q['Cmd'][1])
                                    break

                        # Making dataframe using list of DataCmdID, CmdID, Fun_ID, Cmds and Res
                        df = pd.DataFrame({'DataCmdID': DataCmdID, 'CmdID': CmdID, 'byte0_ids':byte0_ids, 'byte1_ids':byte1_ids, 'Cmds': Cmds, 'Res':Res})
                        sorted_df = df.sort_values(by=['byte0_ids', 'byte1_ids'])

                        # Getting unique list of byte0 id
                        byte0_list = df.byte0_ids.unique()

                        # Converting sorted dataframe to list of dictionary
                        sorted_list = sorted_df.to_dict('records')

                        parent_dict = {}
                        # Creating Main sorted parent dictionary using byte0_id as keys
                        for r in byte0_list:
                            child_list = []
                            for s in sorted_list:
                                if s['byte0_ids'] == r:
                                    child_list.append(s)
                            parent_dict[r] = child_list

                        # Calling and passing the parent dictionary
                        result = dcu_cmd_function_call(parent_dict)
                        datacmdres[datacmdid] = result
                        Result.append(datacmdres)
                        break

        else:
            response = {}
            response['message'] = "Input json and response json has not matching either config version or device profile id"
            response['status_code'] = 204
            response['status'] = False
            Result.append(response)

        return Result
    except Exception as e:
        print(e)

#print(dcu_command_parser(input_json, response_json))
if __name__ == "__main__":
    input_json_path = sys.argv[1]
    response_json_path = sys.argv[2]
    output_json_path = sys.argv[3]

    with open(input_json_path) as file:
        input_json = json.load(file)
    with open(response_json_path) as file:
        response_json = json.load(file)
    with open(output_json_path) as file:
        output_json = json.load(file)

    print("Expected Output::::",output_json)
    output_from_code = dcu_command_parser(input_json, response_json)
    # print("\n\nOutput from code::::", dcu_command_parser(input_json, response_json))
    with open('.\jsonfiles\result.json', 'w') as fp:
        json.dump(output_from_code, fp)
