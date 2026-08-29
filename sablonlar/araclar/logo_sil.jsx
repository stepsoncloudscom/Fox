#target photoshop
// Verilen dikdörtgenleri içerik-duyarlı doldurma ile temizler, PNG olarak üzerine yazar.
// İş listesi satırı:  <dosya>\t<x,y,w,h>;<x,y,w,h>;...
function icerikDuyarliDoldur() {
  var d = new ActionDescriptor();
  d.putEnumerated(charIDToTypeID("Usng"), charIDToTypeID("FlCn"), stringIDToTypeID("contentAware"));
  d.putBoolean(stringIDToTypeID("contentAwareColorAdaptationFill"), true);
  d.putUnitDouble(charIDToTypeID("Opct"), charIDToTypeID("#Prc"), 100);
  d.putEnumerated(charIDToTypeID("Md  "), charIDToTypeID("BlnM"), charIDToTypeID("Nrml"));
  executeAction(charIDToTypeID("Fl  "), d, DialogModes.NO);
}
function isle(yol, kutular) {
  var doc = app.open(new File(yol));
  try {
    if (doc.mode != DocumentMode.RGB) doc.changeMode(ChangeMode.RGB);
    if (doc.activeLayer.isBackgroundLayer) doc.activeLayer.isBackgroundLayer = false;
    var W = doc.width.as("px"), H = doc.height.as("px");
    for (var i = 0; i < kutular.length; i++) {
      var k = kutular[i];
      var x1 = Math.max(0, k[0] - 3), y1 = Math.max(0, k[1] - 3);
      var x2 = Math.min(W, k[0] + k[2] + 3), y2 = Math.min(H, k[1] + k[3] + 3);
      if (x2 - x1 < 2 || y2 - y1 < 2) continue;
      doc.selection.select([[x1, y1], [x2, y1], [x2, y2], [x1, y2]]);
      icerikDuyarliDoldur();
    }
    doc.selection.deselect();
    var o = new PNGSaveOptions(); o.compression = 6; o.interlaced = false;
    doc.saveAs(new File(yol), o, true, Extension.LOWERCASE);
  } finally { doc.close(SaveOptions.DONOTSAVECHANGES); }
}
function main() {
  var jf = new File("/private/tmp/claude-501/-Users-ayhanerden-Fox/7b601d01-63e5-4e7e-a3d4-6a17aff71d26/scratchpad/logo_is.txt"); jf.open("r"); var ham = jf.read(); jf.close();
  var sat = ham.split("\n"); var log = [];
  for (var i = 0; i < sat.length; i++) {
    if (!sat[i] || sat[i].replace(/\s/g, "") === "") continue;
    var p = sat[i].split("\t");
    var kutular = [], g = p[1].split(";");
    for (var j = 0; j < g.length; j++) {
      if (!g[j]) continue;
      var v = g[j].split(",");
      kutular.push([parseInt(v[0],10), parseInt(v[1],10), parseInt(v[2],10), parseInt(v[3],10)]);
    }
    try { isle(p[0], kutular); log.push("OK\t" + kutular.length + "\t" + p[0]); }
    catch (e) { log.push("HATA\t" + p[0] + "\t" + e); }
  }
  var lf = new File("/private/tmp/claude-501/-Users-ayhanerden-Fox/7b601d01-63e5-4e7e-a3d4-6a17aff71d26/scratchpad/logo_log.txt"); lf.open("w"); lf.write(log.join("\n")); lf.close();
  return "bitti:" + log.length;
}
main();
