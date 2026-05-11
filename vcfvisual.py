import pandas as pd
import svgwrite


#================================

filename    = 'tst.vcf'
max_x       = 4411532               # M. tuberculosis H37Rv genome length 
outputfile  = 'out.svg'

dim_x       = 3000
dim_y       = 200
round_to    = 2
opacity     = 0.5
line_wid    = 0.4

#================================

#--- vcf reading
vcf_pos     = []
vcf_qual    = []
fn_open     = open
with fn_open(filename) as fh:
    for line in fh:
        if not line.startswith('#'):
            rec = line.strip().split('\t')
            vcf_pos.append(int(rec[1]))
            vcf_qual.append(float(rec[5]))
nrec    = len(vcf_pos)
max_y   = max(vcf_qual)


#-----
dwg = svgwrite.Drawing(outputfile, size = (dim_x+2,dim_y+2), debug=True)
shapes = dwg.add(dwg.g(id='shapes'))
color = svgwrite.rgb(0, 0, 100, '%')
shapes.add(dwg.line((0,0),(dim_x+2,0), stroke=color, stroke_width=line_wid))
shapes.add(dwg.line((dim_x+2,0),(dim_x+2,dim_y+2), stroke=color, stroke_width=line_wid))
shapes.add(dwg.line((dim_x+2,dim_y+2),(0,dim_y+2), stroke=color, stroke_width=line_wid))
shapes.add(dwg.line((0,dim_y+2),(0,0), stroke=color, stroke_width=line_wid))

for i in range(0,nrec):
    x = round(dim_x/max_x*vcf_pos[i],round_to)
    y = round(dim_y*vcf_qual[i]/max_y,round_to)
    color = svgwrite.rgb(0, 0, 0, '%')
    shapes.add(dwg.line((x+1,dim_y+1),(x+1, dim_y-y+1), stroke=color, stroke_width=line_wid, stroke_opacity=opacity))
dwg.save()








