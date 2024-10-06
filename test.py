

import re

def check_snmp_acl(config_file):
    with open(config_file, 'r') as file:
        config_lines = file.readlines()
    
    # 定義匹配 SNMP ACL 的正則表達式
    snmp_acl_pattern = re.compile(r'snmp-server community \S+ (RO|RW) use-acl (\S+)')
    acl_rule_pattern = re.compile(r'ip access-list (standard|extended) (\S+)')
    acl_entry_pattern = re.compile(r'permit ip 10\.21\.28\.0 0\.0\.0\.255')

    acl_rules = {}
    for line in config_lines:
        snmp_match = snmp_acl_pattern.search(line)
        acl_match = acl_rule_pattern.search(line)

        # 如果是 SNMP 配置行，記錄使用的 ACL 名稱
        if snmp_match:
            acl_name = snmp_match.group(2)
            acl_rules[acl_name] = False  # 初始化為 False

        # 如果是 ACL 定義行，則檢查條目
        if acl_match:
            current_acl_name = acl_match.group(2)

            # 檢查 ACL 條目是否包含指定網段
            if current_acl_name in acl_rules:
                for entry in config_lines[config_lines.index(line)+1:]:
                    if entry.strip() == 'exit':
                        break
                    if acl_entry_pattern.search(entry):
                        acl_rules[current_acl_name] = True
                        break

    # 檢查結果
    for acl_name, has_entry in acl_rules.items():
        if has_entry:
            print(f"ACL '{acl_name}' contains the entry for 10.21.28.0/24.")
        else:
            print(f"ACL '{acl_name}' does not contain the entry for 10.21.28.0/24.")






