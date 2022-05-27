{
    "mem_server_id":{
        "required":True,
        'type': 'number',
        'regex': '/^([0-9]{1})$/',
        'schema':{
            "memory_type":{
                "required": True,
                "type": 'string',
                'regex':'/vol|per/',
            },
            "fam_path":{
                "required": True,
                "type": 'string',
                'regex':'(/vol|per/)/$'
            },
            "rpc_interface":{
                "required": True,
                "type": 'string',
                "regex":'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?=:)[0-9]{4}$/'
            },
            "libfabric_port":{
                "required": True,
                "type": 'number',
                "min":1000,
                "max":9999,
            },
            "if_device":{
                "required": True,
                "type": 'string',
                'regex': "^.[0-9]{1}/$",
            }
        }
    }
}