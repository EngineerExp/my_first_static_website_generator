import os
import shutil
from generate_pages_recursive import generate_pages_recursive

def copy_src_to_dst(src_path, dst_path):
    # Ensure the destination directory exists
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    for item in os.listdir(src_path):
        src_item_path = os.path.join(src_path, item)
        dst_item_path = os.path.join(dst_path, item)

        if os.path.isfile(src_item_path) and not item.endswith('Zone.Identifier'):
            print(f"Copying file: \n{src_item_path} to \n{dst_item_path}")
            shutil.copy(src_item_path, dst_item_path)
        elif os.path.isdir(src_item_path):
            print(f"Entering directory:\n{src_item_path}")
            # Recursively call the function for subdirectories
            copy_src_to_dst(src_item_path, dst_item_path)

# ... (your main function setup) ...

def main():
    print("Welcome to My First Static Website Generator!")

    # delete public directory if it exists
    public_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')
    if os.path.exists(public_dir):
        print(f"Deleting existing public directory: {public_dir}")
        shutil.rmtree(public_dir)

    # remake public directory
    print(f"Creating public directory: {public_dir}")
    os.makedirs(public_dir)

    # define source and destination directories
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_static_dir = os.path.join(project_root, 'static')
    dst_public_dir = os.path.join(project_root, 'public')

    print(f"\nStarting copy from \n{src_static_dir} to \n{dst_public_dir}")
    copy_src_to_dst(src_static_dir, dst_public_dir)
    print("\nCopy process complete!\n")

    # reciursively generate pages from content markdown files to public directory as html files
    from_path = os.path.join(project_root, 'content')
    template_path = os.path.join(project_root, 'template.html')
    dest_path = os.path.join(project_root, 'public')
    generate_pages_recursive(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()