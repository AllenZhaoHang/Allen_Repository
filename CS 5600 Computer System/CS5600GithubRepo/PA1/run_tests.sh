#!/bin/bash
# 自动化测试脚本

echo "======================================"
echo "CS5600 PA1 Shell 自动化测试"
echo "======================================"
echo ""

# 确保shell已编译
if [ ! -f "./shell" ]; then
    echo "错误: shell程序未找到，正在编译..."
    make
    if [ $? -ne 0 ]; then
        echo "编译失败！"
        exit 1
    fi
fi

# 测试计数器
TOTAL_TESTS=0
PASSED_TESTS=0

# 测试函数
run_test() {
    local test_name=$1
    local test_file=$2
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo "----------------------------------------"
    echo "测试 $TOTAL_TESTS: $test_name"
    echo "----------------------------------------"
    
    if [ ! -f "$test_file" ]; then
        echo "❌ 失败: 测试文件 $test_file 不存在"
        return 1
    fi
    
    ./shell "$test_file" > /tmp/shell_output_$$.txt 2>&1
    local exit_code=$?
    
    echo "输出："
    cat /tmp/shell_output_$$.txt
    echo ""
    echo "退出码: $exit_code"
    
    # 简单检查: 如果测试文件包含quit，退出码应该是0
    if grep -q "quit" "$test_file"; then
        if [ $exit_code -eq 0 ]; then
            echo "✅ 通过"
            PASSED_TESTS=$((PASSED_TESTS + 1))
        else
            echo "❌ 失败: 预期退出码0，实际为 $exit_code"
        fi
    else
        # 无quit命令的文件也应该正常退出
        if [ $exit_code -eq 0 ]; then
            echo "✅ 通过"
            PASSED_TESTS=$((PASSED_TESTS + 1))
        else
            echo "❌ 失败: 预期退出码0，实际为 $exit_code"
        fi
    fi
    
    rm -f /tmp/shell_output_$$.txt
    echo ""
}

# 错误处理测试
test_error_handling() {
    local test_name=$1
    local expected_exit=$2
    shift 2
    local args="$@"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo "----------------------------------------"
    echo "测试 $TOTAL_TESTS: $test_name"
    echo "----------------------------------------"
    echo "命令: ./shell $args"
    
    ./shell $args > /tmp/shell_output_$$.txt 2>&1
    local exit_code=$?
    
    echo "输出："
    cat /tmp/shell_output_$$.txt
    echo ""
    echo "退出码: $exit_code (预期: $expected_exit)"
    
    if [ $exit_code -eq $expected_exit ]; then
        echo "✅ 通过"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "❌ 失败"
    fi
    
    rm -f /tmp/shell_output_$$.txt
    echo ""
}

# 运行批处理文件测试
if [ -f "test_basic.txt" ]; then
    run_test "基本命令" "test_basic.txt"
fi

if [ -f "test_concurrent.txt" ]; then
    run_test "并发命令" "test_concurrent.txt"
fi

if [ -f "test_quit.txt" ]; then
    run_test "Quit命令" "test_quit.txt"
fi

if [ -f "test_empty.txt" ]; then
    run_test "空命令处理" "test_empty.txt"
fi

if [ -f "test_no_quit.txt" ]; then
    run_test "无Quit命令" "test_no_quit.txt"
fi

if [ -f "test_errors.txt" ]; then
    run_test "错误命令处理" "test_errors.txt"
fi

if [ -f "test_output.txt" ]; then
    if [ -f "./output" ]; then
        run_test "Output程序并发测试" "test_output.txt"
    else
        echo "跳过 Output 测试（output程序未编译）"
    fi
fi

if [ -f "test_args.txt" ]; then
    run_test "带参数的命令" "test_args.txt"
fi

if [ -f "test_paths.txt" ]; then
    run_test "完整路径命令" "test_paths.txt"
fi

if [ -f "test_spaces.txt" ]; then
    run_test "额外空格处理" "test_spaces.txt"
fi

# 错误处理测试
test_error_handling "错误参数数量" 1 file1.txt file2.txt
test_error_handling "不存在的批处理文件" 1 nonexistent_file_xyz.txt

# 总结
echo "======================================"
echo "测试完成"
echo "======================================"
echo "总测试数: $TOTAL_TESTS"
echo "通过: $PASSED_TESTS"
echo "失败: $((TOTAL_TESTS - PASSED_TESTS))"
echo ""

if [ $PASSED_TESTS -eq $TOTAL_TESTS ]; then
    echo "🎉 所有测试通过！"
    exit 0
else
    echo "⚠️  有测试失败"
    exit 1
fi
