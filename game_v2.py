import numpy as np

def random_predict(number:int=1) -> int:
    """Random predicting of number

    Args:
        number (int, optional): Intended number. Defaults to 1.

    Returns:
        int: Count of tries
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
         
        if number == predict_number:
            break
        
    return(count)
print(f'Count of tries: {random_predict()}')

def score_game(random_predict) -> int:
    """How much tries need to predict number with 1000 repeats

    Args:
        random_predict (_type_): predicting function

    Returns:
        int: mean count of tries
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'the mean count tries of predicting the number by ypur program is: {score} ')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)