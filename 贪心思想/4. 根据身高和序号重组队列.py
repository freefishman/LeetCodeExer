# 406. Queue Reconstruction by Height(Medium)
class Solution:
    def reconstructQueue(people):
        if len(people) <= 1:
            return people

        ## 对队列排序，先按h降序，再按k升序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = [people[0]]  # 这个人是从前往后、从上往下看到的第一个人
        for i in people[1:]:
            new_people.insert(i[1], i)
        return new_people
print(Solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))