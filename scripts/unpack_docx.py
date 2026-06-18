#!/usr/bin/env python3
"""解包 .docx 文件，提取 XML 格式信息用于深度模式第三轮检查"""
import zipfile, sys, os, json

def unpack_docx(docx_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with zipfile.ZipFile(docx_path) as z:
        z.extractall(output_dir)

    info = {}
    info_path = os.path.join(output_dir, 'format_info.json')
    with open(info_path, 'w') as f:
        json.dump({
            'files': os.listdir(os.path.join(output_dir, 'word')),
            'has_footer': os.path.exists(os.path.join(output_dir, 'word', 'footer1.xml')),
            'has_header': os.path.exists(os.path.join(output_dir, 'word', 'header1.xml')),
        }, f, ensure_ascii=False, indent=2)

    print(f"Unpacked to {output_dir}")
    print(f"Format info: {info_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: unpack_docx.py <input.docx> <output_dir>")
        sys.exit(1)
    unpack_docx(sys.argv[1], sys.argv[2])
