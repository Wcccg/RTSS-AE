from subprocess import run
import datetime
import random

def RD_GEN_user(n, ns, ne, O_degree, I_degree):
    seed = str(random.randint(1, 999))
    I_list = []
    for i in range(I_degree):
        I_list.append(i+1)
    I_list = str(I_list)
    O_list = []
    for i in range(O_degree):
        O_list.append(i+1)
    O_list =str(O_list)

    Note=open('fan_in_fan_out.yaml',mode='w')
    
    fan_in_fan_out_setting = ''
    fan_in_fan_out_setting += 'Seed: '+seed+'\n'
    fan_in_fan_out_setting += 'Number of DAGs: '+'1'+'\n'
    fan_in_fan_out_setting += 'Graph structure:\n'
    fan_in_fan_out_setting +='  Generation method: "Fan-in/Fan-out"\n'
    fan_in_fan_out_setting +='  Number of nodes:'+n+'\n'
    fan_in_fan_out_setting +='      Fixed: 20\n'
    fan_in_fan_out_setting +='  In-degree:\n'
    fan_in_fan_out_setting +='      Random: '+I_list+'\n'
    fan_in_fan_out_setting +='  Out-degree:\n'
    fan_in_fan_out_setting +='      Random: '+O_list+'\n'
    fan_in_fan_out_setting +='  Number of source nodes:\n'
    fan_in_fan_out_setting +='      Fixed: '+str(ns)+'\n'
    fan_in_fan_out_setting +='  Number of sink nodes:\n'
    fan_in_fan_out_setting +='      Fixed: '+str(ne)+'\n'
    fan_in_fan_out_setting +='  Ensure weakly connected: True\n'
    fan_in_fan_out_setting +='\n'
    fan_in_fan_out_setting +='Properties:\n'
    fan_in_fan_out_setting +='  Execution time:\n'
    fan_in_fan_out_setting +='      Random: (1, 50, 1)\n'
    fan_in_fan_out_setting +='\n'
    fan_in_fan_out_setting +='Output formats:\n'
    fan_in_fan_out_setting +='  Naming of combination directory: "Abbreviation"\n'
    fan_in_fan_out_setting +='  DAG:\n'
    fan_in_fan_out_setting +='      YAML: True\n'
    fan_in_fan_out_setting +='      JSON: False\n'
    fan_in_fan_out_setting +='      XML: False\n'
    fan_in_fan_out_setting +='      DOT: False\n'
    fan_in_fan_out_setting +='  Figure:\n'
    fan_in_fan_out_setting +='      Draw legend: False\n'
    fan_in_fan_out_setting +='      PNG: True\n'
    fan_in_fan_out_setting +='      SVG: False\n'
    fan_in_fan_out_setting +='      EPS: False\n'
    fan_in_fan_out_setting +='      PDF: False\n'
    Note.write(fan_in_fan_out_setting)
    Note.close()
    command = 'python run_generator.py -c ./fan_in_fan_out.yaml'
    run(command, shell = True) 
    # command = 'python ./useRD-Gen/run_generator.py -c ./useRD-Gen/fan_in_fan_out.yaml'
    # run(command, shell = True)
    return







    
    # Graph structure:
    # Generation method: "Fan-in/Fan-out"
    # Number of nodes:
    #     Fixed: 20
    # In-degree:
    #     Random: [1, 2, 3]
    # Out-degree:
    #     Random: [1, 2, 3]
    # Number of source nodes:
    #     Combination: (1, 5, 1)
    # Number of sink nodes:
    #     Combination: (1, 5, 1)
    # Ensure weakly connected: True

    # Properties:
    # Execution time:
    #     Random: (1, 50, 1)

    # Output formats:
    # Naming of combination directory: "Abbreviation"
    # DAG:
    #     YAML: True
    #     JSON: False
    #     XML: False
    #     DOT: False
    # Figure:
    #     Draw legend: False
    #     PNG: True
    #     SVG: False
    #     EPS: False
    #     PDF: False

