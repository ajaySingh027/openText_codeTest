# importing argparse lib for reading users input in a beautiful way
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("namesList", nargs="+", type=str, help="List of unordered company names")
parser.add_argument("--order", default='False', choices=['False', 'True'], help= "Order for ascending or descending")
args = parser.parse_args()


def compNames_filter(sequence, reverse=False):
  '''
  Input: 
    sequence: list of unordered company names
    reverse: [default is False: ascending] ascending or descending alphabetical order
  
  Output:
    returns the sorted filtered list of company names
  '''
  # order False is for ascending order
  order = reverse

  if len(sequence) <=1:
    return sequence
  
  else:
    # declaring pivot point as median
    pivot = sequence.pop()

  left_lower_seq = []
  right_high_seq = []

  # iterating over each element in sequence
  for item in sequence:
    if item.lower().strip() > pivot.lower().strip():
      right_high_seq.append(item)

    else:
      left_lower_seq.append(item)
          
  if order == 'False':
    return compNames_filter(left_lower_seq, order) + [pivot] + compNames_filter(right_high_seq, order)
  else:
    return compNames_filter(right_high_seq, order) + [pivot] + compNames_filter(left_lower_seq, order)



if __name__ == '__main__':

  compList = (args.namesList)
  reverse = str(args.order)
  # print(reverse)
  print(compNames_filter(compList, reverse))