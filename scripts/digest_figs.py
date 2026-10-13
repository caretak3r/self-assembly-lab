"""Generate schematic SVG figures for daily digest pages (public/images/latest/).
Schematics are illustrative concept sketches, not data from the papers."""
import math, os, random
OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'images', 'latest')
# icon kinds: cluster, lattice, network, swarm, droplet, chain, curve, fold, rotor, layers
SPEC = {
 '2026-09-16': [('cluster','Nanocubes','depletion + shape','surface arrays'),('lattice','Colloids','corrugated surface','guided crystals'),('swarm','Robots','continuous tweaks','covering structures')],
 '2026-09-17': [('layers','Capsid proteins','molecular imaging','virus-like particle'),('network','DNA nanostars','membrane packing','tuned dynamics'),('cluster','Hard + soft grains','shaking','self-organised mix')],
 '2026-09-18': [('chain','Active filaments','phase separation','spontaneous network'),('lattice','>100 RNA parts','programmed pairing','RNA nanostructures'),('fold','Star polymers','active embrace','autonomous tweezing')],
 '2026-09-21': [('droplet','Colloidal raft','swimming strokes','droplet propulsion'),('network','Dynamic bonds','pySNAP pipeline','soft networks'),('swarm','Active particles','circular obstacles','condensation')],
 '2026-09-22': [('droplet','Droplets','chemical gradient','propulsion'),('curve','Soft glass','activity','yielding/flow'),('rotor','Inertial rotors','spin','phase separation')],
 '2026-09-23': [('layers','Curved shells','geometric frustration','self-limited stacks'),('lattice','Tetrahedra','cylinder confinement','dense packings'),('swarm','Microswimmers','environment','motility statistics')],
 '2026-09-24': [('cluster','Proteins','free-boundary growth','aggregate shapes'),('curve','Active walker','uphill vs downhill','first passage'),('layers','Liquid crystal','twist-bend interface','ordering')],
 '2026-09-25': [('rotor','Janus beads','triangular array','spin-like order'),('swarm','Tracers','active chemistry','faster diffusion'),('fold','Origami hinges','bistable buckling','reprogrammable folds')],
 '2026-09-28': [('swarm','Motile spheres','collective order','active engine'),('network','Collagen','shear while gelling','stiffer network'),('chain','Semi-rigid polymers','packing','left/right helices')],
 '2026-09-29': [('swarm','Nematodes','push soft walls','moving fingers'),('cluster','Agents','quorum sensing','spots + mazes'),('network','3D weaves','active fibers','load-bearing robots')],
 '2026-09-30': [('rotor','Bead pairs','acoustic trap','rocking -> chaos'),('rotor','Quincke spinners','ratchet','plasma engine'),('droplet','Hydrogel capsule','magnetothermal latch','fast release')],
 '2026-10-01': [('rotor','Spinners + colloids','chirality transfer','passive rotors'),('swarm','Active fluid','vortex web spans','turbulence transition'),('curve','Many routes','active Reynolds no.','one threshold')],
 '2026-10-02': [('swarm','Bacteria','tilted dish','biased swarming'),('cluster','Active particles','box walls','ideal-gas law'),('chain','Peptides','generative MD','assembly paths')],
 '2026-10-05': [('chain','Peptide pairs','mix partners','nanotapes'),('droplet','Cell clusters','surface tension','asymmetric motion'),('swarm','1,000 spacecraft','magnetic coils','shared structure')],
 '2026-10-06': [('layers','Polymer platelets','37 C melt','hollow + rebuild'),('chain','Giant melts','bond swaps','local tangles'),('cluster','Active particles','random obstacles','slower clumping')],
 '2026-10-07': [('network','Robots','local branch swaps','near-Steiner tree'),('lattice','Triblock ellipses','patchy ends','kagome/porous'),('network','Topological gels','sliding rings','reprogrammable')],
 '2026-10-08': [('network','Soft parts','fluidic logic','circuits w/o chips'),('fold','Robot bodies','filter/route/switch','mechanical intelligence'),('chain','Cyanobacteria','twisting glide','dense clumps')],
 '2026-10-09': [('fold','Soft swimmer','2 air channels','3 swim modes'),('lattice','Silicone + iron','48 recipes','magnetic soft robots'),('curve','Shape capsules','warm/cool spots','mobile heat engine')],
 '2026-10-12': [('cluster','DNA + RNA','growing ice','nanoparticles'),('droplet','Cell spheroids','microbubbles','stacked assemblies'),('lattice','Charged fluids','charge frustration','fixed-size patterns')],
}
BG,CARD,EDGE,TXT,SUB,ACC='#0f172a','#1e293b','#38bdf8','#e2e8f0','#94a3b8','#f472b6'
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def icon(kind, cx, cy, rnd):
    o=[]
    if kind=='cluster':
        for i in range(14):
            a=rnd.random()*6.28; r=rnd.random()*38
            o.append(f'<circle cx="{cx+r*math.cos(a):.1f}" cy="{cy+r*math.sin(a):.1f}" r="7" fill="{EDGE}" opacity=".85"/>')
    elif kind=='lattice':
        for i in range(-2,3):
            for j in range(-2,3):
                x=cx+i*18+(j%2)*9; y=cy+j*16
                o.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{EDGE}"/>')
    elif kind=='network':
        pts=[(cx+rnd.uniform(-45,45),cy+rnd.uniform(-35,35)) for _ in range(9)]
        for i,p in enumerate(pts):
            for q in pts[i+1:]:
                if math.dist(p,q)<40: o.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{SUB}" stroke-width="2"/>')
        o+= [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{EDGE}"/>' for x,y in pts]
    elif kind=='swarm':
        for i in range(10):
            x=cx+rnd.uniform(-45,45); y=cy+rnd.uniform(-35,35); a=rnd.uniform(-.5,.5)
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{EDGE}"/><line x1="{x:.1f}" y1="{y:.1f}" x2="{x+14*math.cos(a):.1f}" y2="{y+14*math.sin(a):.1f}" stroke="{ACC}" stroke-width="2"/>')
    elif kind=='droplet':
        o.append(f'<path d="M{cx-40},{cy} C{cx-40},{cy-35} {cx+20},{cy-40} {cx+45},{cy} C{cx+20},{cy+40} {cx-40},{cy+35} {cx-40},{cy}Z" fill="none" stroke="{EDGE}" stroke-width="3"/>')
        o.append(f'<line x1="{cx+50}" y1="{cy}" x2="{cx+70}" y2="{cy}" stroke="{ACC}" stroke-width="3"/>')
        o+= [f'<circle cx="{cx-20+i*12}" cy="{cy+rnd.uniform(-10,10):.1f}" r="4" fill="{ACC}"/>' for i in range(4)]
    elif kind=='chain':
        d='M'+' '.join(f'{cx-55+i*5},{cy+22*math.sin(i*.45):.1f}' for i in range(23))
        o.append(f'<path d="{d}" fill="none" stroke="{EDGE}" stroke-width="4" stroke-linecap="round"/>')
    elif kind=='curve':
        o.append(f'<line x1="{cx-55}" y1="{cy+35}" x2="{cx+55}" y2="{cy+35}" stroke="{SUB}"/><line x1="{cx-55}" y1="{cy+35}" x2="{cx-55}" y2="{cy-40}" stroke="{SUB}"/>')
        d='M'+' '.join(f'{cx-55+i*5},{cy+30-65/(1+math.exp(-(i-11)*.6)):.1f}' for i in range(23))
        o.append(f'<path d="{d}" fill="none" stroke="{ACC}" stroke-width="3"/>')
    elif kind=='fold':
        o.append(f'<path d="M{cx-50},{cy+25} L{cx-15},{cy-30} L{cx+15},{cy+25} L{cx+50},{cy-30}" fill="none" stroke="{EDGE}" stroke-width="4" stroke-linejoin="round"/>')
    elif kind=='rotor':
        for k,(dx,dy) in enumerate([(-30,-15),(25,-20),(0,25)]):
            x,y=cx+dx,cy+dy
            o.append(f'<circle cx="{x}" cy="{y}" r="14" fill="none" stroke="{EDGE}" stroke-width="3"/><path d="M{x+14},{y} l5,-7 M{x+14},{y} l-6,-5" stroke="{ACC}" stroke-width="2"/>')
    elif kind=='layers':
        for i in range(4):
            o.append(f'<rect x="{cx-45+i*4}" y="{cy-30+i*15}" width="90" height="10" rx="4" fill="{EDGE if i%2==0 else ACC}" opacity=".85"/>')
    return ''.join(o)
def make(date, items):
    W,H=900,330; rnd=random.Random(date); s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Schematic of the top three finds for {date}">',f'<rect width="{W}" height="{H}" fill="{BG}"/>',f'<text x="20" y="30" fill="{TXT}" font-family="system-ui,sans-serif" font-size="18" font-weight="700">Top finds {date} — parts → driver → result</text>']
    for k,(kind,parts,driver,res) in enumerate(items):
        x=20+k*292
        s.append(f'<rect x="{x}" y="45" width="276" height="270" rx="12" fill="{CARD}" stroke="{EDGE}" stroke-width="1.5"/>')
        s.append(f'<text x="{x+14}" y="72" fill="{ACC}" font-family="system-ui,sans-serif" font-size="15" font-weight="700">{k+1}</text>')
        s.append(icon(kind,x+138,140,rnd))
        for j,(lab,val) in enumerate([('Parts',parts),('Driver',driver),('Result',res)]):
            y=230+j*28
            s.append(f'<text x="{x+14}" y="{y}" fill="{SUB}" font-family="system-ui,sans-serif" font-size="12">{lab}</text><text x="{x+70}" y="{y}" fill="{TXT}" font-family="system-ui,sans-serif" font-size="14" font-weight="600">{esc(val)}</text>')
    s.append(f'<text x="{W-20}" y="{H-4}" text-anchor="end" fill="{SUB}" font-family="system-ui,sans-serif" font-size="10">Illustrative schematic, not paper data</text></svg>')
    return '\n'.join(s)
os.makedirs(OUT,exist_ok=True)
for d,it in SPEC.items():
    open(os.path.join(OUT,f'{d}-top-finds.svg'),'w').write(make(d,it))
print(len(SPEC))
