//==================================================================
// 《剑指Offer——名企面试官精讲典型编程题》代码
//==================================================================
// 面试题5：替换空格
// 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
// 则输出“We%20are%20happy.”

// 用swift来做这道题目感觉怪怪的😓
// 本意是要求在时间复杂度O(n)下完成
// 方法是先查找出所有的空格，计算出替换之后字符串的长度L，然后在原字符串L处开始从尾到头进行替换

import Foundation
import XCTest

class Solution {
    /**
     - Parameters:
        - charArray 输入的字符数组
     - Returns: 替换之后的字符数组
     */
    func replace(_ charArray: [Character]) -> [Character] {
        /// TODO
        return charArray
    }
}

class UnitTests: XCTestCase {
    var solution: Solution!
    
    override func setUp() {
        super.setUp()
        solution = Solution()
    }
}
