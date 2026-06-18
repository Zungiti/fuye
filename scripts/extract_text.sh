#!/bin/bash
# 提取 .docx / .pdf 文本内容
# 用法: bash extract_text.sh <input_file> [output_file]

set -e
INPUT="$1"
OUTPUT="${2:-/tmp/proofread_text.txt}"
EXT="${INPUT##*.}"

case "$EXT" in
  docx)
    pandoc "$INPUT" -t plain -o "$OUTPUT" 2>/dev/null
    ;;
  pdf)
    pdftotext -layout "$INPUT" "$OUTPUT" 2>/dev/null
    ;;
  txt|md)
    cp "$INPUT" "$OUTPUT"
    ;;
  *)
    echo "Unsupported format: $EXT" >&2
    exit 1
    ;;
esac

echo "$OUTPUT"
