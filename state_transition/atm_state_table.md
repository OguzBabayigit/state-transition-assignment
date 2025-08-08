# ATM - State Transition Table

## States
1. Start
2. WaitForPin
3. AccessGranted
4. CardEaten

## Events / Transitions
- Start -> WaitForPin : user starts ATM
- WaitForPin -> AccessGranted : correct PIN entered
- WaitForPin -> WaitForPin : incorrect PIN entered and tries < 3
- WaitForPin -> CardEaten : incorrect PIN entered and tries >= 3
- AccessGranted -> Start : user logs out / finishes

## Table
| State \ Event | enter_start | correct_pin | incorrect_pin (tries<3) | incorrect_pin (tries>=3) | logout |
| --- | ---: | ---: | ---: | ---: | ---: |
| Start | WaitForPin |  |  |  |  |
| WaitForPin |  | AccessGranted | WaitForPin | CardEaten |  |
| AccessGranted |  |  |  |  | Start |
| CardEaten |  |  |  |  |  |
