target = "gowin"
action = "synthesis"

syn_family = "GW5"
syn_family_surfix = "A"
syn_device_prefix = "LV"
syn_device = "25"
syn_grade = "NES"
syn_device_version = "A"
syn_package = "MG121"
syn_top = "top"
syn_properties = [{'use_i2c_as_gpio' : '1', 'use_sspi_as_gpio' : '1', 'use_cpu_as_gpio' : '1'}]
syn_project = "pmod_led"
syn_tool = "gowin"

modules = {"local" :
              [ "src" ]
          }
