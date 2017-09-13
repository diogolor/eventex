function ErrorPage(t, n, e) {
    this.$container = $(t), this.$contentContainer = this.$container.find("sign" == e ? ".sign-container" : ".content-container"), this.pageType = n, this.templateName = e
}
ErrorPage.prototype.centerContent = function() {
    var t = this.$container.outerHeight(),
        n = this.$contentContainer.outerHeight(),
        e = (t - n) / 2,
        i = "sign" == this.templateName ? -100 : 0;
    this.$contentContainer.css("top", e + i)
}, ErrorPage.prototype.initialize = function() {
    var t = this;
    this.centerContent(), this.$container.on("resize", function(n) {
        n.preventDefault(), n.stopPropagation(), t.centerContent()
    }), "plain" == this.templateName && window.setTimeout(function() {
        t.$contentContainer.addClass("in")
    }, 500), "sign" == this.templateName && $(".sign-container").animate({
        textIndent: 0
    }, {
        step: function(t) {
            $(this).css({
                transform: "rotate(" + t + "deg)",
                "transform-origin": "top center"
            })
        },
        duration: 1e3,
        easing: "easeOutBounce"
    })
};
var ep = new ErrorPage("body", "404", "plain");
ep.initialize(), $(window).on("resize", function() {
    $("body").trigger("resize")
});