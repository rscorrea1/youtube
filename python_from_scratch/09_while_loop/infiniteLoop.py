######################################
# Let's learn while loops in Python! #
######################################

# boss battle: level easy
boss_life = 100
hit_damage = 10
print("Boss life:", boss_life)
while boss_life > 0:
    # hit the boss
    boss_life = boss_life - hit_damage
    print("Hit! => Boss life:", boss_life)
print("The Boss is no longer alive. You won!")
