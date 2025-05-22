def sum_list_substring(base_list: list[str]) -> None:
    """
  Sums each number in the list of strings, if letter is present in the string catches it and outputs a message.
  :param base_list: input list of strings
  """
    for item in base_list:
        item_splt = item.split(",")
        # print(sum(int(new_item) for new_item in item_splt if new_item.isdigit()))
        total = 0
        for new_item in item_splt:
            if new_item.isdigit():
                total += int(new_item)
            else:
                raise ValueError("Can't do that.")
        print(total)


try:
    sum_list_substring(["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"])
except ValueError as e:
    print(e)