class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        max_index = damage.index(max_damage)

        if armor >= max_damage:
            damage[max_index] = 0
        else:
            damage[max_index] = damage[max_index] - armor

        return sum(damage) + 1