;Header and description

(define (domain control)

;remove requirements that are not needed
(:requirements :strips :typing :negative-preconditions )

(:types ;todo: enumerate types and their hierarchy here, e.g. car truck bus - vehicle
  led motor dustbin - object
   l1 l2 - led
   m1 m2 - motor
   d1 d2 - dustbin
)
; un-comment following line if constants are needed
;(:constants )

(:predicates ;todo: define predicates here
  (wetdustbin-control)
  (drydustbin-control)
  (off1 ?l1 - led)
  (off2 ?l2 - led)
  (on1 ?m1 - motor)
  (on2 ?m2 - motor)

)

(:functions ;todo: define numeric functions here
  (ultra ?d2 - dustbin)
  (ultra-weight ?d1 - dustbin)
     (ultra_threshold)
     (ultra-weight_threshold)
)


(:action wet_actuation
      :parameters (?l1 - led ?m1 - motor ?d1 - dustbin)
      :precondition (and (off1 ?l1) (on1 ?m1) (>(ultra-weight ?d1)(ultra-weight_threshold)))
      :effect (and (not(off1 ?l1)) (not(on1 ?m1)) (wetdustbin-control))
)
(:action wet-no-actuation
      :parameters (?l1 - led ?m1 - motor ?d1 - dustbin)
      :precondition (and (off1 ?l1) (on1 ?m1) (<(ultra-weight ?d1)(ultra-weight_threshold)))
      :effect (and (off1 ?l1) (on1 ?m1) (wetdustbin-control))
)
(:action dry_actuation
      :parameters (?l2 - led ?m2 - motor ?d2 - dustbin)
      :precondition (and (off2 ?l2) (on2 ?m2) (>(ultra ?d2)(ultra_threshold)))
      :effect (and (not(off2 ?l2)) (not(on2 ?m2)) (drydustbin-control))
)

(:action dry-no-actuation
      :parameters (?l2 - led ?m2 - motor ?d2 - dustbin)
      :precondition (and (off2 ?l2) (on2 ?m2) (<(ultra ?d2)(ultra_threshold)))
      :effect (and (off2 ?l2) (on2 ?m2) (drydustbin-control))
)


;define actions here

)
