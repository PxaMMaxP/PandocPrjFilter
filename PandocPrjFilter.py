import panflute as pf

def filter_prj_codeblocks(elem, doc):
    # Find all code blocks with the class 'prj'
    # In Markdown, this would be 
    # ```prj
    # ...
    # ```
    if isinstance(elem, pf.CodeBlock) and 'prj' in elem.classes:
        # Remove the code block from the document
        return []

def main(doc=None):
    return pf.run_filter(filter_prj_codeblocks, doc=doc)

if __name__ == '__main__':
    main()