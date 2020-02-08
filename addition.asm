li $t0 4
sw $t0 0($sp)
li $t0 4
sw $t0 -4($sp)
lw $t1 0($sp)
mul $t0 $t0 $t1
sw $t0 0($sp)
li $t0 3
sw $t0 -4($sp)
sw $t0 -4($sp)
lw $t1 0($sp)
add $t0 $t0 $t1
sw $t0 0($sp)
li $t0 5
sw $t0 -4($sp)
li $t0 5
sw $t0 -8($sp)
lw $t1 -4($sp)
mul $t0 $t0 $t1
sw $t0 -4($sp)
lw $t0 0($sp)
sw $t0 -8($sp)
sw $t0 -8($sp)
lw $t0 -4($sp)
sw $t0 -12($sp)
sw $t0 -12($sp)
lw $t1 -8($sp)
add $t0 $t0 $t1
sw $t0 -8($sp)

