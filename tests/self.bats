load harness

@test "self-1" {
  check 'x := 1 ; x = 1 ? x := x + 1 : x := 3' '⇒ skip; if (x=1) then { x := (x+1) } else { x := 3 }, {x → 1}
⇒ if (x=1) then { x := (x+1) } else { x := 3 }, {x → 1}
⇒ x := (x+1), {x → 1}
⇒ skip, {x → 2}'
}

@test "self-2" {
  check '0 < x ∧ 4 < y ? x := 1 : x := 3' '⇒ x := 3, {}
⇒ skip, {x → 3}'
}

@test "self-3" {
  check 'false ? kj := 12 : while false do l0 := 0' '⇒ while false do { l0 := 0 }, {}
⇒ skip, {}'
}

@test "self-4" {
  check 'while false do x := 1 ; true ? y := 1 : z := 1' '⇒ skip; if true then { y := 1 } else { z := 1 }, {}
⇒ if true then { y := 1 } else { z := 1 }, {}
⇒ y := 1, {}
⇒ skip, {y → 1}'
}

@test "self-5" {
  check '( y < z ) ? g := 3 : gh := 2' '⇒ gh := 2, {}
⇒ skip, {gh → 2}'
}