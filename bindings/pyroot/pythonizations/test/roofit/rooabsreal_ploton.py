import unittest

import ROOT


class RooAbsRealPlotOn(unittest.TestCase):
    """
    Test for the PlotOn callable.
    """

    x = ROOT.RooRealVar("x", "x", -10, 10)
    mean = ROOT.RooRealVar("mean", "mean of guassian", 1, -10, 10)
    sig = ROOT.RooRealVar("sigma", "width of gaussian", 1, 0.1, 10)
    gauss = ROOT.RooGaussian("gauss", "gaussian PDF", x, mean, sig)
    xframe = x.frame(ROOT.RooFit.Title("Gaussian pdf"))


    def test_save(self):
        # test that kwargs can be passed
        # and lead to correct result
        self.assertEqual(self.gauss.plotOn(self.xframe, LineColor=ROOT.kRed), self.gauss.plotOn(self.xframe, ROOT.RooFit.LineColor(ROOT.kRed)))
        self.assertTrue(bool(self.gauss.plotOn(self.xframe, LineColor=ROOT.kRed)))

    def test_wrong_kwargs(self):
        # test that TypeError is raised 
        # if keyword does not correspong to CmdArg
        self.assertRaises(TypeError, self.gauss.plotOn, self.xframe, ThisIsNotACmgArg=True)

    def test_identical_result(self):
        # test that fitting with keyword arguments and passed ROOT objects leads to the same plot
        x1 = ROOT.RooRealVar("x", "x", -10, 10)
        mu1 = ROOT.RooRealVar("mu", "mean", 1, -10, 10)
        sig1 = ROOT.RooRealVar("sig", "variance", 1, 0.1, 10)
        gauss1 = ROOT.RooGaussian("gauss", "gaussian", x1, mu1, sig1)

        xframe1 = x1.frame(ROOT.RooFit.Title("Gaussian pdf with data"))
        plot1 = gauss1.plotOn(xframe1, LineColor=ROOT.kRed, Range="left,right")

        x2 = ROOT.RooRealVar("x", "x", -10, 10)
        mu2 = ROOT.RooRealVar("mu", "mean", 1, -10, 10)
        sig2 = ROOT.RooRealVar("sig", "variance", 1, 0.1, 10)
        gauss2 = ROOT.RooGaussian("gauss", "gaussian", x2, mu2, sig2)

        xframe2 = x2.frame(ROOT.RooFit.Title("Gaussian pdf with data"))
        plot2 = gauss2.plotOn(xframe2, ROOT.RooFit.Range("left,right"), ROOT.RooFit.LineColor(ROOT.kRed))

        self.assertTrue(plot1.isIdentical(plot2))

    def test_mixed_styles(self):
        # test that no error is causes if python style and cpp style
        # args are provided to ploton and that results are identical
        x1 = ROOT.RooRealVar("x", "x", -10, 10)
        mu1 = ROOT.RooRealVar("mu", "mean", 1, -10, 10)
        sig1 = ROOT.RooRealVar("sig", "variance", 1, 0.1, 10)
        gauss1 = ROOT.RooGaussian("gauss", "gaussian", x1, mu1, sig1)

        x2 = ROOT.RooRealVar("x", "x", -10, 10)
        mu2 = ROOT.RooRealVar("mu", "mean", 1, -10, 10)
        sig2 = ROOT.RooRealVar("sig", "variance", 1, 0.1, 10)
        gauss2 = ROOT.RooGaussian("gauss", "gaussian", x2, mu2, sig2)
        
        xframe1 = x1.frame(ROOT.RooFit.Title("Gaussian pdf with data"))
        plot1 = gauss1.plotOn(xframe1, ROOT.RooFit.LineColor(ROOT.kRed), Range="left,right")

        xframe2 = x.frame(ROOT.RooFit.Title("Gaussian pdf with data"))
        plot2 = gauss2.plotOn(xframe2, ROOT.RooFit.Range("left,right"), LineColor=ROOT.kRed)
        print(plot1)
        print(plot2)
        self.assertTrue(plot1.isIdentical(plot2))


if __name__ == '__main__':
    unittest.main()
