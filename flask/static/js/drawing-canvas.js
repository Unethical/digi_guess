import SignaturePad from 'signature_pad';

function DrawingCanvas(element, options) {
    this.element = element;
    this.ctx = element.getContext('2d');
    this.opts = options || {};
    this.signaturePad = new SignaturePad(element, {
        minWidth: 3,
        maxWidth: 3,
        minDistance: 5
    });
    this.isDisplayingResult = false;
    this.enable();
}

DrawingCanvas.prototype.clear = function () {
    this.signaturePad.clear();
    this.isDisplayingResult = false;
    this.enable();
    return this;
}

DrawingCanvas.prototype.data = function () {
    return this.ctx.getImageData(0, 0, this.ctx.canvas.width, this.ctx.canvas.height).data;
}

DrawingCanvas.prototype.disable = function () {
    this.signaturePad.penColor = "rgba(0,0,0,0)";
}

DrawingCanvas.prototype.enable = function () {
    this.signaturePad.penColor = "black";
}

DrawingCanvas.prototype.writeDigit = function(digit) {
    this.ctx.font = '5em sans-serif';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(digit, this.element.width/2, this.element.height/2);
}

DrawingCanvas.prototype.isEmpty = function() {
    return this.signaturePad.isEmpty();
}

export default DrawingCanvas;
