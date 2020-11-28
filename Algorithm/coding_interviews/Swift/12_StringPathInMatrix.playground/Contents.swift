//==================================================================
// 《剑指Offer——名企面试官精讲典型编程题》代码
//==================================================================
// 面试题12：矩阵中的路径
// 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
// 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
// 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
// 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
// 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
// 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
// A B T G
// C F C S
// J D E H

import Foundation
import XCTest

class Solution {
    /**
     判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
     - Parameters:
        - matrix: 字符矩阵
        - path: 需要查找的字符串
     - Returns: 是否存在
     */
    func Find(_ matrix: [[Character]], _ path: String) -> Bool{
        var visited = Array(repeating: Array(repeating: false, count: matrix[0].count), count: matrix.count)
        var pathIndex = 0
        for row in 0..<matrix.count {
            for col in 0..<matrix[row].count {
                if FindCore(matrix: matrix, row: row, col: col, path: path,
                            pathIndex: &pathIndex, visited: &visited) {
                    return true
                }
            }
        }
        return false
    }
    /**
     查找matrix的第row行和第col列的字符是否和path的第pathIndex个字符相同
     并判断矩阵相邻的字符串是否与pathIndex下一个字符相同
     - Parameters:
        - matrix: 字符矩阵
        - row: 矩阵第row行
        - col: 矩阵第col列
        - path: 查找的字符串
        - pathIndex: 当前查找的第pathIndex个字符
        - visited：已经对比过的记录
     - Returns: 是否相同
     */
    private func FindCore(matrix: [[Character]], row: Int, col: Int, path: String,
                          pathIndex: inout Int, visited: inout [[Bool]]) -> Bool{
        if pathIndex >= path.count {
            return true
        }
        var result = false
        if(row >= 0 && row < matrix.count && col >= 0 && col < matrix[0].count &&
            matrix[row][col] == path[path.index(path.startIndex, offsetBy: pathIndex)] && !visited[row][col]) {
            pathIndex += 1
            visited[row][col] = true
            result = FindCore(matrix: matrix, row: row, col: col - 1, path: path, pathIndex: &pathIndex, visited: &visited) ||
                FindCore(matrix: matrix, row: row - 1, col: col, path: path, pathIndex: &pathIndex, visited: &visited) ||
                FindCore(matrix: matrix, row: row, col: col + 1, path: path, pathIndex: &pathIndex, visited: &visited) ||
                FindCore(matrix: matrix, row: row + 1, col: col, path: path, pathIndex: &pathIndex, visited: &visited)
            
            if !result {
                pathIndex -= 1
                visited[row][col] = false
            }
        }
        return result
    }
}


class UnitTests: XCTestCase {
    var solution: Solution!
    
    override func setUp() {
        super.setUp()
        solution = Solution()
    }
    //ABTG
    //CFCS
    //JDEH
    func testCase1() {
        let matrix: [[Character]] = [["A","B","T","G"],["C","F","C","S"],["J","D","E","H"]]
        let str = "BFCE"
        XCTAssertTrue(solution.Find(matrix, str))
    }
    //ABCE
    //SFCS
    //ADEE
    func testCase2() {
        let matrix: [[Character]] = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        let str = "SEE"
        XCTAssertTrue(solution.Find(matrix, str))
    }
    //ABTG
    //CFCS
    //JDEH
    func testCase3() {
        let matrix: [[Character]] = [["A","B","T","G"],["C","F","C","S"],["J","D","E","H"]]
        let str = "ABFB"
        XCTAssertFalse(solution.Find(matrix, str))
    }
    
    //ABCEHJIG
    //SFCSLOPQ
    //ADEEMNOE
    //ADIDEJFM
    //VCEIFGGS
    func testCase4() {
        let matrix: [[Character]] = [["A","B","C","E","H","J","I","G"],
                                     ["S","F","C","S","L","O","P","Q"],
                                     ["A","D","E","E","M","N","O","E"],
                                     ["A","D","I","D","E","J","F","M"],
                                     ["V","C","E","I","F","G","G","S"]]
        let str = "SLHECCEIDEJFGGFIE"
        XCTAssertTrue(solution.Find(matrix, str))
    }
    
    //ABCEHJIG
    //SFCSLOPQ
    //ADEEMNOE
    //ADIDEJFM
    //VCEIFGGS
    func testCase5() {
        let matrix: [[Character]] = [["A","B","C","E","H","J","I","G"],
                                     ["S","F","C","S","L","O","P","Q"],
                                     ["A","D","E","E","M","N","O","E"],
                                     ["A","D","I","D","E","J","F","M"],
                                     ["V","C","E","I","F","G","G","S"]]
        let str = "SGGFIECVAASABCEHJIGQEM"
        XCTAssertTrue(solution.Find(matrix, str))
    }
    //ABCEHJIG
    //SFCSLOPQ
    //ADEEMNOE
    //ADIDEJFM
    //VCEIFGGS
    func testCase6() {
        let matrix: [[Character]] = [["A","B","C","E","H","J","I","G"],
                                     ["S","F","C","S","L","O","P","Q"],
                                     ["A","D","E","E","M","N","O","E"],
                                     ["A","D","I","D","E","J","F","M"],
                                     ["V","C","E","I","F","G","G","S"]]
        let str = "SGGFIECVAASABCEEJIGOEM"
        XCTAssertFalse(solution.Find(matrix, str))
    }
    
    //ABCEHJIG
    //SFCSLOPQ
    //ADEEMNOE
    //ADIDEJFM
    //VCEIFGGS
    func testCase7() {
        let matrix: [[Character]] = [["A","B","C","E","H","J","I","G"],
                                     ["S","F","C","S","L","O","P","Q"],
                                     ["A","D","E","E","M","N","O","E"],
                                     ["A","D","I","D","E","J","F","M"],
                                     ["V","C","E","I","F","G","G","S"]]
        let str = "SGGFIECVAASABCEHJIGQEMS"
        XCTAssertFalse(solution.Find(matrix, str))
    }
    
    //AAAA
    //AAAA
    //AAAA
    func testCase8() {
        let matrix: [[Character]] = [["A","A","A","A"],["A","A","A","A"],["A","A","A","A"]]
        let str = "AAAAAAAAAAAA" //12
        XCTAssertTrue(solution.Find(matrix, str))
    }
    
    //AAAA
    //AAAA
    //AAAA
    func testCase9() {
        let matrix: [[Character]] = [["A","A","A","A"],["A","A","A","A"],["A","A","A","A"]]
        let str = "AAAAAAAAAAAAA" //13
        XCTAssertFalse(solution.Find(matrix, str))
    }
    
    func testCase10() {
        let matrix: [[Character]] = [["A"]]
        let str = "A"
        XCTAssertTrue(solution.Find(matrix, str))
    }
    
    func testCase11() {
        let matrix: [[Character]] = [["A"]]
        let str = "B"
        XCTAssertFalse(solution.Find(matrix, str))
    }
}

//UnitTests.defaultTestSuite.run()
