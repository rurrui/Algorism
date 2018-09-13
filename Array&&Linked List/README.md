# 数组和链表的操作比较
<table>
    <tr>
        <th>
            种类
        </th>
        <th>
            查找
        </th>
         <th>
            插入
        </th>
         <th>
            删除
        </th>
    </tr>
     <tr>
        <th>
            数组
        </th>
        <th>
            O(1)
        </th>
         <th>
            O(n)
        </th>
         <th>
            O(n)
        </th>
    </tr>
    <tr>
        <th>
            链表
        </th>
        <th>
            O(n)
        </th>
         <th>
            O(1)
        </th>
         <th>
            O(1)
        </th>
    </tr>
</table>

Note:  
1.数组是线性排列的  
2.链表的排列是非线性的  
3.数组的位置用索引标记，所以支持随机访问  
4.链表的位置由相邻元素保存了链表的地址，所以不可以随机访问，必须从第一个元素one by one地链接过来  
5.数组的删除和添加操作需要移动操作元素后的所有元素，所以比较耗费时间  
6.链表删除添加元素只需要把相邻元素的指向地址修改，所以执行速度很快