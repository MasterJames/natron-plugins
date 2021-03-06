# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named pixelDisplace_GLExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from pixelDisplace_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.pixelDisplace_GL"

def getLabel():
    return "pixelDisplace_GL"

def getVersion():
    return 1

def getIconPath():
    return "pixelDisplace_GL.png"

def getGrouping():
    return "Community/GLSL/Distort"

def getPluginDescription():
    return "GPU accelerated Image displace effect for Shadertoy."
def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("pixelDisplace_GL", "pixelDisplace_GL")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.pixelDisplace_GL = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("line01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line01 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat0", "global X displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat1", "global Y displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat2", "global X offset")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat3", "global Y offset")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat3 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat4", "red X displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat4 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat5", "red Y displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat5 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat6", "green X displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat6 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat7", "green Y displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat7 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat8", "blue X displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat8 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat9", "blue Y displace")
    param.setMinimum(0, 0)
    param.setMaximum(49.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(49.99999999999999, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat9 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line02", "pixelDisplace_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
    del param

    param = lastNode.createSeparatorParam("line03", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator27", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator27 = param
    del param

    param = lastNode.createStringParam("separator28", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator28 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3646)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3810)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1 = lastNode

    param = lastNode.getParam("paramValueFloat6")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("// setting inputs names and filtering options\n// iChannel0: Source, filter=linear\n// iChannel1: Displace Map, filter=linear\n// iChannel2: Mask, filter=linear\n\n// creating user parameters\nuniform float scanlineX = 10;  // global X displace, min=-0., max=50.\nuniform float scanlineY = 10;  // global Y displace, min=-0., max=50.\n\nuniform float offsetX; // global X offset, min=-0., max=50.\nuniform float offsetY; // global Y offset, min=-0., max=50.\n\nuniform float rx = 10; // red X displace, min=-0., max=50.\nuniform float ry = 10; // red Y displace, min=-0., max=50.\nuniform float gx; // green X displace, min=-0., max=50.\nuniform float gy; // green Y displace, min=-0., max=50.\nuniform float bx; // blue X displace, min=-0., max=50.\nuniform float by; // blue Y displace, min=-0., max=50.\n\n\n// main function\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tfloat blender = 0;\n\n\tvec2 stDisp;\n\tstDisp.x = fragCoord.x / iResolution.x;\n\tstDisp.y = fragCoord.y / iResolution.y;\n\t\n\t// get the diplace map input (iChannel1)\n\tvec4 getDispInput1;\n\tgetDispInput1 = texture2D(iChannel1, stDisp);\n\n\t\n\tvec2 st2;\t\n\tst2.x =( fragCoord.x - (((rx)*getDispInput1.x + (bx) * getDispInput1.z + (gx) * getDispInput1.y)*scanlineX)+ offsetX) / iResolution.x;\n\tst2.y =( fragCoord.y - (((ry)*getDispInput1.x + (by) * getDispInput1.z + (gy) * getDispInput1.y)*scanlineY)+ offsetY) / iResolution.y;\n\n\n\t// get the displaced image\n\tvec4 getColorInputDisp;\n\tgetColorInputDisp = texture2D(iChannel0, st2);\n\t\n\n\tvec4 getColorInputDispMap;\n\tgetColorInputDispMap = texture2D(iChannel0, st2);\n\n\t// get pixel informations RGB for each input\n\tvec2 st;\n\tst.x = fragCoord.x  / iResolution.x;\n\tst.y = fragCoord.y / iResolution.y;\n\n\t// get the image to be displaced\n\tvec4 getColorInputClean;\n\tgetColorInputClean = texture2D(iChannel0, st);\n\t\n\tvec4 outColor;\n\toutColor =( (getColorInputDisp) );\t\t\n\toutColor.a = getColorInputDispMap.r;\n\t\n\t//process the output\n\tfragColor = outColor;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Displace Map")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("scanlineX")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("global X displace")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("scanlineY")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("global Y displace")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("offsetX")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("global X offset")
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("offsetY")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("global Y offset")
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("rx")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("red X displace")
        del param

    param = lastNode.getParam("paramDefaultFloat4")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat4")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("ry")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("red Y displace")
        del param

    param = lastNode.getParam("paramDefaultFloat5")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat5")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat5")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("gx")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("green X displace")
        del param

    param = lastNode.getParam("paramMinFloat6")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat6")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("gy")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("green Y displace")
        del param

    param = lastNode.getParam("paramMinFloat7")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat7")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("bx")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("blue X displace")
        del param

    param = lastNode.getParam("paramMinFloat8")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat8")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("by")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("blue Y displace")
        del param

    param = lastNode.getParam("paramMinFloat9")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat9")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    del lastNode
    # End of node "Shadertoy1"

    # Start of node "Displace_Map"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Displace_Map")
    lastNode.setLabel("Displace Map")
    lastNode.setPosition(4334, 3813)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupDisplace_Map = lastNode

    del lastNode
    # End of node "Displace_Map"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1)
    groupShadertoy1.connectInput(0, groupSource)
    groupShadertoy1.connectInput(1, groupDisplace_Map)

    param = groupShadertoy1.getParam("paramValueFloat0")
    group.getParam("Shadertoy1paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat1")
    group.getParam("Shadertoy1paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat2")
    group.getParam("Shadertoy1paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat3")
    group.getParam("Shadertoy1paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat4")
    group.getParam("Shadertoy1paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat5")
    group.getParam("Shadertoy1paramValueFloat5").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat6")
    group.getParam("Shadertoy1paramValueFloat6").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat7")
    group.getParam("Shadertoy1paramValueFloat7").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat8")
    group.getParam("Shadertoy1paramValueFloat8").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat9")
    group.getParam("Shadertoy1paramValueFloat9").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["pixelDisplace_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
