import json

from datasets import load_dataset
from test import check_correctness

def main():
    ds = load_dataset("codeparrot/apps", "all")
    
    i=0
    for element in ds['train']:
        element['solutions']=json.loads(element['solutions'])
        element['input_output']=json.loads(element['input_output'])

        for sol in element['solutions']:
            # test=generate(sol)
            pass

            #for test_case in test:
            #    element['input_output']['inputs'].append(test_case['input'])
            #    element['input_output']['outputs'].append(test_case['output])

        # print(element['input_output'])

        result = check_correctness(element, element['solutions'][0], 5, False)

        test_case_number=len(result)        
        passed_case=sum(result)

        i+=1
        if i==1:
            break

if __name__ == "__main__":
    main()
