import nbformat

with open('main.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

modified = False
for cell in nb.cells:
    if cell.cell_type == 'code':
        if 'class SkipGramNCE(nn.Module):' in cell.source:
            old_line = 'neg_dot = torch.bmm(v_ni, -v_wc.unsqueeze(2)).squeeze()'
            new_line = 'neg_dot = torch.bmm(v_ni, v_wc.unsqueeze(2)).squeeze() # Fixed bug: removed minus sign'
            if old_line in cell.source:
                cell.source = cell.source.replace(old_line, new_line)
                modified = True

if modified:
    with open('main.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Notebook successfully fixed.")
else:
    print("Bug not found or already fixed.")
