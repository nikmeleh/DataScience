import numpy as np

def random_predict(number:int=1) -> int:
    """Random predicting of number

    Args:
        number (int, optional): Intended number. Defaults to 1.

    Returns:
        int: Count of tries
    """
    
    count = 0
    predict_number = 0 
    while True:
        count += 1
        
        if predict_number > number:
            predict_number -= 1 #уменьшаем число на 1 если оно больше загаданного
        
        elif predict_number < number:
            predict_number += 10 #увеличиваем число на 10 если оно меньше
        
        else:
            break # конец игры
        
    return(count)

def score_game(random_predict) -> int:
    """How much tries need to predict number after 1000 repeats

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
    
    print(f'the mean count tries of predicting the number by your program is: {score} ')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)