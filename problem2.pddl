(define (problem problem_name) (:domain control)
(:objects 
;u1 - sensor
;p1 - sensor
l1 -  led
l2 - led
m1 - motor
m2 - motor
d1 - dustbin
d2 - dustbin
)


(:init
    ;(Usensor Usensor1) (Psensor Psensor1)  (motor motor1)
    (off1 l1)
    (off2 l2)
    (on1 m1)
    (on2 m2)
    ;initialise sensor
    (=(ultra_threshold) 25)
    (=(ultra d2) 26)
    (=(ultra-weight_threshold) 28)
    (=(ultra-weight d1) 27)
)

(:goal(and (wetdustbin-control)
         (drydustbin-control))
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
