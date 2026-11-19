def dfa_at_least_three_ones(s: str) -> bool:
    """
    Simulates a DFA that accepts strings containing at least three 1s over {0, 1}.
    States represent the count of 1s encountered so far: 
      - 0: q0 (Start)
      - 1: q1 (One '1' seen)
      - 2: q2 (Two '1's seen)
      - 3: q3 (Three or more '1's seen - Accepting state)
    """
    current_state = 0  # Start at state q0
    
    for char in s:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid character '{char}'. Alphabet must be {{0, 1}}[span_1](start_span)[span_1](end_span).")
        
        if current_state == 0:
            if char == '1':
                current_state = 1
            # If '0', stay in state 0 (loops on q0)
            
        elif current_state == 1:
            if char == '1':
                current_state = 2
            # If '0', stay in state 1 (loops on q1)
            
        elif current_state == 2:
            if char == '1':
                current_state = 3
            # If '0', stay in state 2 (loops on q2)
            
        elif current_state == 3:
            # Once state q3 (accepting) is reached, any further '0' or '1' 
            # keeps it in state 3.
            pass

    # The string is accepted if the final state is q3 (state 3)
    return current_state == 3

# --- Test Cases ---
if __name__ == "__main__":
    test_strings = [
        "001110",  # Contains three 1s -> True
        "10101",   # Contains three 1s -> True
        "1111",    # Contains four 1s -> True
        "00011",   # Contains only two 1s -> False
        "0000"     # Contains zero 1s -> False
    ]
    
    for test_str in test_strings:
        result = dfa_at_least_three_ones(test_str)
        print(f"String: '{test_str}' --> Accepted? {result}")