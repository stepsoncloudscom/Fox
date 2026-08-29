#target photoshop
// Beyaz stüdyo zeminini şeffaflaştırıp PNG kaydeder.
// Yöntem: 4 köşeden BİTİŞİK (contiguous) sihirli değnek -> yalnız zemine bağlı beyaz gider,
// ürünün İÇİNDEKİ beyaz/krem alanlar (taban, sargı) korunur.
function wand(x, y, tol, ekle) {
  var d = new ActionDescriptor();
  var r = new ActionReference();
  r.putProperty(charIDToTypeID("Chnl"), charIDToTypeID("fsel"));
  d.putReference(charIDToTypeID("null"), r);
  var p = new ActionDescriptor();
  p.putUnitDouble(charIDToTypeID("Hrzn"), charIDToTypeID("#Pxl"), x);
  p.putUnitDouble(charIDToTypeID("Vrtc"), charIDToTypeID("#Pxl"), y);
  d.putObject(charIDToTypeID("T   "), charIDToTypeID("Pnt "), p);
  d.putInteger(charIDToTypeID("Tlrn"), tol);
  d.putBoolean(charIDToTypeID("AntA"), true);
  executeAction(charIDToTypeID(ekle ? "AddT" : "setd"), d, DialogModes.NO);
}
function isle(inPath, outPath, tol, maske) {
  maske = maske || "1111";
  var doc = app.open(new File(inPath));
  try {
    if (doc.mode != DocumentMode.RGB) doc.changeMode(ChangeMode.RGB);
    doc.flatten();
    if (doc.activeLayer.isBackgroundLayer) doc.activeLayer.isBackgroundLayer = false;
    var w = doc.width.as("px"), h = doc.height.as("px");
    var kose = [[1,1],[w-2,1],[1,h-2],[w-2,h-2]];
    var ilk = true;
    for (var c = 0; c < 4; c++) {
      if (maske.charAt(c) !== "1") continue;
      wand(kose[c][0], kose[c][1], tol, !ilk); ilk = false;
    }
    if (ilk) throw new Error("hicbir kose secilmedi");
    doc.selection.expand(1);          // anti-alias saçağını yut
    doc.selection.clear();
    doc.selection.deselect();
    var o = new PNGSaveOptions(); o.compression = 6; o.interlaced = false;
    doc.saveAs(new File(outPath), o, true, Extension.LOWERCASE);
  } finally { doc.close(SaveOptions.DONOTSAVECHANGES); }
}
function main() {
  var jf = new File("/private/tmp/claude-501/-Users-ayhanerden-Fox/7b601d01-63e5-4e7e-a3d4-6a17aff71d26/scratchpad/is_listesi.txt");
  jf.open("r"); var ham = jf.read(); jf.close();
  var satirlar = ham.split("\n"); var log = [];
  for (var i = 0; i < satirlar.length; i++) {
    var s = satirlar[i]; if (!s || s.replace(/\s/g, "") === "") continue;
    var p = s.split("\t");
    try { isle(p[0], p[1], parseInt(p[2], 10), p[3]); log.push("OK\t" + p[1]); }
    catch (e) { log.push("HATA\t" + p[0] + "\t" + e); }
  }
  var lf = new File("/private/tmp/claude-501/-Users-ayhanerden-Fox/7b601d01-63e5-4e7e-a3d4-6a17aff71d26/scratchpad/ps_log.txt"); lf.open("w"); lf.write(log.join("\n")); lf.close();
  return "bitti:" + log.length;
}
main();
