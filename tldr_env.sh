#!/bin/bash

# 获取脚本所在的目录
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # 解析 $SOURCE 直到脚本的真实路径
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # 如果是相对路径，则解析为绝对路径
done
SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"


if ! grep -q "export PATH=$SCRIPT_DIR" ~/.bashrc; then
  echo "export PATH=$SCRIPT_DIR:\$PATH" >> ~/.bashrc
  echo "export PATH=$SCRIPT_DIR:\$PATH"
fi

CONFIG_FILE="$SCRIPT_DIR/tip"
if [ -f "$CONFIG_FILE" ]; then
  sed -i "s|current_directory *= *\".*\"|current_directory = \"$SCRIPT_DIR\"|" $CONFIG_FILE
else
  echo "Warning: Configuration file not found at $CONFIG_FILE"
fi

source ~/.bashrc

chmod u+x "$SCRIPT_DIR/tip"

echo "tldr environment variable configuration successful!"
