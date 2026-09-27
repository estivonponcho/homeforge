// Units: mm. CAD-only example; not a validated fit.
slot_width=10.2;
difference(){ cube([30,20,3],center=true); cube([slot_width,6,5],center=true); }
