
def aaf2fcp(terminate=int, waitCompletion=int, progress=int, getFileName=int, dstPath="string", deleteFile=bool, srcFile="string"):
    """
    aaf2fcp is NOT undoable, NOT queryable, and NOT editable.
    

    
This command is used to convert an aff file to a Final Cut Pro (fcp) xml file The conversion process can take several seconds to complete and the command is meant to be run asynchronously

    """
    pass
    


def about(application=bool, localizedResourceLocation=bool, product=bool, apiVersion=bool, operatingSystemVersion=bool, macOSx86=bool, helpDataDirectory=bool, uiLanguageIsLocalized=bool, ctime=bool, ntOS=bool, codeset=bool, win64=bool, linux64=bool, currentTime=bool, irix=bool, date=bool, compositingManager=bool, uiLanguageForStartup=bool, languageResources=bool, evalVersion=bool, cutIdentifier=bool, environmentFile=bool, installedVersion=bool, version=bool, qtVersion=bool, uiLanguage=bool, operatingSystem=bool, windowManager=bool, buildDirectory=bool, buildVariant=bool, tablet=bool, currentDate=bool, fontInfo=bool, macOS=bool, batch=bool, uiLocaleLanguage=bool, tabletMode=bool, windows=bool, macOSppc=bool, linux=bool, file=bool, ltVersion=bool, liveUpdate=bool, is64=bool, connected=bool, preferences=bool):
    """
    about is undoable, NOT queryable, and NOT editable.
    

    
This command displays version information about the application if it is executed without flags. If one of the above flags is specified then the specified version information is returned.

    """
    pass
    


def addAttr(attributeType="string", parent="string", defaultValue=float, hidden=bool, writable=bool, keyable=bool, dataType="string", softMinValue=float, numberOfChildren=int, binaryTag="string", multi=bool, longName="string", storable=bool, softMaxValue=float, usedAsFilename=bool, hasMaxValue=bool, exists=bool, usedAsProxy=bool, proxy="string", internalSet=bool, category="string", fromPlugin=bool, readable=bool, shortName="string", hasSoftMaxValue=bool, enumName="string", hasMinValue=bool, disconnectBehaviour=int, maxValue=float, cachedInternally=bool, minValue=float, usedAsColor=bool, indexMatters=bool, niceName="string", hasSoftMinValue=bool):
    """
    addAttr is undoable, queryable, and editable.
    

    
This command is used to add a dynamic attribute to a node or nodes. Either the longName or the shortName or both must be specified. If neither a dataType nor an attributeType is specified, a double attribute will be added. The dataType flag can be specified more than once indicating that any of the supplied types will be accepted (logical-or).
To add a non-double attribute the following criteria can be used to determine whether the dataType or the attributeType flag is appropriate. Some types, such as double3 can use either. In these cases the -dt flag should be used when you only wish to access the data as an atomic entity (eg. you never want to access the three individual values that make up a double3). In general it is best to use the -at in these cases for maximum flexibility. In most cases the -dt version will not display in the attribute editor as it is an atomic type and you are not allowed to change individual parts of it.
All attributes flagged as "(compound)" below or the compound attribute itself are not actually added to the node until all of the children are defined (using the "-p" flag to set their parent to the compound being created). See the EXAMPLES section for more details.
Type of attribute Flag and argument to use
boolean -at bool
32 bit integer -at long
16 bit integer -at short
8 bit integer -at byte
char -at char
enum -at enum (specify the enum names using the enumName flag)
float -at "float" (use quotes since float is a mel keyword)
double -at double
angle value -at doubleAngle
linear value -at doubleLinear
string -dt "string" (use quotes since string is a mel keyword)
array of strings -dt stringArray
compound -at compound
message (no data) -at message
time -at time
4x4 double matrix -dt "matrix" (use quotes since matrix is a mel keyword)
4x4 float matrix -at fltMatrix
reflectance -dt reflectanceRGB
reflectance (compound) -at reflectance
spectrum -dt spectrumRGB
spectrum (compound) -at spectrum
2 floats -dt float2
2 floats (compound) -at float2
3 floats -dt float3
3 floats (compound) -at float3
2 doubles -dt double2
2 doubles (compound) -at double2
3 doubles -dt double3
3 doubles (compound) -at double3
2 32-bit integers -dt long2
2 32-bit integers (compound) -at long2
3 32-bit integers -dt long3
3 32-bit integers (compound) -at long3
2 16-bit integers -dt short2
2 16-bit integers (compound) -at short2
3 16-bit integers -dt short3
3 16-bit integers (compound) -at short3
array of doubles -dt doubleArray
array of floats -dt floatArray
array of 32-bit ints -dt Int32Array
array of vectors -dt vectorArray
nurbs curve -dt nurbsCurve
nurbs surface -dt nurbsSurface
polygonal mesh -dt mesh
lattice -dt lattice
array of double 4D points -dt pointArray

    """
    pass
    


def addDynamic():
    """
    addDynamic is undoable, NOT queryable, and NOT editable.
    

    
Makes the "object" specified as second argument the source of an existing field or emitter specified as the first argument. In practical terms, what this means is that a field will emanate its force from its owner object, and an emitter will emit from its owner object.
addDynamic makes the specified field or emitter a child of the owner's transform (adding it to the model if it was not already there), and makes the necessary attribute connections.
If either of the arguments is omitted, addDynamic searches the selection list for objects to use instead. If more than one possible owner or field/emitter is selected, addDynamic will do nothing.
If the specified field/emitter already has a source, addDynamic will remove the current source and replace it with the newly specified source.
If a subset of the owner object's cvs/particles/vertices is selected, addDynamic will add the field/emitter to that subset only.

    """
    pass
    


def addExtension(attributeType="string", parent="string", defaultValue=float, hidden=bool, writable=bool, keyable=bool, dataType="string", softMinValue=float, numberOfChildren=int, binaryTag="string", multi=bool, longName="string", storable=bool, softMaxValue=float, usedAsFilename=bool, hasMaxValue=bool, exists=bool, usedAsProxy=bool, proxy="string", internalSet=bool, category="string", fromPlugin=bool, readable=bool, shortName="string", hasSoftMaxValue=bool, enumName="string", hasMinValue=bool, disconnectBehaviour=int, maxValue=float, cachedInternally=bool, nodeType="string", minValue=float, usedAsColor=bool, indexMatters=bool, niceName="string", hasSoftMinValue=bool):
    """
    addExtension is NOT undoable, NOT queryable, and editable.
    

    
This command is used to add an extension attribute to a node type. Either the longName or the shortName or both must be specified. If neither a dataType nor an attributeType is specified, a double attribute will be added. The dataType flag can be specified more than once indicating that any of the supplied types will be accepted (logical-or).
To add a non-double attribute the following criteria can be used to determine whether the dataType or the attributeType flag is appropriate. Some types, such as double3 can use either. In these cases the -dt flag should be used when you only wish to access the data as an atomic entity (eg. you never want to access the three individual values that make up a double3). In general it is best to use the -at in these cases for maximum flexibility. In most cases the -dt version will not display in the attribute editor as it is an atomic type and you are not allowed to change individual parts of it.
All attributes flagged as "(compound)" below or the compound attribute itself are not actually added to the node until all of the children are defined (using the "-p" flag to set their parent to the compound being created). See the EXAMPLES section for more details.
Type of attribute Flag and argument to use
boolean -at bool
32 bit integer -at long
16 bit integer -at short
8 bit integer -at byte
char -at char
enum -at enum (specify the enum names using the enumName flag)
float -at "float" (use quotes since float is a mel keyword)
double -at double
angle value -at doubleAngle
linear value -at doubleLinear
string -dt "string" (use quotes since string is a mel keyword)
array of strings -dt stringArray
compound -at compound
message (no data) -at message
time -at time
4x4 double matrix -dt "matrix" (use quotes since matrix is a mel keyword)
4x4 float matrix -at fltMatrix
reflectance -dt reflectanceRGB
reflectance (compound) -at reflectance
spectrum -dt spectrumRGB
spectrum (compound) -at spectrum
2 floats -dt float2
2 floats (compound) -at float2
3 floats -dt float3
3 floats (compound) -at float3
2 doubles -dt double2
2 doubles (compound) -at double2
3 doubles -dt double3
3 doubles (compound) -at double3
2 32-bit integers -dt long2
2 32-bit integers (compound) -at long2
3 32-bit integers -dt long3
3 32-bit integers (compound) -at long3
2 16-bit integers -dt short2
2 16-bit integers (compound) -at short2
3 16-bit integers -dt short3
3 16-bit integers (compound) -at short3
array of doubles -dt doubleArray
array of floats -dt floatArray
array of 32-bit ints -dt Int32Array
array of vectors -dt vectorArray
nurbs curve -dt nurbsCurve
nurbs surface -dt nurbsSurface
polygonal mesh -dt mesh
lattice -dt lattice
array of double 4D points -dt pointArray

    """
    pass
    


def addMetadata(streamName="string", scene=bool, channelName="string", indexType="string", channelType="string", structure="string"):
    """
    addMetadata is undoable, queryable, and NOT editable.
    

    
Defines the attachment of a metadata structure to one or more selected objects. This creates a placeholder with an empty metadata Stream for later population through the editMetadata command. It's similar in concept to the addAttr command for nodes - a data description is added but no data is actually set.
When assigning a metadata structure you must specify these flags - channelName is the metadata channel type (e.g. "vertex"), streamName is the name of the metadata stream to be created, and structure is the name of the structure type defining the contents of the metadata. The indexType flag is optional. If it is not present then the index will be presumed to be a standard numerical value.
You can query metadata information at a variety of levels. See the table below for a full list of the queryable arguments. In each case the specification of any of the non-queried arguments filters the list of metadata to be examined during the query. For all queries a single object must be selected for querying.
For example querying the channelName flag with no other arguments will return the list of all Channel types on the selected object that contain any metadata. Querying the channelName flag with the indexType flag specified will return only those channel types containing metadata streams that use that particular type of index.
Query the channelName flag to return the list of any channel types that have metadata.
Specify the channelName and streamName flags and query the structure flag to return the name of the structure assigned to the given stream (if any).
Specify a channelName and query the streamName to return the list of all streams assigned to that particular channel type.
If you query the streamName without a specific channelName then it returns a list of pairs of (channelName, streamName) for all metadata streams.
Flag Combinations:
ChannelName IndexType StreamName Structure   Create   Can Query
     0          0          0         0         X        ChannelName, StreamName, Structure
     0          0          0         1         X        ChannelName, StreamName, IndexType
     0          0          1         0         X        ChannelName, Structure, IndexType
     0          0          1         1         X        ChannelName, IndexType
     0          1          0         0         X        ChannelName, StreamName, Structure
     0          1          0         1         X        ChannelName, StreamName
     0          1          1         0         X        ChannelName, Structure
     0          1          1         1         X        ChannelName
     1          0          0         0         X        StreamName, Structure, IndexType
     1          0          0         1         X        StreamName, IndexType
     1          0          1         0         X        Structure, IndexType
     1          0          1         1        (a)       IndexType
     1          1          0         0         X        StreamName, Structure
     1          1          0         1         X        StreamName
     1          1          1         0         X        Structure
     1          1          1         1        (b)       X
    (a) Assign an empty metadata stream with default index type
    (b) Assign an empty metadata stream with the named index type

    """
    pass
    


def addPP(attribute="string"):
    """
    addPP is undoable, NOT queryable, and NOT editable.
    

    
Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for an attribute of an emitter or field. The -atr flag identifies the attribute. If no attribute is named, addPP returns a warning and does nothing.
The command adds any other necessary attributes wherever they are needed, and makes all necessary connections. If any of the attributes already exist, the command simply connects to them. The command also toggles any relevant attributes in the emitter or field to indicate that per-point capability is being used.
The command adds a separate per-point attribute to the owning object for each emitter/field. For example, for emission rate, there is a separate ratePP for each emitter. These attributes are named according to the convention <emitter/field name><attr name>PP. For example, if a particle shape owned an emitter "smoke", that shape would get attribute "smokeRatePP."
The name of the object must be the emitter or field for which per-point capability is to be added (or the name of its parent transform). The addPP command adds the per-point capability for that emitter or field but not for any others owned by the same object. If per-point capability is not supported for a named object, the command will trigger a warning, but will continue executing for any other objects which were valid.
If no objects are named, addPP uses any objects in the current selection list for which the specified attribute is applicable. (For example, it would add per-point rate for all selected emitters.)
If addPP detects that the owner object has left-over attributes from a deleted emitter, it will remove those attributes before adding the new ones. Thus, you can delete the emitter, make a new one, and run addPP again, and addPP will clean up after the deleted emitter. This is most commonly used if you have a geometry emitter and then decide to change the geometry. Likewise, if addPP detects that some cvs or vertices have been added to the geometry, then it will expand the corresponding multi-attributes as necessary. However, if it detects that some cvs/vertices have been removed, it will not remove any entries from the multi. See the user manual for more discussion.

    """
    pass
    


def affectedNet(node, type="string"):
    """
    affectedNet is undoable, queryable, and editable.
    

    
This command gets the list of attributes on a node or node type and creates nodes of type TdnAffect, one for each attribute, that are connected iff the source node's attribute affects the destination node's attribute.

    """
    pass
    


def affects(type="string", by=bool):
    """
    affects is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns the list of attributes on a node or node type which affect the named attribute.

    """
    pass
    


def aimConstraint(targetobject, worldUpObject="string", worldUpVector=float, remove=bool, skip="string", worldUpType="string", maintainOffset=bool, weightAliasList=bool, layer="string", offset=float, targetList=bool, upVector=float, aimVector=float, weight=float, name="string"):
    """
    aimConstraint is undoable, queryable, and editable.    

    
Constrain an object's orientation to point at a target object or at the average position of a number of targets.
An aimConstraint takes as input one or more "target" DAG transform nodes at which to aim the single "constraint object" DAG transform node. The aimConstraint orients the constrained object such that the aimVector (in the object's local coordinate system) points to the in weighted average of the world space position target objects. The upVector (again the the object's local coordinate system) is aligned in world space with the worldUpVector.

    """
    pass
    


def air(objects, directionX=float, magnitude=float, inheritVelocity=float, directionY=float, inheritRotation=bool, perVertex=bool, enableSpread=bool, spread=float, directionZ=float, velocityComponentOnly=bool, wakeSetup=bool, fanSetup=bool, attenuation=float, maxDistance="string", position="string", speed=float, windSetup=bool, name="string"):
    """
    air is undoable, queryable, and editable.
    

    
The air field simulates the effects of moving air. The affected objects will be accelerated or decelerated so that their velocities match that of the air.
With the '-vco true' flag thrown, only accelerations are applied. By parenting an air field to a moving part of an object (ie. a foot of a character) and using '-i 1 -m 0 -s .5 -vco true' flags, one can simulate the movement of air around the foot as it moves, since the TOTAL velocity vector of the field would be only based on the movement of the foot. This can be done while the character walks through leaves or dust on the ground.
For each listed object, the command creates a new field. The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the field names. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If the -pos flag is specified, a field is created at the position specified. If not, if object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object; otherwise the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def aliasAttr(remove=bool):
    """
    aliasAttr is undoable, queryable, and editable.
    

    
Allows aliases (alternate names) to be defined for any attribute of a specified node. When an attribute is aliased, the alias will be used by the system to display information about the attribute. The user may, however, freely use either the alias or the original name of the attribute. Only a single alias can be specified for an attribute so setting an alias on an already-aliased attribute destroys the old alias.

    """
    pass
    


def align(yAxis="string", xAxis="string", zAxis="string", coordinateSystem="string", alignToLead=bool):
    """
    align is undoable, NOT queryable, and NOT editable.
    

    
Align or spread objects along X Y and Z axis.

    """
    pass
    


def alignCtx(contextName, anchorFirstObject=bool, align=bool, distribute=bool, image1="string", history=bool, exists=bool, showAlignTouch=bool, image2="string", name="string", image3="string"):
    """
    alignCtx is undoable, queryable, and editable.
    

    
The alignCtx command creates a tool for aligning and distributing objects.

    """
    pass
    


def alignCurve(curvecurve, reverse2=bool, tangentContinuityType=int, tangentScale1=float, curvatureContinuity=bool, joinParameter=float, positionalContinuity=bool, object=bool, nodeState=int, curvatureScale1=float, name="string", replaceOriginal=bool, positionalContinuityType=int, tangentContinuity=bool, reverse1=bool, caching=bool, tangentScale2=float, constructionHistory=bool, curvatureScale2=float):
    """
    alignCurve is undoable, queryable, and editable.
    

    
The curve align command is used to align curves in maya. The main alignment options are positional, tangent and curvature continuity. Curvature continuity implies tangent continuity.
Positional continuity means the curves (move) or the ends of the curves (modify) are changed.
Tangent continuity means one of the curves is modified to be tangent at the points where they meet.
Curvature continuity means one of the curves is modified to be curvature continuous as well as tangent.
The default behaviour, when no curves or flags are passed, is to only do positional and tangent continuity on the active list with the end of the first curve and the start of the other curve used for alignment.

    """
    pass
    


def alignSurface(surfacesurface, reverse2=bool, swap1=bool, twist=bool, tangentScale1=float, positionalContinuity=bool, keepMultipleKnots=bool, tangentContinuity=bool, object=bool, replaceOriginal=bool, tangentContinuityType=int, name="string", joinParameter=float, swap2=bool, reverse1=bool, positionalContinuityType=int, curvatureScale2=float, directionU=bool, curvatureContinuity=bool, caching=bool, nodeState=int, attach=bool, curvatureScale1=float, tangentScale2=float, constructionHistory=bool):
    """
    alignSurface is undoable, queryable, and editable.
    

    
The surface align command is used to align surfaces in maya. The main alignment options are positional, tangent and curvature continuity. Curvature continuity implies tangent continuity.
NOTE: this tool is based on Studio's align tool.
Positional continuity means the surfaces (move) or the ends of the surfaces (modify) are changed.
Tangent continuity means one of the surfaces is modified to be tangent at the points where they meet.
Curvature continuity means one of the surfaces is modified to be curvature continuous as well as tangent.
The default behaviour, when no surfaces or flags are passed, is to only do positional and tangent continuity on the active list with the end of the first surface and the start of the other surface used for alignment.

    """
    pass
    


def allNodeTypes(includeAbstract=bool):
    """
    allNodeTypes is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns a list containing the type names of every kind of creatable node registered with the system. Note that some node types are abstract and cannot be created. These will not show up on this list. (e.g. transform and polyShape both inherit from dagObject, but dagObject cannot be created directly so it will not appear on this list.)

    """
    pass
    


def ambientLight(discRadius="string", shadowColor=float, softShadow=bool, ambientShade=float, useRayTraceShadows=bool, intensity=float, rgb=float, shadowSamples=int, shadowDither=float, name="string"):
    """
    ambientLight is undoable, queryable, and editable.
    

    
The ambientLight command is used to edit the parameters of existing ambientLights, or to create new ones. The default behaviour is to create a new ambientlight.

    """
    pass
    


def angleBetween(vector1="string", euler=bool, constructionHistory=bool, vector2="string"):
    """
    angleBetween is undoable, NOT queryable, and NOT editable.
    

    
Returns the axis and angle required to rotate one vector onto another. If the construction history (ch) flag is ON, then the name of the new dependency node is returned.

    """
    pass
    


def animCurveEditor(stackedCurvesMax=float, docTag="string", stackedCurvesMin=float, defineTemplate="string", parent="string", displayTangents="string", useTemplate="string", lockMainConnection=bool, outliner="string", unParent=bool, curvesShownForceUpdate=bool, smoothness="string", panel="string", preSelectionHighlight=bool, keyingTime="string", displayActiveKeyTangents="string", mainListConnection="string", displayValues="string", snapValue="string", highlightConnection="string", denormalizeCurvesCommand="string", curvesShown=bool, lookAt="string", constrainDrag=int, exists=bool, resultScreenSamples=int, displayInfinities="string", stackedCurvesSpace=float, displayActiveKeys="string", normalizeCurvesCommand="string", resultSamples=(), control=bool, stackedCurves=bool, menu="string", snapTime="string", showUpstreamCurves=bool, autoFit="string", showActiveCurveNames=bool, valueLinesToggle="string", selectionConnection="string", stateString=bool, forceMainConnection="string", showCurveNames=bool, renormalizeCurves=bool, unlockMainConnection=bool, classicMode=bool, resultUpdate="string", updateMainConnection=bool, showBufferCurves="string", showResults="string", displayNormalized=bool, clipTime="string", displayKeys="string", areCurvesSelected=bool, filter="string"):
    """
    animCurveEditor is undoable, queryable, and editable.
    

    
Edit a characteristic of a graph editor

    """
    pass
    


def animDisplay(modelUpdate="string", timeCodeOffset="string", timeCode=bool, refAnimCurvesEditable=bool):
    """
    animDisplay is undoable, queryable, and editable.
    

    
This command changes certain display options used by animation windows.

    """
    pass
    


def animLayer(bestAnimLayer=bool, addSelectedObjects=bool, preferred=bool, animCurves=bool, affectedLayers=bool, removeAllAttributes=bool, excludeBoolean=bool, mute=bool, removeAttribute="string", addRelatedKG=bool, moveLayerBefore="string", maxLayers=bool, bestLayer=bool, weight=float, children="string", copyNoAnimation="string", selected=bool, collapse=bool, override=bool, extractAnimation="string", excludeDynamic=bool, exists=bool, parent="string", excludeVisibility=bool, solo=bool, excludeEnum=bool, forceUIRebuild=bool, attribute="string", baseAnimCurves=bool, excludeScale=bool, writeBlendnodeDestinations=bool, passthrough=bool, findCurveForPlug="string", blendNodes=bool, copyAnimation="string", excludeTranslate=bool, root="string", excludeRotate=bool, lock=bool, forceUIRefresh=bool, copy="string", moveLayerAfter="string", layeredPlug="string"):
    """
    animLayer is undoable, queryable, and editable.
    

    
This command creates and edits animation layers.

    """
    pass
    


def animView(string, nextView=bool, minValue=float, maxValue=float, previousView=bool, endTime=(), startTime=()):
    """
    animView is undoable, queryable, and editable.
    

    
This command allows you to specify the current view range within an animation editor.

    """
    pass
    


def annotate(objects, point="string", text="string"):
    """
    annotate is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create an annotation to be attached to the specified objects at the specified point.

    """
    pass
    


def applyAttrPattern(nodeType="string", patternName="string"):
    """
    applyAttrPattern is undoable, NOT queryable, and NOT editable.
    

    
Take the attribute structure described by a pre-defined pattern and apply it either to a node (as dynamic attributes) or a node type (as extension attributes). The same pattern can be applied more than once to different nodes or node types as the operation duplicates the attribute structure described by the pattern. See the 'createAttrPatterns' command for a description of how to create a pattern.

    """
    pass
    


def applyMetadata(scene=bool, format="string", value="string"):
    """
    applyMetadata is undoable, NOT queryable, and NOT editable.
    

    
Define the values of a particular set of metadata on selected objects. This command is used in preservation of metadata through Maya file formats (.ma/.mb). If any metadata already exists it will be kept and merged with the new metadata, overwriting duplicate entries. (i.e. if this command specifies data at index N and you already have a value at index N then the one this command specifies will be the new value and the old one will cease to exist.)
Unlike the editMetadata command it is not necessary to first use the addMetadata command or API equivalent to attach a metadata stream to the object, this command will do both assignment of structure and of metadata values. You do have to use the dataStructure command or API equivalent to create the structure being assigned first though.
The formatted input will be in a form expected by the data associations serializer (see adsk::Data::AssociationsSerializer for more information). The specific serialization type will be the default 'raw' if the format flag is not used.
For example the "raw" format input string "channel face\n[STREAMDATA]\nendChannels\nendAssociations" with no flags is equivalent to the input "[STREAMDATA]\nendChannels" with the channel flag set to 'face'

    """
    pass
    


def applyTake(reset=bool, preview=bool, startTime=(), device="string", specifyChannel=bool, recurseChannel=bool, channel="string", filter="string"):
    """
    applyTake is undoable, NOT queryable, and NOT editable.
    

    
This command takes data in a device (refered to as a take) and converts it into a form that may be played back and reviewed. The take can either be imported through the readTake action, or recorded by the recordDevice action. The take is either converted into animation curves or if the -preview flag is used, into blendDevice nodes.
The command looks for animation curves attached to the target attributes of a device attachment. If animation curves exist, the take is pasted over the existing curves. If the curves do not exist, new animation curves are created.
If devices are not specified, all of the devices with take data and that are enabled for applyTake, will have their data applied.
See also: recordDevice, enableDevice, readTake, writeTake

    """
    pass
    


def arclen(constructionHistory=bool):
    """
    arclen is undoable, queryable, and editable.
    

    
This command returns the arclength of a curve if the history flag is not set (the default). If the history flag is set, a node is created that can produce the arclength, and is connected and its name returned. Having the construction history option on makes this command useful for expressions.

    """
    pass
    


def arcLenDimContext(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    arcLenDimContext is undoable, queryable, and editable.
    

    
Command used to register the arcLenDimCtx tool.

    """
    pass
    


def arcLengthDimension(curve ,surface):
    """
    arcLengthDimension is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create an arcLength dimension to display the arcLength of a curve/surface at a specified point on the curve/surface.

    """
    pass
    


def arrayMapper(mapTo="string", destAttr="string", type="string", inputV="string", inputU="string", target="string"):
    """
    arrayMapper is undoable, NOT queryable, and NOT editable.
    

    
Create an arrayMapper node and connect it to a target object. If the -type flag is used, then this command also creates an external node used for computing the output values. If the input attribute does not already exist, it will be created. The output attribute must exists. If a flag is omitted, the selection list will be used to supply the needed objects. If none are found, that action is omitted.

    """
    pass
    


def art3dPaintCtx(mappressure="string", outline=bool, soloAsDiffuse=bool, painttxtattr="string", filetxtsizex=int, reflectionaxis="string", exportfilesave="string", commonattr="string", saveonstroke=bool, reflection=bool, dragSlider="string", usepressure=bool, paintoperationtype="string", tangentOutline=bool, image1="string", exportfiletype="string", lowerradius=float, filetxtaspectratio=float, opacity=float, savetexture=bool, saveTextureOnStroke=bool, pfxScale=float, accopacity=bool, shapeattr=bool, exists=bool, brushalignment=bool, shapenames="string", name="string", showactive=bool, surfaceConformedBrushVertices=bool, exportfilemode="string", keepaspectratio=bool, reloadtexfile=bool, filetxtsizey=int, resizetxt=bool, exportfilesizey=int, image3="string", textureFilenames=bool, stampSpacing=float, outwhilepaint=bool, tablet=bool, shadernames="string", importfileload="string", paintmode="string", profileShapeFile="string", projective=bool, expandfilename=bool, brushfeedback=bool, stampProfile="string", resizeratio=float, pfxWidth=float, clear=bool, importfilemode="string", painttxtattrname="string", importreassign=bool, extendFillColor=bool, history=bool, image2="string", radius=float, assigntxt=bool, exportfilesizex=int, alphablendmode="string"):
    """
    art3dPaintCtx is undoable, queryable, and editable.
    

    
This is a tool context command for 3d Paint tool.

    """
    pass
    


def artAttrCtx(paintattrselected="string", mappressure="string", outline=bool, clampupper=float, reflectionaxis="string", exportfilesave="string", paintNodeArray="string", image3="string", rampMaxColor=float, reflection=bool, dragSlider="string", tangentOutline=bool, surfaceConformedBrushVertices=bool, exportfilesizey=int, exportfiletype="string", toolOnProc="string", lowerradius=float, exportfilesizex=int, opacity=float, objattrArray="string", paintmode="string", useMaxMinColor=bool, attrSelected="string", accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, colorRamp="string", name="string", showactive=bool, afterStrokeCmd="string", selectedattroper="string", exportfilemode="string", clamplower=float, useColorRamp=bool, minvalue=float, colorrangelower=float, activeListChangedProc="string", clamp="string", expandfilename=bool, outwhilepaint=bool, filterNodes=bool, value=float, alphaclamp="string", tablet=bool, colorfeedback=bool, importfileload="string", image1="string", stampProfile="string", profileShapeFile="string", projective=bool, duringStrokeCmd="string", brushfeedback=bool, dataTypeIndex=int, interactiveUpdate=bool, whichTool="string", clear=bool, importfilemode="string", alphaclamplower=float, maxvalue=float, importreassign=bool, rampMinColor=float, toolOffProc="string", colorrangeupper=float, history=bool, beforeStrokeCmd="string", image2="string", alphaclampupper=float, disablelighting=bool, radius=float):
    """
    artAttrCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This is a context command to set the flags on the Attribute Paint Tool context.

    """
    pass
    


def artAttrPaintVertexCtx(context, paintattrselected="string", mappressure="string", paintComponent=int, outline=bool, clampupper=float, vertexColorRangeUpper=float, reflectionaxis="string", exportfilesave="string", paintNodeArray="string", image3="string", rampMaxColor=float, reflection=bool, dragSlider="string", tangentOutline=bool, surfaceConformedBrushVertices=bool, exportfilesizey=int, exportfiletype="string", toolOnProc="string", lowerradius=float, exportfilesizex=int, opacity=float, objattrArray="string", paintmode="string", useMaxMinColor=bool, vertexColorRangeLower=float, paintVertexFace=bool, attrSelected="string", accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, colorRamp="string", name="string", showactive=bool, afterStrokeCmd="string", selectedattroper="string", exportfilemode="string", clamplower=float, useColorRamp=bool, minvalue=float, colorrangelower=float, activeListChangedProc="string", clamp="string", expandfilename=bool, paintRGBA=bool, outwhilepaint=bool, filterNodes=bool, value=float, alphaclamp="string", tablet=bool, colorfeedback=bool, importfileload="string", image1="string", stampProfile="string", profileShapeFile="string", projective=bool, duringStrokeCmd="string", brushfeedback=bool, dataTypeIndex=int, interactiveUpdate=bool, whichTool="string", clear=bool, importfilemode="string", alphaclamplower=float, maxvalue=float, vertexColorRange=bool, importreassign=bool, rampMinColor=float, toolOffProc="string", colorrangeupper=float, history=bool, beforeStrokeCmd="string", image2="string", alphaclampupper=float, disablelighting=bool, radius=float):
    """
    artAttrPaintVertexCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This is a context command to set the flags on the Paint color on vertex Tool context.

    """
    pass
    


def artAttrSkinPaintCtx(context, xrayJoints=bool, paintattrselected="string", mappressure="string", outline=bool, clampupper=float, reflectionaxis="string", exportfilesave="string", paintNodeArray="string", image3="string", rampMaxColor=float, useMaxMinColor=bool, reflection=bool, dragSlider="string", tangentOutline=bool, surfaceConformedBrushVertices=bool, exportfilesizey=int, exportfiletype="string", toolOnProc="string", lowerradius=float, exportfilesizex=int, opacity=float, objattrArray="string", paintmode="string", skinPaintMode=int, paintSelectMode=int, attrSelected="string", accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, colorRamp="string", name="string", showactive=bool, afterStrokeCmd="string", selectedattroper="string", exportfilemode="string", clamplower=float, useColorRamp=bool, minvalue=float, influence="string", colorrangelower=float, activeListChangedProc="string", clamp="string", expandfilename=bool, outwhilepaint=bool, filterNodes=bool, value=float, alphaclamp="string", tablet=bool, colorfeedback=bool, importfileload="string", image1="string", stampProfile="string", profileShapeFile="string", projective=bool, duringStrokeCmd="string", brushfeedback=bool, dataTypeIndex=int, interactiveUpdate=bool, whichTool="string", clear=bool, importfilemode="string", alphaclamplower=float, maxvalue=float, importreassign=bool, rampMinColor=float, toolOffProc="string", colorrangeupper=float, history=bool, beforeStrokeCmd="string", image2="string", alphaclampupper=float, disablelighting=bool, radius=float):
    """
    artAttrSkinPaintCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This is a context command to set the flags on the Paint skin weights tool context.

    """
    pass
    


def artAttrTool(exists="string", remove="string", add="string"):
    """
    artAttrTool is NOT undoable, queryable, and NOT editable.
    

    
The artAttrTool command manages the list of tool types which are used for attribute painting. This command supports querying the list contents as well as adding new tools to the list. Note that there is a set of built-in tools. The list of built-ins can be queried by starting Maya and doing an "artAttrTool -q".
The tools which are managed by this command are all intended for attribute painting via Artisan: when you create a new context via artAttrCtx you specify the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to simply use one of the built-in tools. However, if you need to have custom Properties and Values sheets asscociated with your tool, you will need to define a custom tool via artAttrTool -add "toolName". For an example of a custom attribute painting tool, see the devkit example customtoolPaint.mel.

    """
    pass
    


def artBuildPaintMenu():
    """
    artBuildPaintMenu is NOT undoable, NOT queryable, and NOT editable.
    

    
??

    """
    pass
    


def artFluidAttrCtx(doAutoSave=bool, importfilemode="string", displayVelocity=bool, mappressure="string", useStrokeDirection=bool, outline=bool, rgbValue=float, reflectionaxis="string", exportfilesave="string", image3="string", displayAsRender=bool, reflection=bool, dragSlider="string", exportfilesizey=int, exportfiletype="string", lowerradius=float, exportfilesizex=int, opacity=float, accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, name="string", showactive=bool, surfaceConformedBrushVertices=bool, exportfilemode="string", image1="string", velocity=float, outwhilepaint=bool, tablet=bool, importfileload="string", paintmode="string", delaySelectionChanged=bool, profileShapeFile="string", expandfilename=bool, brushfeedback=bool, stampProfile="string", clear=bool, currentPaintableFluid="string", projective=bool, importreassign=bool, property="string", autoSave="string", history=bool, image2="string", tangentOutline=bool, radius=float):
    """
    artFluidAttrCtx is undoable, queryable, and editable.
    

    
This command is used to paint properties (such as density) of selected fluid volumes.

    """
    pass
    


def artPuttyCtx(reflectionaxis="string", brushalignment=bool, updaterefsrf=bool, exportfilemode="string", updateerasesrf=bool, clamp="string", tablet=bool, paintmode="string", refvectorv=float, objattrArray="string", importfilemode="string", importreassign=bool, brushStrength=float, useColorRamp=bool, history=bool, image2="string", alphaclampupper=float, disablelighting=bool, clampupper=float, rampMaxColor=float, exportfiletype="string", exportfilesizex=int, value=float, colorRamp="string", name="string", invertrefvector=bool, exportfilesizey=int, polecv=bool, colorrangelower=float, brushfeedback=bool, stampProfile="string", interactiveUpdate=bool, autosmooth=bool, refvector="string", maxdisp=float, rampMinColor=float, toolOffProc="string", paintattrselected="string", maxvalue=float, refvectoru=float, exportfilesave="string", image3="string", dispdecr=bool, projective=bool, paintNodeArray="string", usepressure=bool, duringStrokeCmd="string", surfaceConformedBrushVertices=bool, tangentOutline=bool, mouldtypemouse="string", collapsecvtol=float, colorfeedback=bool, activeListChangedProc="string", filterNodes=bool, outwhilepaint=bool, expandfilename=bool, whichTool="string", clear=bool, alphaclamplower=float, reflection=bool, showactive=bool, beforeStrokeCmd="string", radius=float, mappressure="string", outline=bool, dragSlider="string", image1="string", toolOnProc="string", lowerradius=float, stitchtype="string", opacity=float, useMaxMinColor=bool, attrSelected="string", accopacity=bool, exists=bool, stitchcorner=bool, afterStrokeCmd="string", selectedattroper="string", clamplower=float, minvalue=float, stitchedgeflood=bool, alphaclamp="string", importfileload="string", profileShapeFile="string", dataTypeIndex=int, smoothiters=int, colorrangeupper=float, dispincr=bool, refsurface=bool):
    """
    artPuttyCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This command is used to modify NURBS surfaces using a brush based interface (Maya Artisan). This is accomplished by moving the control vertices (CVs) under the brush in the specified direction.

    """
    pass
    


def artSelectCtx(unselectall=bool, mappressure="string", outline=bool, selectop="string", reflectionaxis="string", exportfilesave="string", image3="string", reflection=bool, dragSlider="string", image1="string", exportfiletype="string", lowerradius=float, exportfilesizex=int, opacity=float, accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, name="string", showactive=bool, afterStrokeCmd="string", surfaceConformedBrushVertices=bool, exportfilemode="string", addselection=bool, toggleall=bool, exportfilesizey=int, selectall=bool, outwhilepaint=bool, tablet=bool, importfileload="string", paintmode="string", profileShapeFile="string", expandfilename=bool, brushfeedback=bool, stampProfile="string", clear=bool, importfilemode="string", projective=bool, importreassign=bool, importthreshold=float, history=bool, beforeStrokeCmd="string", image2="string", tangentOutline=bool, radius=float):
    """
    artSelectCtx is undoable, queryable, and editable.
    

    
This command is used to select/deselect/toggle components on selected surfaces using a brush interface (Maya Artisan). Since, it selects components of the surface, it only works in the component mode.

    """
    pass
    


def artSetPaintCtx(mappressure="string", outline=bool, reflectionaxis="string", exportfilesave="string", image3="string", reflection=bool, dragSlider="string", image1="string", exportfiletype="string", lowerradius=float, exportfilesizex=int, opacity=float, setopertype="string", setdisplaycvs=bool, settomodify="string", accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, name="string", showactive=bool, surfaceConformedBrushVertices=bool, exportfilemode="string", setcolorfeedback=bool, exportfilesizey=int, outwhilepaint=bool, tablet=bool, importfileload="string", paintmode="string", profileShapeFile="string", expandfilename=bool, brushfeedback=bool, stampProfile="string", clear=bool, importfilemode="string", projective=bool, importreassign=bool, history=bool, image2="string", tangentOutline=bool, radius=float):
    """
    artSetPaintCtx is undoable, queryable, and editable.
    

    
This tool allows the user to modify the set membership (add, transfer, remove cvs) on nurbs surfaces using Maya Artisan's interface.

    """
    pass
    


def artUserPaintCtx(paintattrselected="string", getSurfaceCommand="string", outline=bool, clampupper=float, reflectionaxis="string", exportfilesave="string", getArrayAttrCommand="string", paintNodeArray="string", image3="string", finalizeCmd="string", rampMaxColor=float, reflection=bool, dragSlider="string", mappressure="string", fullpaths=bool, tangentOutline=bool, surfaceConformedBrushVertices=bool, exportfilesizey=int, exportfiletype="string", toolOnProc="string", lowerradius=float, exportfilesizex=int, opacity=float, objattrArray="string", paintmode="string", useMaxMinColor=bool, attrSelected="string", accopacity=bool, usepressure=bool, exists=bool, brushalignment=bool, colorRamp="string", name="string", showactive=bool, afterStrokeCmd="string", selectedattroper="string", exportfilemode="string", clamplower=float, setValueCommand="string", getValueCommand="string", minvalue=float, toolCleanupCmd="string", colorrangelower=float, activeListChangedProc="string", clamp="string", expandfilename=bool, outwhilepaint=bool, filterNodes=bool, value=float, alphaclamp="string", tablet=bool, colorfeedback=bool, importfileload="string", image1="string", stampProfile="string", profileShapeFile="string", projective=bool, duringStrokeCmd="string", brushfeedback=bool, dataTypeIndex=int, interactiveUpdate=bool, whichTool="string", clear=bool, importfilemode="string", alphaclamplower=float, maxvalue=float, importreassign=bool, initializeCmd="string", useColorRamp=bool, rampMinColor=float, toolOffProc="string", colorrangeupper=float, history=bool, toolSetupCmd="string", beforeStrokeCmd="string", image2="string", alphaclampupper=float, disablelighting=bool, setArrayValueCommand="string", radius=float):
    """
    artUserPaintCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This command executes a scriptable paint (Maya Artisan). It allows the user to apply mel commands/scripts to modify cvs' attributes for all cvs under the paint brush.

    """
    pass
    


def assembly(listRepTypesProc="string", input="string", deleteRepresentation="string", repPreCreateUIProc="string", deregister="string", type="string", label="string", active="string", defaultType="string", createOptionBoxProc="string", createRepresentation="string", repLabel="string", repType="string", proc="string", isTrackingMemberEdits="string", postCreateUIProc="string", repName="string", activeLabel="string", name="string", repNamespace="string", repTypeLabelProc="string", repTypeLabel="string", repPostCreateUIProc="string", listRepresentations=bool, renameRepresentation="string", newRepLabel="string", listTypes=bool, isAType="string", canCreate="string", listRepTypes=bool):
    """
    assembly is undoable, queryable, and editable.
    

    
Command to register assemblies for the scene assembly framework, to create them, and to edit and query them. Assembly nodes are DAG nodes, and are therefore shown in the various DAG editors (Outliner, Hypergraph, Node Editor). At assembly creation time, the node name defaults to the node type name. The assembly command can create any node that is derived from the assembly node base class. It also acts as a registry of these types, so that various scripting callbacks can be defined and registered with the assembly command. These callbacks are invoked by Maya during operations on assembly nodes, and can be used to customize behavior.
Registering a new assembly type
When defining a new type of assembly derived from the assembly node base class, a number of procedures can be defined through the assembly command to properly integrate the new assembly node type into Maya. Most of these procedures are used to integrate the assembly type with the Maya user interface, and are not required for non-interactive scripting use. For more information, see the MPxAssembly class description in the Maya API documentation. Some of the important procedures that can be registered through the assembly command are the following:
listRepTypesProc
Procedure to list the representation types that the new assembly type can create. This allows Maya to query representation types that can be created by an assembly without actually creating an assembly node.
repTypeLabelProc
Procedure to return a (possibly localized) label which is shown in the user interface for the representation types the assembly can create. The label should be a short, user-friendly, readable description of the representation type.
createOptionBoxProc
Procedure to populate an option box for creation options for the assembly type. If defined, this procedure will populate an option box that is available for creation of that assembly's type.
repPreCreateUIProc
Procedure to provide a dialog before representation creation. If defined, will be invoked by Maya so that the user can interactively make choices before the creation of a type of representation for the assembly.
postCreateUIProc
Procedure to provide a dialog after assembly creation. If defined, will be invoked by Maya so that the user can interactively make choices and apply them to the assembly after its creation.

    """
    pass
    


def assignCommand(data2="string", dividerString="string", optionModifier=bool, data1="string", sourceUserCommands=bool, data3="string", commandModifier=bool, name=bool, altModifier=bool, command="string", numDividersPreceding=int, addDivider="string", delete=int, factorySettings=bool, keyString="string", numElements=bool, sortByKey=bool, ctrlModifier=bool, index=int, annotation="string", keyUp=bool):
    """
    assignCommand is undoable, queryable, and editable.
    

    
This command allows the user to assign hotkeys and manipulate the internal array of named command objects. Each object in the array has an 1-based index which is used for referencing. Under expected usage you should not need to use this command directly as the Hotkey Editor may be used to assign hotkeys.
This command is obsolete for setting new hotkeys, instead please use the "hotkey" command.

    """
    pass
    


def assignInputDevice(multiple=bool, clutch="string", continuous=bool, immediate=bool, device="string"):
    """
    assignInputDevice is undoable, queryable, and NOT editable.
    

    
This command associates a command string (i.e. a mel script) with the input device. When the device moves or a button on the device is pressed, the command string is executed as if you typed it into the window. If the command string contains the names of buttons or axes of the device, the current value of these buttons/axes are substituted in. Buttons are reported as booleans and axes as doubles.
This command is most useful for associating buttons on a device with commands. For using a device to capture continous movements it is much more efficient to attach the device directly into the dependency graph.

    """
    pass
    


def assignViewportFactories(string, textureFactory="string", materialFactory="string", nodeType="string"):
    """
    assignViewportFactories is NOT undoable, queryable, and editable.
    

    
Sets viewport factories for displays as materials or textures.

    """
    pass
    


def attachCurve(curvecurvecurve, blendBias=float, reverse2=bool, keepMultipleKnots=bool, method=int, blendKnotInsertion=bool, object=bool, nodeState=int, replaceOriginal=bool, name="string", parameter=float, caching=bool, constructionHistory=bool, reverse1=bool):
    """
    attachCurve is undoable, queryable, and editable.
    

    
This attach command is used to attach curves. Once the curves are attached, there will be multiple knots at the joined point(s). These can be kept or removed if the user wishes.
If there are two curves, the end of the first curve is attached to the start of the second curve. If there are more than two curves, closest endpoints are joined.
Note: if the command is done with Keep Original off, the first curve is replaced by the attached curve. All other curves will remain, the command does not delete them.

    """
    pass
    


def attachDeviceAttr(axis="string", clutch="string", selection=bool, camera=bool, attribute="string", cameraRotate=bool, cameraTranslate=bool, device="string"):
    """
    attachDeviceAttr is undoable, queryable, and NOT editable.
    

    
This command associates a device/axis pair with a node/attribute pair. When the device axis moves, the value of the attribute is set to the value of the axis. This value can be scaled and offset using the setAttrScale command.

    """
    pass
    


def attachSurface(surfacesurface, blendBias=float, reverse2=bool, directionU=bool, keepMultipleKnots=bool, method=int, swap1=bool, blendKnotInsertion=bool, caching=bool, object=bool, swap2=bool, nodeState=int, replaceOriginal=bool, name="string", twist=bool, parameter=float, constructionHistory=bool, reverse1=bool):
    """
    attachSurface is undoable, queryable, and editable.
    

    
This attach command is used to attach surfaces. Once the surfaces are attached, there will be multiple knots at the joined point(s). These can be kept or removed if the user wishes.
The end of the first surface is attached to the start of the second surface in the specified direction.
Note: if the command is done with Keep Original off there will be an extra surface in the model (the second surface). The command does not delete it. The first surface is replaced by the attached surface.

    """
    pass
    


def attrColorSliderGrp(docTag="string", height=int, columnWidth4=int, parent="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", rgbValue=float, label="string", highlightColor=float, dragCallback="string", hsvValue=float, columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, attribute="string", dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, attrNavDecision="string", manage=bool, showButton=bool, columnOffset4=int, columnAttach2="string", width=int, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    attrColorSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
Create a color slider group consisting of a label, a color canvas, a slider and a button. Clicking on the canvas will bring up the color editor. If the button is visible, it will allow you to map a texture to the attribute.

    """
    pass
    


def attrCompatibility(stringstring, dumpTable=bool, enable=bool, clear=bool, nodeRename="string", type="string", pluginNode="string", addAttr=bool, version="string", removeAttr=bool, renameAttr="string"):
    """
    attrCompatibility is undoable, NOT queryable, and NOT editable.
    

    
This command is used by Maya to handle compatibility issues between file format versions by providing a mechanism to describe differences between two versions. Plug-in writers can make use of this command to handle attribute compatibility changes to files.
The first optional command argument argument is a node type name and the second optional command argument is the short name of an attribute.
Warning: Only use this command to describe changes in names or attributes of nodes that you have written as plugins. Do not use this command to change information about builtin dependency graph nodes. Removing attributes on a plug-in node is a special case. Use a separate attrCompatibility call with pluginNode flag and name so that these attributes can be tracked even though the plug-in may not be loaded.
Only one flag may be used per invocation of the command. If multiple flags are provided one will arbitrarily be chosen as the action to perform and the others will be silently ignored.

    """
    pass
    


def attrControlGrp(enable=bool, hideMapButton=bool, label="string", handlesAttribute="string", attribute="string", preventOverride=bool, annotation="string", changeCommand="string"):
    """
    attrControlGrp is NOT undoable, queryable, and editable.
    

    
This command creates a control of the type most appropriate for the specified attribute, and associates the control with the attribute. Any change to the control will cause a change in the attribute value, and any change to the attribute value will be reflected in the control. Not all attribute types are supported.

    """
    pass
    


def attrEnumOptionMenu(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", manage=bool, label="string", dragCallback="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, width=int, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, attribute="string", dropCallback="string", noBackground=bool, backgroundColor=float, enumeratedItem=int, isObscured=bool):
    """
    attrEnumOptionMenu is undoable, queryable, and editable.
    

    
This command creates an enumerated attribute control. It is usually an option menu.

    """
    pass
    


def attrEnumOptionMenuGrp(groupName, docTag="string", height=int, columnWidth4=int, parent="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", manage=bool, label="string", highlightColor=float, dragCallback="string", columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, attribute="string", dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, enumeratedItem=int, columnOffset4=int, columnAttach2="string", width=int, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    attrEnumOptionMenuGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label and option menu button associated with an attribute of a node. The attribute should be an integer, and this control allows a UI association of strings to the integers of the attribute. When a new menu item is choosen the corresponding integer will be assigned to the attribute.
This control will automatically read the enumeration values from the attribute if none are provided.

    """
    pass
    


def attrFieldGrp(groupName, docTag="string", extraButton=bool, step=float, columnWidth4=int, extraLabel="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, height=int, dragCallback="string", columnOffset2=int, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, hideMapButton=bool, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, forceAddMapButton=bool, exists=bool, columnAttach4="string", extraButtonCommand="string", numberOfFields=int, extraButtonIcon="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", precision=int, fullPathName=bool, attribute="string", dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, minValue=float, columnWidth=int, maxValue=float, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    attrFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text, plus two to four float fields. These fields will be attached to the specified vector attribute, so that changes in either will be reflected in the other.
The fields created here are expression fields -- while normally operating as a float field, the user can type in any expression starting with the character "-".
The field also has an automatic menu brought up by the right mouse button. The contents of this menu change depending on the state of the attribute being watched by the field.

    """
    pass
    


def attrFieldSliderGrp(groupName, docTag="string", vertical=bool, extraButton=bool, step=float, columnWidth4=int, parent="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, height=int, sliderStep=float, dragCallback="string", columnOffset2=int, isObscured=bool, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, hideMapButton=bool, fieldMinValue=float, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, forceAddMapButton=bool, sliderMaxValue=float, exists=bool, columnAttach4="string", extraButtonCommand="string", extraButtonIcon="string", adjustableColumn2=int, visible=bool, fieldStep=float, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", precision=int, fullPathName=bool, attribute="string", dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, minValue=float, columnWidth=int, maxValue=float, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", sliderMinValue=float, columnAttach6="string", fieldMaxValue=float, rowAttach=int, columnOffset6=int):
    """
    attrFieldSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text, float field and float slider (for values with a min or max specified) The group also supports the notion of a larger secondary range of possible field values.
If an attribute is specified for this object, then it will use any min and max values defined in the attribute. The user-specified values can reduce the min and max, but cannot expand them.
The field created here is an expression field -- while normally operating as a float field, the user can type in any expression starting with the character "=". This will expand the field to occupy the space previously taken by the slider.
The field also has an automatic menu brought up by the right mouse button. The contents of this menu change depending on the state of the attribute being watched by the field.

    """
    pass
    


def attributeInfo(multi=bool, inherited=bool, bool=bool, internal=bool, type="string", hidden=bool, enumerated=bool, allAttributes=bool, logicalAnd=bool, writable=bool, userInterface=bool, leaf=bool, short=bool):
    """
    attributeInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
This command lists all of the attributes that are marked with certain flags. Combinations of flags may be specified and all will be considered. (The method of combination depends on the state of the "logicalAnd/and" flag.) When the "allAttributes/all" flag is specified, attributes of all types will be listed.

    """
    pass
    


def attributeMenu(beginMenu=bool, inputs=bool, editor="string", unregPulldownMenuCommand=int, regPulldownMenuCommand="string", plug="string", finishMenu=bool):
    """
    attributeMenu is NOT undoable, NOT queryable, and NOT editable.
    

    
Action to generate popup connection menus for Hypershade. This command is used internally by the Hypershade panel.

    """
    pass
    


def attributeName(leaf=bool, long=bool, nice=bool, short=bool):
    """
    attributeName is NOT undoable, NOT queryable, and NOT editable.
    

    
This command takes one "node.attribute"-style specifier on the command line and returns either the attribute's long, short, or nice name. (The "nice" name, or UI name, is the name used to display the attribute in Maya's interface, and may be localized when running Maya in a language other than English.) If more than one "node.attribute" specifier is given on the command line, only the first valid specifier is processed.

    """
    pass
    


def attributeQuery(minimum=bool, numberOfChildren=bool, softMinExists=bool, listDefault=bool, softMin=bool, attributeType=bool, niceName=bool, hidden=bool, maximum=bool, softMaxExists=bool, writable=bool, listEnum=bool, keyable=bool, affectsWorldspace=bool, usedAsColor=bool, multi=bool, type="string", storable=bool, usedAsFilename=bool, range=bool, softRange=bool, message=bool, channelBox=bool, listParent=bool, affectsAppearance=bool, exists=bool, listSiblings=bool, categories=bool, minExists=bool, usesMultiBuilder=bool, internalSet=bool, listChildren=bool, enum=bool, softRangeExists=bool, shortName=bool, readable=bool, typeExact="string", internalGet=bool, indeterminant=bool, node="string", longName=bool, rangeExists=bool, worldspace=bool, maxExists=bool, internal=bool, cachedInternally=bool, renderSource=bool, softMax=bool, indexMatters=bool, connectable=bool):
    """
    attributeQuery is NOT undoable, NOT queryable, and NOT editable.
    

    
attributeQuery returns information about the configuration of an attribute. It handles both boolean flags, returning true or false, as well as other return values. Specifying more than one boolean flag will return the logical "and" of all the specified boolean flags. You may not specify any two flags when both do not provide a boolean return type. (eg. "-internal -hidden" is okay but "-range -hidden" or "-range -softRange" is not.)

    """
    pass
    


def attrNavigationControlGrp(groupName, unignore="string", docTag="string", extraButton=bool, delete="string", columnWidth4=int, createNew="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", connectAttrToDropped="string", label="string", highlightColor=float, height=int, dragCallback="string", disconnect="string", columnOffset2=int, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, connectNodeToDropped="string", columnAlign4="string", adjustableColumn5=int, manage=bool, exists=bool, columnAttach4="string", extraButtonCommand="string", relatedNodes="string", extraButtonIcon="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, noIgnorableMenu=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, attribute="string", dropCallback="string", columnAlign3="string", columnAttach=int, noKeyableMenu=bool, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, attrNavDecision="string", ignoreNotSupported=bool, columnOffset4=int, columnAttach2="string", width=int, defaultTraversal="string", columnAttach6="string", isObscured=bool, connectToExisting="string", ignore="string", columnOffset6=int):
    """
    attrNavigationControlGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged label navigation button.
The group is used to help the user manage connections to a particular attribute.
When creating the control you have the opportunity to attach scripts to the control that are executed on various UI events. You can define what happens when the navigation button is pressed, and when a node is dragged and dropped onto this attribute.
The navigation button can traverse to the connected node or can bring up UI to create new connections to the attribute. The button also can show you state information: if there already exists a connection/if the connection is ignored.

    """
    pass
    


def audioTrack(solo=bool, insertTrack=int, track=int, lock=bool, removeTrack=int, mute=bool, title="string", numTracks=int, removeEmptyTracks=bool, swapTracks=int):
    """
    audioTrack is undoable, queryable, and editable.
    

    
This command is used for inserting and removing tracks related to the audio clips displayed in the sequencer. It can also be used to modify the track state, for example, to lock or mute a track.

    """
    pass
    


def autoKeyframe(characterOption="string", state=bool, noReset=bool):
    """
    autoKeyframe is undoable, queryable, and editable.
    

    
With no flags, this command will set keyframes on all attributes that have been modified since an "autoKeyframe -state on" command was issued. To stop keeping track of modified attributes, use "autoKeyframe -state off"
autoKeyframe does not create new animation curves. An attribute must have already been keyframed (with the setKeyframe command) for autoKeyframe to add new keyframes for modified attributes.
You can also query the current state of autoKeyframing with "autoKeyframe -query -state".

    """
    pass
    


def autoPlace(useMouse=bool):
    """
    autoPlace is undoable, NOT queryable, and NOT editable.
    

    
This command takes a point in the centre of the current modeling pane and projects it onto the live surface. This produces a point in 3 space which is returned. If the um/useMouse flag is set the current mouse position is used rather than the centre of the modeling pane.

    """
    pass
    


def autoSave(prompt=bool, folder="string", enable=bool, destination=int, limitBackups=bool, perform=bool, maxBackups=int, destinationFolder=bool, interval=float):
    """
    autoSave is undoable, queryable, and NOT editable.
    

    
Provides an interface to the auto-save mechanism.

    """
    pass
    


def bakeClip(blend=int, keepOriginals=bool, name="string", clipIndex=int):
    """
    bakeClip is undoable, NOT queryable, and NOT editable.
    

    
This command is used to bake clips and blends into a single clip.

    """
    pass
    


def bakePartialHistory(preCache=bool, postSmooth=bool, preDeformers=bool, prePostDeformers=bool, allShapes=bool):
    """
    bakePartialHistory is undoable, queryable, and editable.
    

    
This command is used to bake sections of the construction history of a shape node when possible. A typical usage would be on a shape that has both modelling operations and deformers in its history. Using this command with the -prePostDeformers flag will bake the modeling portions of the graph, so that only the deformers remain.
Note that not all modeling operations can be baked such that they create exactly the same effect after baking. For example, imagine the history contains a skinning operation followed by a smooth. Before baking, the smooth operation is performed each time the skin deforms, so it will smooth differently depending on the output of the skin. When the smooth operation is baked into the skinning, the skin will be reweighted based on the smooth points to attempt to approximate the original behavior. However, the skin node does not perform the smooth operation, it merely performs skinning with the newly calculated weights and the result will not be identical to before the bake.
In general, modeling operations that occur before deformers can be baked precisely. Those which occur after can only be approximated. The -pre and -post flags allow you to control whether only the operations before or after the deformers are baked.
When the command is used on an object with no deformers, the entire history will be deleted.

    """
    pass
    


def bakeResults(time=(), hierarchy="string", destinationLayer="string", float=(), includeUpperBound=bool, bakeOnOverrideLayer=bool, controlPoints=bool, preserveOutsideKeys=bool, simulation=bool, smart=(), disableImplicitControl=bool, removeBakedAttributeFromLayer=bool, shape=bool, sparseAnimCurveBake=bool, minimizeRotation=bool, sampleBy=(), resolveWithoutLayer="string", attribute="string", oversamplingRate=int, animation="string", index=int):
    """
    bakeResults is undoable, queryable, and editable.
    

    
This command allows the user to replace a chain of dependency nodes which define the value for an attribute with a single animation curve. Command allows the user to specify the range and frequency of sampling.
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, do not do anything.
objects: Only act on specified objects. If there are no objects specified, do not do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices should be specified as a range, as shown below.
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

    """
    pass
    


def bakeSimulation(time=(), hierarchy="string", destinationLayer="string", float=(), includeUpperBound=bool, bakeOnOverrideLayer=bool, controlPoints=bool, preserveOutsideKeys=bool, simulation=bool, smart=(), disableImplicitControl=bool, removeBakedAnimFromLayer=bool, shape=bool, sparseAnimCurveBake=bool, minimizeRotation=bool, sampleBy=(), resolveWithoutLayer="string", attribute="string", removeBakedAttributeFromLayer=bool, animation="string", index=int):
    """
    bakeSimulation is undoable, queryable, and editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
The bakeSimulation command is obsolete. Instead, "bakeResults -simulation true" should be used. The bakeSimulation command has retained for backwards compatibility.
This command allows the user to replace a chain of dependency nodes, or implicit relationship, such as those between joints and IK handles, which define the value of an attribute, with a single animation curve. Command allows the user to specify the range and frequency of sampling. Unlike the bakeResults command, this command will actually set the time of the current scene to all the times, in sequence, inside the given time interval before it sets the time back to when it is started. As a result, it may modify the scene.

    """
    pass
    


def baseTemplate(string, force=bool, unload=bool, fileName="string", load=bool, silent=bool, viewList="string", exists=bool, matchFile="string"):
    """
    baseTemplate is NOT undoable, queryable, and editable.
    

    
This is the class for the commands that edit and/or query templates.

    """
    pass
    


def baseView(itemList=bool, itemInfo="string", viewDescription=bool, viewList=bool, viewLabel=bool, viewName="string"):
    """
    baseView is NOT undoable, queryable, and editable.
    

    
A view defines the layout information for the attributes of a particular node type or container. Views can be selected from a set of built-in views or may be defined on an associated container template. This command queries the view-related information for a container node or for a given template. The information returned from this command will be based on the view-related settings in force on the container node at the time of the query (i.e. the container's view mode, template name, view name attributes), when applicable.

    """
    pass
    


def batchRender(renderCommandOptions="string", verbosity=int, filename="string", useRemoteRender=bool, numProcs=int, preRenderCommand="string", useStandalone=bool, melCommand="string", showImage=bool, remoteRenderMachine="string"):
    """
    batchRender is undoable, NOT queryable, and NOT editable.
    

    
The batchRender command is used to spawn off a separate rendering session of the current maya file. If no mayaFile is specified, it'll ask you whether you want the current job killed.
The batchRender will spawn a separate maya process in which commands will be communicated to it through a commandPort. If Maya is unable to find an available port an error will be produced. Maya will attempt to use ports 7835 through 7844.

    """
    pass
    


def bevel(depth="string", bevelShapeType=int, width="string", tolerance="string", cornerType=int, extrudeDepth="string", nodeState=int, range=bool, name="string", caching=bool, object=bool, constructionHistory=bool, polygon=int):
    """
    bevel is undoable, queryable, and editable.
    

    
The bevel command creates a new bevel surface for the specified curve. The curve can be any nurbs curves.

    """
    pass
    


def bevelPlus(curvecurvecurve, polyOutExtrusionType=int, polyOutMethod=int, numberOfSides=int, normalsOutwards=bool, polyOutChordHeight="string", polyOutExtrusionSamples=int, polyOutChordHeightRatio=float, depth="string", polygon=int, extrudeDepth="string", joinSurfaces=bool, polyOutCurveType=int, polyOutUseChordHeight=bool, name="string", polyOutCurveSamples=int, capSides=int, polyOutCount=int, innerStyle=int, width="string", tolerance="string", outerStyle=int, polyOutUseChordHeightRatio=bool, constructionHistory=bool):
    """
    bevelPlus is undoable, queryable, and editable.
    

    
The bevelPlus command creates a new bevel surface for the specified curves using a given style curve. The first curve should be the "outside" curve, and the (optional) rest of them should be inside of the first one. For predictable results, the curves should be planar and all in the same plane.

    """
    pass
    


def bezierAnchorPreset(preset=int):
    """
    bezierAnchorPreset is undoable, NOT queryable, and NOT editable.
    

    
This command provides a queryable interface for Bezier curve shapes.

    """
    pass
    


def bezierAnchorState(smooth=bool, even=bool):
    """
    bezierAnchorState is undoable, NOT queryable, and NOT editable.
    

    
The bezierAnchorState command provides an easy interface to modify anchor states:
- Smooth/Broken anchor tangents - Even/Uneven weighted anchor tangents

    """
    pass
    


def bezierCurveToNurbs():
    """
    bezierCurveToNurbs is undoable, NOT queryable, and NOT editable.
    

    
The bezierCurveToNurbs command attempts to convert an existing NURBS curve to a Bezier curve.

    """
    pass
    


def bezierInfo(anchorFromCV=int, onlyTangentsSelected=bool, onlyAnchorsSelected=bool, isTangentSelected=bool, cvFromAnchor=int, isAnchorSelected=bool):
    """
    bezierInfo is undoable, NOT queryable, and NOT editable.
    

    
This command provides a queryable interface for Bezier curve shapes.

    """
    pass
    


def bindSkin(objects, unbindKeepHistory=bool, delete=bool, colorJoints=bool, byPartition=bool, enable=bool, unlock=bool, toSelectedBones=bool, byClosestPoint=bool, unbind=bool, toSkeleton=bool, partition="string", toAll=bool, doNotDescend=bool, name="string"):
    """
    bindSkin is undoable, queryable, and editable.
    

    
This command binds the currently selected objects to the currently selected skeletons. Shapes which can be bound are: meshes, nurbs curves, nurbs surfaces, lattices, subdivision surfaces, and API shapes. Multiple shapes and multiple skeletons can be bound at once by selecting them or specifying them on the command line. Selection order is not important.
The skin is bound using the so-called "rigid" bind, in which the components are rigidly attached to the closest bone in the skeleton. Flexors can later be added to the skeleton to smooth out the skinning around joints.
The skin(s) can be bound either to the entire skeleton hierarchy of the selected joint(s), or to only the selected joints. The entire hierarchy is the default. The -tsb/-toSelectedBones flag allows binding to only the selected bones.
This command can also be used to detach the skin from the skeleton. Detaching the skin is useful in a variety of situations, such as: inserting additional bones, deleting bones, changing the bind position of the skeleton or skin, or simply getting rid of the skinning nodes altogether. The options to use when detaching the skin depend on how much of the skinning info you want to get rid of. Namely: (1) -delete or -unbind: remove all skinning nodes, (2) -unbindKeepHistory: remove the skinning sets, but keep the weights, (3) -disable: disable the skinning but keep the skinning sets and the weights.

    """
    pass
    


def binMembership(listBins=bool, exists="string", addToBin="string", inheritBinsFromNodes="string", notifyChanged=bool, isValidBinName="string", makeExclusive="string", removeFromBin="string"):
    """
    binMembership is undoable, queryable, and NOT editable.
    

    
Command to assign nodes to bins.

    """
    pass
    


def blend2(curvecurvecurve, polygon=int, leftAnchor=float, reverseLeft=bool, rightAnchor=float, object=bool, tangentTolerance=float, leftStart=float, reverseRight=bool, name="string", positionTolerance=float, rightEnd=float, autoAnchor=bool, leftEnd=float, flipLeftNormal=bool, caching=bool, rightStart=float, autoNormal=bool, multipleKnots=bool, nodeState=int, flipRightNormal=bool, constructionHistory=bool):
    """
    blend2 is undoable, queryable, and editable.
    

    
This command creates a surface by blending between given curves. This is an enhancement (more user control) compared to blend which is now obsolete.

    """
    pass
    


def blendShape(objects, before=bool, exclusive="string", after=bool, resetTargetDelta=int, frontOfChain=bool, includeHiddenSelections=bool, inBetweenIndex=int, prune=bool, geometryIndices=bool, transform="string", inBetween=bool, split=bool, origin="string", envelope=float, geometry="string", name="string", weightCount=int, weight=int, parallel=bool, normalizationGroups=bool, ignoreSelected=bool, afterReference=bool, remove=bool, tangentSpace=bool, automatic=bool, deformerTools=bool, target="string", inBetweenType="string", topologyCheck=bool):
    """
    blendShape is undoable, queryable, and editable.
    

    
This command creates a blendShape deformer, which blends in specified amounts of each target shape to the initial base shape. Each base shape is deformed by its own set of target shapes. Every target shape has an index that associates it with one of the shape weight values.
In the create mode the first item on the selection list is treated as the base and the remaining inputs as targets. If the first item on the list has multiple shapes grouped beneath it, the targets must have an identical shape hierarchy. Additional base shapes can be added in edit mode using the deformers -g flag.

    """
    pass
    


def blendShapeEditor(panel="string", docTag="string", verticalSliders=bool, control=bool, mainListConnection="string", defineTemplate="string", parent="string", unParent=bool, highlightConnection="string", unlockMainConnection=bool, useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", targetList=bool, stateString=bool, exists=bool, updateMainConnection=bool, forceMainConnection="string", targetControlList=bool):
    """
    blendShapeEditor is undoable, queryable, and editable.
    

    
This command creates an editor that derives from the base editor class that has controls for blendShape, control nodes.

    """
    pass
    


def blendShapePanel(tearOff=bool, docTag="string", isUnique=bool, control=bool, tearOffRestore=bool, defineTemplate="string", parent="string", createString=bool, unParent=bool, needsInit=bool, useTemplate="string", init=bool, label="string", replacePanel="string", blendShapeEditor=bool, editString=bool, copy="string", exists=bool, menuBarVisible=bool, tearOffCopy="string", popupMenuProcedure="string"):
    """
    blendShapePanel is undoable, queryable, and editable.
    

    
This command creates a panel that derives from the base panel class that houses a blendShapeEditor.

    """
    pass
    


def blendTwoAttr(objects, time=(), blender="string", controlPoints=bool, attribute0="string", attribute1="string", shape=bool, driver=int, attribute="string", name="string"):
    """
    blendTwoAttr is undoable, queryable, and editable.
    

    
A blendTwoAttr nodes takes two inputs, and blends the values of the inputs from one to the other, into an output value. The blending of the two inputs uses a blending function, and the following formula:
     (1 - blendFunction) * input[0]  +  blendFunction * input[1] 
The blendTwoAttr command can be used to blend the animation of an object to transition smoothly between the animation of two other objects.
When the blendTwoAttr command is issued, it creates a blendTwoAttr node on the specified attributes, and reconnects whatever was previously connected to the attributes to the new blend nodes. You may also specify which two attributes should be used to blend together.
The driver is used when you want to keyframe an object after it is being animated by a blend node. The current driver index specifies which of the two blended attributes should be keyframed.

    """
    pass
    


def blindDataType(longDataName="string", longNames=bool, shortDataName="string", typeId=int, shortNames=bool, query=bool, typeNames=bool, dataType="string"):
    """
    blindDataType is undoable, NOT queryable, and NOT editable.
    

    
This command creates a blind data type, which is represented by a blindDataTemplate node in the DG. A blind data type can have one or more attributes. On the command line, the attributes should be ordered by type for best memory utilization, largest first: string, binary, double, float, int, and finally boolean. Once a blind data type is created, blind data of that type may be assigned using the polyBlindData command. Note that as well as polygon components, blind data may be assigned to objects and to NURBS patches. A blind data type may not be modified after it is created: in order to do so it must be deleted and recreated. Any existing blind data of that type would also need to be deleted and recreated. When used with the query flag, this command will return information about the attributes of the specified blind data type.

    """
    pass
    


def boneLattice(before=bool, exclusive="string", after=bool, bicep=float, joint="string", includeHiddenSelections=bool, frontOfChain=bool, prune=bool, widthRight=float, geometryIndices=bool, transform="string", split=bool, geometry="string", name="string", parallel=bool, ignoreSelected=bool, afterReference=bool, remove=bool, tricep=float, widthLeft=float, lengthOut=float, deformerTools=bool, lengthIn=float):
    """
    boneLattice is undoable, queryable, and editable.
    

    
This command creates/edits/queries a boneLattice deformer. The name of the created/edited object is returned. Usually you would make use of this functionality through the higher level flexor command.

    """
    pass
    


def boundary(stringstringstringstring, range=bool, object=bool, name="string", nodeState=int, order=bool, constructionHistory=bool, endPoint=bool, caching=bool, endPointTolerance="string", polygon=int):
    """
    boundary is undoable, queryable, and editable.
    

    
This command produces a boundary surface given 3 or 4 curves. This resulting boundary surface passes through two of the given curves in one direction, while in the other direction the shape is defined by the remaining curve(s). If the "endPoint" option is on, then the curve endpoints must touch before a surface will be created. This is the usual situation where a boundary surface is useful.
Note that there is no tangent continuity option with this command. Unless all the curve end points are touching, the resulting surface will not pass through all curves. Instead, use the birail command.

    """
    pass
    


def boxDollyCtx(image1="string", alternateContext=bool, history=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    boxDollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a dolly context.

    """
    pass
    


def boxZoomCtx(image1="string", history=bool, zoomScale=float, exists=bool, image2="string", name="string", image3="string"):
    """
    boxZoomCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a box zoom context. If this context is used on a perspective camera, the field of view and view direction are changed. If the camera is orthographic, the orthographic width and eye point are changed. The left and middle mouse interactively zoom the view. The control key can be used to enable box zoom. A box starting from left to right will zoom in, and a box starting from right to left will zoom out.

    """
    pass
    


def bufferCurve(time=(), hierarchy="string", float=(), includeUpperBound=bool, controlPoints=bool, index=int, shape=bool, overwrite=bool, useReferencedCurve=bool, attribute="string", swap=bool, animation="string", exists=bool):
    """
    bufferCurve is undoable, queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command helps manage buffer curve for animated objects

    """
    pass
    


def buildBookmarkMenu(type="string", editor="string"):
    """
    buildBookmarkMenu is undoable, NOT queryable, and NOT editable.
    

    
This command handles building the "dynamic" Bookmark menu, to show all bookmarks ("sets") of a specified type ("sets -text")
menuName is the string returned by the "menu" command.

    """
    pass
    


def buildKeyframeMenu():
    """
    buildKeyframeMenu is undoable, NOT queryable, and NOT editable.
    

    
This command handles building the "dynamic" Keyframe menu, to show attributes of currently selected objects, filtered by the current manipulator.
menuName is the string returned by the "menu" command. The target menu will entries appended to it (and deleted from it) to always show what's currently keyframable.

    """
    pass
    


def button(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", recomputeSize=bool, width=int, label="string", dragCallback="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, exists=bool, enableBackground=bool, actionIsSubstitute=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, align="string", manage=bool, command="string", actOnPress=bool, isObscured=bool):
    """
    button is undoable, queryable, and editable.
    

    
Create a button control capable of displaying a textual label and executing a command when selected by the user.

    """
    pass
    


def buttonManip(scriptselectionItem, icon="string"):
    """
    buttonManip is undoable, NOT queryable, and NOT editable.
    

    
This creates a button manipulator. This manipulator has a position in space and a triad manip for positioning. When you click on the top part of the manip, the command defined by the first argument is executed. The command is associated with the manipulator when it is created.
If a dag object is included on the command line, the manip will be parented to the object. This means moving the object will move the manip. You can move the manip independently of the object using its triad.
Note that a buttonManip may not be parented to more than one object.

    """
    pass
    


def cacheFile(cacheInfo="string", noBackup=bool, prefix=bool, pointCount=bool, fileName="string", refresh=bool, geometry=bool, runupFrames=int, interpEndTime=(), format="string", inTangent="string", worldSpace=bool, doubleToFloat=bool, sampleMultiplier=int, cacheFileNode="string", outAttr="string", pointsAndNormals="string", startTime=(), inAttr="string", replaceCachedFrame=bool, staticCache=bool, deleteCachedFrame=bool, simulationRate=(), channelName="string", createCacheNode=bool, attachFile=bool, pc2File="string", replaceWithoutSimulating=bool, channelIndex=bool, points="string", dataSize=bool, singleCache=bool, cacheFormat="string", convertPc2=bool, cacheableNode="string", directory="string", outTangent="string", interpStartTime=(), appendFrame=bool, endTime=(), creationChannelName="string", cacheableAttrs="string", descriptionFileName=bool):
    """
    cacheFile is undoable, queryable, and editable.
    

    
Creates one or more cache files on disk to store attribute data for a span of frames. The caches can be created for points/normals on a geometry (using the pts/points or pan/pointsAndNormals flag), for vectorArray output data (using the oa/outAttr flag), or for additional node specific data (using the cnd/cacheableNode flag for those nodes that support it).
When the ia/inAttr flag is used, connects a cacheFile node that associates the data file on disk with the attribute.
Frames can be replaced/appended to an existing cache with the rcf/replaceCachedFrame and apf/appendFrame flag. Replaced frames are never deleted. They are stored in the same directory as the original cache files with the name provided by the f/fileName flag. If no file name is provided, the cacheFile name is prefixed with "backup" followed by a unique number.
Single file caches are backed up in their entirety. To revert to an older version, simply attach to this cache. One file per frame caches only backup the description file and the frames that were replaced. To recover these types of caches, the user must rename these files to the original name.

    """
    pass
    


def cacheFileCombine(keepWeights=bool, object="string", connectCache="string", channelName="string", nextAvailable=bool, objectIndex=int, cacheIndex=bool, layerNode=bool):
    """
    cacheFileCombine is undoable, queryable, and editable.
    

    
Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles for a given object.

    """
    pass
    


def cacheFileMerge(endTime=(), geometry=bool, startTime=()):
    """
    cacheFileMerge is undoable, queryable, and editable.
    

    
If selected/specified caches can be successfully merged, will return the start/end frames of the new cache followed by the start/end frames of any gaps in the merged cache for which no data should be written to file. In query mode, will return the names of geometry associated with the specified cache file nodes.

    """
    pass
    


def cacheFileTrack(solo=bool, insertTrack=int, track=int, lock=bool, removeTrack=int, mute=bool, removeEmptyTracks=bool):
    """
    cacheFileTrack is undoable, queryable, and editable.
    

    
This command is used for inserting and removing tracks related to the caches displayed in the trax editor. It can also be used to modify the track state, for example, to lock or mute a track.

    """
    pass
    


def callbacks(dumpCallbacks=bool, hook="string", listCallbacks=bool, clearCallbacks=bool, removeCallback="string", addCallback="string", executeCallbacks=bool, describeHooks=bool, owner="string", clearAllCallbacks=bool):
    """
    callbacks is NOT undoable, NOT queryable, and NOT editable.
    

    
This command allows you to add callbacks at key times during UI creation so that the Maya UI can be extended. The list of standard Maya hooks, as well as the arguments which will be passed to the callback based on the context are enumerated in the describeHooks section below. Custom hooks can also be added if third parties want to add UI extensibility to their plugins.

    """
    pass
    


def camera(camera, nearClipPlane="string", farClipPlane="string", worldCenterOfInterest="string", cameraScale=float, shutterAngle=int, overscan=float, focalLength=float, shakeOverscanEnabled=bool, displaySafeTitle=bool, horizontalFilmOffset=float, shakeEnabled=bool, focusDistance="string", journalCommand=bool, farFocusDistance="string", renderPanZoom=bool, verticalFilmOffset=float, horizontalPan=float, displayFieldChart=bool, displayFilmPivot=bool, verticalRollPivot=float, filmFitOffset=float, worldUp="string", zoom=float, verticalPan=float, filmFit="string", depthOfField=bool, lockTransform=bool, lensSqueezeRatio=float, displaySafeAction=bool, clippingPlanes=bool, preScale=float, orthographicWidth="string", startupCamera=bool, filmRollOrder="string", homeCommand="string", aspectRatio=float, postScale=float, verticalFieldOfView=int, filmTranslateV=float, displayFilmGate=bool, panZoomEnabled=bool, centerOfInterest="string", filmTranslateH=float, rotation=int, filmRollValue=int, shakeOverscan=float, horizontalFilmAperture=float, horizontalFieldOfView=int, orthographic=bool, horizontalRollPivot=float, displayGateMask=bool, verticalFilmAperture=float, verticalLock=bool, displayResolution=bool, verticalShake=float, motionBlur=bool, nearFocusDistance="string", displayFilmOrigin=bool, position="string", horizontalShake=float, stereoHorizontalImageTranslate=float, fStop=float, stereoHorizontalImageTranslateEnabled=bool):
    """
    camera is undoable, queryable, and editable.
    

    
Create, edit, or query a camera with the specified properties.
The resulting camera can be repositioned using the viewPlace command. Many of the camera settings only affect the resulting rendered image. E.g. the F/Stop, shutter speed, the film related options, etc. Scaling the camera icon does not change any camera properties.

    """
    pass
    


def cameraSet(camera="string", insertAt=bool, deleteLayer=bool, objectSet="string", clearDepth=bool, appendTo=bool, layer=int, active=bool, numLayers=bool, order=int, deleteAll=bool, name="string"):
    """
    cameraSet is undoable, queryable, and editable.
    

    
This command manages camera set nodes. Camera sets allow the users to break a single camera shot into layers. Instead of drawing all objects with a single camera, you can isolate the camera to only focus on certain objects and layer another camera into the viewport that draws the other objects. The situation to use camera sets primarily occurs when building stereoscopic scenes.
For example, a set of stereo parameters may make the background objects divergent beyond the tolerable range of the human perceptual system. However, you like the settings because the main focus is in the foreground and the depth is important to the visual look of the scene. You can use camera sets to break apart the shot into a foreground stereo camera and background stereo camera. The foreground stereo camera will retain the original parameters; however, it will only focus on the foreground elements. The background stereo camera will have a different set of stereo parameters and will only draw the background element.
Camera sets can be viewed using the stereo viewer and are currently only designed to work with stereo camera rigs.

    """
    pass
    


def cameraView(object, bookmarkType=int, camera="string", setView=bool, removeBookmark=bool, addBookmark=bool, setCamera=bool, name="string"):
    """
    cameraView is undoable, NOT queryable, and editable.
    

    
This command creates a preset view for a camera which is then independent of the camera. The view stores a camera's eye point, center of interest point, up vector, tumble pivot, horizontal aperture, vertical aperature, focal length, orthographic width, and whether the camera is orthographic or perspective by default. Or you can only store 2D pan/zoom attributes by setting the bookmarkType to 1. These settings can be applied to any other camera through the set camera flag.
This command can be used for creation or edit of camera view objects. This command can only be executed with one of the add bookmark, or remove bookmark and one of set camera, or the set view flags set.

    """
    pass
    


def canCreateCaddyManip():
    """
    canCreateCaddyManip is undoable, NOT queryable, and NOT editable.
    

    
This command returns true if there can be a manipulator made for the specified selection, false otherwise.

    """
    pass
    


def canCreateManip():
    """
    canCreateManip is undoable, NOT queryable, and NOT editable.
    

    
This command returns true if there can be a manipulator made for the specified selection, false otherwise.

    """
    pass
    


def canvas(string, docTag="string", height=int, defineTemplate="string", parent="string", pressCommand="string", numberOfPopupMenus=bool, useTemplate="string", rgbValue=float, highlightColor=float, popupMenuArray=bool, hsvValue=float, annotation="string", enable=bool, dropCallback="string", width=int, exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    canvas is undoable, queryable, and editable.
    

    
Creates a control capable of displaying a color swatch. This control can also accept a command to be called when the colour swatch is pressed by the user.
Note: The -dgc/dragCallback and -dpc/dropCallback are not available for this control.

    """
    pass
    


def changeSubdivComponentDisplayLevel(relative=bool, level=int):
    """
    changeSubdivComponentDisplayLevel is undoable, queryable, and NOT editable.
    

    
Explicitly forces the subdivision surface to display components at a particular level of refinement.

    """
    pass
    


def changeSubdivRegion(action=int, level=int):
    """
    changeSubdivRegion is undoable, NOT queryable, and NOT editable.
    

    
Changes a subdivision surface region based on the command parameters. The command operates on the selected subdivision surfaces.

    """
    pass
    


def channelBox(string, docTag="string", height=int, defineTemplate="string", outputObjectList=bool, hyperbolic=bool, preventOverride=bool, numberOfPopupMenus=bool, useTemplate="string", maxHeight=int, shapeObjectList=bool, historyObjectList=bool, highlightColor=float, select=bool, inputs=bool, nodeRegex="string", dragCallback="string", enableLabelSelection=bool, annotation="string", enable=bool, attrColor=float, longNames=bool, selectedShapeAttributes=bool, attributeEditorMode=bool, labelWidth=int, maxWidth=int, attrFilter="string", parent="string", shapes=bool, execute="string", outputs=bool, isObscured=bool, exists=bool, speed=float, update=bool, niceNames=bool, noBackground=bool, enableBackground=bool, selectedOutputAttributes=bool, visibleChangeCommand="string", visible=bool, mainListConnection="string", takeFocus=bool, precision=int, fullPathName=bool, dropCallback="string", mainObjectList=bool, popupMenuArray=bool, containerAtTop=bool, showTransforms=bool, backgroundColor=float, selectedMainAttributes=bool, manage=bool, fieldWidth=int, useManips="string", attrRegex="string", selectedHistoryAttributes=bool, width=int, attrBgColor=float, fixedAttrList="string", showNamespace=bool):
    """
    channelBox is undoable, queryable, and editable.
    

    
This command creates a channel box, which is sensitive to the active list. It displays certain attributes (channels) of the last node on the active list, and provides a two-way connection to keep the widget up to date.
Note: when setting the color of attribute names, that color is only valid for its current Maya session; each subsequent session will display the default color for the attribute name(s) listed in the Channel Box. Any subsequent attributes that are added to the Channel Box will be affected by prior regular expressions in their current Maya session.

    """
    pass
    


def character(subtract="string", split="string", include="string", offsetNode=bool, addOffsetObject="string", excludeRotate=bool, flatten="string", intersection="string", isIntersecting="string", scheduler=bool, memberIndex=int, text="string", isMember="string", characterPlug=bool, removeOffsetObject="string", excludeDynamic=bool, library=bool, userAlias="string", noWarnings=bool, name="string", excludeVisibility=bool, union="string", addElement="string", excludeScale=bool, forceElement="string", clear="string", excludeTranslate=bool, root="string", empty=bool, nodesOnly=bool, remove="string"):
    """
    character is undoable, queryable, and editable.
    

    
This command is used to manage the membership of a character. Characters are a type of set that gathers together the attributes of a node or nodes that a user wishes to animate as a single entity.

    """
    pass
    


def characterize(posture="string", effectors="string", changePivotPlacement=bool, addFloorContactPlane=bool, autoActivateBodyPart=bool, addAuxEffector=bool, type="string", placeNewPivot=bool, addMissingEffectors=bool, activatePivot=bool, pinHandFeet=bool, stancePose="string", sourceSkeleton="string", attributeFromHIKProperty="string", attributeFromHIKPropertyMode="string", name="string", fkSkeleton="string"):
    """
    characterize is undoable, queryable, and editable.
    

    
This command is used to scan a joint hierarchy for predefined joint names or labels. If the required joints are found, human IK effectors will be created to control the skeleton using full-body IK. Alternatively, you can manually create all of the components required for fullbody IK, and use this command to hook them up. Fullbody IK needs 3 major components: the user input skeleton (sk), the fk skeleton on which keys are set (fk) and the hik effectors (ik). Together fk and ik provide parameters to the fullbody IK engine, which solves for the output and plots it onto sk. This command usage is used internally by Maya when importing data from fbx files, but is not generally recommended.
Note that a minimum set of required joint names or joint labels must be found in order for the characterize command to succeed. Please refer to the Maya documentation for details on properly naming or labeling your skeleton. The skeleton should also be z-facing, with its y-axis up, its left hand parallel to positive x-axis and right hand parallel to negative x-axis. END_COMMENT

    """
    pass
    


def characterMap(mapMethod="string", mapping="string", unmapNode="string", mapNode="string", unmapAttr="string", proposedMapping=bool, mapAttr="string"):
    """
    characterMap is undoable, queryable, and editable.
    

    
This command is used to create a correlation between the attributes of 2 or more characters.

    """
    pass
    


def checkBox(string, docTag="string", height=int, onCommand="string", defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", highlightColor=float, annotation="string", enable=bool, offCommand="string", preventOverride=bool, popupMenuArray=bool, exists=bool, changeCommand="string", enableBackground=bool, recomputeSize=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", value=bool, noBackground=bool, backgroundColor=float, align="string", manage=bool, editable=bool, isObscured=bool):
    """
    checkBox is undoable, queryable, and editable.
    

    
This command creates a check box. A check box is a simple control containing a text label and a state of either on or off. Commands can be attached to any or all of the following events: when the check box is turned on, turned off, or simply when it's state is changed.

    """
    pass
    


def checkBoxGrp(groupName, docTag="string", height=int, onCommand="string", useTemplate="string", offCommand1="string", popupMenuArray=bool, rowAttach=int, changeCommand3="string", changeCommand4="string", visibleChangeCommand="string", columnAttach3="string", numberOfCheckBoxes=int, columnWidth1=int, dropCallback="string", noBackground=bool, vertical=bool, columnWidth4=int, parent="string", label="string", highlightColor=float, columnAlign4="string", onCommand2="string", columnAttach4="string", valueArray3=bool, changeCommand2="string", offCommand="string", visible=bool, columnWidth2=int, changeCommand1="string", adjustableColumn3=int, backgroundColor=float, columnWidth5=int, label3="string", enable1=bool, onCommand3="string", columnOffset6=int, valueArray4=bool, offCommand4="string", value2=bool, dragCallback="string", columnAlign5="string", columnOffset5=int, columnAlign3="string", adjustableColumn5=int, columnWidth6=int, value1=bool, columnOffset3=int, label4="string", valueArray2=bool, adjustableColumn2=int, enable=bool, adjustableColumn6=int, columnWidth3=int, preventOverride=bool, value3=bool, offCommand2="string", enable4=bool, onCommand4="string", isObscured=bool, enable3=bool, numberOfPopupMenus=bool, defineTemplate="string", width=int, labelArray3="string", offCommand3="string", columnOffset2=int, annotation="string", changeCommand="string", adjustableColumn4=int, value4=bool, exists=bool, onCommand1="string", columnAlign=int, enableBackground=bool, label1="string", adjustableColumn=int, columnAlign2="string", columnAlign6="string", labelArray4="string", fullPathName=bool, enable2=bool, labelArray2="string", columnAttach=int, columnAttach5="string", columnWidth=int, manage=bool, editable=bool, columnOffset4=int, label2="string", columnAttach2="string", columnAttach6="string"):
    """
    checkBoxGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates from one to four check boxes in a single row. They can have an optional text label.
TelfBaseGrpCmd.cpp

    """
    pass
    


def checkDefaultRenderGlobals(string):
    """
    checkDefaultRenderGlobals is NOT undoable, queryable, and editable.
    

    
To query whether or not the defaultRenderGlobals node has been modified since the last file save, use `ls -modified`. To force the scene to be dirty/clean use `file -modified`

    """
    pass
    


def choice(objects, time=(), controlPoints=bool, selector="string", shape=bool, sourceAttribute="string", attribute="string", index=int, name="string"):
    """
    choice is undoable, queryable, and editable.
    

    
The choice command provides a mechanism for changing the inputs to an attribute based on some (usually time-based) criteria. For example, an object could be animated from frames 1 to 30 by a motion path, then from frames 30 to 50 it follows keyframe animation, and after frame 50 it returns to the motion path. Or, a revolve surface could change its input curve depending on some transform's rotation value.
The choice command creates a choice node (if one does not already exist) on all specified attributes of the selected objects. If the attribute was already connected to something, that something is now reconnected to the i'th index of the choice node's input (or the next available input if the -in/index flag is not specified). If a source attribute is specified, then that attribute is connected to the choice node's i'th input instead.
The choice node operates by using the value of its selector attribute to determine which of its input attributes to pass through to its output. The input attributes can be of any type. For example, if the selector attribute was connected by an animation curve with keyframes at (1,1), (30,2) and (50,1), then that would mean that the choice node would pass on the data from input[1] from time 1 to 30, and after time 50, and the data from input[2] between times 30 and 50.
This command returns the names of the created or modified choice nodes, and if a keyframe was added to the animation curve, it specifies the index (or value on the animation curve).

    """
    pass
    


def circle(centerY="string", radius="string", center="string", object=bool, normal="string", degree=int, firstPointZ="string", fixCenter=bool, centerZ="string", centerX="string", caching=bool, tolerance="string", name="string", first="string", firstPointX="string", sweep=int, sections=int, useTolerance=bool, firstPointY="string", nodeState=int, normalY="string", normalX="string", normalZ="string", constructionHistory=bool):
    """
    circle is undoable, queryable, and editable.
    

    
The circle command creates a circle or partial circle (arc)

    """
    pass
    


def circularFillet(surfacesurface, positionTolerance=float, curveOnSurface=bool, object=bool, secondaryRadius="string", nodeState=int, tangentTolerance=float, primaryRadius="string", constructionHistory=bool, caching=bool, name="string"):
    """
    circularFillet is undoable, queryable, and editable.
    

    
The cmd is used to compute the rolling ball surface fillet ( circular fillet ) between two given NURBS surfaces. To generate trim curves on the surfaces, use -cos true.

    """
    pass
    


def clearCache(computed=bool, allNodes=bool, dirty=bool):
    """
    clearCache is NOT undoable, NOT queryable, and NOT editable.
    

    
Even though dependency graph values are computed or dirty they may still occupy space temporarily within the nodes. This command goes in to all of the data that can be regenerated if required and removes it from the caches (datablocks), thus clearing up space in memory.

    """
    pass
    


def clip(sourceClipName=bool, mapMethod="string", pasteInstance=bool, animCurveRange=bool, defaultAbsolute=bool, absoluteRotations=bool, active="string", translationOffset=float, isolate=bool, copy=bool, character=bool, rotationsAbsolute=bool, rotationOffset=float, expression=bool, addTrack=bool, split=(), ignoreSubcharacters=bool, allAbsolute=bool, newName="string", startTime=(), name="string", allSourceClips=bool, paste=bool, leaveOriginal=bool, constraint=bool, allClips=bool, removeTrack=bool, scheduleClip=bool, absolute=bool, allRelative=bool, remove=bool, useChannel="string", duplicate=bool, endTime=()):
    """
    clip is undoable, queryable, and editable.
    

    
This command is used to create, edit and query character clips.

    """
    pass
    


def clipEditor(docTag="string", allTrackHeights=int, defineTemplate="string", parent="string", displayTangents="string", lookAt="string", clipDropCmd="string", lockMainConnection=bool, deselectAll=bool, unParent=bool, clipStyle=int, listAllCharacters=bool, panel="string", displayActiveKeyTangents="string", mainListConnection="string", displayValues="string", snapValue="string", highlightConnection="string", highlightedBlend="string", frameRange=float, stateString=bool, exists=bool, displayInfinities="string", selectClip="string", displayActiveKeys="string", frameAll=bool, control=bool, selectBlend="string", snapTime="string", autoFit="string", useTemplate="string", manageSequencer=bool, selectionConnection="string", forceMainConnection="string", unlockMainConnection=bool, highlightedClip="string", updateMainConnection=bool, menuContext="string", initialized=bool, displayKeys="string", deleteCmd="string", filter="string", listCurrentCharacters=bool):
    """
    clipEditor is undoable, queryable, and editable.
    

    
Create a clip editor with the given name.

    """
    pass
    


def clipEditorCurrentTimeCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    clipEditorCurrentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the track area of a clip editor.

    """
    pass
    


def clipMatching(matchRotation=int, clipDst="string", matchTranslation=int, clipSrc="string"):
    """
    clipMatching is undoable, NOT queryable, and NOT editable.
    

    
This command is used to compute an offset to apply on a source clip in order to automatically align it to a destination clip at a specified match element. For this command to work, offset objects must be specified for the character.

    """
    pass
    


def clipSchedule(sourceClipName=bool, shift=int, group=bool, weightStyle=int, blendUsingNode="string", defaultAbsolute=bool, removeTrack=int, scale=float, mute=bool, clipIndex=int, groupIndex=int, instance="string", character=bool, preCycle=float, sourceEnd=(), postCycle=float, solo=bool, track=int, listCurves=bool, weight=float, blend=int, groupName="string", allAbsolute=bool, hold=(), removeEmptyTracks=bool, sourceStart=(), name="string", start=(), cycle=float, blendNode=int, enable=bool, rotationsAbsolute=bool, insertTrack=int, listPairs=bool, shiftIndex=int, allRelative=bool, remove=bool, removeBlend=int, lock=bool):
    """
    clipSchedule is undoable, queryable, and editable.
    

    
This command is used to create, edit and query clips and blends in the Trax editor. It operates on the clipScheduler node attached to the character. In query mode, if no flags are specified, returns an array of strings in this form: (clipName,clipIndex,clipStart,clipSourceStart,clipSourceEnd,clipScale,clipPreCycle,clipPostCycle,clipHold)

    """
    pass
    


def clipSchedulerOutliner(docTag="string", height=int, clipScheduler="string", defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    clipSchedulerOutliner is undoable, queryable, and editable.
    

    
This command creates/edits/queries a clip scheduler outliner control.

    """
    pass
    


def closeCurve(blendBias=float, blendKnotInsertion=bool, curveOnSurface=bool, object=bool, nodeState=int, replaceOriginal=bool, constructionHistory=bool, preserveShape=int, parameter=float, caching=bool, name="string"):
    """
    closeCurve is undoable, queryable, and editable.
    

    
The closeCurve command closes a curve, making it periodic. The pathname to the newly closed curve and the name of the resulting dependency node are returned. If a curve is not specified in the command, then the first active curve will be used.

    """
    pass
    


def closeSurface(surface ,surfaceIsoparm, blendBias=float, blendKnotInsertion=bool, caching=bool, nodeState=int, object=bool, direction=int, replaceOriginal=bool, name="string", preserveShape=int, parameter=float, constructionHistory=bool):
    """
    closeSurface is undoable, queryable, and editable.
    

    
The closeSurface command closes a surface in the U, V, or both directions, making it periodic. The close direction is controlled by the direction flag. If a surface is not specified in the command, then the first selected surface will be used.
The pathname to the newly closed surface and the name of the resulting dependency node are returned.
This command also handles selected surface isoparms. For example, if an isoparm is specified, surface1.u[0.33], then the surface will be closed in V, regardless of the direction flag.

    """
    pass
    


def cluster(objects, before=bool, exclusive="string", split=bool, geometryIndices=bool, after=bool, relative=bool, resetGeometry=bool, ignoreSelected=bool, frontOfChain=bool, includeHiddenSelections=bool, weightedNode="string", envelope=float, deformerTools=bool, parallel=bool, bindState=bool, geometry="string", remove=bool, prune=bool, afterReference=bool, name="string"):
    """
    cluster is undoable, queryable, and editable.
    

    
The cluster command creates a cluster or edits the membership of an existing cluster. The command returns the name of the cluster node upon creation of a new cluster.
After creating a cluster, the cluster's weights can be modified using the percent command or the set editor window.

    """
    pass
    


def cmdFileOutput(status=int, closeAll=bool, close=int, open="string"):
    """
    cmdFileOutput is undoable, queryable, and NOT editable.
    

    
This command will open a text file to receive all of the commands and results that normally get printed to the Script Editor window or console. The file will stay open until an explicit -close with the correct file descriptor or a -closeAll, so care should be taken not to leave a file open.
To enable logging to commence as soon as Maya starts up, the environment variable MAYA_CMD_FILE_OUTPUT may be specified prior to launching Maya. Setting MAYA_CMD_FILE_OUTPUT to a filename will create and output to that given file. To access the descriptor after Maya has started, use the -query and -open flags together.

    """
    pass
    


def cmdScrollFieldExecuter(commandCompletion=bool, autoCloseBraces=bool, hasSelection=bool, selectedText=bool, insertText="string", redo=bool, filterKeyPress="string", searchWraps=bool, numberOfLines=int, copySelection=bool, saveSelection="string", text="string", searchMatchCase=bool, source=bool, load=bool, selectAll=bool, spacesPerTab=int, removeStoredContents="string", currentLine=int, showTooltipHelp=bool, textLength=bool, loadContents="string", sourceType="string", storeContents="string", saveSelectionToShelf=bool, select=int, searchAndSelect=bool, tabsForIndent=bool, executeAll=bool, execute=bool, showLineNumbers=bool, hasFocus=bool, clear=bool, pasteSelection=bool, searchString="string", cutSelection=bool, appendText="string", searchDown=bool, replaceAll="string", objectPathCompletion=bool, undo=bool):
    """
    cmdScrollFieldExecuter is undoable, queryable, and editable.
    

    
A script editor executer control used to issue script commands to Maya.

    """
    pass
    


def cmdScrollFieldReporter(docTag="string", height=int, suppressStackTrace=bool, defineTemplate="string", parent="string", suppressErrors=bool, numberOfPopupMenus=bool, useTemplate="string", pasteSelection=bool, dragCallback="string", highlightColor=float, annotation="string", copySelection=bool, preventOverride=bool, popupMenuArray=bool, text="string", width=int, suppressWarnings=bool, echoAllCommands=bool, selectAll=bool, stackTrace=bool, exists=bool, hasFocus=bool, suppressResults=bool, enable=bool, enableBackground=bool, textLength=bool, visibleChangeCommand="string", visible=bool, lineNumbers=bool, saveSelection="string", saveSelectionToShelf=bool, fullPathName=bool, select=int, dropCallback="string", noBackground=bool, backgroundColor=float, clear=bool, manage=bool, cutSelection=bool, suppressInfo=bool, isObscured=bool, receiveFocusCommand="string", filterSourceType="string"):
    """
    cmdScrollFieldReporter is undoable, queryable, and editable.
    

    
A script editor reporter control used to receive and display the history of processed commmands.

    """
    pass
    


def cmdShell(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, prompt="string", popupMenuArray=bool, annotation="string", numberOfHistoryLines=int, preventOverride=bool, numberOfSavedLines=int, exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, enable=bool, fullPathName=bool, dropCallback="string", dragCallback="string", noBackground=bool, backgroundColor=float, clear=bool, manage=bool, isObscured=bool):
    """
    cmdShell is undoable, queryable, and editable.
    

    
This command creates a scrolling field that behaves similar to a unix shell for entering user input. You may specify the number of lines that will be remembered by the field with the -nsl/numberOfSavedLines flag. The default number of lines saved is 100. The shellField also maintains a command history buffer. You can specify the number of input lines that will be saved with the -hlc/historyLineCount flag. The default size of this buffer is 10.

    """
    pass
    


def coarsenSubdivSelectionList():
    """
    coarsenSubdivSelectionList is undoable, NOT queryable, and NOT editable.
    

    
Coarsens a subdivision surface set of components based on the selection list. The selected components are selected at a coarser level.

    """
    pass
    


def collision(objects, friction=float, resilience=float, name="string"):
    """
    collision is undoable, queryable, and editable.
    

    
The collision command causes particles to collide with geometry. It also allows you to specify values for the surface properties (friction and resilience) of the collision. These values are stored in the geoConnector node for the geometry object. Unlike earlier versions of Maya, there is no separate "collision node."
If a soft object is in the selection list, the collision command assumes that you want to make it a collider. In order to make the soft object collide with something use, use connectDynamic -c. The collision menu option sorts this out using the lead object rule and issues the necessary commands. On creation, this command returns a string array of the geometry names that were setup for particle collision.
When the command is used to query information, there are several possible return types. These include:
If the -resilience or -friction flag is passed on the command line and a single collision geometry is either selected or on the command line, then resilience or friction value for that collision geometry is returned as a single float value.
If the -resilience or -friction flag is passed on the command line and a single collision geometry and a single particle object are either selected or on the command line, then two results might occur. If the particle object is not set up to collide with the geometry, then an error is displayed stating that. If the objects are set up to collide with each other, then the resilience or friction value that the particle object is using for collisions with the geometry is returned as a single float value. This can be different than the geometry's resilience and friction, because the user may break the connection from the geometry's geoConnector node's resilience or friction to the particle, and set a different value in the particle's collisionResilience, collisionFriction or collisionOffset attribute that is used for that geometry. This allows the user to make each particle respond to the same surface differently.
If neither flag is pass on the command line and a single geometry and single particle object are either selected or on the command line, then a single integer value of 1 is returned if the objects are set up to collide with each other, and 0 is returned if they are not.
Lastly, if no flags are passed on the command line and a single particle object is either selected or on the command line, then a string array with the names of all geometries that the particle object will collide against and the multiIndex that the geometries are connected to is returned. The array is formatted as follows:
pPlaneShape1:0 pPlaneShape2:2 nurbsSphereShape1:3
...where the number following the ":" is the multiIndex.

    """
    pass
    


def color(objects, userDefined=int, rgbColor=float):
    """
    color is undoable, NOT queryable, and NOT editable.
    

    
This command sets the dormant wireframe color of the specified objects to be their class color or if the -ud/userDefined flag is specified, one of the user defined colors. The -rgb/rgbColor flags can be specified if the user requires floating point RGB colors.

    """
    pass
    


def colorAtPoint(samplesV=int, coordU=float, maxV=float, output="string", minV=float, maxU=float, coordV=float, minU=float, samplesU=int):
    """
    colorAtPoint is NOT undoable, NOT queryable, and NOT editable.
    

    
The colorAtPoint command is used to query textures or ocean shaders at passed in uv coordinates. (For ocean shaders uv is x and z in worldspace ). The return value is a floating point array whose size is determined by either the number of input uv arguments passed in and the the queried value. One can query alpha only, rgb only, or rgba values. The returned array is only single indexed, so if rgb is specified then the index for red values would be index * 3. Blue is index * 3 + 1, and green is index * 3 + 2. For rgba use a multiple of 4 instead of 3. For alpha only one can simply use the index. There are two basic argument formats that may be used: colorAtPoint -u 0 -v 0 -u .2 -v .1 etc.. for all points or colorAtPoint -mu 0 -mv 0 -xu 1 -xv 1 -su 10 -sv 10 // samples 100 points If one is sampling several points and they are all in a regular grid formation it is more efficient to call this routine with the latter method, which uses a min/max uv and number of samples, rather than a long argument list of uv coords.
return values (-o A or RGB or RGBA )
individual UV coordinates to sample (-u float -v float )
(numbers of calls to -u and -v must match)
uniform grid of points to sample (-su int -sv int)
(may not use this in combination with -u or -v)
bounds for sample grid (-mu float -mv float -xu float -xv float)

    """
    pass
    


def colorEditor(parent="string", mini=bool, result=bool, rgbValue=float, hsvValue=float, position=bool):
    """
    colorEditor is undoable, queryable, and NOT editable.
    

    
The colorEditor command displays a modal dialog that may be used to specify colors in RGB or HSV. The default behaviour when no arguments are specified is to provide an initial color of black (rgb 0.0 0.0 0.0).
The command will return the user's color component values along with a boolean to indicate whether the dialog was dismissed by pressing the "OK" button. As an alternative to responding to the colorEditor command's return string you can now query the -rgb/rgbValue, -hsv/hsvValue, and -r/result flags to get the same information.

    """
    pass
    


def colorIndex(intfloatfloatfloat, resetToSaved=bool, resetToFactory=bool, hueSaturationValue=bool):
    """
    colorIndex is undoable, queryable, and NOT editable.
    

    
The index specifies a color index in the color palette. The r, g, and b values (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is used) for the color.

    """
    pass
    


def colorIndexSliderGrp(docTag="string", height=int, columnWidth4=int, extraLabel="string", popupMenuArray=bool, invisible=int, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, value=int, dragCallback="string", columnOffset2=int, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, minValue=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", exists=bool, columnAttach4="string", maxValue=int, adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, numberOfPopupMenus=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    colorIndexSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a color slider group consisting of a label, a color canvas and a slider. The value of the slider defines a color index into the a color table. The corresponding color is displayed in the canvas.

    """
    pass
    


def colorInputWidgetGrp(docTag="string", height=int, columnWidth4=int, parent="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", rgbValue=float, label="string", highlightColor=float, dragCallback="string", hsvValue=float, columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", width=int, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    colorInputWidgetGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
Create a color slider group consisting of a label, a color canvas, RGB and HSV sliders. Clicking on the canvas will bring up the color editor.

    """
    pass
    


def colorManagementCatalog(transformConnection="string", removeTransform="string", listTransformConnections=bool, addTransform="string", editUserTransformPath="string", queryUserTransformPath=bool, type="string", listSupportedExtensions=bool, path="string"):
    """
    colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.
    

    
This non-undoable action performs additions and removals of custom color transforms from the Autodesk native color transform catalog. Once a custom color transform has been added to the catalog, it can be used in the same way as the builtin Autodesk native color transforms.

    """
    pass
    


def colorManagementConvert(toDisplaySpace=float):
    """
    colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.
    

    
This command can be used to convert rendering (a.k.a. working) space color values to display space color values. This is useful if you create custom UI with colors painted to screen, where you need to handle color management yourself. The current view transform set in the Color Management user preferences will be used.

    """
    pass
    


def colorManagementFileRules(colorSpace="string", evaluate="string", down="string", moveUp="string", listRules=bool, load=bool, addRule="string", extension="string", save=bool, pattern="string", remove="string"):
    """
    colorManagementFileRules is NOT undoable, queryable, and editable.
    

    
This non-undoable action manages the list of rules that Maya uses to assign an initial input color space to dependency graph nodes that read in color information from a file. Rules are structured in a chain of responsibility, from highest priority rule to lowest priority rule, each rule matching a file path pattern and extension. If a rule matches a given file path, its color space is returned as the result of rules evaluation, and no further rule is considered. The lowest priority rule will always return a match. Rules can be added, removed, and changed in priority in the list. Each rule can have its file path pattern, extension, and color space changed. The rule list can be saved to user preferences, and loaded from user preferences.

    """
    pass
    


def colorManagementPrefs(outputUseViewTransform=bool, refresh=bool, loadedDefaultInputSpaceName="string", viewTransformNames=bool, ocioRulesEnabled=bool, missingColorSpaceNodes=bool, defaultInputSpaceName="string", outputTransformNames=bool, policyFileName="string", popupOnError=bool, colorManagePots=bool, viewTransformName="string", loadedViewTransformName="string", loadedOutputTransformName="string", inputSpaceNames=bool, exportPolicy="string", colorManagementSDKVersion="string", outputTransformName="string", outputTarget="string", loadPolicy="string", colorManagedNodes=bool, renderingSpaceName="string", renderingSpaceNames=bool, loadedRenderingSpaceName="string", outputTransformEnabled=bool, configFilePath="string", equalsToPolicyFile="string", restoreDefaults=bool, cmConfigFileEnabled=bool, cmEnabled=bool):
    """
    colorManagementPrefs is undoable, queryable, and editable.
    

    
This command allows querying and editing the color management global data in a scene. It also allows for setting the view transform and rendering space which automatically configures the color processing in the enabled views.

    """
    pass
    


def colorSliderButtonGrp(string, docTag="string", buttonCommand="string", buttonLabel="string", parent="string", popupMenuArray=bool, image="string", numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", rgbValue=float, label="string", highlightColor=float, height=int, dragCallback="string", hsvValue=float, columnOffset2=int, symbolButtonDisplay=bool, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, adjustableColumn6=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnWidth4=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", exists=bool, columnAttach4="string", useTemplate="string", adjustableColumn2=int, visible=bool, columnAlign=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", symbolButtonCommand="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", enable=bool, fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", width=int, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    colorSliderButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command object creates a new color slider group with a button and a symbol button. This control is primarily used in the rendering UI. In this context, the button brings up a dialog that allows the user to assign a texture map to this parameter. Once a texture map is available, a symbol button shows up. When this symbol button is pressed, the user is taken to another dialog to edit the texture map.

    """
    pass
    


def colorSliderGrp(docTag="string", height=int, columnWidth4=int, parent="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", rgbValue=float, label="string", highlightColor=float, dragCallback="string", hsvValue=float, columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", width=int, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    colorSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a color Slider group consisting of a label, a color canvas and a slider. Clicking on the canvas will bring up the color editor dialog.

    """
    pass
    


def columnLayout(string, adjustableColumn=bool, height=int, defineTemplate="string", docTag="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", rowSpacing=int, numberOfChildren=bool, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, parent="string", columnOffset="string", childArray=bool, exists=bool, columnAttach="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, columnWidth=int, manage=bool, columnAlign="string", isObscured=bool):
    """
    columnLayout is undoable, queryable, and editable.
    

    
This command creates a layout that arranges its children in a single column.

    """
    pass
    


def combinationShape(allDrivers=bool, driverTargetName="string", combinationTargetIndex=int, combineMethod=int, driverTargetIndex=int, combinationTargetName="string", exist=bool, addDriver=bool, removeDriver=bool, blendShape="string"):
    """
    combinationShape is undoable, queryable, and editable.
    

    
Command to create or edit drive relationship of blend shape targets

    """
    pass
    


def commandEcho(state=bool, filter="string", lineNumbers=bool, addFilter="string"):
    """
    commandEcho is undoable, queryable, and NOT editable.
    

    
This command controls what is echoed to the command window.

    """
    pass
    


def commandLine(name, docTag="string", height=int, holdFocus=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", enterCommand="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, exists=bool, outputAnnotation="string", numberOfHistoryLines=int, enableBackground=bool, visibleChangeCommand="string", visible=bool, sourceType="string", fullPathName=bool, dropCallback="string", backgroundColor=float, inputAnnotation="string", noBackground=bool, manage=bool, command="string", isObscured=bool):
    """
    commandLine is undoable, queryable, and editable.
    

    
This command creates a single line for command input/output.
The left half is for input, the right half for output.

    """
    pass
    


def commandLogging(historySize=int, logCommands=bool, logFile="string", resetLogFile=bool, recordCommands=bool):
    """
    commandLogging is undoable, queryable, and NOT editable.
    

    
This command controls logging of Maya commands, in memory and on disk.
Note that if commands are logged in memory, they will be available to the crash reporter and appear in crash logs.

    """
    pass
    


def commandPort(returnNumCommands=bool, securityWarning=bool, echoOutput=bool, pickleOutput=bool, prefix="string", noreturn=bool, close=bool, sourceType="string", bufferSize=int, name="string"):
    """
    commandPort is undoable, queryable, and NOT editable.
    

    
Opens or closes the Maya command port. The command port comprises a socket to which a client program may connect. An example command port client "mcp" is included in the Motion Capture developers kit.
It supports multi-byte commands and uses utf-8 as its transform format. It will receive utf8 command string and decode it to Maya native coding. The result will also be encoded to utf-8 before sending back.
Care should be taken regarding INET domain sockets as no user identification, or authorization is required to connect to a given socket, and all commands (including "system(...)") are allowed and executed with the user id and permissions of the Maya user. The prefix flag can be used to reduce this security risk, as only the prefix command is executed.
The query flag can be used to determine if a given command port exists. See examples below.

    """
    pass
    


def componentBox(name, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", maxHeight=int, width=int, dragCallback="string", highlightColor=float, annotation="string", preventOverride=bool, labelWidth=int, maxWidth=int, popupMenuArray=bool, execute="string", exists=bool, enable=bool, enableBackground=bool, rowHeight=int, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", backgroundColor=float, noBackground=bool, manage=bool, precision=int, selectedAttr=bool, isObscured=bool):
    """
    componentBox is undoable, queryable, and editable.
    

    
This command creates a component box, which is sensitive to the active list. It displays certain components of the last node on the active list, and provides a two-way connection to keep the widget up to date.

    """
    pass
    


def componentEditor(docTag="string", selectionConnection="string", defineTemplate="string", parent="string", newTab="string", useTemplate="string", lockMainConnection=bool, unParent=bool, panel="string", mainListConnection="string", hideZeroColumns=bool, setOperationLabel=int, highlightConnection="string", selected=bool, stateString=bool, exists=bool, updateMainConnection=bool, operationType=int, control=bool, showSelected=bool, operationLabels=bool, operationCount=bool, lockInput=bool, forceMainConnection="string", floatField="string", unlockMainConnection=bool, sortAlpha=bool, floatSlider="string", hidePathName=bool, removeTab="string", precision=int, filter="string", showObjects=bool):
    """
    componentEditor is undoable, queryable, and editable.
    

    
This command creates a new component editor in the current layout.

    """
    pass
    


def condition(delete=bool, dependency="string", state=bool, initialize=bool, script="string"):
    """
    condition is undoable, queryable, and editable.
    

    
This command creates a new named condition object whose true/false value is calculated by running a mel script. This new condition can then be used for dimming, or controlling other scripts, or whatever.

    """
    pass
    


def cone(useOldInitBehaviour=bool, degree=int, axis="string", pivot="string", sections=int, radius="string", tolerance="string", object=bool, useTolerance=bool, polygon=int, spans=int, nodeState=int, name="string", heightRatio=float, startSweep=int, caching=bool, endSweep=int, constructionHistory=bool):
    """
    cone is undoable, queryable, and editable.
    

    
The cone command creates a new cone and/or a dependency node that creates one, and returns their names.

    """
    pass
    


def confirmDialog(messageAlign="string", icon="string", backgroundColor=float, defaultButton="string", message="string", button="string", cancelButton="string", title="string", dismissString="string", parent="string", annotation="string"):
    """
    confirmDialog is undoable, NOT queryable, and NOT editable.
    

    
The confirmDialog command creates a modal dialog with a message to the user and a variable number of buttons to dismiss the dialog. The dialog is dismissed when the user presses any button or chooses the close item from the window menu. In the case where a button is pressed then the name of the button selected is returned. If the dialog is dismissed via the close item then the string returned is specified by the dismissString flag.
The default behaviour when no arguments are specified is to create an empty single button dialog.

    """
    pass
    


def connectAttr(force=bool, nextAvailable=bool, referenceDest="string", lock=bool):
    """
    connectAttr is undoable, NOT queryable, and NOT editable.
    

    
Connect the attributes of two dependency nodes and return the names of the two connected attributes. The connected attributes must be be of compatible types. First argument is the source attribute, second one is the destination.
Refer to dependency node documentation.

    """
    pass
    


def connectControl(preventOverride=bool, preventContextualMenu=bool, fileName=bool, index=int):
    """
    connectControl is undoable, NOT queryable, and NOT editable.
    

    
This command attaches a UI widget, specified as the first argument, to one or more dependency node attributes. The attributes/nodes don't have to exist yet, they will get looked up as needed. With no flag specified, this command works on these kinds of controls: floatField, floatScrollBar, floatSlider, intField, intScrollBar, intSlider, floatFieldGrp, intFieldGrp, checkBox, radioCollection, and optionMenu. With the index flag, It will also work on the individual components of all other groups.
This command sets up a two-way connection between the control and the (first-specified) attribute. If this first attribute is changed in any way, the control will be appropriately updated to match its value.
Summary: if you change the control, ALL the connected attributes change. If you change the FIRST attribute attached to the control, then the control will change.
NOTE: the two-way connection will not be established if the attributes do not exist when the connectControl command is run. If the user later uses the control, the connection will be established at that time.
To effectively use connectControl with radioCollections and optionMenus, you must attach a piece of data to each radioButton and menuItem. This piece of data (an integer) can be attached using the data flag in the radioButton and menuItem commands. When the button/item is selected, the attribute will be set to the value of its data. When the attribute is changed, the collection (or optionMenu) will switch to the item that matches the new attribute value. If no item matches, it will be left unchanged.
There are some specialized controls that have connection capability (and more) built right into them. See attrFieldSliderGrp, attrFieldGrp, and attrColorSliderGrp. Using these classes can be easier than using connectControl.

    """
    pass
    


def connectDynamic(objects, delete=bool, emitters="string", addScriptHandler="string", fields="string", removeScriptHandler=int, collisions="string"):
    """
    connectDynamic is undoable, NOT queryable, and NOT editable.
    

    
Dynamic connection specifies that the force fields, emitters, or collisions of an object affect another dynamic object. The dynamic object that is connected to a field, emitter, or collision object is influenced by those fields, emitters and collision objects.
Connections are made to individual fields, emitters, collisions. So, if an object owns several fields, if the user wants some of the fields to affect an object, s/he can specify each field with a "-f" flag; but if the user wants to connect all the fields owned by an object, s/he can specify the object name with the "-f" flag. The same is true for emitters and collisions. Different connection types (i.e., for fields vs. emitters) between the same pair of objects are logically independent. In other words, an object can be influenced by another object's fields without being influenced by its emitters or collisions.
Each connected object must be a dynamic object. The object connected to can be any object that owns fields, emitters, etc.; it need not be dynamic. Objects that can own influences are particles, geometry objects (nurbs and polys) and lattices. You can specify either the shape name or the transform name of the object to be influenced.

    """
    pass
    


def connectionInfo(destinationFromSource=bool, isExactSource=bool, isExactDestination=bool, isSource=bool, getExactDestination=bool, sourceFromDestination=bool, getLockedAncestor=bool, isDestination=bool, getExactSource=bool, isLocked=bool):
    """
    connectionInfo is undoable, NOT queryable, and NOT editable.
    

    
The connectionInfo command is used to get information about connection sources and destinations. Unlike the isConnected command, this command needs only one end of the connection.

    """
    pass
    


def connectJoint(objects, connectMode=bool, parentMode=bool):
    """
    connectJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will connect two skeletons based on the two selected joints. The first selected joint can be made a child of the parent of the second selected joint or a child of the second selected joint, depending on the flags used.
Note1: The first selected joint must be the root of a skeleton. The second selected joint must have a parent.
Note2: If a joint name is specified in the command line, it is used as the child and the first selected joint will be the parent. If no joint name is given at the command line, two joints must be selected.

    """
    pass
    


def constrain(stiffness=float, spring=bool, nail=bool, orientation=float, directionalHinge=bool, restLength=float, barrier=bool, hinge=bool, name="string", position=float, pinConstraint=bool, interpenetrate=bool, damping=float):
    """
    constrain is undoable, queryable, and editable.
    

    
This command constrains rigid bodies to the world or other rigid bodies.

    """
    pass
    


def constructionHistory(toggle=bool):
    """
    constructionHistory is undoable, queryable, and NOT editable.
    

    
This command turns construction history on or off.

    """
    pass
    


def container(string, addNode="string", assetMember="string", includeHierarchyAbove=bool, nodeNamePrefix=bool, unbindAndUnpublish="string", fileName="string", publishAndBind="string", publishAsParent="string", asset="string", unsortedOrder=bool, removeContainer=bool, type="string", parentContainer=bool, preview=bool, nodeList=bool, bindAttr="string", publishName="string", includeShaders=bool, name="string", publishAsChild="string", unpublishName="string", includeNetworkDetails="string", removeNode="string", publishAttr="string", unbindChild="string", publishConnections=bool, connectionList=bool, includeTransform=bool, unpublishChild="string", force=bool, unbindAttr="string", findContainer="string", includeShapes=bool, unpublishParent="string", current=bool, unbindParent="string", includeNetwork=bool, publishAsRoot="string", isContainer=bool, includeHierarchyBelow=bool):
    """
    container is undoable, queryable, and editable.
    

    
This command can be used to create and query container nodes. It is also used to perform operations on containers such as:
add and remove nodes from the container
publish attributes from nodes inside the container
replace the connections and values from one container onto another one
remove a container without removing its member nodes

    """
    pass
    


def containerBind(force=bool, allNames=bool, bindingSetList=bool, bindingSet="string", bindingSetConditions=bool, preview=bool):
    """
    containerBind is undoable, queryable, and editable.
    

    
This is an accessory command to the container command which is used for some automated binding operations on the container. A container's published interface can be bound using a bindingSet on the associated container template.

    """
    pass
    


def containerProxy(type="string", fromTemplate="string"):
    """
    containerProxy is undoable, queryable, and editable.
    

    
Creates a new container with the same published interface, dynamic attributes and attribute values as the specified container but with fewer container members. This proxy container can be used as a reference proxy so that values can be set on container attributes without loading in the full container. The proxy container will contain one or more locator nodes. The first locator has dynamic attributes that serve as stand-ins for the original published attributes. The remaining locators serve as stand-ins for any dag nodes that have been published as parent or as child and will be placed at the world space location of the published parent/child nodes. The expected usage of container proxies is to serve as a reference proxy for a referenced container. For automated creation, export and setup of the proxy see the doExportContainerProxy.mel script which is invoked by the "Export Container Proxy" menu item.

    """
    pass
    


def containerPublish(bindTemplateStandins=bool, mergeShared=bool, inConnections=bool, unbindNode="string", bindNode="string", unpublishNode="string", outConnections=bool, publishNode="string"):
    """
    containerPublish is undoable, queryable, and editable.
    

    
This is an accessory command to the container command which is used for some advanced publishing operations on the container. For example, the "publishConnections" flag on the container will publish all the connections, but this command can be used to publish just the inputs, outputs, or to collapse the shared inputs into a single attribute before publishing.

    """
    pass
    


def containerTemplate(templateList="string", fileName="string", fromContainer="string", removeView="string", viewList="string", addBindingSet="string", matchFile="string", baseName="string", searchPath="string", load=bool, layoutMode=int, silent=bool, bindingSetList="string", exists=bool, attributeList="string", unload=bool, matchName="string", expandCompounds=bool, parentAnchor=bool, removeBindingSet="string", addNames=bool, attribute="string", delete=bool, childAnchor=bool, force=bool, updateBindingSet="string", allKeyable=bool, fromSelection=bool, addView="string", rootTransform=bool, publishedNodeList="string", save=bool, useHierarchy=bool):
    """
    containerTemplate is NOT undoable, queryable, and editable.
    

    
A container template is a description of a container's published interface. This command provides the ability to create and save a template file for a container or load an existing template file. Once a template exists, the user can query the template information.

    """
    pass
    


def containerView(itemList=bool, itemInfo="string", viewDescription=bool, viewList=bool, viewLabel=bool, viewName="string"):
    """
    containerView is NOT undoable, queryable, and editable.
    

    
A container view defines the layout information for the published attributes of a particular container. Container views can be selected from a set of built-in views or may be defined on an associated container template. This command queries the view-related information for a container node. The information returned from this command will be based on the view-related settings in force on the container node at the time of the query (i.e. the container's view mode, template name, view name attributes).

    """
    pass
    


def contentBrowser( string, docTag="string", addContentPath="string", defineTemplate="string", parent="string", preview=bool, unParent=bool, useTemplate="string", lockMainConnection=bool, saveCurrentContext=bool, panel="string", location="string", thumbnailView=bool, highlightConnection="string", context="string", removeContentPath="string", stateString=bool, exists=bool, updateMainConnection=bool, control=bool, unlockMainConnection=bool, selectionConnection="string", forceMainConnection="string", treeView=bool, mainListConnection="string", refreshTreeView=bool, filter="string"):
    """
    contentBrowser is undoable, queryable, and editable.
    

    
This command is used to edit and query a Content Browser. The Content Browser is a unique panel, so only one instance of it can exist at a given time. The optional argument is the name of the control.

    """
    pass
    


def contextInfo(contextname, title=bool, image1=bool, exists=bool, image3=bool, c=bool, image2=bool, escapeContext=bool):
    """
    contextInfo is undoable, queryable, and editable.
    

    
This command allows you to get information on named contexts.

    """
    pass
    


def control(docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    control is undoable, queryable, and editable.
    

    
This command allows you to edit or query the properties of any control.

    """
    pass
    


def controller(pickWalkDown=bool, pickWalkRight=bool, group=bool, pickWalkUp=bool, isController="string", children=bool, allControllers=bool, unparent=bool, pickWalkLeft=bool, parent=bool, index=int):
    """
    controller is undoable, queryable, and editable.
    

    
Commands for managing animation sources

    """
    pass
    


def convertIffToPsd(yResolution=int, iffFileName="string", xResolution=int, psdFileName="string"):
    """
    convertIffToPsd is NOT undoable, queryable, and NOT editable.
    

    
Converts iff file to PSD file of given size

    """
    pass
    


def convertSolidTx(node ,attributeobject, uvSetName="string", fillTextureSeams=bool, uvRange=float, antiAlias=bool, samplePlaneRange=float, camera="string", shadows=bool, alpha=bool, name="string", resolutionY=int, samplePlane=bool, fullUvRange=bool, reuseDepthMap=bool, fileFormat="string", backgroundMode="string", resolutionX=int, componentRange=bool, force=bool, backgroundColor=int, doubleSided=bool, fileImageName="string", uvBBoxIntersect=bool, pixelFormat="string"):
    """
    convertSolidTx is undoable, queryable, and editable.
    

    
Command to convert a texture on a surface to a file texture. The first argument is a rendering node or attribute. If only the node is specified, the outColor attribute will be sampled. If the node does not have an outColor attribute, the first attribute on the node which is: readable, not writable, not hidden, connectable, and not a multi is used. If lighting is to be baked, a shading group must be specified as the texture.
The current selection will be used if a texture and surface are not specified.
An image file will be generated for each object and stored in your image segment of your project. The filename will be formatted using the texture and surface names as follows:
{texture}-{surface}.{fileExtension}
However, if force is off and there is a name collision a version number will be determined and the filename will be formatted as follows:
{texture}-{surface}.{version}.{fileExtension}
If uv/uvsetName option is specified the filename will include {surface}-{uvname} instead of {surface}.

    """
    pass
    


def convertTessellation(camera="string", allCameras=bool):
    """
    convertTessellation is undoable, NOT queryable, and NOT editable.
    

    
Command to translate the basic tessellation attributes to advanced. If a camera flag is specified the translation will be based on the distance the surface is from the camera. The closer the surface is to the camera the more triangles there will be in the tessellation. If the "-allCameras" flags is specified, the renderable camera closest to the surface will be used to set the tessellation. The camera tessellation estimate is also dependent on the current render resolution; a higher resolution the result in a more finely tessellated surface. Multiple NURB surfaces may be specified on the command line, or if no command arguments are specified the surfaces on the active list will be used. This command operates by calculating the chord height such that smooth tessellation is achieved when the surface is rendered. The advanced tessellation setting will be enabled on each surface specified, the primary tessellation parameters will be set, and chord height will be used as the secondary criteria.

    """
    pass
    


def convertUnit(toUnit="string", fromUnit="string"):
    """
    convertUnit is undoable, NOT queryable, and NOT editable.
    

    
This command converts values between different units of measure. The command takes a string, because a string can incorporate unit names as well as values (see examples).

    """
    pass
    


def copyAttr(renameTargetContainer=bool, containerParentChild=bool, values=bool, attribute="string", outConnections=bool, keepSourceConnections=bool, inConnections=bool):
    """
    copyAttr is undoable, queryable, and editable.
    

    
Given two nodes, transfer the connections and/or the values from the first node to the second for all attributes whose names and data types match. When values are transferred, they are transferred directly. They are not mapped or modified in any way. The transferAttributes command can be used to transfer and remap some mesh attributes. The attributes flag can be used to specify a list of attributes to be processed. If the attributes flag is unused, all attributes will be processed. For dynamic attributes, the values and/or connections will only be transferred if the attributes names on both nodes match. This command does not support geometry shape nodes such as meshes, subds and nurbs. This command does not support transfer of multi-attribute values such as weight arrays.

    """
    pass
    


def copyDeformerWeights(noMirror=bool, sourceShape="string", surfaceAssociation="string", uvSpace="string", smooth=bool, mirrorInverse=bool, destinationDeformer="string", destinationShape="string", mirrorMode="string", sourceDeformer="string"):
    """
    copyDeformerWeights is undoable, queryable, and editable.
    

    
Command to copy or mirror the deformer weights accross one of the three major axes. The command can be used to mirror weights either from one surface to another or within the same surface.

    """
    pass
    


def copyFlexor(objects):
    """
    copyFlexor is undoable, NOT queryable, and NOT editable.
    

    
This command copies an existing bone or joint flexor from one bone (joint) to another. The attributes of the flexor and their connections as well as any tweaks in on the latticeFfd are copied from the original to the new flexor. If the selected bone (joint) appears to be a mirror reflection of the bone (joint) of the existing flexor then the transform of the ffd lattice group gets reflected to the new bone (joint). The arguments for the command are the name of the ffd Lattice and the name of the destination joint. If they are not specified at the command line, they will be picked up from the current selection list.

    """
    pass
    


def copyKey(objects, time=(), hierarchy="string", animLayer="string", float=(), includeUpperBound=bool, clipboard="string", shape=bool, controlPoints=bool, forceIndependentEulerAngles=bool, attribute="string", animation="string", index=int, option="string"):
    """
    copyKey is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command copies curve segments's hierarchies from specified targets and puts them in the clipboard. Source curves are unchanged. The pasteKey command applies these curves to other objects.
The shape of the copied curve placed in the clipboard depends on the copyKey "-option" specified. Each of these options below will be explained using an example. For all the explanations, let us assume that the source animation curve (from which keys will be copied) has 5 keyframes at times 10, 15, 20, 25, and 30.
copyKey -t "12:22" -option keys
A 5-frame animation curve with one key at 15 and another key at 20 is placed into the keyset clipboard.
copyKey -t "12:22" -option curve
A 10-frame animation is placed into the clipboard. The curve contains the original source-curve keys at times 15 and 20, as well as new keys inserted at times 12 and 22 to preserve the shape of the curve at the given time segment.
TbaseKeySetCmd.h

    """
    pass
    


def copySkinWeights(noMirror=bool, noBlendWeight=bool, surfaceAssociation="string", influenceAssociation="string", smooth=bool, mirrorInverse=bool, sampleSpace=int, uvSpace="string", sourceSkin="string", normalize=bool, mirrorMode="string", destinationSkin="string"):
    """
    copySkinWeights is undoable, queryable, and editable.
    

    
Command to copy or mirror the skinCluster weights accross one of the three major axes. The command can be used to mirror weights either from one surface to another or within the same surface.

    """
    pass
    


def createAttrPatterns(patternFile="string", patternDefinition="string", patternType="string"):
    """
    createAttrPatterns is undoable, NOT queryable, and NOT editable.
    

    
Create a new instance of an attribute pattern given a pattern type (e.g. XML) and a string or data file containing the description of the attribute tree in the pattern's format.

    """
    pass
    


def createDisplayLayer(makeCurrent=bool, number=int, name="string", empty=bool, noRecurse=bool):
    """
    createDisplayLayer is undoable, NOT queryable, and NOT editable.
    

    
Create a new display layer. The display layer number will be assigned based on the first unassigned number not less than the base index number found in the display layer global parameters. Normally all objects and their descendants will be added to the new display layer but if the '-nr' flag is specified then only the objects themselves will be added.

    """
    pass
    


def createEditor(queueForDelete=bool):
    """
    createEditor is undoable, NOT queryable, and NOT editable.
    

    
This command creates a property sheet for any dependency node. The second argument is the name of the node, and the first is the name of a layout into which the property sheet controls should be placed.
The property sheets created by this command can by user-customized using the editorTemplate command.

    """
    pass
    


def createLayeredPsdFile(yResolution=int, psdFileName="string", imageFileName="string", xResolution=int):
    """
    createLayeredPsdFile is undoable, NOT queryable, and NOT editable.
    

    
Creates a layered PSD file with image names as input to individual layers

    """
    pass
    


def createNode(skipSelect=bool, shared=bool, name="string", parent="string"):
    """
    createNode is undoable, NOT queryable, and NOT editable.
    

    
This command creates a new node in the dependency graph of the specified type.

    """
    pass
    


def createRenderLayer(empty=bool, g=bool, number=int, makeCurrent=bool, name="string", noRecurse=bool):
    """
    createRenderLayer is undoable, NOT queryable, and NOT editable.
    

    
Create a new render layer. The render layer number will be assigned based on the first unassigned number not less than the base index number found in the render layer global parameters. Normally all objects and their descendants will be added to the new render layer but if '-noRecurse' is specified then only the objects themselves will be added. Only transforms and geometry will be added to the new render layer.

    """
    pass
    


def createSubdivRegion():
    """
    createSubdivRegion is undoable, NOT queryable, and NOT editable.
    

    
Creates a subdivision surface region based on the selection list. Once a selection region is created, only the components in the selection list or converted from the selection list will be displayed and selectible through the UI.

    """
    pass
    


def ctxAbort():
    """
    ctxAbort is undoable, NOT queryable, and NOT editable.
    

    
This command tells the current context to reset itself, losing what has been done so far. If a escape context has been set it then makes that context current.

    """
    pass
    


def ctxCompletion():
    """
    ctxCompletion is undoable, NOT queryable, and NOT editable.
    

    
This command tells the current context to finish what it is doing and create any objects that is is working on.

    """
    pass
    


def ctxEditMode(buttonUp=bool, buttonDown=bool):
    """
    ctxEditMode is undoable, NOT queryable, and NOT editable.
    

    
This command tells the current context to switch edit modes.
It acts as a toggle.

    """
    pass
    


def ctxTraverse(up=bool, down=bool, left=bool, right=bool):
    """
    ctxTraverse is undoable, NOT queryable, and NOT editable.
    

    
This command tells the current context to do a traversal.

Some contexts will ignore this command. Individual contexts determine what up/down left/right mean.

    """
    pass
    


def currentCtx():
    """
    currentCtx is undoable, NOT queryable, and NOT editable.
    

    
This command returns the currently selected tool context.

    """
    pass
    


def currentTime(time, update=bool):
    """
    currentTime is NOT undoable, queryable, and editable.
    

    
When given a time argument (with or without the -edit flag) this command sets the current global time. The model updates and displays at the new time, unless "-update off" is present on the command line.

    """
    pass
    


def currentTimeCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    currentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the graph editor

    """
    pass
    


def currentUnit(updateAnimation=bool, time="string", angle="string", fullName=bool, linear="string"):
    """
    currentUnit is undoable, queryable, and NOT editable.
    

    
This command allows you to change the units in which you will work in Maya. There are three types of units: linear, angular and time.
The current unit affects how all commands in Maya interpret their numeric values. For example, if the current linear unit is cm, then the command:
move 5 -2 3;
sphere -radius 4;
will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as creating a sphere with radius 4cm. Similarly, if the current time unit is Film (24 frames per second), then the command:
currentTime 6;
will be interpreted as setting the current time to frame 6 in the Film unit, which is 6/24 or 0.25 seconds.
You can always override the unit of a particular numeric value to a command be specifying it one the command. For example, using the above examples:
move 5m -2mm 3cm;
sphere -radius 4inch;
currentTime 6ntsc;
would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters in Z, create a sphere of radius 4 inches, and change the current time to 6 frames in the NTSC unit, which would be 0.2 seconds, or 4.8 frames in the current (Film) unit.

    """
    pass
    


def curve(replace=bool, periodic=bool, objectSpace=bool, bezier=bool, worldSpace=bool, point="string", append=bool, editPoint="string", knot=float, pointWeight="string", degree=float):
    """
    curve is undoable, NOT queryable, and NOT editable.
    

    
The curve command creates a new curve from a list of control vertices (CVs). A string is returned containing the pathname to the newly created curve. You can create a curve from points either in world space or object (local) space, either with weights or without. You can replace an existing curve by using the "-r/replace" flag. You can append a point to an existing curve by using the "-a/append" flag.
To create a curve-on-surface, use the curveOnSurface command.
To change the degree of a curve, use the rebuildCurve command.
To change the of parameter range curve, use the rebuildCurve command.

    """
    pass
    


def curveAddPtCtx(exists=bool, image1="string", image2="string", image3="string"):
    """
    curveAddPtCtx is undoable, queryable, and editable.
    

    
The curveAddPtCtx command creates a new curve add points context, which adds either control vertices (CVs) or edit points to an existing curve.

    """
    pass
    


def curveCVCtx(degree=int, image1="string", uniform=bool, multEndKnots=bool, image3="string", exists=bool, image2="string", name="string", history=bool):
    """
    curveCVCtx is undoable, queryable, and editable.
    

    
The curveCVCtx command creates a new context for creating curves by placing control vertices (CVs).

    """
    pass
    


def curveEditorCtx(image1="string", relativeTangentSize=float, direction=int, image3="string", title="string", exists=bool, image2="string", name="string", history=bool):
    """
    curveEditorCtx is undoable, queryable, and editable.
    

    
The curveEditorCtx command creates a new NURBS editor context, which is used to edit a NURBS curve or surface.

    """
    pass
    


def curveEPCtx(degree=int, image1="string", uniform=bool, image3="string", exists=bool, image2="string", name="string", history=bool):
    """
    curveEPCtx is undoable, queryable, and editable.
    

    
The curveEPCtx command creates a new context for creating curves by placing edit points.

    """
    pass
    


def curveIntersect(direction="string", useDirection=bool, tolerance="string", constructionHistory=bool):
    """
    curveIntersect is undoable, queryable, and editable.
    

    
You must specify two curves to intersect.
This command either returns the parameter values at which the given pair of curves intersect, or returns a dependency node that provides the intersection information. If you want to find the intersection of the curves in a specific direction you must use BOTH the "-useDirection" flag and the "direction" flag.

    """
    pass
    


def curveMoveEPCtx(exists=bool, image1="string", image2="string", image3="string"):
    """
    curveMoveEPCtx is undoable, queryable, and editable.
    

    
The curveMoveEPCtx command creates a new context for moving curve edit points using a manipulator. Edit points can only be moved one at a time.

    """
    pass
    


def curveOnSurface(replace=bool, periodic=bool, positionUV=float, append=bool, knot=float, degree=float):
    """
    curveOnSurface is undoable, NOT queryable, and NOT editable.
    

    
The curve-on-surface command creates a new curve-on-surface from a list of control vertices (CVs). A string is returned containing the pathname to the newly created curve-on-surface. You can replace an existing curve by using the "-r/replace" flag. You can append points to an existing curve-on-surface by using the "-a/append" flag. See also the curve command, which describes how to query curve attributes.

    """
    pass
    


def curveRGBColor(list=bool, hueSaturationValue=bool, remove=bool, listNames=bool, resetToSaved=bool, resetToFactory=bool):
    """
    curveRGBColor is undoable, queryable, and NOT editable.
    

    
This command creates, changes or removes custom curve colors, which are used to draw the curves in the Graph Editor. The custom curve names may contain the wildcards "?", which marches a single character, and "*", which matches any number of characters. These colors are part of the UI and not part of the saved data for a model. This command is not undoable.

    """
    pass
    


def curveSketchCtx(object, degree=int, image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    curveSketchCtx is undoable, queryable, and editable.
    

    
The curveSketchCtx command creates a new curve sketch context, also known as the "pencil context".

    """
    pass
    


def cutKey(targetList, time=(), hierarchy="string", float=(), includeUpperBound=bool, controlPoints=bool, clear=bool, index=int, shape=bool, selectKey=bool, attribute="string", animation="string", option="string"):
    """
    cutKey is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
The cutKey command cuts curve segment hierarchies from specified targets and puts them in the clipboard. The pasteKey command applies these curves to other objects.
The shape of the cut curve placed in the clipboard, and the effect of the cutKey command on the source animation curve depends on the cutKey "-option" specified. Each of these options below will be explained using an example. For all the explanations, let us assume that the source animation curve (from which keys will be cut) has 5 keyframes at times 10, 15, 20, 25, and 30.
TbaseKeySetCmd.h
cutKey -t "12:22" -option keys
Keyframes at times 15 and 20 are removed. All other keys are unchanged.
A 5-frame animation curve is placed into the keyset clipboard.
cutKey -t "12:22" -option keysCollapse
Keyframes at times 15 and 20 are removed. Shift all keys after time 20 to the left by 5 frames, preserving all their values.
A 5-frame animation curve is placed into the keyset clipboard.
cutKey -t "12:22" -option keysConnect
Keyframes at times 15 and 20 are removed. Shift all keys after time 20 to the left by 5 frames, and place the key that used to be at time 25 at the value of the key that used to be at time 15.
A 5-frame animation curve is placed into the keyset clipboard.
cutKey -t "12:22" -option curve
Keyframes at times 15 and 20 are removed. Keys are inserted at times 12 and 22.
A 10-frame animation curve is placed into the keyset clipboard.
cutKey -t "12:22" -option curveCollapse
Keyframes at times 15 and 20 are removed. Keys are inserted at times 12 and 22. Shift all keys from time 22 to the left by 10 frames, preserving their values.
A 10-frame animation curve is placed into the keyset clipboard.
cutKey -t "12:22" -option curveConnect
Keyframes at times 15 and 20 are removed. Keys are inserted at times 12 and 22. Shift all keys from time 22 to the left by 10 frames, and replace the key inserted at time 12 with the newly inserted key at time 22.
A 10-frame animation curve is placed into the keyset clipboard.
cutKey -t "12:22" -option areaCollapse
Keyframes at times 15 and 20 are removed. Shift all keys from time 22 to the left by 10 frames, preserving their values.
A 10-frame animation curve is placed into the keyset clipboard.

    """
    pass
    


def cycleCheck(string, list=bool, parents=bool, firstCycleOnly=bool, lastPlugPerNode=bool, evaluation=bool, listSeparator="string", all=bool, children=bool, secondary=bool, dag=bool, timeLimit=(), firstPlugPerNode=bool):
    """
    cycleCheck is undoable, queryable, and NOT editable.
    

    
This command searches for plug cycles in the dependency graph. If a plug or node is selected then it searches for cycles that that plug or node is involved with. Plugs or nodes can also be passed as arguments. If the -all flag is used then the entire graph is searched.
Normally the return value is a boolean indicating whether or not the given items were involved in a cycle. If the -list flag is used then the return value is the list of all plugs in cycles (involving the selected plug or node if any).
Note that it is possible for evaluation cycles to occur even where no DG connections exist. Here are some examples:
1) Nodes with evaluation-time dependent connections: An example is expression nodes, because we cannot tell what an expression node is actually referring to until it is evaluated, and such evaluation-time dependent nodes may behave differently based on the context (e.g. time) they are evaluated at. If you suspect a cycle due to such a connection, the best way to detect the cycle is through manual inspection.
2) Cycles due to DAG hierarchy: noting that DAG nodes are implicitely connected through parenting, if a child DAG node connects an output into the input of a parent node, a cycle will exist if the plugs involved also affect each other. In order to enable detection of cycles involving the DAG, add the -dag flag to the command line.
Note also that this command may incorrectly report a cycle on an instanced skeleton where some of the instances use IK. You will have to examine the reported cycle yourself to determine if it is truly a cycle or not. The evaluation time cycle checking will not report false cycles.

    """
    pass
    


def cylinder(degree=int, axis="string", pivot="string", sections=int, radius="string", tolerance="string", object=bool, useTolerance=bool, polygon=int, spans=int, nodeState=int, name="string", heightRatio=float, startSweep=int, caching=bool, endSweep=int, constructionHistory=bool):
    """
    cylinder is undoable, queryable, and editable.
    

    
The cylinder command creates a new cylinder and/or a dependency node that creates one, and returns their names.

    """
    pass
    


def dagObjectCompare(namespace="string", bail="string", type=bool, relative=bool, connection=bool, short=bool, attribute=bool):
    """
    dagObjectCompare is NOT undoable, NOT queryable, and NOT editable.
    

    
dagObjectCompare can be used to compare to compare objects based on:
type - Currently supports transform nodes and shape nodes
relatives - Compares DAG objects' children and parents
connections - Checks to make sure the two dags are connected to the same sources and destinations
attributes - Checks to make sure that the properties of active attributes are the same

    """
    pass
    


def dagPose(objects, remove=bool, reset=bool, bindPose=bool, addToPose=bool, selection=bool, g=bool, name="string", atPose=bool, save=bool, restore=bool, worldParent=bool, members=bool):
    """
    dagPose is undoable, queryable, and editable.
    

    
This command is used to save and restore the matrix information for a dag hierarchy. Specifically, the data stored will restore the translate, rotate, scale, scale pivot, rotate pivot, rotation order, and (for joints) joint order for all the objects on the hierarchy. Data for other attributes is not stored by this command.
This command can also be used to store a bindPose for an object. When you skin an object, a dagPose is automatically created for the skin.

    """
    pass
    


def dataStructure(remove=bool, removeAll=bool, dataType=bool, asString="string", listMemberNames="string", asFile="string", format="string", name="string"):
    """
    dataStructure is undoable, queryable, and NOT editable.
    

    
Takes in a description of the structure and creates it, adding it to the list of available data structures. The structure definition can either be supplied in the asString flag or exist in a file that is referenced by the asFile flag.
If the remove flag is specified with a name flag then the data structure will be removed. This is to keep all structure operations in a single command rather than create separate commands to create, remove, and query the data structures. When you use the removeAll flag then every existing metadata structure is removed. Use with care! Note that removed structures may still be in use in metadata Streams after removal, they are just no longer available for the creation of new Streams.
Both the creation modes and the remove mode are undoable.
Creation of an exact duplicate of an existing structure (including name) will succeed silently without actually creating a new structure. Attempting to create a new non-duplicate structure with the same name as an existing structure will fail as there is no way to disambiguate two structures with the same name.
Querying modes are defined to show information both on the created structures and the structure serialization formats that have been registered. The serialization formats preserve the structure information as text (e.g. raw, XML, JSON). Since the raw structure type is built in it will be assumed when none are specified.
General query with no flags will return the list of names of all currently existing structures.
Querying the format flag will return the list of all registered structure serialization formats.
Querying with the format supplied before the query flag will show the detailed description of that particular structure serialization format.
Querying the asString flag with a structure name and serialization format supplied before the query flag will return a string representing the named data structure in the serialization format specified by the format flag. Even if the format is the same as the one that created the structure the query return string may not be identical since the queried value is formatted in a standard way - original formatting is not preserved.
Querying the asFile flag with a structure name supplied before the query flag will return the original file from which the structure was generated. If the structure was created using the asString flag or through the API then an empty string will be returned.
Querying the name flag returns the list of all structures created so far.

    """
    pass
    


def date(format="string", date=bool, shortDate=bool, shortTime=bool, time=bool):
    """
    date is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns information about current time and date. Use the predefined formats, or the -format flag to specify the output format.

    """
    pass
    


def dbcount(list=bool, keyword="string", reset=bool, spreadsheet=bool, file="string", enabled=bool, maxdepth=int, quick=bool):
    """
    dbcount is NOT undoable, NOT queryable, and NOT editable.
    

    
The dbcount command is used to print and manage a list of statistics collected for counting operations. These statistics are displayed as a list of hits on a particular location in code, with added reference information for pointers/strings/whatever. If -reset is not specified then statistics are printed.

    """
    pass
    


def dbmessage(list=bool, file="string", type="string", monitor=bool):
    """
    dbmessage is NOT undoable, NOT queryable, and NOT editable.
    

    
The dbmessage command is used to install monitors for certain message types, dumping debug information as they are sent so that the flow of messages can be examined.

    """
    pass
    


def dbpeek(allObjects=bool, count=int, outputFile="string", evaluationGraph=bool, argument="string", operation="string"):
    """
    dbpeek is NOT undoable, queryable, and NOT editable.
    

    
The dbpeek command is used to analyze the Maya data for information of interest. See a description of the flags for details on what types of things can be analyzed.

    """
    pass
    


def dbtrace(off=bool, keyword="string", verbose=bool, mark=bool, info=bool, title="string", output="string", timed=bool, filter="string"):
    """
    dbtrace is NOT undoable, queryable, and NOT editable.
    

    
The dbtrace command is used to manipulate trace objects. The keyword is the only mandatory argument, indicating which trace object is to be altered.
Trace Objects to affect (keyword KEY)
Optional filtering criteria (filter FILTER)
Function (off, output FILE, mark, title TITLE, timed : default operation is to enable traces)
You can use the query mode to find out which keywords are currently active (query with no arguments) or inactive (query with the off argument). You can enhance that query with or without a keyword argument to find out where their output is going (query with the output argument), out what filters are currently applied (query with the filter argument), or if their output will be timestamped (query with the timed argument).

    """
    pass
    


def defaultLightListCheckBox(docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", shadingGroup="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    defaultLightListCheckBox is undoable, queryable, and editable.
    

    
This command creates a checkBox that controls whether a shadingGroup is connected/disconnected from the defaultLightList.

    """
    pass
    


def defaultNavigation(delete=bool, navigatorDecisionString="string", quiet=bool, unignore=bool, force=bool, defaultWorkingNode=bool, ignore=bool, connectToExisting=bool, relatedNodes=bool, source="string", defaultAttribute=bool, defaultTraversal=bool, createNew=bool, destination="string"):
    """
    defaultNavigation is undoable, NOT queryable, and NOT editable.
    

    
The defaultNavigation command defines default behaviours when creating or manipulating connections between nodes and when navigating between nodes via those connections. This command is primarily used by attribute editors.

    """
    pass
    


def defineDataServer(undefine=bool, server="string", device="string"):
    """
    defineDataServer is undoable, NOT queryable, and NOT editable.
    

    
Connects to the specified data servername, creating a named device which then can be attached to device handlers.
When the device is defined, it queries queries the server for data axis information. The "CapChannels" present are represented as axis in form "channelName"."usage" for scalar channels and "channelName"."component" for compound channels. See listInputDeviceAxes to list axis names.
Note that undoing
defineDataServer -d "myDevice" -s "myServer"
does not break the connection with the data server until it cannot be redone. Executing any other command (sphere for example) will cause this to occur. Similarly, the command
defineDataServer -d "myDevice" -u
does not break the connection with the data server until it cannot be undone. Either flushUndo, or the 'defineDataServer' command falling" off the end of the undo queue causes this to occur, and the connection. to be broken.
No return value.

    """
    pass
    


def defineVirtualDevice(parent="string", clear=bool, axis=int, undefine=bool, device="string", usage="string", channel="string", create=bool):
    """
    defineVirtualDevice is undoable, queryable, and NOT editable.
    

    
This command defines a virtual device. Virtual devices act like real devices and are useful to manipulate/playback data when an command device is not connected to the computer.

    """
    pass
    


def deformer(before=bool, exclusive="string", geometryIndices=bool, after=bool, ignoreSelected=bool, split=bool, includeHiddenSelections=bool, type="string", deformerTools=bool, parallel=bool, frontOfChain=bool, geometry="string", remove=bool, prune=bool, afterReference=bool, name="string"):
    """
    deformer is undoable, queryable, and editable.
    

    
This command creates a deformer of the specified type. The deformer will deform the selected objects.

    """
    pass
    


def deformerEvaluator(chains=bool, meshes=bool):
    """
    deformerEvaluator is NOT undoable, queryable, and NOT editable.
    

    
Print debug information about deformer evaluator status. In query mode the debug information is returned as a string[], otherwise the information is displayed in the script editor.

    """
    pass
    


def deformerWeights(im=bool, positionTolerance=float, shape="string", deformer="string", weightTolerance=float, method="string", weightPrecision=int, skip="string", defaultValue=float, export=bool, ignoreName=bool, worldSpace=bool, attribute="string", vertexConnections=bool, path="string", remap="string"):
    """
    deformerWeights is undoable, queryable, and editable.
    

    
Command to import and export deformer weights to and from a simple XML file. The weight data is stored in a per-vertex fashion along with a "point cloud" corresponding to the vertices from the geometry input to the deformer. For example a cluster deformer would have the following information: On import the weights are then mapped back to a specified deformer based on the specified mapping method. Note that the geometry used to perform the mapping association is not the visible shape but rather the incoming geometry to the deformer. For example, in the case of a skin cluster this would be the bind pose geometry.

    """
    pass
    


def delete(hierarchy="string", expressions=bool, controlPoints=bool, all=bool, inputConnectionsAndNodes=bool, shape=bool, channels=bool, staticChannels=bool, timeAnimationCurves=bool, attribute="string", unitlessAnimationCurves=bool, constraints=bool, constructionHistory=bool):
    """
    delete is undoable, NOT queryable, and NOT editable.
    

    
This command is used to delete selected objects, or all objects, or objects specified along with the command. Flags are available to filter the type of objects that the command acts on.
At times, more than just specified items will be deleted. For example, deleting two CVs in the same "row" on a NURBS surface will delete the whole row.

    """
    pass
    


def deleteAttr(attribute="string", name="string"):
    """
    deleteAttr is undoable, queryable, and editable.
    

    
This command is used to delete a dynamic attribute from a node or nodes. The attribute can be specified by using either the long or short name. Only one dynamic attribute can be deleted at a time. Static attributes cannot be deleted. Children of a compound attribute cannot be deleted. You must delete the complete compound attribute. This command has no edit capabilities. The only query ability is to list all the dynamic attributes of a node.

    """
    pass
    


def deleteAttrPattern(allPatterns=bool, patternName="string", patternType="string"):
    """
    deleteAttrPattern is undoable, NOT queryable, and NOT editable.
    

    
After a while the list of attribute patterns could become cluttered. This command provides a way to remove patterns from memory so that only the ones of interest will show.

    """
    pass
    


def deleteExtension(forceDelete=bool, attribute="string", nodeType="string"):
    """
    deleteExtension is NOT undoable, NOT queryable, and NOT editable.
    

    
This command is used to delete an extension attribute from a node type. The attribute can be specified by using either the long or short name. Only one extension attribute can be deleted at a time. Children of a compound attribute cannot be deleted, you must delete the complete compound attribute. This command has no undo, edit, or query capabilities.

    """
    pass
    


def deleteUI(stringstring, layout=bool, control=bool, window=bool, editor=bool, uiTemplate=bool, menuItem=bool, radioMenuItemCollection=bool, menu=bool, collection=bool, panelConfig=bool, toolContext=bool, panel=bool):
    """
    deleteUI is undoable, NOT queryable, and NOT editable.
    

    
This command deletes UI objects such as windows and controls. Deleting a layout or window will also delete all of its children. If a flag is used then all objects being deleted must be of the specified type. This command may not be edited or queried.
NOTE: it is recommended that the type flags be used to disambiguate different kinds of objects with the same name.

    """
    pass
    


def deltaMush(before=bool, exclusive="string", geometryIndices=bool, after=bool, smoothingIterations=int, ignoreSelected=bool, split=bool, includeHiddenSelections=bool, smoothingStep=float, pinBorderVertices=bool, deformerTools=bool, envelope=float, parallel=bool, frontOfChain=bool, geometry="string", remove=bool, prune=bool, afterReference=bool, name="string"):
    """
    deltaMush is undoable, queryable, and editable.
    

    
This command is used to create, edit and query deltaMush nodes.

    """
    pass
    


def detachCurve(curveOnSurface=bool, object=bool, nodeState=int, replaceOriginal=bool, name="string", parameter=float, caching=bool, keep=bool, constructionHistory=bool):
    """
    detachCurve is undoable, queryable, and editable.
    

    
The detachCurve command detaches a curve into pieces, given a list of parameter values. You can also specify which pieces to keep and which to discard using the "-k" flag. The names of the newly detached curve(s) is returned. If history is on, then the name of the resulting dependency node is also returned.
You can use this command to open a periodic curve at a particular parameter value. You would use this command with only one "-p" flag.
If you are specifying "-k" flags, then you must specify one, none or all "-k" flags. If you are specifying all "-k" flags, there must be one more "-k" flag than "-p" flags.

    """
    pass
    


def detachDeviceAttr(selection=bool, all=bool, axis="string", attribute="string", device="string"):
    """
    detachDeviceAttr is undoable, queryable, and NOT editable.
    

    
This command detaches connections between device axes and node attributes. The command line arguments are the same as for the corresponding attachDeviceAttr except for the clutch argument which can not be used in this command.

    """
    pass
    


def detachSurface(direction=int, object=bool, nodeState=int, replaceOriginal=bool, name="string", parameter=float, caching=bool, keep=bool, constructionHistory=bool):
    """
    detachSurface is undoable, queryable, and editable.
    

    
The detachSurface command detaches a surface into pieces, given a list of parameter values and a direction. You can also specify which pieces to keep and which to discard using the "-k" flag. The names of the newly detached surface(s) are returned. If history is on, the name of the resulting dependency node is also returned.
You can only detach in either U or V (not both) with a single detachSurface operation.
You can use this command to open a closed surface at a particular parameter value. You would use this command with only one "-p" flag.
If you are specifying "-k" flags, then you must specify one, none or all "-k" flags. If you are specifying all "-k" flags, there must be one more "-k" flag than "-p" flags.

    """
    pass
    


def deviceEditor(panel="string", docTag="string", control=bool, mainListConnection="string", defineTemplate="string", parent="string", highlightConnection="string", takePath="string", useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", unParent=bool, stateString=bool, exists=bool, updateMainConnection=bool, forceMainConnection="string", unlockMainConnection=bool):
    """
    deviceEditor is undoable, queryable, and editable.
    

    
This creates an editor for creating/modifying attachments to input devices.

    """
    pass
    


def deviceManager(axisName=bool, numDevices=bool, axisIndex=int, deviceNameFromIndex=int, axisOffset=bool, deviceIndex=int, axisCoordChanges=bool, axisScale=bool, numAxis=bool, attachment=bool):
    """
    deviceManager is undoable, queryable, and editable.
    

    
This command queriers the internal device manager for information on attached devices.

    """
    pass
    


def devicePanel():
    """
    devicePanel is undoable, queryable, and editable.
    

    
This command is now obsolete. It is included only for the purpose of file compatibility. It creates a blank panel.

    """
    pass
    


def dgdirty(propagation=bool, showTiming=bool, clean=bool, verbose=bool, implicit=bool, allPlugs=bool, list="string"):
    """
    dgdirty is NOT undoable, queryable, and NOT editable.
    

    
The dgdirty command is used to force a dependency graph dirty message on a node or plug. Used for debugging to find evaluation problems. If no nodes are specified then the current selection list is used. If the list flag is used it will return the list of things currently marked as dirty (or clean if the clean flag was also used). The returned values will be the names of plugs either clean/dirty themselves, at both ends of a clean/dirty connection, or representing the location of clean/dirty data on the node. Be careful using this option in conjunction with the all flag, the list could be huge.

    """
    pass
    


def dgeval(objects, src=bool, verbose=bool):
    """
    dgeval is undoable, NOT queryable, and NOT editable.
    

    
The dgeval command is used to force a dependency graph evaluate of a node or plug. Used for debugging to find propagation problems.
Normally the selection list is used to determine which objects to evaluate, but you can add to the selection list by specifying which objects you want on the command line.

    """
    pass
    


def dgfilter(list=bool, logicalNot="string", logicalAnd="string", nodeType="string", plug="string", logicalOr="string", node="string", attribute="string", name="string"):
    """
    dgfilter is NOT undoable, NOT queryable, and NOT editable.
    

    
The dgfilter command is used to define Dependency Graph filters that select DG objects based on certain criteria. The command itself can be used to filter objects or it can be attached to a dbtrace object to selectively filter what output is traced. If objects are specified then apply the filter to those objects and return a boolean indicating whether they passed or not, otherwise return then name of the filter. An invalid filter will pass all objects. For multiple objects the return value is the logical "AND" of all object's return values.

    """
    pass
    


def dgInfo(subgraph=bool, propagation=bool, outputFile="string", dirty=bool, size=bool, type="string", connections=bool, nonDeletable=bool, nodes=bool, allNodes=bool, short=bool):
    """
    dgInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
This command prints information about the DG in plain text. The scope of the information printed is the entire graph if the all flag is used, the nodes/plugs on the command line if they were specified, and the selection list, in that order. Each plug on a connection will have two pieces of state information displayed together at the end of the line on which they are printed. There are two possible values for each of the two states displayed. The values are updated when the DG pulls data across them, usually through evaluation, or pushes a dirty message through them. There are some subtleties in how the data is pulled through the connection but for simplicity it will be referred to as "evaluation". The values displayed will be CLEAN or DIRTY followed by PROP or BLOCK. The first keyword has these meanings:
CLEAN means that evaluation of the plug's connection succeeded and no dirty messages have come through it since then. It also implies that the destination end of the connection has received the value from the source end.
DIRTY means that a dirty message has passed through the plug's connection since the last time an evaluation was made on the destination side of that connection.
Note: the data on the node has its own dirty state that depends on other factors so having a clean connection doesn't necessarily mean the plug's data is clean, and vice versa. The second keyword has these meanings:
PROP means that the connection will allow dirty messages to pass through and forwards them to all destinations.
BLOCK means that a dirty message will stop at this connection and not continue on to any destinations. This is an optimization that prevents excessive dirty flag propagation when many values are changing, for example, a frame change in an animated sequece.
The combination CLEAN BLOCK should never be seen in a valid DG. This indicates that while the plug connection has been evaluated since the last dirty message it will not propagate any new dirty messages coming in to it. That in turn means downstream nodes will not be notified that the graph is changing and they will not evaluate properly. Recovering from this invalid state requires entering the command dgdirty -a to mark everything dirty and restart proper evaluation. Think of this command as the reset/reboot of the DG world. Both state types behave differently depending on your connection type.
Simple A -> B : Plugs at both ends of the connection share the same state information. The state information updates when an evaluation request comes to A from B, or a dirty message is sent from A to B.
Fan-Out A -> B, A -> C : Each of A, B, and C have their own unique state information. B and C behave as described above. A has its state information linked to B and C - it will have CLEAN only when both B and C have CLEAN, it will have BLOCK only when both B and C have BLOCK.
In-Out A -> B, C -> A : Each of A, B, and C have their own unique state information. B and C behave as described above. A has its state information linked to B and C. The CLEAN|DIRTY flag looks backwards, then forwards:
if( C == CLEAN ) A = CLEAN
else if( B == CLEAN ) A = CLEAN
The BLOCK state is set when a dirty message passes through A, and the PROP state is set either when A is set clean or an evaluation passes through A.
There are some other exceptions to these rules:
All of this state change information only applies to dirty messages and evaluations that use the normal context. Any changes in other contexts, for example, through the getAttr -t TIME command, does not affect the state in the connections.
Param curves and other passive inputs, for example blend nodes coming from param curves, will not disable propagation. Doing so would make the keyframing workflow impossible.
Certain messages can choose to completely ignore the connection state information. For example when a node's state attribute changes a connection may change to a blocking one so the message has to be propagated at least one step further to all of its destinations. This way they can update their information.
Certain operations can globally disable the use of the propagaton state to reduce message flow. The simplest example is when the evaluation manager is building its graph. It has to visit all nodes so the propagation cannot be blocked.
The messaging system has safeguards against cyclic messages flowing through connections but sometimes a message bypasses the connection completely and goes directly to the node. DAG parents do this to send messages to their children. So despite connections into a node all having the BLOCK state it could still receive dirty messages.

    """
    pass
    


def dgmodified():
    """
    dgmodified is NOT undoable, NOT queryable, and NOT editable.
    

    
The dgmodified command is used to find out which nodes in the dependency graph have been modified. This is mostly useful for fixing instances where file new asks you to save when no changes have been made to the scene.

    """
    pass
    


def dgtimer(returnCode="string", hierarchy=bool, updateHeatMap=int, uniqueName=bool, type="string", timerOn=bool, returnType="string", name="string", rangeLower=float, combineType=bool, trace=bool, show="string", overhead=bool, reset=bool, hide="string", timerOff=bool, outputFile="string", rangeUpper=float, sortType="string", sortMetric="string", noHeader=bool, threshold=float, maxDisplay=int):
    """
    dgtimer is NOT undoable, queryable, and NOT editable.
    

    
This command measures dependency graph node performance by managing timers on a per-node basis. Logically, each DG node has a timer associated with it which records the amount of real time spent in various operations on its plugs. The time measurement includes the cost of copying data to the node on behalf of the operation, MEL commands executed by an expression contained in an expression invoked by the node, and includes any wait time such as when a fileTexture node loads an image file from disk. Most DG operations are reported including compute, draw, and dirty propagation.
The various operations we measure are called "metrics" and the types of timers are called "timer types". The various metrics are always measured when timing is on, but are only queried when specified via the -show and -hide flags. The metrics currently supported are listed in detail under the -show flag below. For each metric we support a standard set of timer types. There are three of these: "self" for self time (the time specific to the node and not its children), "inclusive" (time including children of the node), and "count" (number of operations of the given metric on the node).
The timing mechanism which is used by dgtimer is built into the DG itself, thus ALL depend nodes can be timed and there is no need for programmers writing plug-ins using the OpenMaya API to add any special code in order for their nodes to be timed -- its all handled transparently.
The dgtimer command allows node timers to be turned on, off, reset to zero, and have their current value displayed, and these operations can be performed globally on all nodes or on a specific set of nodes defined by name, type or parentage. Note that all timer measurements are computed in "real time" (the same time measurement you get from a wristwatch) as opposed to "CPU time" (which only measures time when the processor is executing your code). All times are displayed in seconds.
Use the -query flag to display the current timer values on a node,
use -on to turn on timing,
use -off to turn off timing,
and -reset to reset timers to zero.
To display the values measured during timing, there are two approaches. The first method is to use the -query flag can be used to report the information which has been measured. The second method is to use the query methods available on the OpenMaya class MFnDependencyNode (see the OpenMaya documentation for details).
What follows is a description of what is generated via -query. The output is broken out into several sections and these are described as follows:
SECTION 1:
Section 1 of the dgtimer output contains global information. This section can be disabled via the -hoHeader flag. These values are reset whenever a global timer reset occurs (i.e. dgtimer -reset; is specified). The global values which are reported are:
Total real time: the total wall-clock time since the last global timer reset. This is the actual time which has been spent as you might measure it measure it with your watch. On a multi-processing system, this value will always remain true to to real time (unlike user and sys time).
Total user time: the total time the CPU(s) spent processing Maya not including any system time since the last global timer reset.
Total sys time: the total time the CPU(s) spent in operating system calls on behalf of Maya since the last global timer reset.
Summary of each metric for all nodes: a summary of self and count for each metric that we measure:
Real time in callbacks reports the self time and count for the "callback" metric.
Real time in compute reports the self time and count for the "compute" metric.
Real time in dirty propagation reports the self time and count for the "dirty" metric.
Real time in drawing reports the self time and count for the "draw" metric.
Real time fetching data from plugs reports the self time and count for the "fetch" metric.
Breakdown of select metrics in greater detail: a reporting of certain combinations of metrics that we measure:
Real time in compute invoked from callback reports the self time spent in compute when invoked either directly or indirectly by a callback.
Real time in compute not invoked from callback reports the self time spent in compute not invoked either directly or indirectly by a callback.
SECTION 2:
Section 2 of the dgtimer -query output contains per-node information. There is a header which describes the meaning of each column, followed by the actual per-node data, and this is ultimately followed by a footer which summarises the totals per column. Note that the data contained in the footer is the global total for each metric and will include any nodes that have been deleted since the last reset, so the value in the footer MAY exceed what you get when you total the individual values in the column. To prevent the header and footer from appearing, use the -noHeader flag to just display the per-node data.
The columns which are displayed are as follows:
Rank: The order of this node in the sorted list of all nodes, where the list is sorted by -sortMetric and -sortType flag values (if these are omitted the default is to sort by self compute time).
ON: Tells you if the timer for that node is currently on or off. (With dgtimer, you have the ability to turn timing on and off on a per-node basis).
Per-metric information: various columns are reported for each metric. The name of the metric is reported at in the header in capital letters (e.g. "DRAW"). The standard columns for each metric are:
Self: The amount of real time (i.e. elapsed time as you might measure it with a stopwatch) spent performing the operation (thus if the metric is "DRAW", then this will be time spent drawing the node).
Inclusive: The amount of real time (i.e. elapsed time as you might measure it with a stopwatch) spent performing the operation including any child operations that were invoked on behalf of the operation (thus if the metric is "DRAW", then this will be the total time taken to draw the node including any child operations).
Count: The number of operations that occued on this node (thus if the metric is "DRAW", then the number of draw operations on the node will be reported).
Sort information if a column is the one being used to sort all the per-node dgtimer information, then that column is followed by a Percent and Cumulative column which describe a running total through the listing. Note that "-sortType none" prevents these two columns from appearing and implicitely sorts on "self" time.
After the per-metric columns, the node name and type are reported:
Type The node type.
Name The name of the node. If the node is file referenced and you are using namespaces, the namespace will be included. You can also force the dagpath to be displayed by specifying the -uniqueName flag.
Plug-in name If the node was implemented in an OpenMaya plug-in, the name of that plug-in is reported.
SECTION 3:
Section 3 of the dgtimer -query output describes time spent in callbacks. Note that section 3 only appears when the CALLBACK metric is shown (see the -show flag).
The first part is SECTION 3.1 lists the time per callback with each entry comprising:
The name of the callback, such as "attributeChangedMsg". These names are internal Maya names, and in the cases where the callback is available through the OpenMaya API, the API access to the callback is similarly named.
The name is followed by a breakdown per callbackId. The callbackId is an identifying number which is unique to each client that is registered to a callback and can be deduced by the user, such as through the OpenMaya API. You can cross-reference by finding the same callbackId value listed in SECTIONs 3.1 and 3.3.
Self time (i.e. real time spent within that callbackId type not including any child operations which occur while processing the callback).
Percent (see the -sortType flag). Note that the percent values are listed to sum up to 100% for that callback. This is not a global percent.
Cumulative (see the -sortType flag).
Inclusive time (i.e. real time spent within that callbackId including any child operations).
Count (number of times the callbackId was invoked).
API lists "Y" if the callbackId was defined through the OpenMaya API, and "N" if the callbackId was defined internally within Maya.
Node lists the name of the node this callbackId was associated with. If the callbackId was associated with more than one node, the string "*multiple*" is printed. If there was no node associated with the callbackId (or its a callback type in which the node is hard to deduce), the entry is blank.
After the callbackId entries are listed, a dashed line is printed followed by a single line listing the self, inclusive and count values for the callback. Note that the percent is relative to the global callback time.
At the bottom of SECTION 3.1 is the per-column total. The values printed match the summation at the bottom of the listing in section 2. Note that the values from SECTION 3.1 include any nodes that have been deleted since the last reset. The thresholding parameters (-threshold, -rangeLower, -rangeUpper and -maxDisplay) are honoured when generating the listing. The sorting of the rows and display of the Percent and Cumulative columns obeys the -sortType flag. As the listing can be long, zero entries are not displayed.
The second part is SECTION 3.2 which lists the data per callbackId. As noted earlier, the callbackId is an identifying number which is unique to each client that is registered to a callback and can be deduced by the user, such as through the OpenMaya API. The entries in SECTION 3.2 appear as follows:
CallbackId the numeric identifier for the callback. You can cross reference by finding the same callbackId value listed in SECTIONs 3.1 and 3.3.
For each callbackId, the data is broken down per-callback:
Callback the name of the callback, e.g. "attributeChangedMsg".
Percent, Cumulative, Inclusive, Count, API and Node entries as described in SECTION 3.1.
After the callback entries are listed for the callbackId, a dashed followed by a summary line is printed. The summary line lists the self, inclusive and count values for the callback. Note that the percent is relative to the global callback time.
The third part is SECTION 3.3 which lists data per-callback per-node. The nodes are sorted based on the -sortType flag, and for each node, the callbacks are listed, also sorted based on the -sortType flag. As this listing can be long, zero entries are not displayed. An important note for SECTION 3.3 is that only nodes which still exist are displayed. If a node has been deleted, no infromation is listed.

    """
    pass
    


def dimWhen(false=bool, true=bool, clear=bool):
    """
    dimWhen is undoable, NOT queryable, and NOT editable.
    

    
This method attaches the named UI object (first argument) to the named condition (second argument) so that the object will be dimmed when the condition is in a particular state.
This command will fail if the object does not exist. If the condition does not exist (yet), that's okay --- a placeholder will be used until such a condition comes into existence.
The UI object should be one of two things, either a control or a menu item.

    """
    pass
    


def directionalLight(discRadius="string", decayRate=int, softShadow=bool, shadowColor=float, useRayTraceShadows=bool, intensity=float, rgb=float, shadowSamples=int, shadowDither=float, name="string"):
    """
    directionalLight is undoable, queryable, and editable.
    

    
The directionalLight command is used to edit the parameters of existing directionalLights, or to create new ones. The default behaviour is to create a new directionallight.

    """
    pass
    


def directKeyCtx(image1="string", selectedOnly=bool, history=bool, exists=bool, option="string", image2="string", name="string", image3="string"):
    """
    directKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to directly manipulate keyframes within the graph editor

    """
    pass
    


def dirmap(mapDirectory="string", enable=bool, getAllMappings=bool, convertDirectory="string", getMappedDirectory="string", unmapDirectory="string"):
    """
    dirmap is undoable, queryable, and NOT editable.
    

    
Use this command to map a directory to another directory. The first argument is the directory to map, and the second is the destination directory to map to.
Directories must both be absolute paths, and should be separated with forward slashes ('/'). The mapping is case-sensitive on all platforms. This command can be useful when moving projects to another machine where some textures may not be contained in the Maya project, or when a texture archive moves to a new location. This command is not necessary when moving a (self-contained) project from one machine to another - instead copy the entire project over and set the Maya project to the new location.
For one-time directory moves, if the command is enabled and the mapping configured correctly, when a scene is opened and saved the mapped locations will be reflected in the filenames saved with the file. To set up a permanent mapping the command should be enabled and the mappings set up in a script which is executed every time you launch Maya (userSetup.mel is sourced on startup). The directory mappings and enabled state are not preserved between Maya sessions. This command requires one "main" flag that specifies the action to take. Flags are:
-[m|um|gmd|gam|cd|en]

    """
    pass
    


def disable(string, value=bool):
    """
    disable is undoable, NOT queryable, and NOT editable.
    

    
This command enables or disables the control passed as argument.

    """
    pass
    


def disableIncorrectNameWarning():
    """
    disableIncorrectNameWarning is NOT undoable, NOT queryable, and NOT editable.
    

    
Disable the warning dialog which complains about incorrect node names when opening Maya files.

    """
    pass
    


def disconnectAttr(nextAvailable=bool):
    """
    disconnectAttr is undoable, NOT queryable, and NOT editable.
    

    
Disconnects two connected attributes. First argument is the source attribute, second is the destination.

    """
    pass
    


def disconnectJoint(attachHandleMode=bool, deleteHandleMode=bool):
    """
    disconnectJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will break a skeleton at the selected joint and delete any associated handles.

    """
    pass
    


def diskCache(close="string", delete="string", samplingRate=int, empty="string", enabledCachesOnly=bool, frameRangeType="string", startTime=(), append=bool, closeAll=bool, emptyAll=bool, cacheType="string", endTime=(), tempDir=bool, deleteAll=bool, overSample=bool):
    """
    diskCache is NOT undoable, queryable, and NOT editable.
    

    
Command to create, clear, or close disk cache(s).

    """
    pass
    


def displacementToPoly(findBboxOnly=bool):
    """
    displacementToPoly is undoable, queryable, and editable.
    

    
Command bakes geometry with displacement mapping into a polygonal object.

    """
    pass
    


def displayAffected():
    """
    displayAffected is undoable, queryable, and NOT editable.
    

    
Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list.
If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be highlighted because it is affected by the loft curve.

    """
    pass
    


def displayColor(list=bool, dormant=bool, queryIndex=int, resetToSaved=bool, resetToFactory=bool, active=bool, create=bool):
    """
    displayColor is undoable, queryable, and NOT editable.
    

    
This command changes or queries the display color for anything in the application that allows the user to set its color. The color is defined by a color index into either the dormant or active color palette. These colors are part of the UI and not part of the saved data for a model. This command is not undoable.

    """
    pass
    


def displayCull(objects, backFaceCulling=bool):
    """
    displayCull is undoable, queryable, and NOT editable.
    

    
This command is responsible for setting the display culling property of back faces of surfaces.

    """
    pass
    


def displayLevelOfDetail(levelOfDetail=bool):
    """
    displayLevelOfDetail is undoable, queryable, and NOT editable.
    

    
This command is responsible for setting the display level-of-detail for edit refreshes. If enabled, objects will draw with lower detail based on their distance from the camera. When disabled objects will display at full resolution at all times. This is not an undoable command

    """
    pass
    


def displayPref(materialLoadingMode="string", regionOfEffect=bool, shadeTemplates=bool, maxTextureResolution=int, displayGradient=bool, wireframeOnShadedActive="string", purgeExistingTextures=bool, activeObjectPivots=bool, maxHardwareTextureResolution=bool, textureDrawPixel=bool, ghostFrames=int, displayAffected=bool):
    """
    displayPref is undoable, queryable, and NOT editable.
    

    
This command sets/queries the state of global display parameters.

    """
    pass
    


def displayRGBColor(list=bool, hueSaturationValue=bool, resetToFactory=bool, create=bool, resetToSaved=bool):
    """
    displayRGBColor is undoable, queryable, and NOT editable.
    

    
This command changes or queries the display color for anything in the application that allows the user to set its color. These colors are part of the UI and not part of the saved data for a model. This command is not undoable.

    """
    pass
    


def displaySmoothness(objects, full=bool, renderTessellation=bool, divisionsV=int, all=bool, divisionsU=int, hull=bool, pointsShaded=int, polygonObject=int, boundary=bool, simplifyU=int, simplifyV=int, defaultCreation=bool, pointsWire=int):
    """
    displaySmoothness is undoable, queryable, and NOT editable.
    

    
This command is responsible for setting the display smoothness of NURBS curves and surfaces to either predefined or custom values. It also sets display modes for smoothness such as hulls and the hull simplification factors. At present, this command is NOT un-doable.

    """
    pass
    


def displayString(stringstringstringstring, delete=bool, replace=bool, value="string", exists=bool, keys=bool):
    """
    displayString is NOT undoable, queryable, and NOT editable.
    

    
Assign a string value to a string identifier. Allows you define a string in one location and then refer to it by its identifier in many other locations. Formatted strings are also supported (NOTE however, this functionality is now provided in a more general fashion by the format command, use of format is recommended). You may embed up to 3 special character sequences ^1s, ^2s, and ^3s to perform automatic string replacement. The embedded characters will be replaced with the extra command arguments. See example section for more detail. Note the extra command arguments do not need to be display string identifiers.

    """
    pass
    


def displaySurface(objects, flipNormals=bool, xRay=bool, twoSidedLighting=bool):
    """
    displaySurface is undoable, queryable, and NOT editable.
    

    
This command toggles display options on the specified or active surfaces. Typically this command applies to NURBS or poly mesh surfaces and ignores other type of objects.

    """
    pass
    


def distanceDimContext(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    distanceDimContext is undoable, queryable, and editable.
    

    
Command used to register the distanceDimCtx tool.

    """
    pass
    


def distanceDimension(endPoint="string", startPoint="string"):
    """
    distanceDimension is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create a distance dimension to display the distance between two specified points.

    """
    pass
    


def doBlur(length=float, sharpness=float, colorFile="string", smoothColor=bool, smooth=float, vectorFile="string"):
    """
    doBlur is undoable, NOT queryable, and NOT editable.
    

    
The doBlur command will invoke the blur2d, which is a Maya stand-alone application to do 2.5 motion blur given the color image and the motion vector file. For a given input colorFile name, e.g. "xxx.iff", the output blurred image will be "xxx_blur.iff" in the same directory as the input colorFile. There is currently no control over the name of the output blurred image.

    """
    pass
    


def dockControl(name, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", highlightColor=float, splitLayout="string", dragCallback="string", moveable=bool, annotation="string", dockStation="string", preventOverride=bool, popupMenuArray=bool, fixedWidth=bool, exists=bool, retain=bool, floatChangeCommand="string", enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, closeCommand="string", state="string", sizeable=bool, fullPathName=bool, dropCallback="string", r=bool, noBackground=bool, backgroundColor=float, area="string", manage=bool, allowedArea="string", floating=bool, enablePopupOption=bool, isObscured=bool, fixedHeight=bool, content="string"):
    """
    dockControl is undoable, queryable, and editable.
    

    
Create a dockable control, also known as tool palette or utility window. Dock controls are secondary windows placed in the dock area around the central control in a main window. Dock windows can be moved inside their current area, moved into new areas and floated (e.g. undocked). Dock control consists of a title bar and the content area. The titlebar displays the dock control window title, a float button and a close button. Depending on the state of the dock control, the float and close buttons may be either disabled or not shown at all.

    """
    pass
    


def dolly(camera, orthoScale=float, distance="string", dollyTowardsCenter=bool, relative=bool, absolute=bool):
    """
    dolly is undoable, NOT queryable, and NOT editable.
    

    
The dolly command moves a camera along the viewing direction in the world space. The viewing-direction and up-direction of the camera are not altered. There are two modes of operation:
Relative mode: for a perspective camera, the camera is moved along its viewing direction, and the distance of travel is computed with respect to the current position of the camera in the world space. In relative mode, when the camera is moved, its COI is moved along with it, and is kept at the same distance, in front of the camera, as before applying the dolly operation. For orthographic camera, the viewing width of the camera is changed by scaling its ortho width by the new value specified on the command line.
Absolute mode: for a perspective camera, the camera is moved along its viewing direction, to the distance that is computed with respect to the current position of the world center of interest (COI) of the camera. In the absolute mode, when the camera is moved, the COI of the camera is not moved with the camera, but it is fixed at its current location in space. For orthographic camera, the viewing width of the camera is changed by replacing its ortho width with the new value specified on the command line. This command may be applied to more than one cameras; objects that are not cameras are ignored. When no camera name supplied on the command line, this command is applied to all currently active cameras.
The dolly command can be applied to either a perspective or an orthographic camera.

    """
    pass
    


def dollyCtx(image1="string", boxDollyType="string", dollyTowardsCenter=bool, alternateContext=bool, orthoZoom=bool, scale=float, history=bool, toolName="string", centerOfInterestDolly=bool, exists=bool, localDolly=bool, image2="string", name="string", image3="string"):
    """
    dollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a dolly context.

    """
    pass
    


def dopeSheetEditor(docTag="string", defineTemplate="string", parent="string", displayTangents="string", useTemplate="string", lockMainConnection=bool, outliner="string", unParent=bool, showScene=bool, selectionWindow=float, panel="string", showTicks=bool, displayActiveKeyTangents="string", mainListConnection="string", displayValues="string", snapValue="string", highlightConnection="string", lookAt="string", stateString=bool, hierarchyBelow=bool, displayInfinities="string", displayActiveKeys="string", control=bool, showSummary=bool, snapTime="string", autoFit="string", selectionConnection="string", forceMainConnection="string", exists=bool, unlockMainConnection=bool, updateMainConnection=bool, displayKeys="string", filter="string"):
    """
    dopeSheetEditor is undoable, queryable, and editable.
    

    
Edit a characteristic of a dope sheet editor

    """
    pass
    


def doubleProfileBirailSurface(transformMode=int, object=bool, polygon=int, tangentContinuityProfile2=bool, nodeState=int, blendFactor=float, constructionHistory=bool, tangentContinuityProfile1=bool, caching=bool, name="string"):
    """
    doubleProfileBirailSurface is undoable, queryable, and editable.
    

    
The arguments are 4 cuves called "profile1" "profile2" "rail1" "rail2".
This command builds a railed surface by sweeping profile "profile1" along the two given rail curves "rail1", "rail2" until "profile2" is reached. By using the -blend control, the railed surface creation could be biased more towards one of the two profile curves. The curves ( both profiles and rails ) could also be surface curves ( isoparams, curve on surfaces ). If the profile curves are surface curves the surface constructed could be made tangent continuous to the surfaces underlying the profiles using the flags -tp1, -tp2 respectively. Current Limitation: Its necessary that the two profile curves intersect the rail curves for successful surface creation.

    """
    pass
    


def drag(objects, directionX=float, magnitude=float, directionY=float, perVertex=bool, directionZ=float, attenuation=float, maxDistance="string", position="string", useDirection=bool, name="string"):
    """
    drag is undoable, queryable, and editable.
    

    
Drag exerts a friction, or braking force proportional to the speed of a moving object. If direction is not enabled, the drag acts opposite to the current velocity of the object. If direction is enabled, it acts opposite to the component of the velocity in the specified direction. The force is independent of the position of the affected object.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def dragAttrContext(name, image1="string", reset=bool, connectTo="string", history=bool, exists=bool, image2="string", image3="string"):
    """
    dragAttrContext is undoable, queryable, and editable.
    

    
The dragAttrContext allows a user to manipulate the attributes of an object by using a virtual slider within the viewport. The virtual slider is used by dragging in a viewport with the middle mouse button. The speed at which the attributes are changed can be controlled by holding down the Ctrl key to slow it down and the Shift key to speed it up.

    """
    pass
    


def draggerContext(currentStep=int, plane=float, button=int, pressCommand="string", snapping=bool, image3="string", projection="string", image1="string", stepsCount=int, anchorPoint=float, dragCommand="string", drawString="string", exists=bool, finalize="string", name="string", releaseCommand="string", initialize="string", dragPoint=float, undoMode="string", holdCommand="string", modifier="string", prePressCommand="string", history=bool, space="string", image2="string", cursor="string"):
    """
    draggerContext is undoable, queryable, and editable.
    

    
The draggerContext allows the user to program the behavior of the mouse or an equivalent dragging device in MEL.

    """
    pass
    


def dropoffLocator():
    """
    dropoffLocator is undoable, NOT queryable, and NOT editable.
    

    
This command adds one or more dropoff locators to a wire curve, one for each selected curve point. The dropoff locators can be used to provide localized tuning of the wire deformation about the curve point.
The arguments are two floats, the envelope and percentage, followed by the wire node name and then by the curve point(s).

    """
    pass
    


def duplicate(objects, renameChildren=bool, returnRootsOnly=bool, parentOnly=bool, instanceLeaf=bool, smartTransform=bool, inputConnections=bool, name="string", upstreamNodes=bool):
    """
    duplicate is undoable, NOT queryable, and NOT editable.
    

    
This command duplicates the given objects. If no objects are given, then the selected list is duplicated.
The smart transform feature allows duplicate to transform newly duplicated objects based on previous transformations between duplications.
Example: Duplicate an object and move it to a new location. Duplicate it again with the smart duplicate flag. It should have moved once again the distance you had previously moved it.
Note: changing the selected list between smart duplications will cause the transform information to be deleted
The upstream Nodes option forces duplication of all upstream nodes leading upto the selected objects.. Upstream nodes are defined as all nodes feeding into selected nodes. During traversal of Dependency graph, if another dagObject is encountered, then that node and all it's parent transforms are also duplicated.
The inputConnections option forces the duplication of input connections to the nodes that are to be duplicated. This is very useful especially in cases where two nodes that are connected to each other are specified as nodes to be duplicated. In that situation, the connection between the nodes is also duplicated.
See also: instance

    """
    pass
    


def duplicateCurve(local=bool, range=bool, name="string", constructionHistory=bool, object=bool):
    """
    duplicateCurve is undoable, queryable, and editable.
    

    
The duplicateCurve command takes a curve on a surface and and returns the 3D curve. The curve on a surface could be isoparam component, trimmed edge or curve on surface object.

    """
    pass
    


def duplicateSurface(local=bool, name="string", constructionHistory=bool, object=bool):
    """
    duplicateSurface is undoable, queryable, and editable.
    

    
The duplicateSurface command takes a surface patch (face) and and returns the 3D surface. Connected patches are returned as a single surface.

    """
    pass
    


def dynamicLoad():
    """
    dynamicLoad is undoable, queryable, and NOT editable.
    

    
Dynamically load the DLL passed as argument.

    """
    pass
    


def dynCache():
    """
    dynCache is undoable, NOT queryable, and NOT editable.
    

    
Cache the current state of all particle shapes at the current time.

    """
    pass
    


def dynExport(objects, overSampling=int, allObjects=bool, maxFrame=(), attribute="string", format="string", path="string", minFrame=()):
    """
    dynExport is undoable, NOT queryable, and NOT editable.
    

    
Export particle data to disk files.
For cache export (-format cache), dynExport also sets three attributes of the current dynGlobals node. It sets the useParticleRenderCache attribute to true, and the min/maxFrameOfLastParticleRenderCache attributes to correspond to the min and max frames.
Exported .pda or .pdb files are assigned a name of form object name.frame.extension, where extension is "pda" or "pdb."
The naming convention for .pdc files is similar but does not use frame numbers, it uses a more precise representation of the time instead.
By default, the pda and pdb formats export all per-particle attributes, and all integer or float type attributes except those which are hidden or not storable. (Exception: level of detail is not exported, by default) The pdc format exports all attributes which the particle object needs for its state cache.
To specify only selected attributes, use the -atr flag (which is multi-use). In general, it is recommended not to use this flag with pdc type, since you need all the attributes in order for the cache to be useful.
dynExport exports data for the current frame, or for a range of frames specified with -mnf and -mxf. If you are not already at the start frame, dynExport will run up the scene for you. VERY VERY IMPORTANT NOTE: If you use dynExport in -prompt mode, it does NOT automatically force evaluation of your objects. You must do this yourself from your script. The easiest way is to request each particle object's "count" attribute each frame. You must request the count attribute for each object you want to export, because their solvers run independently of one another. In interactive mode, objects WILL get evaluated automatically and you don't have to worry about any of this.
When exporting a particle object whose particles are created from collisions involving particles in another particle object(s), you must make sure you simultaneously export all the particle objects involved in the dependency chain otherwise you will get an empty cache file.
For non-per-particle attributes, pda and pdb formats write the identical value once for each particle. The following types of non-per-particle attributes can be exported: float, double, doubleLinear, doubleAngle, byte, short, long, enum. The first four are exported as "Real" (in PDB parlance), and the last four as "Integer."
In the pda and pdb formats, "particleId" and "particleId0" are exported as Integer, and are exported under the names "id" and "id0" respectively. All other attributes are exported under their long names.

    """
    pass
    


def dynExpression(runtimeAfterDynamics=bool, creation=bool, runtimeBeforeDynamics=bool, string="string"):
    """
    dynExpression is undoable, queryable, and editable.
    

    
This command describes an expression that belongs to the specified particle shape. The expression is a block of code of unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any numeric attribute(s) or per-particle attribute(s) in the scene. One expression can read and alter any number of these attributes. Every particle shape in your scene has three expressions, one for the runtimeBeforeDynamics, one for the runtimeAfterDynamics and one for creation time. The create expression gets executed for every particle in the object whose age is 0.0. The runtime expression gets executed for each particle with an age greater then 0.0. Unlike expressions created with the expression command, particle expressions always exist and are a part of the owning particle object's shape. They default to empty strings, but they are always there. Because of this, there is no need to use the '-e' flag. Every call to the dynExpression command is considered an edit by default. Per-particle attributes are those attributes of a particle shape that have a potentially different value for each particle in the object. Examples of these include position and velocity.
If this command is being sent by the command line or in a script, then the user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when reading them in the expression editor. Also, quotes in an expression must be escaped (\") so that they are not confused by the system as the end of your string. When using the expression editor, these characters are escaped for you unless they are already within quotes.
This type of expression is executed during the evaluation of the dynamics. If an output of the expression is requested before that, then the dynamics will be force to compute at that time. If dynamics is disabled, then these expressions will have no effect.

    """
    pass
    


def dynGlobals(overSampling=int, active=bool, listAll=bool):
    """
    dynGlobals is undoable, queryable, and editable.
    

    
This node edits and queries the attributes of the active dynGlobals node in the scene. There can be only one active node of this type. The active dynGlobals node is the first one that was created, either with a "createNode" command or by accessing/editing any of the attributes on the node through this command.

    """
    pass
    


def dynPaintEditor(drawContext=bool, docTag="string", paintAll=float, refreshMode=int, displayFog=bool, refresh=bool, defineTemplate="string", parent="string", removeAllImages=bool, fileName="string", useTemplate="string", lockMainConnection=bool, displayStyle="string", unParent=bool, nbImages=bool, forceMainConnection="string", changeCommand="string", camera="string", scaleGreen=float, doubleBuffer=bool, mainListConnection="string", currentCanvasSize=bool, zoom=float, highlightConnection="string", newImage=int, rollImage=float, writeImage="string", loadImage="string", clear=float, stateString=bool, exists=bool, iconGrab=bool, updateMainConnection=bool, scaleBlue=float, displayLights="string", panel="string", control=bool, unlockMainConnection=bool, menu="string", saveAlpha=bool, activeOnly=bool, undoCache=bool, selectionConnection="string", removeImage=bool, redrawLast=bool, autoSave=bool, displayTextures=bool, canvasUndo=bool, canvasMode=bool, singleBuffer=bool, snapShot=bool, saveImage=bool, drawAxis=bool, wrap=bool, displayImage=int, saveBumpmap="string", tileSize=int, scaleRed=float, filter="string", displayAppearance="string"):
    """
    dynPaintEditor is undoable, queryable, and editable.
    

    
Create a editor window that can be painted into

    """
    pass
    


def dynParticleCtx(upperZ=float, sketchInterval=int, image3="string", jitterRadius=float, nucleus=bool, image1="string", lowerLeftZ=float, cursorPlacement=bool, lowerLeftY=float, gridSpacing=float, sketch=bool, conserve=float, name="string", upperRightY=float, numJitters=int, grid=bool, textPlacement=bool, upperRightX=float, exists=bool, history=bool, lowerLeftX=float, image2="string", particleName="string"):
    """
    dynParticleCtx is undoable, queryable, and editable.
    

    
The particle context command creates a particle context. The particle context provides an interactive means to create particle objects. The particle context command also provides an interactive means to set the option values, through the Tool Property Sheet, for the "particle" command that the context will issue.

    """
    pass
    


def dynPref(saveRuntimeState=bool, autoCreate=bool, saveOnQuit=bool, runupFrom=int, echoCollision=bool, runupToCurrentTime=bool):
    """
    dynPref is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current state of "autoCreate rigid bodies", "run up to current time", and "run up from" (previous time or start time).

    """
    pass
    


def editDisplayLayerGlobals(mergeType=int, baseId=int, useCurrent=bool, currentDisplayLayer="string"):
    """
    editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    

    
Edit the parameter values common to all display layers. Some of these paremeters, eg. baseId and mergeType, are stored as preferences and some, eg. currentDisplayLayer, are stored in the file.

    """
    pass
    


def editDisplayLayerMembers(fullNames=bool, noRecurse=bool):
    """
    editDisplayLayerMembers is undoable, queryable, and NOT editable.
    

    
This command is used to query and edit membership of display layers. No equivalent 'remove' command is necessary since all objects must be in exactly one display layer. Removing an object from a layer can be accomplished by adding it to a different layer.

    """
    pass
    


def editMetadata(streamName="string", memberName="string", scene=bool, endIndex="string", channelName="string", remove=bool, indexType="string", stringValue="string", startIndex="string", channelType="string", value=float, index="string"):
    """
    editMetadata is undoable, NOT queryable, and NOT editable.
    

    
This command is used to set metadata elements onto or remove metadata elements from an object. Before using this command you must first attach a metadata stream type to the object using the addMetadata command or an API equivalent. The command has four basic variations:
Set per-component metadata on meshes
Remove per-component metadata on meshes
Set generic metadata on any object
Remove generic metadata on any object
The difference between the set and remove variations (1,3 vs. 2,4) is that set requires both a member name to be set and a new value to be set. (The reason removal doesn't use a member name is that you can only remove an entire metadata structural element, you cannot remove only a single member from it.)
When metadata values are set or removed the action is performed on every selected component or index. This provides an easy method to set or remove a bunch of metadata en masse.
The general usage (variations 3, 4) lets you select specific pieces of metadata through the channelName and index flags. Note that since index is a multi-use flag you can select many different elements from the same Channel and set or remove the metadata on all of them in one command.
Metadata on meshes is special in that the Channel types "vertex", "edge", "face", and "vertexFace" are directly connected to the components of the same name. To make setting these metadata Channels easier you can simply select or specify on the command line the corresponding components rather than using the channelName and index flags. For example the selection "myMesh.vtx[8:10]" corresponds to channelName = vertex and index = 8, 9, 10 (as a multi-use flag).
Note that the metadata is assigned to an object and except in the special case of mesh geometry does not flow through the dependency graph. In meshes the metadata will move from node to node wherever the geometry is connected, although it will not adjust itself automatically for changes in topology. Internal data is arranged to minimize the amount of copying no matter how many other nodes are connected to it.
Only a single node or scene, component type, channel type, and value type are allowed in a single command. This keeps the data simple at the possible cost of requiring multiple calls to the command to set more than one structure member's value.
Certain nodes have metadata supplied by input attributes. If you edit one of those with an incoming connection on such an attribute then the metadata edit will not be applied directly it will be put into an 'editMetadata' node for application during DG evaluation. Since the details of the metadata are not known until the evaluation happens less rigorous compatibility checking is performed. The editMetadata node has its own facilities for verifying and reporting illegal metadata edits. Successive edits to the same metadata in this way appends each edit to the same editMetadata node.

    """
    pass
    


def editor(panel="string", docTag="string", control=bool, mainListConnection="string", defineTemplate="string", parent="string", highlightConnection="string", useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", unParent=bool, stateString=bool, exists=bool, updateMainConnection=bool, forceMainConnection="string", unlockMainConnection=bool):
    """
    editor is undoable, queryable, and editable.
    

    
Edit the characteristic of an editor

    """
    pass
    


def editorTemplate(suppress="string", endScrollLayout=bool, callCustom=bool, label="string", queryLabel="string", removeControl="string", queryControl="string", annotation="string", beginScrollLayout=bool, dimControl="string", collapse=bool, endLayout=bool, addExtraControls=bool, addControl=bool, extraControlsLabel="string", endNoOptimize=bool, queryName="string", addComponents=bool, listExtraAttributes="string", preventOverride=bool, beginNoOptimize=bool, addAdskAssetControls=bool, beginLayout="string", addSeparator=bool, interruptOptimize=bool, annotateFieldOnly=bool, addDynamicControl=bool):
    """
    editorTemplate is undoable, NOT queryable, and NOT editable.
    

    
The editorTemplate command allows the user to specify the conceptual layout of an attribute editor and leave the details of exactly which UI elements are used in the final result to the automatic dialog generation mechanism.

    """
    pass
    


def editRenderLayerAdjustment(remove=bool, layer="string", attributeLog=bool, nodeLog=bool):
    """
    editRenderLayerAdjustment is undoable, queryable, and NOT editable.
    

    
This command is used to create, edit, and query adjustments to render layers. An adjustment allows different attribute values or connections to be used depending on the active render layer.

    """
    pass
    


def editRenderLayerGlobals(mergeType=int, baseId=int, useCurrent=bool, currentRenderLayer="string", enableAutoAdjustments=bool):
    """
    editRenderLayerGlobals is undoable, queryable, and NOT editable.
    

    
Edit the parameter values common to all render layers. Some of these paremeters, eg. baseId and mergeType, are stored as preferences and some, eg. currentRenderLayer, are stored in the file.

    """
    pass
    


def editRenderLayerMembers(fullNames=bool, remove=bool, noRecurse=bool):
    """
    editRenderLayerMembers is undoable, queryable, and NOT editable.
    

    
This command is used to query and edit memberships to render layers. Only transform and geometry nodes may be members. At render time, all descendants of the members of a render layer will also be included in the render layer.

    """
    pass
    


def effector(object, hide=bool, name="string"):
    """
    effector is undoable, queryable, and editable.
    

    
The effector command is used to set the name or hidden flag for the effector. The standard edit (-e) and query (-q) flags are used for edit and query functions.

    """
    pass
    


def emit(floatValue=float, object="string", attribute="string", vectorValue=float, position=float):
    """
    emit is undoable, NOT queryable, and NOT editable.
    

    
The emit action allows users to add particles to an existing particle object without the use of an emitter. At the same time, it allows them to set any per-particle attribute for the particles that are created with the action.
The particles created do not become a part of the initial state for the particle object, and will disappear when the scene is rewound unless they are saved into the initial state by the user explicitly. In addition, a particle object will accept particles from an emit action ONLY at frames greater than or equal to its start frame. For example, if you want to use the emit action to create particles at frame -5, you must set startFrame for that particle shape to -5 or less.
Unlike many commands or actions, the emit action uses the order of its flags as important information as to how it works. The -object and -position flags can appear anywhere in the argument list. The -attribute and the value flags are interpreted based on their order. Any value flags after an -attribute flag and before the next -attribute flag will set the values for the attribute specified by the closest -attribute flag before them in the argument list. See the Examples section below for more detail on how these flags work.
Currently, no creation expression is executed for the new particles unless they are created from within a particle expression defined with the dynExpression command or the Expression Editor. If you want any particular values put into the particles at the time they are created, then those values should be set using the -attribute, -vectorValue, and -floatValue flags.

    """
    pass
    


def emitter(objects, torusSectionRadius="string", cycleEmission="string", type="string", directionX="string", maxDistance="string", directionZ="string", alongAxis=float, directionalSpeed=float, tangentSpeed=float, cycleInterval=int, aroundAxis=float, awayFromAxis=float, awayFromCenter=float, minDistance="string", rate=float, volumeSweep=int, spread=float, normalSpeed=float, speed=float, speedRandom=float, volumeShape="string", randomDirection=float, scaleSpeedBySize=bool, volumeOffset="string", scaleRateByObjectSize=bool, position="string", directionY="string", needParentUV=bool):
    """
    emitter is undoable, queryable, and editable.
    

    
Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the named/selected object(s)in the scene. Particles will then be emitted from each. If no objects are named or selected, or if the -pos option is specified, creates a positional emitter.
If an emitter was created, the command returns the name of the object owning the emitter, and the name of emitter shape. If an emitter was queried, the command returns the results of the query.
Keyframeable attributes of the emitter node: rate, directionX, directionY, directionZ, minDistance, maxDistance, spread.

    """
    pass
    


def enableDevice(record=bool, monitor=bool, device="string", enable=bool, apply=bool):
    """
    enableDevice is undoable, queryable, and NOT editable.
    

    
Sets (or queries) the device enable state for actions involving the device.
-monitor
affects all assignInputDevice and attachDeviceAttr actions for the named device
-record
controls if the device is recorded (by default) by a recordDevice action
-apply channelName [channelName ... ]
controls if data from the device channel is applied (by default) by applyTake to the param curves attached to the named channel.
Disabling a channel for applyTake cause applyTake to ignore the enable state of all "child" channels -- treating them as disabled.

    """
    pass
    


def encodeString():
    """
    encodeString is undoable, NOT queryable, and NOT editable.
    

    
This action will take a string and encode any character that would need to be escaped before being sent to some other command. Such characters include:
double quotes
newlines
tabs

    """
    pass
    


def error(showLineNumber=bool, noContext=bool):
    """
    error is NOT undoable, NOT queryable, and NOT editable.
    

    
The error command is provided so that the user can issue error messages from his/her scripts and control execution in the event of runtime errors.
The string argument is displayed in the command window (or stdout if running in batch mode) after being prefixed with an error message heading and surrounded by //.
The error command also causes execution to terminate with an error. Using error is like raising an exception because the error will propagate up through the call chain. You can use catch to handle the error from the caller side. If you don't want execution to end, then you probably want to use the warning command instead.

    """
    pass
    


def eval():
    """
    eval is NOT undoable, NOT queryable, and NOT editable.
    

    
This function takes a string which contains MEL code and evaluates it using the MEL interpreter. The result is converted into a Python data type and is returned. If an error occurs during the execution of the MEL script, a Python exception is raised with the appropriate error message.

    """
    pass
    


def evalDeferred(script, list=bool, lowestPriority=bool, lowPriority=bool):
    """
    evalDeferred is undoable, NOT queryable, and NOT editable.
    

    
This command takes the string it is given and evaluates it during the next available idle time. It is useful for attaching commands to controls that can change or delete the control.

    """
    pass
    


def evaluationManager(upstreamFrom="string", idleBuild=bool, nodeTypeParallel=bool, nodeTypeUntrusted=bool, mode="string", nodeTypeGloballySerialize=bool, safeMode=bool, downstreamFrom="string", cycleCluster="string", enabled=bool, nodeTypeSerialize=bool, invalidate=bool, manipulation=bool):
    """
    evaluationManager is NOT undoable, queryable, and NOT editable.
    

    
Handles turning on and off the evaluation manager method of evaluating the DG. Query the 'mode' flag to see all available evaluation modes. The special mode 'off' disables the evaluation manager. The scheduling override flags 'nodeTypeXXX' force certain node types to use specific scheduling types, even though the node descriptions might indicate otherwise. Use with caution; certain nodes may not react well to alternative scheduling types. Only one scheduling type override will be in force at a time, the most restrictive one. In order, they are untrusted, globally serialized, locally serialized, and parallel. The node types will however remember all overrides. For example, if you set a node type override to be untrusted, then to be parallel it will continue to use the untrusted override. If you then turn off the untrusted override, the scheduling will advance to the parallel one. The actual node scheduling type is always superceded by the overrides. For example, a serial node will still be considered as parallel if the node type has the parallel override set, even though 'serial' is a more restrictive scheduling type. See the 'dbpeek' command 'graph' operation with arguments 'evaluationGraph' and 'scheduling' to see what scheduling type any particular node will end up using after the hierarchy of overrides and native scheduling types is applied.

    """
    pass
    


def evaluator(configuration="string", enable=bool, valueName="string", nodeType="string", info=bool, nodeTypeChildren=bool, priority=bool, name="string", clusters=bool):
    """
    evaluator is NOT undoable, queryable, and NOT editable.
    

    
Handles turning on and off custom evaluation overrides used by the evaluation manager. Query no flag to see all available custom evaluators. Query the 'enable' flag to check if an evaluator is currently enabled. If the 'name' flag isn't used then return all modes and their current active state.

    """
    pass
    


def event(object, list=bool, delete=bool, dieAtCollision=bool, count=int, rename="string", split=int, proc="string", random=bool, emit=int, select=bool, target="string", spread=float, name="string"):
    """
    event is undoable, queryable, and editable.
    

    
The event command assigns collision events to a particle object. Collision events are stored in multi-attributes in the particle shape. The event command returns the event name.

    """
    pass
    


def exactWorldBoundingBox(dagObject, ignoreInvisible=bool):
    """
    exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.
    

    
This command figures out an exact-fit bounding box for the specified objects (or selected objects if none are specified) This bounding box is always in world space.

    """
    pass
    


def exclusiveLightCheckBox(docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, light="string", popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    exclusiveLightCheckBox is undoable, queryable, and editable.
    

    
This command creates a checkBox that controls a light's exclusive non-exclusive status. An exclusive light is one that is not hooked up to the default-light-list, thus it does not illuminate all objects be default. However an exclusive light can be linked to an object.

    """
    pass
    


def exportEdits(editCommand="string", includeSetAttrs=bool, force=bool, includeNode="string", includeAnimation=bool, includeSetDrivenKeys=bool, type="string", selected=bool, excludeNode="string", includeShaders=bool, excludeHierarchy=bool, includeConstraints=bool, onReferenceNode="string", includeDeformers=bool, includeNetwork=bool, exportSelected=bool):
    """
    exportEdits is NOT undoable, queryable, and NOT editable.
    

    
Use this command to export edits made in the scene to a file. The exported file can be subsequently imported to another scene. Edits may include: nodes, connections and reference edits such as value changes. The nodes that are included in the exported file will be based on the options used. At least one option flag that describes the set of target nodes to include in the exported file must be specified (e.g. 'selected', 'onReferenceNode'). Use the inclusion flags ('includeAnimation', 'includeShaders', 'includeNetwork') to specify which additional related nodes will be added to the export list. In export mode, when the command completes successfully, the name of the exported file will be returned. In query mode, this command will return information about the contents of the exported file. The query mode will return the list of nodes that will be considered for inclusion in the exported file based on the specified flags.

    """
    pass
    


def expression(timeDependent="string", object="string", unitConversion="string", shortNames=bool, alwaysEvaluate=int, safe="string", name="string", string="string"):
    """
    expression is undoable, queryable, and editable.
    

    
This command describes an expression that belongs to the current scene. The expression is a block of code of unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any numeric attribute(s) in the scene. One expression can read and alter any number of numeric attributes. Theoretically, every expression in a scene can be combined into one long expression, but it is recommended that they are separated for ease of use and editing, as well as efficiency.
If this command is being sent by the command line or in a script, then the user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when reading them in the expression editor. Also, quotes in an expression must be escaped (\") so that they are not confused by the system as the end of your string. When using the expression editor, these characters are escaped for you unless they are already within quotes.
Note, expressions that alter or use per-particle attributes of a particle shape should use the 'dynExpression' command.

    """
    pass
    


def expressionEditorListen(listenForName="string", stopListenForName="string", listenForAttr="string", stopListenForAttr="string", listenForExpression="string", stopListenForExpression="string", listenFile="string"):
    """
    expressionEditorListen is undoable, NOT queryable, and NOT editable.
    

    
Listens for messages for the Expression Editor, at its request, and communicates them to it. This action is for internal use only and should not be called by users. This action should be called only by the Expression Editor.

    """
    pass
    


def extendCurve(extensionType=int, pointZ="string", inputPoint="string", distance="string", curveOnSurface=bool, pointX="string", object=bool, start=int, nodeState=int, range=bool, replaceOriginal=bool, name="string", join=bool, pointY="string", removeMultipleKnots=bool, caching=bool, constructionHistory=bool, extendMethod=int):
    """
    extendCurve is undoable, queryable, and editable.
    

    
This command extends a curve or creates a new curve as an extension

    """
    pass
    


def extendSurface(surfacesurface, extensionType=int, distance="string", extendDirection=int, object=bool, nodeState=int, replaceOriginal=bool, name="string", extendSide=int, join=bool, caching=bool, constructionHistory=bool, extendMethod=int):
    """
    extendSurface is undoable, queryable, and editable.
    

    
This command extends a surface or creates a new surface as an extension.

    """
    pass
    


def extrude(curvecurve, useComponentPivot=int, rebuild=bool, polygon=int, scale=float, directionX="string", subCurveSubSurface=bool, directionZ="string", length="string", object=bool, range=bool, caching=bool, name="string", reverseSurfaceIfPathReversed=bool, pivot="string", rotation=int, useProfileNormal=bool, fixedPath=bool, direction="string", nodeState=int, directionY="string", extrudeType=int, degreeAlongLength=int, constructionHistory=bool):
    """
    extrude is undoable, queryable, and editable.
    

    
This command computes a surface given a profile curve and possibly a path curve. There are three ways to extrude a profile curve. The most basic method is called a "distance" extrude where direction and length are specified. No path curve is necessary in this case. The second method is called "flat" extrude. This method sweeps the profile curve down the path curve without changing the orientation of the profile curve. Finally, the third method is called "tube" extrude. This method sweeps a profile curve down a path curve while the profile curve rotates so that it maintains a relationship with the path curve.

    """
    pass
    


def falloffCurve(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, asString="string", dragCallback="string", currentKeyValue=float, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, currentKey=int, exists=bool, addControlVertex="string", readOnly=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, customCurveWidget=bool, optionVar="string", snapToGrid=bool, changeCommand="string", isObscured=bool, deleteControlVertex=int):
    """
    falloffCurve is undoable, queryable, and editable.
    

    
This command creates a control for editing a 2D control curve. The control attaches to an optionVar used to store and retrieve the encoded control points stored in a string.

    """
    pass
    


def falloffCurveAttr(string, docTag="string", currentKeyValue=float, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, asString="string", dragCallback="string", height=int, selectedValueControl="string", highlightColor=float, annotation="string", changeCommand="string", preventOverride=bool, popupMenuArray=bool, currentKey=int, exists=bool, addControlVertex="string", readOnly=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, selectedPositionControl="string", enable=bool, fullPathName=bool, attribute="string", dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, customCurveWidget=bool, snapToGrid=bool, isObscured=bool, deleteControlVertex=int):
    """
    falloffCurveAttr is undoable, queryable, and editable.
    

    
This command creates a control for editing a 2D control curve. This control attaches to a curve attribute, which must be a multi attribute where each entry is a compound composed of:
A single float for control point position
A single float for control point value
The MEL command AEaddCurveControl should be used to attach this control to an attribute in the attribute editor templates.

    """
    pass
    


def fcheck():
    """
    fcheck is NOT undoable, NOT queryable, and NOT editable.
    

    
Invokes the fcheck program to display images in a separate window.

    """
    pass
    


def file(returnNewNodes=bool, sharedNodes="string", removeDuplicateNetworks=bool, preSaveScript="string", i=bool, usingNamespaces=bool, exportSelectedNoReference=bool, loadAllDeferred=bool, defaultExtensions=bool, groupLocator=bool, unresolvedName=bool, relativeNamespace="string", moveSelected=bool, uiConfiguration=bool, options="string", loadReference="string", modified=bool, exportAnimFromReference=bool, expandName=bool, applyTo="string", deferReference=bool, mergeNamespaceWithParent=bool, proxyManager="string", defaultNamespace=bool, lockContainerUnpublished=bool, executeScriptNodes=bool, open=bool, cleanReference="string", channels=bool, mergeNamespacesOnClash=bool, prompt=bool, compress=bool, activeProxy=bool, removeReference=bool, exportAnim=bool, groupName="string", selectAll=bool, exportAll=bool, loadSettings="string", lockFile=bool, copyNumberList=bool, saveReference=bool, preserveName=bool, expressions=bool, mergeNamespaceWithRoot=bool, saveTextures="string", segment="string", location=bool, sharedReferenceFile=bool, force=bool, namespace="string", command="string", exportSelectedAnimFromReference=bool, strict=bool, loadReferencePreview="string", constructionHistory=bool, postSaveScript="string", buildLoadSettings=bool, errorStatus=bool, reference=bool, writable=bool, exportAsSegment=bool, lastFileOption=bool, withoutCopyNumber=bool, rename="string", flushReference="string", lockReference=bool, lastTempFile=bool, importReference=bool, saveReferencesUnloaded=bool, ignoreVersion=bool, renameToSave=bool, proxyTag="string", parentNamespace=bool, replaceName="string", shader=bool, groupReference=bool, loadReferenceDepth="string", renamingPrefixList=bool, exportAsReference=bool, anyModified=bool, referenceDepthInfo=int, editCommand="string", preview=bool, referenceNode="string", swapNamespace="string", loadNoReferences=bool, exportSelectedAnim=bool, mapPlaceHolderNamespace="string", renameAll=bool, type="string", preserveReferences=bool, sceneName=bool, newFile=bool, unloadReference="string", exists=bool, saveDiskCache="string", renamingPrefix="string", shortName=bool, save=bool, add=bool, list=bool, exportUnloadedReferences=bool, constraints=bool, resetError=bool, activate=bool, exportSelected=bool, loadAllReferences=bool):
    """
    file is undoable, queryable, and editable.
    

    
Opening, importing, exporting, referencing, saving, or renaming a file
This command needs a single main flag that specifies the action to take. Some of the main flags also take optional secondary flags to modify that action.
The main flags are:
cr ea ean ear eas er esa es
esn ex fr i ir l lr lrp
loc ltf mf new o op ot pmt
r rdi rn rr rts s sa sdx
st stx typ uc ur w
o/open can be modified by the following secondary flags:
f lad lad lnr rnn
es/exportSelected can be modified by the following secondary flags:
ch chn con exp sh
r/reference can be modified by the following secondary flags:
dns dr gr gl gn mnc ns rfn rpr sns srf shd rnn
i/import can be modified by the following secondary flags:
dns dr gr gn mnc pr ra rdn rnn rpr sns
n/new and s/save can be modified by the following secondary flags:
f
er/exportAsReference can be modified by the following secondary flags:
ns rpr
ea/exportAll and es/exportSelected can be modified by the following secondary flags:
f pr
ean/exportAnim, eas/exportSelectedAnim can be modified by the following secondary flags:
f
ear/exportAnimFromReference, esa/exportSelectedAnimFromReference can be modified by the following secondary flags:
f rfn
Querying information about a file
This command needs a single main query flag that specifies the query to take and then optional secondary flags to modify that query.
The main query flags are:
amf ch chn con dr err ex exn
exp l loc ltf mf ns op ot
pmt pns r rfn rpl rpr rts sdc
sh sn stx typ uc w
dr/deferReference can be modified by the following secondary flags:
rfn
exn/expandName, l/list, r/reference, sn/sceneName can be modified by the following secondary flags:
un shn wcn
Querying file names
When querying a file name there are a number of ways to format the result:
Resolved vs. unresolved name:
When a file is loaded into Maya (e.g., by opening or referencing it), the file path provided may not be complete. It could, for example, be a relative path (ex: "scenes/myScene.ma"), it could contain environment variables (ex: "$PRODUCTION_DIR/myScene.ma"), and it could even be a path which simply doesn't exist on the local disk. In each of these cases Maya goes through a number of steps to resolve the path and find the file on disk. By default the 'file' command will return the resolved file name (i.e., the location from which Maya is actually reading the file), but if the un/unresolved flag is used, the unresolved file (e.g., the one that was originally specified) will be returned. When providing a file path with an environment variable; for example, when using the -rename flag, the environment variable should be set to a relative path ( such as "/scenes/scenesSetA"; ). Providing a path using an environment variable that is set to an absolute path ( for example, "C:/scenes/" ) is not supported.
Full vs. short name:
By default the 'file' command will return the full path to a file, but if the shn/shortName flag is used just the file name will be returned.
With vs. without copy number:
When the same file is loaded into Maya more than once (for example by referencing the same file twice), Maya distinguishes between the various copies by appending a copy number to the end of the file name. The first time the file is loaded, no copy number is appended. The second time the file is loaded a "{1}" is appended, the third time a "{2}" is used, and so on. By default the 'file' command will return the file name with the copy number appended, but if the wcn/withoutCopyNumber flag is used the file name will be returned without the copy number.
Additional Details
The file command usually expects a file name as its argument, if none is specified then the root scene is used.
See the individual flag descriptions for details and limitations.

    """
    pass
    


def fileBrowserDialog(fileType="string", mode=int, actionName="string", includeName="string", operationMode="string", fileCommand="string", tipMessage="string", dialogStyle=int, filterList="string", windowTitle="string"):
    """
    fileBrowserDialog is undoable, NOT queryable, and NOT editable.
    

    
The fileBrowserDialog and fileDialog commands have now been deprecated. Both commands are still callable, but it is recommended that the fileDialog2 command be used instead. To maintain some backwards compatibility, both fileBrowserDialog and fileDialog will convert the flags/values passed to them into the appropriate flags/values that the fileDialog2 command uses and will call that command internally. It is not guaranteed that this compatibility will be able to be maintained in future versions so any new scripts that are written should use fileDialog2.
See below for an example of how to change a script to use fileDialog2.

    """
    pass
    


def fileDialog(defaultFileName="string", directoryMask="string", application=bool, title="string", mode=int):
    """
    fileDialog is undoable, NOT queryable, and NOT editable.
    

    
The fileBrowserDialog and fileDialog commands have now been deprecated. Both commands are still callable, but it is recommended that the fileDialog2 command be used instead. To maintain some backwards compatibility, both fileBrowserDialog and fileDialog will convert the flags/values passed to them into the appropriate flags/values that the fileDialog2 command uses and will call that command internally. It is not guaranteed that this compatibility will be able to be maintained in future versions so any new scripts that are written should use fileDialog2.
See below for an example of how to change a script to use fileDialog2.

    """
    pass
    


def fileDialog2(caption="string", selectionChanged="string", fileMode=int, optionsUICreate=bool, cancelCaption="string", optionsUIInit="string", startingDirectory="string", hideNameEdit=bool, returnFilter=bool, optionsUICommit2="string", optionsUICommit="string", okCaption="string", selectFileFilter="string", fileTypeChanged="string", fileFilter="string", dialogStyle=int, optionsUICancel="string", buttonBoxOrientation=int):
    """
    fileDialog2 is undoable, NOT queryable, and NOT editable.
    

    
This command provides a dialog that allows users to select files or directories.

    """
    pass
    


def fileInfo(stringstring, remove="string"):
    """
    fileInfo is NOT undoable, queryable, and NOT editable.
    

    
fileInfo provides a mechanism for keeping information related to a Maya scene file. Each invocation of the command consists of a keyword/value pair, where both the keyword and the associated value are strings. The command may be invoked multiple times with different keywords. Maya emits this command several times into each file it creates, primarily to provide details such as which productization or packaging of the program was used (e.g "Complete", "Unlimited"), the specific version and build identification that was run, and the operating system on which it was run. Maya may make use of this information when present in files it reads. All keyword/value pairs defined by use of the fileInfo command are preserved when Maya saves the scene, whether to an ASCII or binary file.

    """
    pass
    


def filePathEditor(listDirectories="string", refresh=bool, preview=bool, relativeNames=bool, registerType="string", replaceString="string", unresolved=bool, attributeType="string", copyAndRepath="string", listFiles="string", temporary=bool, deregisterType="string", withAttribute=bool, repath="string", listRegisteredTypes=bool, replaceAll=bool, replaceField="string", typeLabel="string", attributeOnly=bool, force=bool, byType="string", recursive=bool, status=bool):
    """
    filePathEditor is undoable, queryable, and NOT editable.
    

    
Maya can reference and use external files, such as textures or other Maya scenes. This command is used to get the information about those file paths and modify them in bulk. By default, only the most frequently used types of files are presented to the user:
Texture
Scene reference
Audio
Image plane
For the command to manage more file types, those must be explicitly requested by the caller using the "registerType" flag. This flag tells the command about attributes or nodes that are to reveal their paths when the command is used.
Currently, the attributes specified through this flag must have the "usedAsFileName" property. Supported nodes are "reference" and plug-in nodes. For example: "brush.flowerImage" or "reference" can be used as value for this flag.
Conversely, the "deregisterType" flag can be used to tell the command to stop handling certain attributes or nodes.
Once the set of attributes and nodes to be searched for external files is selected, the command can be used to obtain a list of plugs that contain file names. Additional information can be obtained, such as each file's name, directory, and report whether the file exists. Additional information about the associated node or plug can also be obtained, such as its name, type and label.
Finally, the command can be used to perform various manipulations such as editing the paths, remapping the files or verifying the presence of identically-named files in target directories. See the "repath", "copyAndRepath" and "replaceField" flags for more information.
The results of these manipulations can be previewed before they are applied using the "preview" flag.

    """
    pass
    


def filletCurve(curvecurve, bias="string", depth="string", caching=bool, object=bool, name="string", freeformBlend=bool, nodeState=int, curveParameter2=float, circular=bool, replaceOriginal=bool, radius="string", blendControl=bool, constructionHistory=bool, curveParameter1=float):
    """
    filletCurve is undoable, queryable, and editable.
    

    
The curve fillet command creates a fillet curve between two curves. If no objects are specified in the command line, then the first two active curves are used. The fillet created can be circular (with a radius) or freeform (with a type of tangent or blend).

    """
    pass
    


def filter(type="string", name="string"):
    """
    filter is undoable, queryable, and editable.
    

    
Creates or modifies a filter node. Filter nodes are used by applyTake to modify recorded device data before assigning it to the param curves for the attached attributes.

    """
    pass
    


def filterCurve(maxTimeStep=float, startTime=(), filter="string", kernel="string", timeTolerance=float, endTime=(), tolerance=float, minTimeStep=float, period=float):
    """
    filterCurve is undoable, NOT queryable, and NOT editable.
    

    
The filterCurve command takes a list of anim curve and filters them. Currently only a Euler filter is supported. The Euler filter demangles discontinous rotation anim curves into smooth curves.

    """
    pass
    


def filterExpand(symSeam=bool, symNegative=bool, symActive=bool, expand=bool, fullPath=bool, symPositive=bool, selectionMask=int):
    """
    filterExpand is undoable, NOT queryable, and NOT editable.
    

    
Based on selected components (or components specified on the command line), the command filters and/or expands the list given the options. Returns a string array containing all matching selection items. Selection masks are as follows:
Object Type Mask
Handle 0
Nurbs Curves 9
Nurbs Surfaces 10
Nurbs Curves On Surface 11
Polygon 12
Locator XYZ 22
Orientation Locator 23
Locator UV 24
Control Vertices (CVs) 28
Edit Points 30
Polygon Vertices 31
Polygon Edges 32
Polygon Face 34
Polygon UVs 35
Subdivision Mesh Points 36
Subdivision Mesh Edges 37
Subdivision Mesh Faces 38
Curve Parameter Points 39
Curve Knot 40
Surface Parameter Points 41
Surface Knot 42
Surface Range 43
Trim Surface Edge 44
Surface Isoparms 45
Lattice Points 46
Particles 47
Scale Pivots 49
Rotate Pivots 50
Select Handles 51
Subdivision Surface 68
Polygon Vertex Face 70
NURBS Surface Face 72
Subdivision Mesh UVs 73

    """
    pass
    


def filterStudioImport(includeCameras=bool, includeLights=bool, convertShellToPoly=bool, transferDirectoryName="string"):
    """
    filterStudioImport is NOT undoable, NOT queryable, and NOT editable.
    

    
Directly sets the filter options on the studioImport plugin from anywhere in MEL without having to use the UI. This is used by ViCE.

    """
    pass
    


def findKeyframe(animatedObject, time=(), hierarchy="string", float=(), includeUpperBound=bool, controlPoints=bool, which="string", curve=bool, shape=bool, timeSlider=bool, attribute="string", animation="string", index=int):
    """
    findKeyframe is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command will return the time (in current units) of the requested key. For the relative direction methods (next, previous) if -time is NOT specified they will use current time. If the specified object is not animated the command will return the current time.

    """
    pass
    


def findType(exact=bool, deep=bool, forward=bool, type="string"):
    """
    findType is NOT undoable, NOT queryable, and NOT editable.
    

    
The findType command is used to search through a dependency subgraph on a certain node to find all nodes of the given type. The search can go either upstream (input connections) or downstream (output connections). The plug/attribute dependencies are not taken into account when searching for matching nodes, only the connections.

    """
    pass
    


def fitBspline(object=bool, nodeState=int, constructionHistory=bool, caching=bool, tolerance="string", name="string"):
    """
    fitBspline is undoable, queryable, and editable.
    

    
The fitBspline command fits the CVs from an input curve and and returns a 3D curve.

    """
    pass
    


def flexor(objects, list=bool, noScale=bool, atBones=bool, type="string", atJoints=bool, toSkeleton=bool, deformerCommand="string", name="string"):
    """
    flexor is undoable, queryable, and editable.
    

    
This command creates a flexor. A flexor a deformer plus a set of driving attributes. For example, a flexor might be a sculpt object that is driven by a joint's x rotation and a cube's y position.

    """
    pass
    


def floatField(string, docTag="string", height=int, step=float, defineTemplate="string", parent="string", numberOfPopupMenus=bool, showTrailingZeros=bool, width=int, dragCallback="string", enterCommand="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, dragCommand="string", value=float, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, useTemplate="string", fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, minValue=float, maxValue=float, manage=bool, editable=bool, precision=int, isObscured=bool, receiveFocusCommand="string"):
    """
    floatField is undoable, queryable, and editable.
    

    
Create a field control that accepts only float values and is bound by a minimum and maximum value. An invisible slider is attached to the field and accessed by holding down the Ctrl modifier key while pressing one of the mouse buttons. Dragging the invisible slider to the right with the middle mouse button increases the field value by the amount specified with the -s/step flag, while dragging to the left decreases the value by the same amount. The left and right mouse buttons apply a factor of 0.1 and 10 to the step value.

    """
    pass
    


def floatFieldGrp(groupName, docTag="string", height=int, step=float, columnWidth4=int, extraLabel="string", enable3=bool, popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, dragCallback="string", columnOffset2=int, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, value2=float, columnAlign4="string", adjustableColumn5=int, value1=float, dragCommand="string", value=float, exists=bool, columnAttach4="string", numberOfFields=int, adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", precision=int, value4=float, fullPathName=bool, enable2=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, enable4=bool, columnWidth=int, showTrailingZeros=bool, manage=bool, columnOffset4=int, enable1=bool, changeCommand="string", columnAttach2="string", value3=float, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    floatFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text and editable float fields. The label text is optional and one to four float fields can be created.

    """
    pass
    


def floatScrollBar(string, docTag="string", height=int, step=float, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, dragCommand="string", value=float, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, horizontal=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, largeStep=float, minValue=float, maxValue=float, manage=bool, isObscured=bool):
    """
    floatScrollBar is undoable, queryable, and editable.
    

    
Create a scroll bar control that accepts only float values and is bound by a minimum and maximum value. The scroll bar displays a marker indicating the current value of the scroll bar relative to it's minimum and maximum values. Click and drag the marker or on the scroll bar itself to change the current value.

    """
    pass
    


def floatSlider(string, docTag="string", height=int, step=float, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, dragCommand="string", value=float, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, horizontal=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, minValue=float, maxValue=float, manage=bool, isObscured=bool):
    """
    floatSlider is undoable, queryable, and editable.
    

    
Create a slider control that accepts only float values and is bound by a minimum and maximum value. The slider displays a marker indicating the current value of the slider relative to it's minimum and maximum values. Click and drag the marker or on the slider itself to change the current value.

    """
    pass
    


def floatSlider2(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", highlightColor=float, annotation="string", preventOverride=bool, positionControl1="string", popupMenuArray=bool, maximum=float, exists=bool, positionControl2="string", minimum=float, enable=bool, changeCommand2="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, value1=float, values=float, fullPathName=bool, dropCallback="string", changeCommand1="string", noBackground=bool, backgroundColor=float, value2=float, polarity=int, manage=bool, isObscured=bool):
    """
    floatSlider2 is undoable, queryable, and editable.
    

    
This command creates a float slider containing two handles. The two handles are arranged such that they cannot pass one another, thus handle 1 will always have a value less than or or equal to handle 2 when you adjust the values. Each handle may have a MEL command associated with it which is issued when the handle moves and thus can be used to update the values of plugs such as via a setAttr command. Each handle can also be associated with a float textfield to display the current value of the handle.
Note: the floatSlider2 widget currently only supports vertical (columnLayout) orientation.

    """
    pass
    


def floatSliderButtonGrp(name, docTag="string", buttonCommand="string", step=float, buttonLabel="string", extraLabel="string", popupMenuArray=bool, image="string", numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, height=int, sliderStep=float, dragCallback="string", columnOffset2=int, isObscured=bool, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, adjustableColumn6=int, columnWidth6=int, field=bool, adjustableColumn4=int, fieldMinValue=float, columnOffset3=int, columnWidth4=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", value=float, exists=bool, columnAttach4="string", useTemplate="string", adjustableColumn2=int, backgroundColor=float, fieldStep=float, enable=bool, columnAlign=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", symbolButtonCommand="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", visible=bool, precision=int, fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", columnWidth5=int, minValue=float, columnWidth=int, maxValue=float, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", columnAttach6="string", fieldMaxValue=float, symbolButtonDisplay=bool, rowAttach=int, columnOffset6=int):
    """
    floatSliderButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a float slider component with optional button and symbol buttons.
TelfFloatSliderGrpCmd.cpp

    """
    pass
    


def floatSliderGrp(groupName, docTag="string", height=int, step=float, columnWidth4=int, extraLabel="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, sliderStep=float, dragCallback="string", columnOffset2=int, isObscured=bool, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, fieldMinValue=float, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", value=float, exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, fieldStep=float, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", precision=int, fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, minValue=float, columnWidth=int, maxValue=float, field=bool, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", columnAttach6="string", fieldMaxValue=float, rowAttach=int, columnOffset6=int):
    """
    floatSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of controls containing a label text, an float field and a float slider. The text and field controls are optional. Editing or querying the field range values has no effect if the -f/field flag was not specified when the group was created.
This group also allows you to enter values into the field outside of the slider range which is limited by the -min/minValue and -max/maxValue flags. To do this, use the -fmn/fieldMinValue and -fmx/fieldMaxValue flags to specify a greater range of values.
Note that the command will not allow you to specify a -fmn/fieldMinValue greater than the -min/minValue value nor a -fmx/fieldMaxValue less than the -max/maxValue value.
If you do supply a larger field range with the -fmn/fieldMinValue and -fmx/fieldMaxValue flags then you will notice that entering a value in the field that is outside of the slider range will result in extending the slider range as well. For example, if you create a slider group with the following command:
floatSliderGrp -min -10 -max 10 -fieldMinValue -100 -fieldMaxValue 100;
Then you will be able to use the slider to select any value from -10 to 10. At the same time you will be able to enter into the field any value from -100 to 100. If you enter a value, say 20, then the new slider range will grow such that this value is now accessible through the slider as well. In fact, the new slider limit will become double of that what you entered. Note that the slider limits will never grow beyond the field limits, in other words if you entered the value 80 then the slider will be clipped to the field limit of 100 and not doubled to 160.

    """
    pass
    


def flow(localDivisions=int, localCompute=bool, divisions=int, objectCentered=bool):
    """
    flow is undoable, queryable, and editable.
    

    
The flow command creates a deformation lattice to `bend' the object that is animated along a curve of a motion path animation. The motion path animation has to have the follow option set to be on.

    """
    pass
    


def flowLayout(string, docTag="string", vertical=bool, height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, popupMenuArray=bool, numberOfChildren=bool, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, childArray=bool, exists=bool, columnSpacing=int, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", dragCallback="string", noBackground=bool, backgroundColor=float, wrap=bool, manage=bool, isObscured=bool):
    """
    flowLayout is undoable, queryable, and editable.
    

    
This command creates a layout that arranges its children along a single line (either horizontal or vertical). Depending on the value of the -wrap boolean flag (default is false), if the layout's parent cannot fit all the children on one line, the children will either wrap onto the next line(s) or be truncated.

    """
    pass
    


def fluidCacheInfo(hasCache=bool, endFrame=bool, resolution=bool, playback=bool, hasData=bool, startFrame=bool, attribute="string", cacheTime=(), initialConditions=bool):
    """
    fluidCacheInfo is undoable, queryable, and editable.
    

    
A command to get information about the fluids cache. Get the startFrame and resolution for InitialConditions. Get the endFrame as well for a playback cache. Note that for the playback cache, it will look at the current time (or last frame if the current time is past end of cache)

    """
    pass
    


def fluidEmitter(torusSectionRadius="string", minDistance="string", rate=float, volumeOffset="string", cycleEmission="string", fuelEmissionRate=float, type="string", volumeSweep=int, position="string", fluidDropoff=float, heatEmissionRate=float, volumeShape="string", cycleInterval=int, maxDistance="string", densityEmissionRate=float):
    """
    fluidEmitter is undoable, queryable, and editable.
    

    
Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the named/selected object(s)in the scene. Fluid will then be emitted from each. If no objects are named or selected, or if the -pos option is specified, creates a positional emitter.
If an emitter was created, the command returns the name of the object owning the emitter, and the name of emitter shape. If an emitter was queried, the command returns the results of the query.

    """
    pass
    


def fluidVoxelInfo(inBounds=int, zIndex=int, checkBounds=bool, xIndex=int, objectSpace=bool, yIndex=int, voxel=float, voxelCenter=bool, radius=float):
    """
    fluidVoxelInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
Provides basic information about the mapping of a fluid voxel grid into world- or object space of the fluid. Use this command to determine the center point of a voxel, or to find the voxel containing a given point, among other things.

    """
    pass
    


def flushUndo():
    """
    flushUndo is undoable, NOT queryable, and NOT editable.
    

    
Removes everything from the undo queue, freeing up memory.

    """
    pass
    


def fontDialog(FontList=bool, scalable=bool):
    """
    fontDialog is undoable, NOT queryable, and NOT editable.
    

    
Displays a dialog of available fonts for the user to select from. The name of the selected font is returned, or an empty string if no font was selected.
When the FontList flag is used, no dialog is displayed. Instead the command returns an array of the available fonts.

    """
    pass
    


def format(stringArg="string"):
    """
    format is NOT undoable, NOT queryable, and NOT editable.
    

    
This command takes a format string, where the format string contains format specifiers. The format specifiers have a number associated with them relating to which parameter they represent to allow for alternate ordering of the passed-in values for other languages by merely changing the format string

    """
    pass
    


def formLayout(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", numberOfChildren=bool, highlightColor=float, attachOppositeControl="string", annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, attachPosition="string", childArray=bool, attachForm="string", attachOppositeForm="string", exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, attachControl="string", manage=bool, attachNone="string", numberOfDivisions=int, isObscured=bool):
    """
    formLayout is undoable, queryable, and editable.
    

    
This command creates a form layout control. A form layout allows absolute and relative positioning of the controls that are its immediate children.
Controls have four edges: top, left, bottom and right. There are only two directions that children can be positioned in, right-left and up-down. The attach flags take the direction of an attachment from the argument that names the edge to attach (the second argument). Any or all edges of a child may be attached. There are six ways to attach them:
Attach to Form - Attaches an edge to the relevant side of the form layout. Thus -attachForm button3 "left" will attach the left edge of the button to the left edge of the form.
Attach to Opposite Side of Form - Attaches an edge relative to the furthest side of the form layout.
Attach to Another Control - Attaches an edge to the closest edge of the other control named.
Attach to Opposite Side of Another Control - Attaches an edge relative to the furthest side of another control.
Attach to Position - Attaches an edge to a position on the form layout. The position is given as a fixed fraction of the -nd/numDivisions value and as this value defaults to 100 it is easiest to think of it as a percentage of the form's size.
Attach to Nothing - Attaches an edge to nothing. The size of the child control will determine this edge's position.
Each edge attachment may have an offset that acts to separate controls visually.
There is no default positioning relationship so to have children appear in the form they must have at least one edge attached in each direction.
Note: In the flag definitions the arguments follow these rules:
control must be the name of an immediate child of the form layout.
edge must be one of "top", "left", "bottom", or "right".
position may range from 0 to the number of divisions as specified with the -nd/numberOfDivisions flag and gives the fraction of the width of the form as a measurement. This normally means 0-100 so position may be thought of as a percentage.
offset is an integer value in pixels.
These are multi-use flags so any number of attachments may be made in a single command.
Note: Avoid making control attachments that form a loop in control dependencies. For example:
window;
string $form = `formLayout`;
string $btn1 = `button`;
string $btn2 = `button`;
string $btn3 = `button`;
formLayout -edit
    -attachControl $btn2 "top"   2 $btn1
    -attachControl $btn3 "top"   2 $btn2
    -attachControl $btn1 "right" 2 $btn3
$form;
showWindow;
$btn2 is attached to $btn1, $btn3 is attached to $btn2, and $btn1 is attached to $btn3. Thus, the placement of $btn1 is dependent on the placement of $btn3, which is dependent on the placement of $btn2, which is dependent on the placement of $btn1. The last control attachment will have created a loop in the dependencies.
To prevent runtime errors, Maya will ignore this attachment and instead issue a warning that a cyclical control attachment has been detected in the script.

    """
    pass
    


def frameBufferName(camera="string", autoTruncate=bool, renderPass="string", renderLayer="string"):
    """
    frameBufferName is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns the frame buffer name for a given renderPass renderLayer and camera combination. Optionally, this command can apply a name truncation algorithm so that the frameBuffer name will respect the maximum length imposed by the destination file format, if applicable.

    """
    pass
    


def frameLayout(string, docTag="string", borderVisible=bool, defineTemplate="string", parent="string", backgroundShade=bool, useTemplate="string", width=int, label="string", dragCallback="string", height=int, collapseCommand="string", numberOfChildren=bool, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, collapse=bool, childArray=bool, font="string", exists=bool, expandCommand="string", visibleChangeCommand="string", marginHeight=int, enableBackground=bool, preCollapseCommand="string", numberOfPopupMenus=bool, preExpandCommand="string", visible=bool, noBackground=bool, marginWidth=int, fullPathName=bool, dropCallback="string", labelVisible=bool, labelIndent=int, backgroundColor=float, manage=bool, collapsable=bool, borderStyle="string", isObscured=bool):
    """
    frameLayout is undoable, queryable, and editable.
    

    
This command creates frame layout control. A frame layout may draw a border around its child controls as well as a display a title. Frame layouts may also be collapsable. Collapsing a frame layout will make the child of the frame layout invisible and shrink the frame layout size. The frame layout may then be expanded to make its child visible. Note that the frame layout may have only one child control. If you wish to have more than one child inside a frame layout then you must use some other control layout as the immediate child of the frame layout.

    """
    pass
    


def freeFormFillet(surfaceIsoparmsurfaceIsoparm, positionTolerance=float, caching=bool, tangentTolerance=float, object=bool, polygon=int, nodeState=int, range=bool, constructionHistory=bool, bias=float, depth=float, name="string"):
    """
    freeFormFillet is undoable, queryable, and editable.
    

    
This command creates a free form surface fillet across two surface trim edges or isoparms or curve on surface. The fillet surface creation has blend controls in the form of bias and depth. The bias value scales the tangents at the two ends across the two selected curves. The depth values controls the curvature of the fillet across the two selected curves. The default values of depth, bias are 0.5 and 0.5 respectively.

    """
    pass
    


def freeze(displayLayers=bool, frozen=bool, unfreeze=bool, invisible=bool, noFreeze=bool, upstream=bool, downstream=bool, allNodes=bool, forceDownstream=bool):
    """
    freeze is undoable, queryable, and NOT editable.
    

    
When a node is frozen none of its inputs will be requested when they change, the node will use the inputs that existed at the time of freezing until the node is unfrozen. A node can be frozen in one of two ways; either directly, via setting the "frozen" attribute on the node to be true, or indirectly, via setting the "frozenAffected" extension attribute on the node to be true. This command lets you freeze nodes based on various criteria. See the flags for the types of criteria the command uses to decide what to freeze or unfreeze. The nodes that are selected are frozen directly. The nodes affected by directly frozen nodes, considering the argument settings, are frozen indirectly. If the frozen attribute, visibililty, or display layer mode has an input connection then the frozen state will not propagate because the node could be unfrozen or become visible at playback time. In query mode this command will find the nodes with each of the frozen states set (frozen, frozenAffected, and neither).

    """
    pass
    


def freezeOptions(displayLayers=bool, upstream="string", referencedNodes=bool, downstream="string", runtimePropagation=bool, explicitPropagation=bool, invisible=bool):
    """
    freezeOptions is NOT undoable, queryable, and NOT editable.
    

    
This command provides access to the options used by the evaluation manager to handle propagation and recognition of when a node is in a frozen state. See the individual flags for the different options available. These values are all stored as user preferences and persist across sessions.

    """
    pass
    


def geomBind(bindMethod=int, geodesicVoxelParams=int, falloff=float, maxInfluences=int):
    """
    geomBind is undoable, queryable, and editable.
    

    
This command is used to compute weights using the GeomBind lib.

    """
    pass
    


def geometryConstraint(targetobject, remove=bool, weightAliasList=bool, layer="string", targetList=bool, weight=float, name="string"):
    """
    geometryConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position based on the shape of the target surface(s) at the closest point(s) to the object.
A geometryConstraint takes as input one or more surface shapes (the targets) and a DAG transform node (the object). The geometryConstraint position constrained object such object lies on the surface of the target with the greatest weight value. If two targets have the same weight value then the one with the lowest index is chosen.

    """
    pass
    


def geomToBBox(combineMesh=bool, shaderColor=float, nameSuffix="string", single=bool, startTime=(), keepOriginal=bool, bakeAnimation=bool, sampleBy=(), endTime=(), name="string"):
    """
    geomToBBox is undoable, NOT queryable, and NOT editable.
    

    
Create polygonal mesh bounding boxes for geometry. Can also create a single bounding box per hierarchy.

    """
    pass
    


def getAttr(asString=bool, time=(), expandEnvironmentVariables=bool, multiIndices=bool, settable=bool, size=bool, lock=bool, type=bool, channelBox=bool, keyable=bool, silent=bool, caching=bool):
    """
    getAttr is undoable, NOT queryable, and NOT editable.
    

    
This command returns the value of the named object's attribute. UI units are used where applicable. Currently, the types of attributes that can be displayed are:
numeric attributes
string attributes
matrix attributes
numeric compound attributes (whose children are all numeric)
vector array attributes
double array attributes
int32 array attributes
point array attributes
data component list attributes
Other data types cannot be retrieved. No result is returned if the attribute contains no data.

    """
    pass
    


def getClassification(satisfies="string"):
    """
    getClassification is undoable, NOT queryable, and NOT editable.
    

    
Returns the classification string for a given node type.
Classification strings look like file pathnames ("shader/reflective" or "texture/2D", for example). Multiple classifications can be combined into a single compound classification string by joining the individual classifications with ':'. For example, the classification string "shader/reflective:texture/2D" means that the node is both a reflective shader and a 2D texture.
The classification string is used to determine how rendering nodes are categorized in various UI, such as the Create Render Node and HyperShade windows:
Category Classification String
2D Textures "texture/2d"
3D Textures "texture/3d"
Env Textures "texture/environment"
Surface Materials "shader/surface"
Volumetric Materials "shader/volume"
Displacement Materials "shader/displacement"
Lights "light"
General Utilities "utility/general"
Color Utilities "utility/color
Particle Utilities "utility/particle"
Image Planes "imageplane"
Glow "postprocess/opticalFX"
The classification string is also used to determine how Viewport 2.0 will interpret the node.
Category Classification String
Geometry "drawdb/geometry"
Transform "drawdb/geometry/transform"
Sub-Scene Object "drawdb/subscene"
Shader "drawdb/shader"
Surface Shader "drawdb/shader/surface"

    """
    pass
    


def getDefaultBrush():
    """
    getDefaultBrush is undoable, NOT queryable, and NOT editable.
    

    
The command returns the name of the default Paint Effects brush.

    """
    pass
    


def getFileList(filespec="string", folder="string"):
    """
    getFileList is undoable, NOT queryable, and NOT editable.
    

    
Returns a list of files matching an optional wildcard pattern. Note that this command works directly on raw system files and does not go through standard Maya file path resolution.

    """
    pass
    


def getFluidAttr(zIndex=int, yvalue=bool, lowerFace=bool, yIndex=int, xIndex=int, xvalue=bool, attribute="string", zvalue=bool):
    """
    getFluidAttr is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in the grid.

    """
    pass
    


def getInputDeviceRange(maxValue=bool, minValue=bool):
    """
    getInputDeviceRange is undoable, NOT queryable, and NOT editable.
    

    
This command lists the minimum and maximum values the device axis can return. This value is the raw device values before any mapping is applied. If you don't specify an axis the values for all axes of the device are returned.

    """
    pass
    


def getMetadata(streamName="string", listChannelNames=bool, memberName="string", scene=bool, endIndex="string", channelName="string", listStreamNames=bool, indexType="string", listMemberNames=bool, startIndex="string", channelType="string", index="string", dataType=bool):
    """
    getMetadata is NOT undoable, NOT queryable, and NOT editable.
    

    
This command is used to retrieve the values of metadata elements from a node or scene. It is restricted to returning a single structure member at a time. For convenience the detail required is only enough to find a single Member of a single Structure on a single metadata Channel.
In the simplest case if there is a single Stream on one metadata Channel which uses a Structure with only one Member then all that is required is the name of the object containing the metadata. In the most complex case the 'channelName', 'streamName', and 'memberName' are all required to narrow down the metadata to a single unique Member.
In general for scripting it's a good idea to use all flags anyway since there could be metadata added anywhere. The shortcuts are mainly for quick entry when entering commands directly in the script editor or command line.
When an Index is specified where data is not present the command fails with a message telling you which Index or Indices didn't have values. Use the hasMetadata command first to determine where metadata exists if you need to know in advance where to find valid metadata. Filter Flags
channelName - Only look for metadata on one particular Channel type
streamName - Only look for metadata on one particular named Stream. When used in conjunction with channelName then ignore Streams with a matching name but a different Channel type
index - Only look for metadata on one or more specific Index values of a Stream. Requires use of the streamName flag. Does not require the indexType flag as that will be inferred by the streamName.
startIndex/endIndex - Same as index but using an entire range of Index values rather than a single one. Not valid for index types not supporting ranges (e.g. strings)
indexType - Only look for metadata using a particular Index type. Can have its scope narrowed by other filter flags as well.
memberName - The particular Member in the metadata in a Structure to retrieve. If this is not specified the Structure can only have a single Member.
Metadata on meshes is special in that the Channel types "vertex", "edge", "face", and "vertexFace" are directly connected to the components of the same name. To make getting these metadata Channels easier you can simply select or specify on the command line the corresponding components rather than using the channelName and index/startIndex/endIndex flags. For example the selection "myMesh.vtx[8:10]" corresponds to channelName = vertex and either index = 8, 9, 10 as a multi-use flag or setIndex = 8, endIndex=10.
Only a single node or scene and unique metadata Structure Member are allowed in a single command. This keeps the data simple at the possible cost of requiring multiple calls to the command to get more than one Structure Member's value.
When the data is returned it will be in Index order with an entire Member appearing together. For example if you were retrieving float[3] metadata on three components you would get the nine values back in the order: index[0]-float[0], index[0]-float[1], index[0]-float[2], index[1]-float[0], index[1]-float[1], index[1]-float[2], index[2]-float[0], index[2]-float[1], index[2]-float[2]. In the Python implementation the float[3] values will be an array each so you would get back three float[3] arrays.

    """
    pass
    


def getModifiers():
    """
    getModifiers is undoable, NOT queryable, and NOT editable.
    

    
This command returns the current state of the modifier keys. The state of each modifier can be obtained by testing for the modifier's corresponding bit value in the return value. Shift is bit 1, Ctrl is bit 3, Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards and the Command key on Mac keyboards. See the provided example for more details on testing for each modifier's bit value.

    """
    pass
    


def getModulePath(moduleName="string"):
    """
    getModulePath is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns the module path for a given module name.

    """
    pass
    


def getPanel(containing="string", allTypes=bool, allPanels=bool, scriptType="string", withLabel="string", invisiblePanels=bool, typeOf="string", type="string", configWithLabel="string", atPosition=int, allConfigs=bool, allScriptedTypes=bool, withFocus=bool, visiblePanels=bool, underPointer=bool):
    """
    getPanel is undoable, NOT queryable, and NOT editable.
    

    
This command returns panel and panel configuration information.

    """
    pass
    


def getParticleAttr(object="string", array=bool, attribute="string"):
    """
    getParticleAttr is undoable, NOT queryable, and NOT editable.
    

    
This action will return either an array of values, or the average value and maximum offset, for a specied per-particle attribute of a particle object or component. If a particle component is specified on the command line, values are returned for that component only. If an object name is given instead, values are returned for all particles in that object. If no object name is passed, but a particle object or component is selected, values are returned for the selection.
If you list components, they must all be from the same particle object; the action ignores all objects after the first. Likewise if you list more than one object, the actiion will return values only for the first one.

    """
    pass
    


def getRenderDependencies():
    """
    getRenderDependencies is NOT undoable, NOT queryable, and NOT editable.
    

    
Command to return dependencies of an image source. Image sources (such as render targets) can depend on other upstream image sources that result from renderings of 3D scene, or renderings of 2D compositing graphs. This command returns these dependencies, so that they can be analyzed and rendered.

    """
    pass
    


def getRenderTasks(camera="string", renderLayer="string"):
    """
    getRenderTasks is NOT undoable, NOT queryable, and NOT editable.
    

    
Command to return render tasks to render an image source. Image source can depend on upstream image sources that result from renderings of 3D scene, or 2D renderings (e.g. render targets). This command obtains the graph of image source render dependencies, and creates render tasks according to these dependencies. A render task has context, which can be camera, render layer, and resolution, or other, renderer-specific context. Because of image source overrides, the render task context depends on the path through the render dependency graph, with the most upstream override for a context item applied. As there can be multiple paths through a render dependency graph to a render dependency, there can be multiple render tasks for a given render dependency.

    """
    pass
    


def globalStitch(stitchPartialEdges=bool, lockSurface=bool, stitchEdges=int, caching=bool, stitchCorners=int, modificationResistance=float, sampling=int, nodeState=int, stitchSmoothness=int, maxSeparation="string"):
    """
    globalStitch is undoable, queryable, and editable.
    

    
This command computes a globalStitch of NURBS surfaces. There should be at least one NURBS surface. The NURBS surface(s) should be untrimmed.

    """
    pass
    


def glRender(collisionIcons=bool, imageSize=int, accumBufferPasses=int, viewport=int, frameIncrement=int, imageName="string", alphaSource="string", frameEnd=int, writeDepthMap=bool, textureDisplay=bool, currentFrame=bool, sharpness=float, fullResolution=bool, imageDirectory="string", crossingEffect=bool, emitterIcons=bool, drawStyle="string", antiAliasMethod="string", grid=bool, transformIcons=bool, cameraIcons=bool, lightIcons=bool, offScreen=bool, shutterAngle=float, fieldIcons=bool, lightingMode="string", flipbookCallback="string", frameStart=int, renderFrame="string", renderSequence="string", edgeSmoothness=float, useAccumBuffer=bool, lineSmoothing=bool, clearClr=float):
    """
    glRender is undoable, queryable, and editable.
    

    
This command provides access to the Hardware Render Manager (HRM). There is one-and-only-one HRM in maya. The HRM controls the rendering performed in the hardware render buffer window. This command allows shell scripts, to modify the render state, and to initiate a render request.

    """
    pass
    


def glRenderEditor(panel="string", docTag="string", control=bool, mainListConnection="string", defineTemplate="string", parent="string", viewCameraName=bool, highlightConnection="string", useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", unParent=bool, stateString=bool, exists=bool, lookThru="string", updateMainConnection=bool, forceMainConnection="string", unlockMainConnection=bool):
    """
    glRenderEditor is undoable, queryable, and editable.
    

    
Create a glRender view. This is a special view used for hardware rendering. This command is used to create and reparent the view as needed to support panels. See the glRender command for controlling the specific behavior of the hardware rendering.

    """
    pass
    


def goal(useTransformAsGoal=bool, weight=float, goal="string", index=bool):
    """
    goal is undoable, queryable, and NOT editable.
    

    
Specifies the given objects as being goals for the given particle object. If the goal objects are geometry, each particle in the particle object will each try to follow or match its position to that of a certain vertex/CV/lattice point of the goal. If the goal object is another particle object, each particle will try to follow a paricle of the goal. In any other case, all the particles will try to follow the current location of the goal object's transform. You can get this latter behavior for a geometry or particle object too by using -utr true.
The goal weight can be keyframed. It lives on the particle object to which the goal was added and is a multi-attribute.

    """
    pass
    


def grabColor(hsvValue=bool, rgbValue=bool):
    """
    grabColor is undoable, NOT queryable, and NOT editable.
    

    
This command changes the cursor and enters a modal state which will be exited by pressing a mouse button. The color component values of the pixel below the cursor at the time of the button press are returned.

    """
    pass
    


def gradientControl(string, docTag="string", upperLimitControl="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", enable=bool, preventOverride=bool, selectedColorControl="string", numberOfControls=int, staticNumberOfControls=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, selectedInterpControl="string", selectedPositionControl="string", fullPathName=bool, attribute="string", dropCallback="string", exists=bool, dragCallback="string", staticPositions=bool, noBackground=bool, backgroundColor=float, refreshOnRelease=int, manage=bool, adaptiveScaling=bool, verticalLayout=bool, isObscured=bool):
    """
    gradientControl is undoable, queryable, and editable.
    

    
This command creates a control that displays the gradient attribute specified. The gradient attribute must be of the correct form and naming. It should be a multi attribute with each entry a compound composed of:
Either a color compound or a float value (the control will automatically detect which and display a ramp or graph accordingly).
A single float attribute for position.
An enum for the interpolation types.
Currently the routines to get the value of a ramp structure (with interpolation) are not available through MEL, which limits the use of this control by end users. The MEL command AEaddRampControl should be used to attach this control to an attribute from attribute editor templates.

    """
    pass
    


def gradientControlNoAttr(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, asString="string", dragCallback="string", highlightColor=float, annotation="string", enable=bool, currentKeyColorValue=float, popupMenuArray=bool, currentKey=int, currentKeyInterpValue=int, dragCommand="string", exists=bool, changeCommand="string", currentKeyCurveValue=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, preventOverride=bool, fullPathName=bool, dropCallback="string", valueAtPoint=float, rampAsColor=bool, noBackground=bool, backgroundColor=float, manage=bool, optionVar="string", currentKeyChanged="string", isObscured=bool):
    """
    gradientControlNoAttr is undoable, queryable, and editable.
    

    
This command creates a control for editing a ramp (2D control curve). The control attaches to an optionVar used to store and retrieve the encoded gradient control points stored in a string.

    """
    pass
    


def graphDollyCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    graphDollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create a dolly context for the graph editor.

    """
    pass
    


def graphSelectContext(exists=bool, image1="string", image2="string", image3="string"):
    """
    graphSelectContext is undoable, queryable, and editable.
    

    
This command can be used to create a selection context for the hypergraph editor.

    """
    pass
    


def graphTrackCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    graphTrackCtx is undoable, queryable, and editable.
    

    
This command can be used to create a track context for the graph editor.

    """
    pass
    


def gravity(objects, directionX=float, magnitude=float, directionY=float, perVertex=bool, directionZ=float, attenuation=float, maxDistance="string", position="string", name="string"):
    """
    gravity is undoable, queryable, and editable.
    

    
A gravity field simulates the Earth's gravitational force. It pulls objects in a fixed direction (generally downward) entirely independent of their position or mass.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.
The default for -dx -dy -dz is always the opposite of the current up direction. For example, if the current up direction is (0,1,0) (a standard Maya configuration), then the gravity default is -dx 0 -dy -1 -dz 0. The default for -a is 9.8. 9.8 meters per second squared happens to be standard Earth gravity, but in fact Maya interprets this value as centimeters per second squared. If we were to use it as meters per second squared then with default Maya units, your particles would vanish almost in the wink of an eye. If you want a different value, set it in the gravity option box.

    """
    pass
    


def greasePencilCtx():
    """
    greasePencilCtx is undoable, queryable, and editable.
    

    
This is a tool context command for the grease pencil tool.

    """
    pass
    


def grid(perspectiveLabelPosition="string", reset=bool, orthographicLabelPosition="string", displayAxes=bool, displayDivisionLines=bool, default=bool, style=int, spacing="string", displayOrthographicLabels=bool, divisions=int, displayAxesBold=bool, displayPerspectiveLabels=bool, size="string", toggle=bool, displayGridLines=bool):
    """
    grid is undoable, queryable, and NOT editable.
    

    
This command changes the size and spacing of lines on the ground plane displayed in the perspective and orthographic views.
This command lets you reset the ground plane, change its size and grid line spacing, grid subdivisions and display options.

    """
    pass
    


def gridLayout(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfRows=int, numberOfPopupMenus=bool, useTemplate="string", manage=bool, dragCallback="string", numberOfChildren=bool, highlightColor=float, annotation="string", enable=bool, cellWidthHeight=int, preventOverride=bool, allowEmptyCells=bool, gridOrder=bool, childArray=bool, cellHeight=int, exists=bool, numberOfColumns=int, numberOfRowsColumns=int, enableBackground=bool, autoGrow=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", popupMenuArray=bool, noBackground=bool, backgroundColor=float, cellWidth=int, position="string", width=int, columnsResizable=bool, isObscured=bool):
    """
    gridLayout is undoable, queryable, and editable.
    

    
This layout arranges children in a grid fashion where every cell in the grid is the same size. You may specify the number of rows and columns as well as the width and height of the grid cells.

    """
    pass
    


def group(objects, parent="string", empty=bool, world=bool, relative=bool, absolute=bool, name="string", useAsGroup="string"):
    """
    group is undoable, NOT queryable, and NOT editable.
    

    
This command groups the specified objects under a new group and returns the name of the new group.
If the -em flag is specified, then an empty group (with no objects) is created.
If the -w flag is specified then the new group is placed under the world, otherwise if -p is specified it is placed under the specified node. If neither -w or -p is specified the new group is placed under the lowest common group they have in common. (or the world if no such group exists)
If an object is grouped with another object that has the same name then one of the objects will be renamed by this command.

    """
    pass
    


def hardenPointCurve(object=bool, nodeState=int, replaceOriginal=bool, name="string", caching=bool, multiplicity=int, constructionHistory=bool):
    """
    hardenPointCurve is undoable, queryable, and editable.
    

    
The hardenPointCurve command changes the knots of a curve given a list of control point indices so that the knot corresponding to that control point gets the specified multiplicity. Multiplicity of -1 is the universal value used for multiplicity equal to the degree of the curve.
limitations
The CV whose multiplicity is being raised needs to have its neighbouring CVs of multiplicity 1. How many neighbours depends on the degree of the curve and the difference in CV multiplicities before and after this operation. For example, if you're changing a CV of multiplicity 1 into a CV of multiplicity 3, you will need the 4 neighbouring CVs (2 on each side) to be of multiplicity 1. The CVs that do not satisfy that requirement will be ignored.

    """
    pass
    


def hardware(graphicsType=bool, numProcessors=bool, cpuType=bool, megaHertz=bool, brdType=bool):
    """
    hardware is undoable, NOT queryable, and NOT editable.
    

    
Return description of the hardware available in the machine.

    """
    pass
    


def hardwareRenderPanel(tearOff=bool, docTag="string", defineTemplate="string", parent="string", useTemplate="string", label="string", replacePanel="string", unParent=bool, tearOffCopy="string", camera="string", isUnique=bool, createString=bool, needsInit=bool, exists=bool, control=bool, glRenderEditor=bool, menuBarVisible=bool, init=bool, tearOffRestore=bool, popupMenuProcedure="string", editString=bool, copy="string"):
    """
    hardwareRenderPanel is undoable, queryable, and editable.
    

    
This command creates, edit and queries hardware render panels which contain only a hardware render editor.

    """
    pass
    


def hasMetadata(streamName="string", memberName="string", scene=bool, channelName="string", endIndex="string", ignoreDefault=bool, indexType="string", asList=bool, startIndex="string", channelType="string", index="string"):
    """
    hasMetadata is NOT undoable, NOT queryable, and NOT editable.
    

    
This command is used to query for the presence of metadata elements on a node, components, or scene. The command works at all levels of metadata presence, from the existence of any metadata at all on a node or scene right down to the presence of metadata values set on a particular metadata Stream index. Filter Flags
channelName - Only look for metadata on one particular Channel type
streamName - Only look for metadata on one particular named Stream. When used in conjunction with channelName then ignore Streams with a matching name but a different Channel type
index - Only look for metadata on one or more specific Index values of a Stream. Requires use of the streamName flag. Does not require the indexType flag as that will be inferred by the streamName.
startIndex/endIndex - Same as index but using an entire range of Index values rather than a single one
indexType - Only look for metadata using a particular Index type. Can have its scope narrowed by other filter flags as well.
ignoreDefault - Treat any metadata that still has the default value (e.g. 0 for numerics, "" for strings) the same as metadata that isn't present. This means that any metadata with default values will not be reported. It is useful for quickly finding values that you have changed. When this flag is set you can also use the memberName filter to narrow down the check to a particular member of the metadata Structure. Without that filter it will only skip over metadata where every member of the Structure has a non-default value.
memberName - Only look at one particular Member in the metadata in a Structure. Only used when checking for non-default values as existence is based on the entire Structure, not any particular Member.
Operation Flags
normal mode - Return True for every specified location containing metadata. This combines with the filter flags as follows:
no flag - True if there is any metadata at all on the node or scene
channelName - True if there is any metadata at all on the Channel with the given name
streamName - True if there is any metadata at all on the Stream with the given name
index/startIndex/endIndex - An array of booleans ordered the same as the natural ordering of the Index values (i.e. specifying index 3, 2, and 4 in that order will still return booleans in the order for indices 2,3,4) where True means that there is metadata assigned at that Index. This form is better suited with the asList modification since with that variation it is easier to tell exactly which indices have the metadata.
asList - Adding this flag switches the return values from a single boolean or array of booleans to an array of strings indicating exactly which metadata elements have values. The return values of the command are changed to be the following:
no flag - List of Channel names with metadata
channelName - List of Stream names in the Channel with metadata
streamName - List of Index values on the Stream with metadata
index/startIndex/endIndex - List of Index values with metadata, restricted to the set of specified Index values.

    """
    pass
    


def headsUpDisplay(string, labelFontSize="string", allowOverlap=bool, nodeChanges="string", conditionTrue="string", listPresets=bool, event="string", label="string", dataWidth=int, dataAlignment="string", refresh=bool, gridColor=int, padding=int, showGrid=bool, listEvents=bool, labelWidth=int, listHeadsUpDisplays=bool, lastOccupiedBlock=int, attributeChange="string", exists=bool, name="string", removeID=int, preset="string", connectionChange="string", allDescendants=bool, conditionFalse="string", listNodeChanges=bool, visible=bool, listConditions=bool, blockAlignment="string", disregardIndex=bool, dataFontSize="string", setOption="string", section=int, nextFreeBlock=int, blockSize="string", scriptResult=bool, remove=bool, decimalPrecision=int, block=int, resetNodeChanges="string", command="string", attachToRefresh=bool, removePosition=int, conditionChange="string", layoutVisibility=bool, getOption="string"):
    """
    headsUpDisplay is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) object which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on information designated by a user script. The text string displayed on the viewport is formatted using the various flags of this command.
The only mandatory flags, on creation are the section and block flags. Note if the preset OR command/trigger flags are not present, only a label will be drawn on the viewport.
Upon creation of a HUD object, an ID number will be assigned to it. This can be used to remove the HUD object (-rid/removeID [int IDNumber]), if desired. Alternatively, HUD objects may be removed via their position (section and block), or their unique name.

    """
    pass
    


def headsUpMessage(messagestring, time=float, horizontalOffset=int, object="string", verticalOffset=int, selection=bool):
    """
    headsUpMessage is undoable, NOT queryable, and NOT editable.
    

    
This command draws a message in the 3d view. The message is automatically erased at the next screen refresh.

    """
    pass
    


def help(string, list=bool, popupMode=bool, language="string", popupSimpleMode=bool, rolloverMode=bool, popupPauseTime=int, syntaxOnly=bool, popupDisplayTime=int, documentation=bool):
    """
    help is undoable, queryable, and NOT editable.
    

    
With no arguments, help tells how to use help. If a command name is specified, help will return the quick help for that command. Other flags can be used to open the online documentation, or to list available commands based on a pattern.
Pattern follows the following syntax:
*            matches any string
?            matches any character
[agj]        matches a, g or j
[^0-9]       matches anything but a digit
x+           matches any number of subsequent x
a{3}         matches aaa
a{3,}        matches aaa, aaaa, ...
a{3,5}       matches aaa, aaaa, or aaaaa

    """
    pass
    


def helpLine(name, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", backgroundColor=float, noBackground=bool, manage=bool, isObscured=bool):
    """
    helpLine is undoable, queryable, and editable.
    

    
This command creates a help line where tool help/hints are shown.

    """
    pass
    


def hide(objects, allObjects=bool, returnHidden=bool, invertComponents=bool, clearSelection=bool, testVisibility=bool):
    """
    hide is undoable, NOT queryable, and NOT editable.
    

    
The hide command is used to make objects invisible. If no flags are used, the objects specified, or the active objects if none are specified, will be made invisible.

    """
    pass
    


def hikGlobals(releaseAllPinning=bool):
    """
    hikGlobals is undoable, queryable, and editable.
    

    
Sets global HumanIK flags for the application.

    """
    pass
    


def hilite(objects, unHilite=bool, replace=bool, toggle=bool):
    """
    hilite is undoable, NOT queryable, and NOT editable.
    

    
Hilites/Unhilites the specified object(s). Hiliting an object makes it possible to select the components of the object. If no objects are specified then the selection list is used.

    """
    pass
    


def hitTest():
    """
    hitTest is NOT undoable, NOT queryable, and NOT editable.
    

    
The hitTest command hit-tests a point in the named control and returns a list of items underneath the point. The point is specified in pixels with the origin (0,0) at the top-left corner. This position is compatible with the coordinates provided by a drop-callback. The types of items that may be returned depends upon the specific control; not all controls currently support hit-testing.

    """
    pass
    


def hotBox(polygonsOnlyMenus=bool, noClickCommand="string", liveOnlyMenus=bool, modelingToggleMenus=bool, PaneToggleMenus=bool, clothOnlyMenus=bool, riggingToggleMenus=bool, showAllToggleMenus=bool, updateMenus=bool, clothToggleMenus=bool, surfacesToggleMenus=bool, displayStyle=bool, displayHotbox=bool, dynamicsOnlyMenus=bool, position=int, renderingToggleMenus=bool, displayZonesOnly=bool, surfacesOnlyMenus=bool, animationToggleMenus=bool, release=bool, noClickPosition=bool, displayCenterOnly=bool, noClickDelay=float, renderingOnlyMenus=bool, liveToggleMenus=bool, commonToggleMenus=bool, animationOnlyMenus=bool, dynamicsToggleMenus=bool, modelingOnlyMenus=bool, noKeyPress=bool, PaneOnlyMenus=bool, commonOnlyMenus=bool, rmbPopups=bool, polygonsToggleMenus=bool, customMenuSetsToggleMenus=bool, transparenyLevel=int, riggingOnlyMenus=bool):
    """
    hotBox is undoable, queryable, and NOT editable.
    

    
This command controls parameters related to the hotBox menubar palette. When the command is invoked with no flags, the hotBox is popped up.

    """
    pass
    


def hotkey(keyShortcut="string", ctxClient="string", sourceUserHotkeys=bool, commandModifier=bool, releaseName="string", isModifier=bool, pressCommandRepeat=bool, altModifier=bool, releaseCommandRepeat=bool, shiftModifier=bool, name="string", dragPress=bool, ctrlModifier=bool, autoSave=bool, factorySettings=bool):
    """
    hotkey is undoable, queryable, and NOT editable.
    

    
This command sets the single-key hotkeys for the entire application.

    """
    pass
    


def hotkeyCheck(keyUp=bool, commandModifier=bool, altModifier=bool, keyString="string", ctrlModifier=bool, optionModifier=bool):
    """
    hotkeyCheck is undoable, NOT queryable, and NOT editable.
    

    
This command checks if the given hotkey is mapped to a nameCommand object. If so, the annotation of the nameCommand object is returned. Otherwise an empty string is returned.

    """
    pass
    


def hotkeyCtx(removeType="string", clientArray=bool, type="string", removeClient="string", typeExists="string", removeAllClients=bool, typeArray=bool, currentClient="string", insertTypeAt="string", addClient="string"):
    """
    hotkeyCtx is undoable, queryable, and NOT editable.
    

    
This command sets the hotkey context for the entire application.

    """
    pass
    


def hotkeyEditorPanel(name, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", backgroundColor=float, noBackground=bool, manage=bool, isObscured=bool):
    """
    hotkeyEditorPanel is undoable, queryable, and editable.
    

    
A hotkeyEditor creates a new hotkey editor in the current layout. The hotkey editor lets you assign predefined commands, MEL scripts, or marking menus to keys and key combinations.

    """
    pass
    


def hotkeySet(name, delete=bool, source="string", export="string", rename="string", ip="string", current=bool, hotkeySetArray=bool, exists=bool):
    """
    hotkeySet is undoable, queryable, and editable.
    

    
Manages hotkey sets in Maya. A hotkey set holds hotkey to command mapping information. Default hotkey sets are hotkey sets that are shipped together with Maya. They are locked and cannot be altered.
A new hotkey set is always duplicated from an existing hotkey set. In create mode, users can choose to specify which hotkey set to duplicate by using the -source flag. A duplicated hotkey set is independent from the source hotkey set.

    """
    pass
    


def hudButton(string, labelFontSize="string", allowOverlap=bool, buttonShape="string", block=int, pressCommand="string", visible=bool, blockAlignment="string", section=int, releaseCommand="string", label="string", buttonWidth=int, padding=int, blockSize="string"):
    """
    hudButton is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) button control which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on interaction designated by a user script. The HUD button is derived from a generic HUD object and thus inherits a similar workflow.
Although this command provides much of the same functionality as the headsUpDisplay command, it does not provide headsUpDisplay layout controls such as layoutVisibility, nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality, please use the headsUpDisplay command. This command is focused solely around the creation and management of HUD button controls. Similarly, all operations performed by this command are limited to HUDs that are button controls.
The only mandatory flags, on creation are the section and block flags.
Like the headsUpDisplay command, upon creation of a HUD button, an ID number will be assigned to it. This can be used to remove the HUD via the headsUpDisplay command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay command can remove HUD objects via their position (section and block), or their unique name.

    """
    pass
    


def hudSlider(string, labelFontSize="string", allowOverlap=bool, pressCommand="string", valueWidth=int, section=int, label="string", internalPadding=int, labelWidth=int, type="string", sliderLength=int, dragCommand="string", padding=int, value=float, sliderIncrement=float, visible=bool, valueFontSize="string", blockAlignment="string", releaseCommand="string", decimalPrecision=int, block=int, minValue=float, maxValue=float, blockSize="string", valueAlignment="string"):
    """
    hudSlider is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) slider control which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on interaction designated by a user script. The HUD slider is derived from a generic HUD object and thus inherits a similar workflow.
Although this command provides much of the same functionality as the headsUpDisplay command, it does not provide headsUpDisplay layout controls such as layoutVisibility, nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality, please use the headsUpDisplay command. This command is focused solely around the creation and management of HUD sliders. Similarly, all operations performed by this command are limited to HUDs that are sliders.
The only mandatory flags, on creation are the section and block flags.
Like the headsUpDisplay command, upon creation of a HUD slider, an ID number will be assigned to it. This can be used to remove the HUD slider via the headsUpDisplay command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay command can remove HUD objects via their position (section and block), or their unique name.

    """
    pass
    


def hudSliderButton(string, allowOverlap=bool, buttonLabel="string", buttonPressCommand="string", buttonLabelFontSize="string", buttonWidth=int, internalPadding=int, type="string", sliderLabel="string", sliderDragCommand="string", sliderLength=int, valueWidth=int, padding=int, value=float, buttonReleaseCommand="string", sliderLabelFontSize="string", sliderIncrement=float, sliderLabelWidth=int, sliderReleaseCommand="string", visible=bool, valueFontSize="string", blockAlignment="string", sliderPressCommand="string", section=int, decimalPrecision=int, buttonShape="string", block=int, minValue=float, maxValue=float, blockSize="string", valueAlignment="string"):
    """
    hudSliderButton is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) slider button control which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on interaction designated by a user script. The HUD slider button control is derived from a generic HUD object and thus inherits a similar workflow.
Although this command provides much of the same functionality as the headsUpDisplay command, it does not provide headsUpDisplay layout controls such as layoutVisibility, nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality, please use the headsUpDisplay command. This command is focused solely around the creation and management of HUD slider button controls. Similarly, all operations performed by this command are limited to HUDs that are slider button controls.
The only mandatory flags, on creation are the section and block flags.
Like the headsUpDisplay command, upon creation of a HUD slider button, an ID number will be assigned to it. This can be used to remove the HUD slider via the headsUpDisplay command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay command can remove HUD objects via their position (section and block), or their unique name.

    """
    pass
    


def hwReflectionMap(backTextureName="string", enable=bool, bottomTextureName="string", topTextureName="string", rightTextureName="string", frontTextureName="string", cubeMap=bool, decalMode=bool, leftTextureName="string", sphereMapTextureName="string"):
    """
    hwReflectionMap is undoable, queryable, and editable.
    

    
This command creates a hwReflectionMap node for having reflection on textured surfaces that currently have their boolean attribute displayHWEnvironment set to true.

    """
    pass
    


def hwRender(height=int, renderSelected=bool, imageFileName=bool, textureResolution=int, activeTextureCount=bool, camera="string", limitedRenderSupport=bool, currentFrame=bool, lowQualityLighting=bool, edgeAntiAliasing=int, writeDepth=bool, layer="string", frame=float, renderHardwareName=bool, fixFileNameNumberPattern=bool, renderRegion=int, noRenderView=bool, fullRenderSupport=bool, width=int, writeAlpha=bool, currentView=bool, printGeometry=bool, acceleratedMultiSampleSupport=bool, notWriteToFile=bool):
    """
    hwRender is NOT undoable, queryable, and NOT editable.
    

    
Renders an image or a sequence using the hardware rendering engine

    """
    pass
    


def hwRenderLoad():
    """
    hwRenderLoad is NOT undoable, NOT queryable, and NOT editable.
    

    
Empty command used to force the dynamic load of HR render

    """
    pass
    


def hyperGraph(string, docTag="string", look=float, opaqueContainers=bool, imagePosition=float, showRelationships=bool, useTemplate="string", addBookmark=bool, nodePressCommand="string", previousView=bool, attributeEditor="string", downstream=bool, panel="string", deleteBookmark="string", dropNode="string", dependNode="string", frame=bool, layout=bool, dependGraph=bool, unlockMainConnection=bool, transitionFrames=int, showInvisible=bool, frameBranch=bool, frameGraph=bool, forceMainConnection="string", range=float, enableAutomaticLayout=bool, graphLayoutStyle="string", showConnectionFromSelected=bool, restoreBookmark="string", showConnectionToSelected=bool, showDeformers=bool, fitImageToWidth=bool, defineTemplate="string", parent="string", rebuild=bool, dropTargetNode="string", mergeConnections=bool, iconSize="string", feedbackGadget="string", collapseContainer=bool, getNodePosition="string", stateString=bool, unfoldAll=bool, unfold=bool, control=bool, addDependNode="string", selectionConnection="string", imageEnabled=bool, showUnderworld=bool, animateTransition=bool, mainListConnection="string", imageForContainer=bool, navigateHome=bool, layoutSelected="string", showConstraints=bool, scrollUpDownNoZoom=bool, expandContainer=bool, image="string", popupMenuScript="string", dragAndDropBehaviorCommand="string", lockMainConnection=bool, showExpressions=bool, graphType="string", focusCommand="string", nodeDropCommand="string", updateMainConnection=bool, isHotkeyTarget=bool, resetFreeform=bool, getNodeList=bool, fromAttr="string", edgeDimmedDblClickCommand="string", clear=bool, viewOption="string", bookmarkName=bool, showShapes=bool, edgeDblClickCommand="string", down=bool, unParent=bool, connectionDrawStyle="string", freeform=bool, filterDetail="string", fold=bool, upstream=bool, zoom=float, highlightConnection="string", visibility=bool, exists=bool, rename=bool, useFeedbackList=bool, nextView=bool, fitImageToHeight=bool, removeNode="string", feedbackNode="string", updateSelection=bool, imageScale=float, addDependGraph="string", updateNodeAdded=bool, frameHierarchy=bool, nodeReleaseCommand="string", setNodePosition="string", forceRefresh=bool, filter="string", orientation="string"):
    """
    hyperGraph is undoable, queryable, and editable.
    

    
The following is an overview of the basic features of the hypergraph. A more detailed description is given in the user manuals.
The hypergraph provides the user with the ability to view and edit the maya scene graph. The hypergraph supports two types of graphs: the DAG or scene hierarchy and the dependency graph.
The default view of the hypergraph editor is the DAG view. The user can show the dependency graph for a collection of nodes by first selecting the nodes and navigating to the dependency graph using one of the graph options. The user can save any view by setting a bookmark to that view. The user can also show previous views using the view options provided.
The hypergraph supports a simple editing mechanism for editing hierarchy in the DAG view and connections in dependency graph view. In the DAG view, the user can reparent or reorder nodes in the graph using drag-and-drop. In the dependency graph view, the user can select connections and delete them or make new connections by dragging and dropping nodes or existing connections.
The hypergraph supports two layout modes in the DAG view: automatic and freeform. In automatic mode, the graph nodes are automatically positioned according to the layout preferences. In freeform mode, the user can position nodes manually. The node position is saved in the scene. A background image can be placed behind DG or DAG in freeform mode. This can be used as a template for positioning nodes in a user-defined layout.
Nodes in the DAG view can be expanded or collapsed. The state is saved in the scene. The performance of the graph drawing will increase as hierarchies are collapsed.
In addition to hierachy relationships, the hypergraph can show expression, constraint and deformation relationships in the DAG. These can be enabled/disabled through the options provided. There are also additional filters for showing shape nodes and invisible nodes. The amount of detail show may affect the speed of the display of the graph.
Most of the UI features of the hypergraph are addressable through the hypergraph command-line interface. The available command-line options are described in the next section.

    """
    pass
    


def hyperPanel(panelName, tearOff=bool, docTag="string", parent="string", useTemplate="string", label="string", replacePanel="string", unParent=bool, tearOffCopy="string", isUnique=bool, defineTemplate="string", createString=bool, needsInit=bool, exists=bool, control=bool, menuBarVisible=bool, init=bool, hyperEditor=bool, tearOffRestore=bool, popupMenuProcedure="string", editString=bool, copy="string"):
    """
    hyperPanel is undoable, queryable, and editable.
    

    
This command creates, edit and queries hypergraph panels which contain only a hypergraph editor.

    """
    pass
    


def hyperShade(listDownstreamShaderNodes="string", assign="string", incremental=bool, networks=bool, objects="string", listDownstreamNodes="string", renderCreateAndDrop="string", listUpstreamNodes="string", workAreaSelectCmd="string", workAreaDeleteCmd="string", fixRenderSize=bool, setWorkArea="string", setAllowsRegraphing=bool, clearWorkArea=bool, downStream=bool, name="string", noSGShapes=bool, resetSwatch=bool, dependGraphArea=bool, resetGraph=bool, uncollapse="string", shaderNetworks=bool, userDefinedLayout=bool, workAreaAddCmd="string", createNode="string", reset=bool, shaderNetworksSelectMaterialNodes=bool, snapShot=bool, duplicate=bool, upStream=bool, collapse="string", noShapes=bool, noTransforms=bool, shaderNetwork="string"):
    """
    hyperShade is undoable, NOT queryable, and NOT editable.
    

    
Commands for shader editing in the hypergraph

    """
    pass
    


def iconTextButton(string, docTag="string", highlightImage="string", height=int, useAlpha=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", highlightColor=float, image3="string", dragCallback="string", imageOverlayLabel="string", overlayLabelBackColor=float, disabledImage="string", annotation="string", enable=bool, scaleIcon=bool, image1="string", popupMenuArray=bool, handleNodeDropCallback="string", labelOffset=int, flipX=bool, font="string", exists=bool, rotation=float, flipY=bool, marginHeight=int, ltVersion="string", doubleClickCommand="string", commandRepeatable=bool, visibleChangeCommand="string", visible=bool, labelEditingCallback="string", marginWidth=int, sourceType="string", preventOverride=bool, fullPathName=bool, dropCallback="string", noBackground=bool, selectionImage="string", backgroundColor=float, enableBackground=bool, align="string", manage=bool, command="string", flat=bool, style="string", version="string", image2="string", isObscured=bool, overlayLabelColor=float):
    """
    iconTextButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextButton that can be displayed with different icons, with or without accompanying text label. When an argument is passed, it is used to give a name to the iconTextButton.

    """
    pass
    


def iconTextCheckBox(string, docTag="string", highlightImage="string", height=int, onCommand="string", useAlpha=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", image3="string", highlightColor=float, imageOverlayLabel="string", overlayLabelBackColor=float, disabledImage="string", annotation="string", enable=bool, offCommand="string", image1="string", popupMenuArray=bool, flat=bool, labelOffset=int, flipX=bool, selectionHighlightImage="string", font="string", exists=bool, changeCommand="string", rotation=float, flipY=bool, marginHeight=int, ltVersion="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, marginWidth=int, preventOverride=bool, fullPathName=bool, dropCallback="string", value=bool, noBackground=bool, selectionImage="string", backgroundColor=float, align="string", manage=bool, style="string", version="string", image2="string", isObscured=bool, overlayLabelColor=float):
    """
    iconTextCheckBox is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextCheckBox.

    """
    pass
    


def iconTextRadioButton(docTag="string", highlightImage="string", height=int, onCommand="string", useAlpha=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", select=bool, image3="string", highlightColor=float, imageOverlayLabel="string", overlayLabelBackColor=float, disabledImage="string", annotation="string", changeCommand="string", offCommand="string", image1="string", popupMenuArray=bool, enableBackground=bool, labelOffset=int, flipX=bool, selectionHighlightImage="string", font="string", exists=bool, rotation=float, flipY=bool, marginHeight=int, enable=bool, ltVersion="string", collection="string", visibleChangeCommand="string", visible=bool, marginWidth=int, preventOverride=bool, fullPathName=bool, dropCallback="string", noBackground=bool, selectionImage="string", backgroundColor=float, align="string", manage=bool, flat=bool, style="string", version="string", image2="string", isObscured=bool, overlayLabelColor=float):
    """
    iconTextRadioButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates a iconTextRadioButton that is added to the most recently created iconTextRadioCollection unless the -cl/cluster flag is used.

    """
    pass
    


def iconTextRadioCollection(string, numberOfCollectionItems=bool, defineTemplate="string", parent="string", gl=bool, select="string", collectionItemArray=bool, disableCommands=bool, exists=bool, useTemplate="string"):
    """
    iconTextRadioCollection is undoable, queryable, and editable.
    

    
This command creates a cluster for iconTextRadioButtons. Clusters will be parented to the current default layout if no parent is specified with the -p/parent flag. As children of the layout they will be deleted when the layout is deleted. Clusters may also span more than one window if the -g/global flag is used. In this case the cluster has no parent so must be explicitly deleted with the 'deleteUI' command.

    """
    pass
    


def iconTextScrollList(string, allowMultiSelection=bool, height=int, defineTemplate="string", docTag="string", numberOfRows=bool, numberOfPopupMenus=bool, useTemplate="string", append="string", dragCallback="string", deselectAll=bool, selectItem="string", highlightColor=float, parent="string", annotation="string", preventOverride=bool, popupMenuArray=bool, dropRectCallback="string", enableBackground=bool, exists=bool, enable=bool, doubleClickCommand="string", visibleChangeCommand="string", visible=bool, itemTextColor=int, selectIndexedItem=int, fullPathName=bool, dropCallback="string", visualRectAt=int, selectCommand="string", itemAt=int, noBackground=bool, removeAll=bool, backgroundColor=float, manage=bool, width=int, isObscured=bool):
    """
    iconTextScrollList is undoable, queryable, and editable.
    

    
This command creates/edits/queries a text scrolling list. The list can be in single select mode where only one item at at time is selected, or in multi-select mode where many items may be selected.

    """
    pass
    


def iconTextStaticLabel(docTag="string", height=int, useAlpha=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", image3="string", highlightColor=float, imageOverlayLabel="string", overlayLabelBackColor=float, disabledImage="string", annotation="string", image1="string", popupMenuArray=bool, labelOffset=int, flipX=bool, font="string", exists=bool, rotation=float, flipY=bool, marginHeight=int, enable=bool, ltVersion="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, marginWidth=int, preventOverride=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, align="string", manage=bool, style="string", version="string", image2="string", isObscured=bool, overlayLabelColor=float):
    """
    iconTextStaticLabel is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextStaticLabel.

    """
    pass
    


def ikfkDisplayMethod(display="string"):
    """
    ikfkDisplayMethod is NOT undoable, queryable, and NOT editable.
    

    
The ikfkDisplayMethod command is used to specify how ik/fk blending should be shown

    """
    pass
    


def ikHandle(createRootAxis=bool, autoPriority=bool, positionWeight=float, disableHandles=bool, startJoint="string", curve="string", weight=float, freezeJoints=bool, endEffector="string", enableHandles=bool, parentCurve=bool, numSpans=int, snapCurve=bool, sticky="string", solver="string", name="string", rootTwistMode=bool, exists="string", jointList=bool, simplifyCurve=bool, setupForRPsolver=bool, snapHandleToEffector=bool, forceSolver=bool, rootOnCurve=bool, snapHandleFlagToggle=bool, connectEffector=bool, priority=int, createCurve=bool, twistType="string"):
    """
    ikHandle is undoable, queryable, and editable.
    

    
The handle command is used to create, edit, and query a handle within Maya. The standard edit (-e) and query (-q) flags are used for edit and query functions.
If there are 2 joints selected and neither -startJoint nor -endEffector flags are not specified, then the handle will be created from the selected joints.
If a single joint is selected and neither -startJoint nor -endEffector flags are specified, then the handle will be created with the selected joint as the end-effector and the start joint will be the top of the joint chain containing the end effector.
The default values of the flags are:
-name "ikHandle#"
-priority 1
-weight 1.0
-positionWeight 1.0
-solver "ikRPsolver"
-forceSolver on
-snapHandleFlagToggle on
-sticky off
-createCurve true
-simplifyCurve true
-rootOnCurve true
-twistType linear
-createRootAxis false
-parentCurve true
-snapCurve false
-numSpans 1
-rootTwistMode false.
These attributes can be specified in creation mode, edited in edit mode (-e) or queried in query mode (-q).

    """
    pass
    


def ikHandleCtx(createRootAxis=bool, forceSolverH=bool, stickyH="string", solverTypeH="string", image1="string", parentCurve=bool, numSpans=int, snapCurve=bool, exists=bool, name="string", rootTwistMode=bool, weightH=float, priorityH=int, simplifyCurve=bool, image3="string", autoPriorityH=bool, snapHandleH=bool, rootOnCurve=bool, history=bool, image2="string", poWeightH=float, createCurve=bool, twistType="string"):
    """
    ikHandleCtx is undoable, queryable, and editable.
    

    
The ikHandle context command (ikHandleCtx) updates parameters of ikHandle tool. The options for the tool will be set to the flags that the user specifies.

    """
    pass
    


def ikHandleDisplayScale():
    """
    ikHandleDisplayScale is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current display size of ikHandle. The default display scale is 1.0.

    """
    pass
    


def ikSolver(object, solverType="string", epsilon=float, name="string", maxIterations=int):
    """
    ikSolver is undoable, queryable, and editable.
    

    
The ikSolver command is used to set the attributes for an IK Solver or create a new one. The standard edit (-e) and query (-q) flags are used for edit and query functions.

    """
    pass
    


def ikSplineHandleCtx(createRootAxis=bool, forceSolverH=bool, stickyH="string", solverTypeH="string", image1="string", parentCurve=bool, numSpans=int, snapCurve=bool, exists=bool, name="string", rootTwistMode=bool, weightH=float, priorityH=int, simplifyCurve=bool, image3="string", autoPriorityH=bool, snapHandleH=bool, rootOnCurve=bool, history=bool, image2="string", poWeightH=float, createCurve=bool, twistType="string"):
    """
    ikSplineHandleCtx is undoable, queryable, and editable.
    

    
The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of ikSplineHandle tool. The options for the tool will be set to the flags the user specifies.

    """
    pass
    


def ikSystem(object, list=int, snap=bool, autoPriorityMC=bool, autoPriority=bool, solve=bool, allowRotation=bool, solverTypes=bool, autoPrioritySC=bool):
    """
    ikSystem is undoable, queryable, and editable.
    

    
The ikSystem command is used to set the global snapping flag for handles and set the global solve flag for solvers. The standard edit (-e) and query (-q) flags are used for edit and query functions.

    """
    pass
    


def ikSystemInfo(globalSnapHandle=bool):
    """
    ikSystemInfo is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current ikSystem controls.

    """
    pass
    


def illustratorCurves(string, illustratorFilename="string", scaleFactor=float, object=bool, name="string", constructionHistory=bool):
    """
    illustratorCurves is undoable, queryable, and editable.
    

    
The illustratorCurves command creates NURBS curves from an input Adobe(R) Illustrator(R) file.

    """
    pass
    


def image(imageName, docTag="string", height=int, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    image is undoable, queryable, and editable.
    

    
This command creates a static image for non-xpm files. Any image file format supported by the file texture node is supported by this command.

    """
    pass
    


def imagePlane(camera="string", imageSize=int, timeCodeTrack=bool, lookThrough="string", negTimesOK=bool, quickTime=bool, width=float, numFrames=int, height=float, fileName="string", dropFrame=bool, frameDuration=int, showInAllViews=bool, timeCode=int, timeScale=int, twentyFourHourMax=bool, counter=bool, maintainRatio=bool, detach=bool, name="string"):
    """
    imagePlane is undoable, queryable, and editable.
    

    
The imagePlane command allows querying of various properties of an image plane and any movie in use by the image plane. It also supports creating and edit. The object passed to the command may either be an imagePlane node, or a camera, in which case the command uses the image plane attached to the camera (if any). If no object is passed in, the current selection is used. Currently, most movie related queries work only on 64 bit Windows systems.

    """
    pass
    


def imfPlugins(string, keyword="string", multiFrameSupport="string", pluginName="string", extension="string", writeSupport="string", readSupport="string"):
    """
    imfPlugins is NOT undoable, queryable, and NOT editable.
    

    
This command queries all the available imf plugins for its name, keyword or image file extension. Only one of the attributes (name, keyword or extension) can be queried at a time. If no flags are specified, this command returns a list of all available plugin names.

    """
    pass
    


def inheritTransform(objects, preserve=bool, toggle=bool):
    """
    inheritTransform is undoable, queryable, and NOT editable.
    

    
This command toggles the inherit state of an object. If this flag is off the object will not inherit transformations from its parent. In other words transformations applied to the parent node will not affect the object and it will act as though it is under the world.
If the -p flag is specified then the object's transformation will be modified to compensate when changing the inherit flag so the object will not change its world-space location.

    """
    pass
    


def insertJoint(object):
    """
    insertJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will insert a new joint under the given or selected joint. If the given joint has child joints, they will be reparented under the new inserted joint.
The given joint(or selected joint) should not have skin attached. The command works on the selected joint. No options or flags are necessary.

    """
    pass
    


def insertJointCtx(exists=bool, image1="string", image2="string", image3="string"):
    """
    insertJointCtx is undoable, queryable, and editable.
    

    
The command will create an insert joint context. The insert joint tool inserts joints into an existing chain of joints.

    """
    pass
    


def insertKeyCtx(image1="string", breakdown=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    insertKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to insert keys within the graph editor

    """
    pass
    


def insertKnotCurve(numberOfKnots=int, curveOnSurface=bool, insertBetween=bool, object=bool, name="string", nodeState=int, replaceOriginal=bool, addKnots=bool, parameter=float, caching=bool, constructionHistory=bool):
    """
    insertKnotCurve is undoable, queryable, and editable.
    

    
The insertKnotCurve command inserts knots into a curve given a list of parameter values. The number of knots to add at each parameter value and whether the knots are added or complemented can be specified. The name of the curve is returned. If construction history is on, the name of the resulting dependency node is also returned.
An edit point will appear where you insert the knot. Also, the number of spans and CVs in the curve will increase in the area where the knot is inserted.
You can insert up to "degree" knots at a curve parameter that isn't already an edit point. eg. for a degree three curve, you can insert up to 3 knots.
Use this operation if you need more CVs in a local area of the curve. Use this operation (or "hardenPoint") if you want to create a corner in a curve.

    """
    pass
    


def insertKnotSurface(numberOfKnots=int, insertBetween=bool, nodeState=int, name="string", direction=int, replaceOriginal=bool, addKnots=bool, parameter=float, caching=bool, object=bool, constructionHistory=bool):
    """
    insertKnotSurface is undoable, queryable, and editable.
    

    
The insertKnotSurface command inserts knots (aka isoparms) into a surface given a list of parameter values. The number of knots to add at each parameter value and whether the knots are added or complemented can be specified. The name of the surface is returned and if history is on, the name of the resulting dependency node is also returned.
You must specify one, none or all number of knots with the "-nk" flag. eg. if you specify none, then the default (one) knot will be added at each specified parameter value. If you specify one "-nk" value then that number of knots will be added at each parameter value. Otherwise, you must specify the same number of "-nk" flags as "-p" flags, defining the number of knots to be added at each specified parameter value.
You can insert up to "degree" knots at a parameter value that isn't already an isoparm. eg. for a degree 3 surface, you can insert up to 3 knots.
Use this operation if you need more CVs in a local area of the surface. Use this operation if you want to create a corner in the surface.
Note: A single insertKnotSurface command cannot insert in both directions at once; you must use two separate commands to do this.

    """
    pass
    


def instance(objects, leaf=bool, smartTransform=bool, name="string"):
    """
    instance is undoable, NOT queryable, and NOT editable.
    

    
Instancing is a way of making the same object appear twice in the scene. This is accomplished by creation of a new transform node that points to an exisiting object. Changes to the transform are independent but changes to the "instanced" object affect all instances since the node is shared.
If no objects are given, then the selected list is instanced. When an object is instanced a new transform node is created that points to the selected object.
The smart transform feature allows instance to transform newly instanced objects based on previous transformations between instances.
Example: Instance an object and move it to a new location. Instance it again with the smart transform flag. It should have moved once again the distance you had previously moved it.
Note: changing the selected list between smart instances will cause the transform information to be deleted.
It returns a list of the new objects created by the instance operation.
See also: duplicate

    """
    pass
    


def instanceable(shape=bool, recursive=bool, allow=bool):
    """
    instanceable is undoable, queryable, and NOT editable.
    

    
Flags one or more DAG nodes so that they can (or cannot) be instanced. This command sets an internal state on the specified DAG nodes which is checked whenever Maya attempts an instancing operation. If no node names are provided on the command line then the current selection list is used.
Sets are automatically expanded to their constituent objects. Nodes which are already instanced (or have children which are already instanced) cannot be marked as non-instancable.

    """
    pass
    


def instancer(cycle="string", cycleStep=float, addObject=bool, object="string", valueName="string", objectPosition="string", removeObject=bool, levelOfDetail="string", rotationOrder="string", objectScale="string", cycleStepUnits="string", pointDataSource=bool, objectRotation="string", rotationUnits="string", index=int, name="string"):
    """
    instancer is undoable, queryable, and editable.
    

    
This command is used to create a instancer node and set the proper attributes in the node.

    """
    pass
    


def internalVar(userBitmapsDir=bool, userHotkeyDir=bool, userShelfDir=bool, userPresetsDir=bool, userPrefDir=bool, userMarkingMenuDir=bool, userWorkspaceDir=bool, userTmpDir=bool, userScriptDir=bool, userAppDir=bool):
    """
    internalVar is undoable, NOT queryable, and NOT editable.
    

    
This command returns the values of internal variables. No modification of these variables is supported.

    """
    pass
    


def intersect(surfacesurface, curveOnSurface=bool, object=bool, firstSurface=bool, nodeState=int, constructionHistory=bool, caching=bool, tolerance="string", name="string"):
    """
    intersect is undoable, queryable, and editable.
    

    
The intersect command creates a curve on surface where all surfaces intersect with each other. By default, the curve on surface is created for both surfaces. However, by using the -fs flag, only the first surface will have a curve on surface. Also, the intersection curve can be created as a 3D curve rather than a curve on surface.

    """
    pass
    


def intField(string, docTag="string", height=int, defineTemplate="string", parent="string", step=int, numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", enterCommand="string", value=int, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, minValue=int, dragCommand="string", exists=bool, changeCommand="string", maxValue=int, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, editable=bool, isObscured=bool, receiveFocusCommand="string"):
    """
    intField is undoable, queryable, and editable.
    

    
Create a field control that accepts only integer values and is bound by a minimum and maximum value. An invisible slider is attached to the field and accessed by holding down the Ctrl modifier key while pressing one of the mouse buttons. Dragging the invisible slider to the right with the middle mouse button increases the field value by the amount specified with the -s/step flag, while dragging to the left decreases the value by the same amount. The left and right mouse buttons apply a factor of 0.1 and 10 to the step value.

    """
    pass
    


def intFieldGrp(groupName, docTag="string", height=int, columnWidth4=int, extraLabel="string", enable3=bool, popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, value=int, dragCallback="string", columnOffset2=int, parent="string", value2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", exists=bool, columnAttach4="string", value3=int, numberOfFields=int, value1=int, adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, enable2=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, enable4=bool, columnWidth=int, manage=bool, columnOffset4=int, enable1=bool, changeCommand="string", columnAttach2="string", value4=int, columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    intFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text and editable integer fields. The label text is optional and one to four fields can be created.

    """
    pass
    


def intScrollBar(string, docTag="string", height=int, defineTemplate="string", parent="string", step=int, numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", value=int, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, minValue=int, dragCommand="string", exists=bool, changeCommand="string", maxValue=int, enableBackground=bool, visibleChangeCommand="string", visible=bool, horizontal=bool, largeStep=int, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    intScrollBar is undoable, queryable, and editable.
    

    
Create a scroll bar control that accepts only integer values and is bound by a minimum and maximum value. The scroll bar displays a marker indicating the current value of the scroll bar relative to it's minimum and maximum values. Click and drag the marker or on the scroll bar itself to change the current value.

    """
    pass
    


def intSlider(docTag="string", height=int, defineTemplate="string", parent="string", step=int, numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", value=int, highlightColor=float, annotation="string", changeCommand="string", preventOverride=bool, popupMenuArray=bool, minValue=int, dragCommand="string", exists=bool, maxValue=int, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, horizontal=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    intSlider is undoable, queryable, and editable.
    

    
Create a slider control that accepts only integer values and is bound by a minimum and maximum value. The slider displays a marker indicating the current value of the slider relative to it's minimum and maximum values. Click and drag the marker or on the slider itself to change the current value.

    """
    pass
    


def intSliderGrp(groupName, docTag="string", height=int, columnWidth4=int, extraLabel="string", popupMenuArray=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, value=int, dragCallback="string", columnOffset2=int, parent="string", annotation="string", columnAlign5="string", fieldMaxValue=int, columnOffset5=int, fieldStep=int, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, minValue=int, columnAlign4="string", adjustableColumn5=int, dragCommand="string", exists=bool, columnAttach4="string", step=int, fieldMinValue=int, maxValue=int, adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", preventOverride=bool, fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, field=bool, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", columnAttach6="string", isObscured=bool, columnOffset6=int, sliderStep=int):
    """
    intSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of controls containing a label text, an integer field and an integer slider. The text and field controls are optional. Editing or querying the field range values has no effect if the -f/field flag was not specified when the group was created.
This group also allows you to enter values into the field outside of the slider range which is limited by the -min/minValue and -max/maxValue flags. To do this, use the -fmn/fieldMinValue and -fmx/fieldMaxValue flags to specify a greater range of values.
Note that the command will not allow you to specify a -fmn/fieldMinValue greater than the -min/minValue value nor a -fmx/fieldMaxValue less than the -max/maxValue value.
If you do supply a larger field range with the -fmn/fieldMinValue and -fmx/fieldMaxValue flags then you will notice that entering a value in the field that is outside of the slider range will result in extending the slider range as well. For example, if you create a slider group with the following command:
intSliderGrp -min -10 -max 10 -fieldMinValue -100 -fieldMaxValue 100;
Then you will be able to use the slider to select any value from -10 to 10. At the same time you will be able to enter into the field any value from -100 to 100. If you enter a value, say 20, then the new slider range will grow such that this value is now accessible through the slider as well. In fact, the new slider limit will become double of that what you entered. Note that the slider limits will never grow beyond the field limits, in other words if you entered the value 80 then the slider will be clipped to the field limit of 100 and not doubled to 160.
TelfBaseGrpCmd.cpp

    """
    pass
    


def inViewEditor(visible=bool):
    """
    inViewEditor is NOT undoable, queryable, and NOT editable.
    

    
Mel access to the In-View Editor. In-View Editors display a customizable subset of a node's attributes, letting you adjust attributes directly in a scene instead of opening the Channel Box or Attribute Editor.

    """
    pass
    


def inViewMessage(message="string", alpha=float, fontSize=int, fade=bool, show=bool, fadeInTime=int, minimize=bool, statusMessage="string", font="string", restore=bool, frameOffset=int, fadeOutTime=int, backColor=int, hide=bool, textOffset=int, assistMessage="string", fadeStayTime=int, dragKill=bool, clear="string", uvEditor=bool, position="string", textAlpha=float):
    """
    inViewMessage is undoable, NOT queryable, and NOT editable.
    

    
Used for displaying in-view messages.
Note: On Linux, the alpha and textAlpha flags for inViewMessage are only supported when running a window manager that supports compositing (transparency and opacity). Otherwise, they are ignored. In addition, the flags for message fading: -fade, -fadeInTime, -fadeStay and -fadeOutTime are supported, but the message will display without a fade effect if the window manager doesn't support compositing.

    """
    pass
    


def iprEngine(releaseIprImage=bool, region=int, underPixel=int, useTemplate="string", updateMotionBlur=bool, updateLightGlow=bool, updatePort="string", showProgressBar=bool, defineTemplate="string", resolution=bool, motionVectorFile=bool, startTuning=bool, exists=bool, update=bool, stopTuning=bool, updateShadowMaps=bool, updateShading=bool, updateDepthOfField=bool, updateShaderGlow=bool, estimatedMemory=bool, scanlineIncrement="string", relatedFiles=bool, object="string", iprImage="string", copy="string"):
    """
    iprEngine is undoable, queryable, and editable.
    

    
Command to create or edit an iprEngine. A iprEngine is an object that watches for changes to shading networks and automatically reshades to generate an up-to-date image.

    """
    pass
    


def isConnected(ignoreUnitConversion=bool):
    """
    isConnected is undoable, NOT queryable, and NOT editable.
    

    
The isConnected command is used to check if two plugs are connected in the dependency graph. The return value is false if they are not and true if they are.

The first string specifies the source plug to check for connection.
The second one specifies the destination plug to check for connection.

    """
    pass
    


def isDirty(datablock=bool, connection=bool):
    """
    isDirty is undoable, NOT queryable, and NOT editable.
    

    
The isDirty command is used to check if a plug is dirty. The return value is 0 if it is not and 1 if it is. If more than one plug is specified then the result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs are dirty).

    """
    pass
    


def isolateSelect(addSelectedObjects=bool, removeDagObject="string", loadSelected=bool, addSelected=bool, state=bool, viewObjects=bool, removeSelected=bool, addDagObject="string", update=bool):
    """
    isolateSelect is undoable, queryable, and NOT editable.
    

    
This command turns on/off isolate select mode in a specified modeling view, specified as the argument. Isolate select mode is a display mode where the currently selected objects are added to a list and only those objects are displayed in the view. It allows for selective viewing of specific objects and object components.

    """
    pass
    


def isTrue():
    """
    isTrue is undoable, NOT queryable, and NOT editable.
    

    
This commmand returns the state of the named condition. If the condition is true, it returns 1. Otherwise it returns 0.

    """
    pass
    


def itemFilter(string, pythonModule="string", classification="string", secondScript="string", clearByType=bool, clearByBin=bool, category="string", byBin="string", text="string", parent="string", byName="string", exists=bool, listBuiltInFilters=bool, intersect="string", union="string", difference="string", listUserFilters=bool, negate=bool, uniqueNodeNames=bool, listOtherFilters=bool, byType="string", byScript="string"):
    """
    itemFilter is undoable, queryable, and editable.
    

    
This command creates a named itemFilter object. This object can be attached to selectionConnection objects, or to editors, in order to filter the item lists going through them. Using union, intersection and difference filters, complex composite filters can be created.

    """
    pass
    


def itemFilterAttr(string, classification="string", hidden=bool, secondScript="string", writable=bool, keyable=bool, hasDrivenKey=bool, byName="string", text="string", parent="string", scaleRotateTranslate=bool, published=bool, listBuiltInFilters=bool, hasCurve=bool, intersect="string", union="string", byNameString="string", readable=bool, listUserFilters=bool, negate=bool, listOtherFilters=bool, byScript="string", hasExpression=bool):
    """
    itemFilterAttr is undoable, queryable, and editable.
    

    
This command creates a named itemFilterAttr object. This object can be attached to editors, in order to filter the attributes going through them. Using union and intersection filters, complex composite filters can be created.

    """
    pass
    


def itemFilterType(type=bool, text="string"):
    """
    itemFilterType is undoable, queryable, and editable.
    

    
This command queries a named itemFilter object. This object can be attached to selectionConnection objects, or to editors, in order to filter the item lists going through them. Using union and intersection filters, complex composite filters can be created.

    """
    pass
    


def joint(objects, zeroScaleOrient=bool, orientation=int, children=bool, relative=bool, limitSwitchX=bool, angleY=int, assumePreferredAngles=bool, setPreferredAngles=bool, angleZ=int, limitY=int, orientJoint="string", symmetryAxis="string", name="string", degreeOfFreedom="string", component=bool, symmetry=bool, limitZ=int, scaleCompensate=bool, exists="string", limitSwitchZ=bool, stiffnessY=float, scaleOrientation=int, limitSwitchY=bool, absolute=bool, stiffnessZ=float, automaticLimits=bool, angleX=int, rotationOrder="string", position="string", limitX=int, secondaryAxisOrient="string", scale=float, stiffnessX=float, radius=float):
    """
    joint is undoable, queryable, and editable.
    

    
The joint command is used to create, edit, and query, joints within Maya. (The standard edit(-e) and query(-q) flags are used for edit and query functions). If the object is not specified, the currently selected object (dag object) will be used.
Multiple objects are allowed only for the edit mode. The same edit flags will be applied on all the joints selected, except for -p without -r (set joint position in the world space). An ik handle in the object list is equivalent to the list of joints the ik handle commands. When -ch/children is present, all the child joints of the specified joints, including the joints implied by possible ik handles, will also be included.
In the creation mode, a new joint will be created as a child of a selected transform or starts a hierarchy by itself if no transform is selected. An ik handle will be treated as a transform in the creation mode.
The default values of the arguments are:
-degreeOfFreedom xyz
-name "Joint#"
-position 0 0 0
-absolute
-dof "xyz"
-scale 1.0 1.0 1.0
-scaleCompensate true
-orientation 0.0 0.0 0.0
-scaleOrientation 0.0 0.0 0.0
-limitX -360 360
-limitY -360 360
-limitZ -360 360
-angleX 0.0
-angleY 0.0
-angleZ 0.0
-stiffnessX 0.0
-stiffnessY 0.0
-stiffnessZ 0.0
-limitSwitchX no
-limitSwitchY no
-limitSwitchZ no
-rotationOrder xyz
Those arguments can be specified in the creation mode, editied in the edit mode (-e), or queried in the query mode (-q).

    """
    pass
    


def jointCluster(belowBound=float, belowCluster=bool, belowValue=float, belowDropoffType="string", joint="string", aboveBound=float, aboveCluster=bool, deformerTools=bool, aboveValue=float, aboveDropoffType="string", name="string"):
    r"""
    jointCluster is undoable, queryable, and editable.
    

    
The joint cluster command adds high-level controls to manage the cluster percentage values on a bound skin around a joint. JointClusters are one way to create smooth bending behaviour on skin when joints rotate.
.                a <---- aboveBound
.    ____________a_________
.                a         \
.     Joint1     a       Joint2
.   _____________a_______    \
.                a       \    \     b  <--- belowBound
.                a        \    \  b
.                          \    b
.                           \ b  \
.                           b\    \
.                         b   \ Joint3
CVs/vertices between Joint1 and aaaaa (aboveBound) receive only translation/rotation/scale from Joint1. CVs vertices between aaaa and bbbb transition between translation/rotatation/scale from Joint1 and Joint2. CV2 beyand bbbbb (below bound) receive only translation/ rotation scale from Joint3.

    """
    pass
    


def jointCtx(object, forceSolverH=bool, scaleCompensateJ=bool, scaleOrientationJ=int, stickyH="string", largeBoneLength=float, image3="string", smallBoneLength=float, smallBoneRadius=float, image1="string", autoJointOrient="string", variableBoneSize=int, symmetryAxis="string", scaleJ=float, exists=bool, degreeOfFreedomJ="string", symmetry=bool, weightH=float, priorityH=int, jointOrientationJ=int, solverTypeH="string", image2="string", createIKHandle=bool, largeBoneRadius=float, autoPriorityH=bool, snapHandleH=bool, secondaryAxisOrient="string", jointAutoLimits=bool, poWeightH=float):
    """
    jointCtx is undoable, queryable, and editable.
    

    
The joint context command (jointCtx) updates the parameters of the joint tool. The options for the tool will be set by the flags the user specifies.

    """
    pass
    


def jointDisplayScale(ikfk=bool, absolute=bool):
    """
    jointDisplayScale is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current display size of skelton joints. The joint display size is controlled by a scale factor; scale factor 1 puts the display size to its default, which is 1 in diameter. With the plain format, the float argument is the factor with respect to the default size. When -a/absolute is used, the float argument refers to the actual diameter of the joint display size.

    """
    pass
    


def jointLattice(before=bool, exclusive="string", after=bool, widthLeft=float, joint="string", includeHiddenSelections=bool, creasing=float, frontOfChain=bool, prune=bool, widthRight=float, geometryIndices=bool, split=bool, lowerTransform="string", geometry="string", upperBindSkin="string", name="string", rounding=float, parallel=bool, ignoreSelected=bool, afterReference=bool, remove=bool, upperTransform="string", lengthOut=float, deformerTools=bool, lengthIn=float, lowerBindSkin="string"):
    """
    jointLattice is undoable, queryable, and editable.
    

    
This command creates/edits/queries a jointLattice deformer. The name of the created/edited object is returned. Usually you would make use of this functionality through the higher level flexor command.

    """
    pass
    


def keyframe(objects, clipTime=(), controlPoints=bool, relative=bool, adjustBreakdown=bool, animation="string", option="string", indexValue=bool, lastSelected=bool, selected=bool, eval=bool, tickDrawSpecial=bool, valueChange=float, hierarchy="string", includeUpperBound=bool, name=bool, timeChange=(), shape=bool, absolute=bool, attribute="string", index=int, time=(), float=(), breakdown=bool, keyframeCount=bool, floatChange=float):
    """
    keyframe is undoable, queryable, and editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command edits the time and/or value of keys of specified objects and/or parameter curves
Unless otherwise specified by the -query flag, the command defaults to editing keyframes.

    """
    pass
    


def keyframeOutliner(docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", animCurve="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, display="string", manage=bool, isObscured=bool):
    """
    keyframeOutliner is undoable, queryable, and editable.
    

    
This command creates/edits/queries a keyframe outliner control.

    """
    pass
    


def keyframeRegionCurrentTimeCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionCurrentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the keyframe region of the dope sheet editor.

    """
    pass
    


def keyframeRegionDirectKeyCtx(image1="string", history=bool, exists=bool, option="string", image2="string", name="string", image3="string"):
    """
    keyframeRegionDirectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to directly manipulate keyframes within the dope sheet editor

    """
    pass
    


def keyframeRegionDollyCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionDollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create a dolly context for the dope sheet editor.

    """
    pass
    


def keyframeRegionInsertKeyCtx(image1="string", breakdown=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionInsertKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to insert keys within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionMoveKeyCtx(image1="string", history=bool, exists=bool, option="string", image2="string", name="string", image3="string"):
    """
    keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to move keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionScaleKeyCtx(image1="string", scaleSpecifiedKeys=bool, type="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionScaleKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionSelectKeyCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionSelectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionSetKeyCtx(image1="string", breakdown=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionSetKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to set keys within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionTrackCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    keyframeRegionTrackCtx is undoable, queryable, and editable.
    

    
This command can be used to create a track context for the dope sheet editor.

    """
    pass
    


def keyframeStats(docTag="string", height=int, columnWidth4=int, parent="string", timeAnnotation="string", numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, popupMenuArray=bool, highlightColor=float, animEditor="string", dragCallback="string", columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, adjustableColumn6=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, enable=bool, columnAlign=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, valueAnnotation="string", columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", precision=int, fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnOffset4=int, columnAttach2="string", columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    keyframeStats is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates, edits, queries a keyframe stats control.

    """
    pass
    


def keyingGroup(subtract="string", split="string", color=int, edges=bool, excludeRotate=bool, flatten="string", intersection="string", isIntersecting="string", category="string", renderable=bool, include="string", text="string", isMember="string", minimizeRotation=bool, activator="string", excludeDynamic=bool, noSurfaceShader=bool, noWarnings=bool, facets=bool, excludeVisibility=bool, layer=bool, removeActivator="string", union="string", size=bool, addElement="string", excludeScale=bool, vertices=bool, setActiveFilter="string", editPoints=bool, forceElement="string", clear="string", excludeTranslate=bool, empty=bool, nodesOnly=bool, name="string", copy="string", afterFilters=bool, remove="string"):
    """
    keyingGroup is undoable, queryable, and editable.
    

    
This command is used to manage the membership of a keying group. Keying groups allow users to effectively manage related keyframe data, allowing keys on attributes in the keying group to be set and edited as a single entity.

    """
    pass
    


def keyTangent(objects, stepAttributes=bool, controlPoints=bool, inWeight=float, relative=bool, ox=float, attribute="string", oy=float, animation="string", iy=float, ix=float, g=bool, inAngle=int, hierarchy="string", inTangentType="string", includeUpperBound=bool, unify=bool, weightLock=bool, weightedTangents=bool, outAngle=int, outTangentType="string", absolute=bool, outWeight=float, index=int, time=(), float=(), shape=bool, lock=bool, pluginTangentTypes="string"):
    """
    keyTangent is undoable, queryable, and editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command edits or queries tangent properties of keyframes in a keyset. It is also used to edit or query the default tangent type of newly created keyframes (see the setKeyframe command for more information on how to override this default).
Tangents help manage the shape of the animation curve and affect the interpolation between keys. The tangent angle specifies the direction the curve will take as it leaves (or enters) a key. The tangent weight specifies how much influence the tangent angle has on the curve before the curve starts towards the next key.
Maya internally represents tangents as x and y values. Refer to the API documentation for MFnAnimCurve for a description of the relationship between tangent angle and weight and the internal x and y values.

    """
    pass
    


def lassoContext(image1="string", history=bool, exists=bool, drawClosed=bool, image2="string", name="string", image3="string"):
    """
    lassoContext is undoable, queryable, and editable.
    

    
Creates a context to perform selection via a "lasso". Use for irregular selection regions, where the "marquee-style" select of the "selectContext" is inappropriate.

    """
    pass
    


def lattice(before=bool, exclusive="string", after=bool, dualBase=bool, freezeMapping=bool, commonParent=bool, removeTweaks=bool, includeHiddenSelections=bool, frontOfChain=bool, outsideFalloffDistance=float, prune=bool, objectCentered=bool, geometryIndices=bool, split=bool, divisions=int, geometry="string", name="string", latticeReset=bool, scale="string", remove=bool, parallel=bool, outsideLattice=int, ignoreSelected=bool, rotation=int, afterReference=bool, ldivisions=int, deformerTools=bool, position="string"):
    """
    lattice is undoable, queryable, and editable.
    

    
This command creates a lattice deformer that will deform the selected objects. If the object centered flag is used, the initial lattice will fit around the selected objects. The lattice will be selected when the command is completed. The lattice deformer has an associated base lattice. Only objects which are contained by the base lattice will be deformed by the lattice.

    """
    pass
    


def latticeDeformKeyCtx(image1="string", latticeRows=int, latticeColumns=int, envelope=float, history=bool, scaleLatticePts=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    latticeDeformKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to deform key frames with lattice manipulator. This context only works in the graph editor.

    """
    pass
    


def launch(pdfFile="string", directory="string", movie="string", webPage="string"):
    """
    launch is undoable, NOT queryable, and NOT editable.
    

    
Launch the appropriate application to open the document, web page or directory specified.

    """
    pass
    


def launchImageEditor(filename, editImageFile="string", viewImageFile="string"):
    """
    launchImageEditor is undoable, NOT queryable, and NOT editable.
    

    
Launch the appropriate application to edit/view the image files specified. This command works only on the Macintosh and Windows platforms.

    """
    pass
    


def layerButton(docTag="string", height=int, layerState="string", defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", select=bool, transparent=bool, highlightColor=float, annotation="string", layerVisible=bool, preventOverride=bool, layerHideOnPlayback=bool, popupMenuArray=bool, enableBackground=bool, hideOnPlaybackCommand="string", visibleCommand="string", exists=bool, typeCommand="string", name="string", visible=bool, enable=bool, doubleClickCommand="string", visibleChangeCommand="string", color=float, renameCommand="string", fullPathName=bool, dropCallback="string", labelWidth=bool, noBackground=bool, backgroundColor=float, manage=bool, command="string", current=bool, isObscured=bool, identification=int):
    """
    layerButton is undoable, queryable, and editable.
    

    
Creates a layer bar button widget. This widget contains both the name of the layer to which it refers and a color swatch indicating it's color assignment. It is used primarily in the construction of the layerBar and layer Editor window, being the widget used for each layer in the respective lists.

    """
    pass
    


def layeredShaderPort(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, fullPathName=bool, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", selectedColorControl="string", exists=bool, selectedTransparencyControl="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, node="string", preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    layeredShaderPort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays an image representing the layered shader node specified.

    """
    pass
    


def layeredTexturePort(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", selectedIsVisibleControl="string", highlightColor=float, fullPathName=bool, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", selectedColorControl="string", width=int, selectedAlphaControl="string", exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, node="string", preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, selectedBlendModeControl="string", isObscured=bool):
    """
    layeredTexturePort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays an image representing the layered texture node specified.

    """
    pass
    


def layout(docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, popupMenuArray=bool, numberOfChildren=bool, highlightColor=float, annotation="string", dropCallback="string", childArray=bool, exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    layout is undoable, queryable, and editable.
    

    
This command allows you to edit or query the properties of any layout. The argument is the name of the layout.

    """
    pass
    


def layoutDialog(title="string", uiScript="string", dismiss="string", backgroundColor=float, parent="string"):
    """
    layoutDialog is undoable, NOT queryable, and NOT editable.
    

    
The layoutDialog command creates a modal dialog containing a formLayout with 100 divisions. The formLayout can be populated with arbitrary UI elements through use of the '-ui/-uiScript' flag.
NOTE:
A layoutDialog is not a window and certain UI elements will not function properly within it. In particular menuBars and panels containing menuBars should not be used with the layoutDialog.

    """
    pass
    


def license(isExported=bool, isBorrowed=bool, showProductInfoDialog=bool, showBorrowInfo=bool, info=bool, licenseMethod=bool, isTrial=bool, productChoice=bool, usage=bool, r=bool, borrow=bool):
    """
    license is undoable, NOT queryable, and NOT editable.
    

    
This command displays version information about the application if it is executed without flags. If one of the above flags is specified then the specified version information is returned.

    """
    pass
    


def lightlink(sets=bool, make=bool, object="string", shapes=bool, hierarchy=bool, b=bool, light="string", transforms=bool):
    """
    lightlink is undoable, queryable, and NOT editable.
    

    
This command is used to make, break and query light linking relationships between lights/sets of lights and objects/sets of objects.
If no make, break or query flag is specified and both lights and objects flags are present, the make flag is assumed to be specified.
If no make, break or query flag is specified and only one of the lights and objects flags is present, the query flag is assumed to be specified.
You can specify as many lights and objects as you like, using the multiuse -light and -object flags.
A better way to perform light linking is to make sets of lights and sets of geometry. If you create a set which contains lights (such as the ceiling lights in your scene) and a set which contains geometry (such as the geometry of your character), you can then link the set containing lights with the set containing geometry in order to get those lights to illuminate those pieces of geometry. In addition, you can add and remove lights and geometry from their respective sets without having to make and break light links.

    """
    pass
    


def lightList(remove="string", add="string"):
    """
    lightList is undoable, queryable, and editable.
    

    
Add/Remove a relationship between an object and the current light. Soon to be replaced by the connect-attribute command.

    """
    pass
    


def linearPrecision():
    """
    linearPrecision is undoable, queryable, and NOT editable.
    

    
This command controls the display of linear strings in the interface. (See the linearField command). Setting this affects any linear strings displayed afterwards, formatting them so they will show at most the specified number of digits after the decimal point. Allowed values are 0 through 6.

    """
    pass
    


def listAnimatable(shape=bool, type=bool, manip=bool, active=bool, manipHandle=bool):
    """
    listAnimatable is undoable, NOT queryable, and NOT editable.
    

    
This command list the animatable attributes of a node. Command flags allow filtering by the current manipulator, or node type.

    """
    pass
    


def listAttr(objects, locked=bool, scalar=bool, fromPlugin=bool, unlocked=bool, keyable=bool, read=bool, string="string", category="string", multi=bool, userDefined=bool, usedAsFilename=bool, hasData=bool, channelBox=bool, write=bool, hasNullData=bool, output=bool, caching=bool, readOnly=bool, inUse=bool, visible=bool, scalarAndArray=bool, leaf=bool, array=bool, ramp=bool, settable=bool, shortNames=bool, extension=bool, changedSinceFileOpen=bool, connectable=bool):
    """
    listAttr is undoable, NOT queryable, and NOT editable.
    

    
This command lists the attributes of a node. If no flags are specified all attributes are listed.

    """
    pass
    


def listAttrPatterns(verbose=bool, patternType=bool):
    """
    listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.
    

    
Attribute patterns are plain text descriptions of an entire Maya attribute forest. ("forest" because there could be an arbitrary number of root level attributes, it's not restricted to having a single common parent though in general that practice is a good idea.) This command lists the various pattern types available, usually created via plugin, as well as any specific patterns that have already been instantiated. A pattern type is a thing that knows how to take some textual description of an attribute tree, e.g. XML or plaintext, and convert it into an attribute pattern that can be applied to any node or node type in Maya.

    """
    pass
    


def listCameras(orthographic=bool, perspective=bool):
    """
    listCameras is undoable, NOT queryable, and NOT editable.
    

    
Command to list all cameras. If no flags are given, both perspective and orthographic cameras will be displayed. This command returns an array of camera names. When the transform name uniquely identifies the camera it is used, otherwise the shape name will be returned.

    """
    pass
    


def listConnections(destination=bool, shapes=bool, type="string", source=bool, connections=bool, skipConversionNodes=bool, plugs=bool, exactType=bool):
    """
    listConnections is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns a list of all attributes/objects of a specified type that are connected to the given object(s). If no objects are specified then the command lists the connections on selected nodes.

    """
    pass
    


def listDeviceAttachments(axis="string", clutch="string", file="string", selection=bool, write=bool, device="string", attribute="string"):
    """
    listDeviceAttachments is undoable, NOT queryable, and NOT editable.
    

    
This command lists the current set of device attachments. The listing is in the form of the commands required to recreate them. This includes both attachments and device mappings.

    """
    pass
    


def listHistory(futureWorldAttr=bool, futureLocalAttr=bool, interestLevel=int, leaf=bool, groupLevels=bool, allConnections=bool, allGraphs=bool, levels=int, breadthFirst=bool, pruneDagObjects=bool, historyAttr=bool, allFuture=bool, future=bool):
    """
    listHistory is undoable, queryable, and NOT editable.
    

    
This command traverses backwards or forwards in the graph from the specified node and returns all of the nodes whose construction history it passes through. The construction history consists of connections to specific attributes of a node defined as the creators and results of the node's main data, eg. the curve for a Nurbs Curve node.
For information on history connections through specific plugs use the "listConnections" command first to find where the history begins then use this command on the resulting node.

    """
    pass
    


def listInputDeviceAxes():
    """
    listInputDeviceAxes is undoable, NOT queryable, and NOT editable.
    

    
This command lists all of the axes of the specified input device.

    """
    pass
    


def listInputDeviceButtons():
    """
    listInputDeviceButtons is undoable, NOT queryable, and NOT editable.
    

    
This command lists all of the buttons of the specified input device specified as an argument.

    """
    pass
    


def listInputDevices():
    """
    listInputDevices is undoable, NOT queryable, and NOT editable.
    

    
This command lists all input devices that maya knows about.

    """
    pass
    


def listNodesWithIncorrectNames():
    """
    listNodesWithIncorrectNames is NOT undoable, NOT queryable, and NOT editable.
    

    
List all nodes with incorrect names in the Script Editor.

    """
    pass
    


def listNodeTypes(exclude="string"):
    """
    listNodeTypes is undoable, NOT queryable, and NOT editable.
    

    
Lists dependency node types satisfying a specified classification string.
See the 'getClassification' command for a list of the standard classification strings.

    """
    pass
    


def listRelatives(objects, allParents=bool, shapes=bool, type="string", children=bool, fullPath=bool, allDescendents=bool, noIntermediate=bool, parent=bool, path=bool):
    """
    listRelatives is undoable, NOT queryable, and NOT editable.
    

    
This command lists parents and children of DAG objects. The flags -c/children, -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually exclusive. Only one can be used in a command.
When listing parents of objects directly under the world, the command will return an empty parent list. Listing parents of objects directly under a shape (underworld objects) will return their containing shape node in the list of parents. Listing parents of components of objects will return the object.
When listing children, shape nodes will return their underworld objects in the list of children. Listing children of components of objects returns nothing.
The -ni/noIntermediate flag works with the -s/shapes flag. It causes any intermediate shapes among the descendents to be ignored.

    """
    pass
    


def listSets(object="string", type=int, extendToShape=bool, allSets=bool):
    """
    listSets is undoable, NOT queryable, and NOT editable.
    

    
The listSets command is used to get a list of all the sets an object belongs to. To get sets of a specific type for an object use the type flag as well.
To get a list of all sets in the scene then don't use an object in the command line but use one of the flags instead.

    """
    pass
    


def loadFluid(initialConditions=bool, currentTime=bool, frame=float):
    """
    loadFluid is undoable, queryable, and editable.
    

    
A command to set builtin fluid attributes such as Density, Velocity, etc for all cells in the grid from the initial state cache

    """
    pass
    


def loadModule(load="string", allModules=bool, scan=bool):
    """
    loadModule is NOT undoable, NOT queryable, and NOT editable.
    

    
Maya plug-ins may be installed individually within one of Maya's standard plug-in directories, or they may be packaged up with other resources in a "module". Each module resides in its own directory and provides a module definition file to make Maya aware of the plug-ins it provides. When Maya starts up it loads all of the module files it finds, making the module's plug-ins, scripts and other resources available for use. Note that the plug-ins themselves are not loaded at this time, Maya is simply made aware of them so that they can be loaded if needed. The loadModule command provides the ability to list and load any new modules which have been added since Maya started up, thereby avoiding the need to restart Maya before being able to use them.

    """
    pass
    


def loadPlugin(stringstring, quiet=bool, addCallback="string", removeCallback="string", allPlugins=bool, name="string"):
    """
    loadPlugin is undoable, NOT queryable, and NOT editable.
    

    
Load plug-ins into Maya. The parameter(s) to this command are either the names or pathnames of plug-in files. The convention for naming plug-ins is to use a .so extension on Linux, a .mll extension on Windows and .bundle extension on Mac OS X. If no extension is provided then the default extension for the platform will be used. To load a Python plugin you must explicitly supply the '.py' extension.
If the plugin was specified with a pathname then that is where the plugin will be searched for. If no pathname was provided then the current working directory (i.e. the one returned by Maya's 'pwd' command) will be searched, followed by the directories in the MAYA_PLUG_IN_PATH environment variable.
When the plug-in is loaded, the name used in Maya's internal plug-in registry for the plug-in information will be the file name with the extension removed. For example, if you load the plug-in "newNode.mll" the name used in the Maya's registry will be "newNode". This value as well as that value with either a ".so", ".mll" or ".bundle" extension can be used as valid arguments to either the unloadPlugin or pluginInfo commands.

    """
    pass
    


def loadPrefObjects():
    """
    loadPrefObjects is undoable, NOT queryable, and NOT editable.
    

    
This command loads preference dependency nodes from "userPrefObjects.ma", if it exists, from the user preference directory.

    """
    pass
    


def loadUI(workingDirectory="string", listTypes=bool, uiFile="string", uiString="string", verbose=bool):
    """
    loadUI is undoable, NOT queryable, and NOT editable.
    

    
loadUI command allows loading of a user interface created in Trolltech Qt Designer.
Some Qt classes have equivalents in Maya. If a widget's class is recognized, the Maya-equivelent will be created instead.
Any dynamic properties on a widget which start with a '-' character will be treated as a MEL flag/value pair. Similarly, any which start with a '+' will be treated as a Python flag/value pair. Such pairs will be applied to the widget upon creation.

    """
    pass
    


def lockNode(lockName=bool, lockUnpublished=bool, ignoreComponents=bool, lock=bool):
    """
    lockNode is undoable, queryable, and NOT editable.
    

    
Locks or unlocks one or more dependency nodes. A locked node is restricted in the following ways:
It may not be deleted.
It may not be renamed.
Its parenting may not be changed.
Attributes may not be added to or removed from it.
Locked attributes may not be unlocked.
Unlocked attributes may not be locked.
Note that an unlocked attribute of a locked node may still have its value set, or connections to it made or broken. For more information on attribute locking, see the setAttr command.
If no node names are specified then the current selection list is used.
There are a few special behaviors when locking containers. Containers are automatically expanded to their constituent objects. When a container is locked, members of the container may not be unlocked and the container membership may not be modified. Containers may also be set to lock unpublished attributes. When in this state, unpublished member attributes may not have existing connections broken, new connections cannot be made, and values on unconnected attributes may not be modified. Parenting is allowed to change on members of locked containers that have been published as parent or child anchors.

    """
    pass
    


def loft(curvecurvecurve, degree=int, uniform=bool, rebuild=bool, reverse=bool, reverseSurfaceNormals=bool, name="string", nodeState=int, close=bool, sectionSpans=int, autoReverse=bool, range=bool, createCusp=bool, caching=bool, object=bool, constructionHistory=bool, polygon=int):
    """
    loft is undoable, queryable, and editable.
    

    
This command computes a skinned (lofted) surface passing through a number of NURBS curves. There must be at least two curves present. The NURBS curves may be surface isoparms, curve on surfaces, trimmed edges or polygon edges.

    """
    pass
    


def lookThru(editorNameobject, farClip=float, nearClip=float):
    """
    lookThru is NOT undoable, queryable, and NOT editable.
    

    
This command sets a particular camera to look through in a view. This command may also be used to view the negative z axis of lights or other DAG objects. The standard camera tools can then be used to place the object.
Note: if there are multiple objects under the transform selected, cameras and lights take precedence.

    """
    pass
    


def ls(objectobject, renderQualities=bool, uuid=bool, renderSetups=bool, type="string", orderedSelection=bool, lockedNodes=bool, noIntermediate=bool, planes=bool, geometry=bool, assemblies=bool, containers=bool, allPaths=bool, defaultNodes=bool, undeletable=bool, shapes=bool, selection=bool, excludeType="string", preSelectHilite=bool, renderResolutions=bool, containerType="string", head=int, long=bool, readOnly=bool, recursive=bool, visible=bool, textures=bool, sets=bool, intermediateObjects=bool, flatten=bool, untemplated=bool, references=bool, partitions=bool, nodeTypes=bool, showType=bool, leaf=bool, absoluteName=bool, objectsOnly=bool, materials=bool, transforms=bool, dagObjects=bool, modified=bool, ghost=bool, templated=bool, tail=int, shortNames=bool, referencedNodes=bool, live=bool, exactType="string", lights=bool, dependencyNodes=bool, cameras=bool, showNamespace=bool, persistentNodes=bool, invisible=bool, hilite=bool, renderGlobals=bool):
    """
    ls is undoable, NOT queryable, and NOT editable.
    

    
The ls command returns the names (and optionally the type names) of objects in the scene.
The most common use of ls is to filter or match objects based on their name (using wildcards) or based on their type. By default ls will match any object in the scene but it can also be used to filter or list the selected objects when used in conjunction with the -selection flag.
If type names are requested, using the showType flag, they will be interleaved with object names so the result will be pairs of <object, type> values.
Internal nodes (for example itemFilter nodes) are typically filtered so that only scene objects are returned. However, using a wildcard will cause all the nodes matching the wild card to show up, including internal nodes. For example, ls * will list all nodes whether internal or not.
When Maya is in relativeNames mode, the ls command will return names relative to the current namespace and ls * will list from the the current namespace. For more details, please refer to the -relativeNames flag of the namespace command.
The command may also be passed node UUIDs instead of names/paths, and can return UUIDs instead of names via the -uuid flag.

    """
    pass
    


def lsThroughFilter(selection=bool, sort="string", item="string", nodeArray=bool, reverse=bool):
    """
    lsThroughFilter is undoable, NOT queryable, and NOT editable.
    

    
List all objects in the world that pass a given filter.

    """
    pass
    


def lsUI(objects, panels=bool, long=bool, menus=bool, type="string", dumpWidgets=bool, tail=int, radioMenuItemCollections=bool, menuItems=bool, editors=bool, collection=bool, cmdTemplates=bool, windows=bool, controlLayouts=bool, controls=bool, numWidgets=bool, contexts=bool, head=int):
    """
    lsUI is undoable, NOT queryable, and NOT editable.
    

    
This command returns the names of UI objects.

    """
    pass
    


def makebot(input="string", verbose=bool, nooverwrite=bool, checkdepends=bool, checkres=int, output="string"):
    """
    makebot is undoable, NOT queryable, and NOT editable.
    

    
The makebot command takes an image file and produces a block ordered texture (BOT) file, to be used for texture caching. If a relative pathname is specified for the input image file, project management rules apply. If a relative pathname is specified for the output BOT file, project management rules apply and gets put into the sourceImages directory.

    """
    pass
    


def makeIdentity(dagObject, jointOrient=bool, scale=bool, rotate=bool, apply=bool, translate=bool, normal=int, preserveNormals=bool):
    """
    makeIdentity is undoable, NOT queryable, and NOT editable.
    

    
The makeIdentity command is a quick way to reset the selected transform and all of its children down to the shape level by the identity transformation. You can also specify which of transform, rotate or scale is applied down from the selected transform. The identity transformation means:
translate = 0, 0, 0
rotate = 0, 0, 0
scale = 1, 1, 1
shear = 1, 1, 1
If a transform is a joint, then the "translate" attribute may not be 0, but will be used to position the joints so that they preserve their world space positions. The translate flag doesn't apply to joints, since joints must preserve their world space positions. Only the rotate and scale flags are meaningful when applied to joints.
If the -a/apply flag is true, then the transforms that are reset are accumulated and applied to the all shapes below the modified transforms, so that the shapes will not move. The pivot positions are recalculated so that they also will not move in world space. If this flag is false, then the transformations are reset to identity, without any changes to preserve position.

    """
    pass
    


def makeLive(surface, none=bool):
    """
    makeLive is undoable, NOT queryable, and NOT editable.
    

    
This commmand makes an object live. A live object defines the surface on which to create objects and to move object relative to. Only construction planes, nurbs surfaces and polygon meshes can be made live.
The makeLive command expects one of these types of objects as an explicit argument. If no argument is explicitly specified, then there are a number of default behaviours based on what is currently active. The command will fail if there is more than one object active or the active object is not one of the valid types of objects. If there is nothing active, the current live object will become dormant. Otherwise, the active object will become the live object.

    """
    pass
    


def makePaintable(stringstring, clearAll=bool, remove=bool, attrType="string", altAttribute="string", shapeMode="string", activateAll=bool, activate=bool, uiName="string"):
    """
    makePaintable is NOT undoable, queryable, and NOT editable.
    

    
Make attributes of nodes paintable to Attribute Paint Tool. This command is used to register new attributes to the Attribute Paint tool as paintable. Once registered the attributes will be recognized by the Attribute Paint tool and the user will be able to paint them.

    """
    pass
    


def makeSingleSurface(stitchTolerance=float, matchNormalDir=bool, uNumber=int, delta="string", useChordHeight=bool, fractionalTolerance=float, uType=int, chordHeight="string", edgeSwap=bool, chordHeightRatio=float, normalizeTrimmedUVRange=bool, polygonCount=int, vType=int, name="string", vNumber=int, minEdgeLength="string", polygonType=int, format=int, useChordHeightRatio=bool, object=bool, constructionHistory=bool):
    """
    makeSingleSurface is undoable, queryable, and editable.
    

    
This command performs a stitch and tessellate operation.

    """
    pass
    


def manipMoveContext(object, snapValue=float, snapRelative=bool, xformConstraint="string", snap=bool, lastMode=int, reflectionTolerance=float, orientTowards=float, snapPivotOri=bool, image3="string", currentActiveHandle=int, translate=float, pinPivot=bool, secondaryAxisOrient="string", image1="string", reflectionAbout=int, reflectionAxis=int, mode=int, preDragCommand="string", orientAxes=float, alignAlong=float, snapLivePoint=bool, orientJoint="string", editPivotMode=bool, exists=bool, position=bool, constrainAlongNormal=bool, snapComponentsRelative=bool, manipVisible=bool, snapPivotPos=bool, tweakMode=bool, orientObject="string", editPivotPosition=bool, postDragCommand="string", pivotOriHandle=bool, postCommand="string", activeHandle=int, preserveUV=bool, preCommand="string", interactiveUpdate=bool, reflection=bool, activeHandleNormal=int, preserveChildPosition=bool, snapLiveFaceCenter=bool, image2="string", orientJointEnabled=bool):
    """
    manipMoveContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a move manip context. Note that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of all move manip context. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing move manip context.

    """
    pass
    


def manipMoveLimitsCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    manipMoveLimitsCtx is undoable, queryable, and editable.
    

    
Create a context for the translate limits manipulator.

    """
    pass
    


def manipOptions(hideManipOnShift=bool, pivotRotateHandleOffset=int, refreshMode=int, lineSize=float, showPivotRotateHandle=int, hideManipOnCtrl=bool, hideManipOnShiftCtrl=bool, showPlaneHandles=int, handleSize=float, planeHandleOffset=int, pointSize=float, relative=bool, rememberActiveHandleAfterToolSwitch=bool, scale=float, forceRefresh=bool, preselectHighlight=bool, linePick=float, rememberActiveHandle=bool):
    """
    manipOptions is undoable, queryable, and NOT editable.
    

    
Changes the global manipulator parameters

    """
    pass
    


def manipPivot(posValid=bool, resetPos=bool, reset=bool, pinPivot=bool, valid=bool, oriValid=bool, snapOri=bool, ori=float, resetOri=bool, pos=float, snapPos=bool):
    """
    manipPivot is undoable, queryable, and NOT editable.
    

    
Changes transform component pivot used by the move/rotate/scale manipulators.

    """
    pass
    


def manipRotateContext(object, useCenterPivot=bool, xformConstraint="string", rotate=float, lastMode=int, reflectionTolerance=float, orientTowards=float, snapPivotOri=bool, image3="string", currentActiveHandle=int, position=bool, image1="string", reflectionAbout=int, reflectionAxis=int, mode=int, preDragCommand="string", orientAxes=float, useObjectPivot=bool, alignAlong=float, tweakMode=bool, editPivotMode=bool, exists=bool, constrainAlongNormal=bool, orientObject="string", manipVisible=bool, pinPivot=bool, snapPivotPos=bool, editPivotPosition=bool, postDragCommand="string", useManipPivot=bool, pivotOriHandle=bool, postCommand="string", activeHandle=int, preserveUV=bool, modifyTranslation=bool, preCommand="string", reflection=bool, preserveChildPosition=bool, image2="string"):
    """
    manipRotateContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a rotate manip context.

    """
    pass
    


def manipRotateLimitsCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    manipRotateLimitsCtx is undoable, queryable, and editable.
    

    
Create a context for the rotate limits manipulator.

    """
    pass
    


def manipScaleContext(object, xformConstraint="string", preventNegativeScale=bool, lastMode=int, reflectionTolerance=float, orientTowards=float, scale=float, image3="string", currentActiveHandle=int, position=bool, image1="string", reflectionAbout=int, reflectionAxis=int, mode=int, preDragCommand="string", orientAxes=float, alignAlong=float, tweakMode=bool, editPivotMode=bool, exists=bool, constrainAlongNormal=bool, manipVisible=bool, pinPivot=bool, snapPivotPos=bool, orientObject="string", editPivotPosition=bool, postDragCommand="string", pivotOriHandle=bool, postCommand="string", activeHandle=int, preserveUV=bool, preCommand="string", reflection=bool, preserveChildPosition=bool, snapPivotOri=bool, image2="string"):
    """
    manipScaleContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a scale manip context.

    """
    pass
    


def manipScaleLimitsCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    manipScaleLimitsCtx is undoable, queryable, and editable.
    

    
Create a context for the scale limits manipulator.

    """
    pass
    


def marker(string, valueU=float, time=(), orientationMarker=bool, sideTwist=int, frontTwist=int, attach=bool, positionMarker=bool, upTwist=int, detach=bool):
    """
    marker is undoable, queryable, and editable.
    

    
The marker command creates one or two markers, on a motion path curve, at the specified time and location. The optionnal string argument is the parent object name.
One can specify "-pm -om" option to create both, a position marker and an orientation marker.
Since there is only one keyframe for each marker of the same type, no more than one marker of the same type with the same time value can exist.
The default marker type is the position marker. The default time is the current time.

    """
    pass
    


def matchTransform(objects, scale=bool, rotation=bool, pivots=bool, position=bool):
    """
    matchTransform is undoable, NOT queryable, and NOT editable.
    

    
This command modifies the source object's transform to match the target object's transform.
If no flags are specified then the command will match position, rotation and scaling.

    """
    pass
    


def mayaDpiSetting(scaleValue=float, mode=int, systemDpi=bool, realScaleValue=bool):
    """
    mayaDpiSetting is NOT undoable, queryable, and NOT editable.
    

    
Provide Maya interface scaling based on system DPI or custom scale setting or no scaling. Please note that the change will only take effect after relaunching Maya.

    """
    pass
    


def melInfo():
    """
    melInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns the names of all global MEL procedures that are currently defined as a string array. The user can query the definition of each MEL procedure using the "whatIs" command.

    """
    pass
    


def melOptions(duplicateVariableWarnings=bool):
    """
    melOptions is NOT undoable, queryable, and NOT editable.
    

    
Set and query options that affect the behavior of Maya's Embedded Language (MEL).

    """
    pass
    


def memory(pageFaults=bool, physicalMemory=bool, swapLogical=bool, summary=bool, pageReclaims=bool, swapPhysical=bool, kiloByte=bool, megaByte=bool, swapFree=bool, freeMemory=bool, swapMax=bool, swapVirtual=bool, gigaByte=bool, heapMemory=bool, swaps=bool, asFloat=bool):
    """
    memory is undoable, NOT queryable, and NOT editable.
    

    
Used to query essential statistics on memory availability and usage.
By default memory sizes are returned in bytes. Since Maya's command engine only supports 32-bit signed integers, any returned value which cannot fit into 31 bits will be truncated to 2,147,483,647 and a warning message displayed. To avoid having memory sizes truncated use one of the memory size flags to return the value in larger units (e.g. megabytes) or use the asFloat flag to return the value as a float.

    """
    pass
    


def menu(string, tearOff=bool, docTag="string", postMenuCommand="string", visible=bool, enable=bool, defineTemplate="string", mnemonic="string", helpMenu=bool, numberOfItems=bool, useTemplate="string", label="string", familyImage="string", itemArray=bool, ltVersion="string", allowOptionBoxes=bool, postMenuCommandOnce=bool, version="string", exists=bool, parent="string", deleteAllItems=bool):
    """
    menu is undoable, queryable, and editable.
    

    
This command creates a new menu and adds it to the default window's menubar if no parent is specified. The menu can be enabled/disabled. Note that this command may also be used on menu objects created using the command menuItem -sm/subMenu true.

    """
    pass
    


def menuBarLayout(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", numberOfChildren=bool, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, childArray=bool, exists=bool, numberOfMenus=bool, visible=bool, enableBackground=bool, visibleChangeCommand="string", menuArray=bool, fullPathName=bool, dropCallback="string", menuBarVisible=bool, noBackground=bool, backgroundColor=float, manage=bool, menuIndex="string", isObscured=bool):
    """
    menuBarLayout is undoable, queryable, and editable.
    

    
Create a layout containing a menu bar. The menu bar will appear and behave similar to any menu bar created with the 'window -menuBar true' command. Menus may be created with a menuBarLayout as their parent. Child controls are simply positioned to fill the menuBarLayout area beneath the menu bar consequently, some other layout should be used as the immediate child.

    """
    pass
    


def menuEditor(string, docTag="string", height=int, delete="string", checkBoxPresent=bool, defineTemplate="string", parent="string", radioButtonState=bool, image="string", numberOfPopupMenus=bool, useTemplate="string", manage=bool, label="string", highlightColor=float, dragCallback="string", annotation="string", checkBoxState=bool, cellWidthHeight=int, preventOverride=bool, popupMenuArray=bool, topLevelMenu="string", radioButtonPresent=bool, subMenuEditorsOpen=bool, subMenuEditorWindow="string", cellHeight=int, exists=bool, subMenuAt="string", menuItemTypes=bool, enableBackground=bool, iconMenuCallback="string", optionBoxPresent=bool, visibleChangeCommand="string", visible=bool, subMenuOf="string", enable=bool, fullPathName=bool, dropCallback="string", separator="string", noBackground=bool, backgroundColor=float, cellWidth=int, command="string", style="string", width=int, isObscured=bool, optionBoxCommand="string"):
    """
    menuEditor is undoable, queryable, and editable.
    

    
A menuEditor displays the contents of a popup menu and allows the menu's items to be edited. Menu items are represented by labelled icons which can be dragged around within the editor to change the menu's layout. Various objects can be dragged and dropped into the menuEditor to create new menu items: toolButtons from the shelf or toolbox, shelfButtons from the shelf, iconTextButtons with attached commands, and scripts from the command window.
When editing a Marking Menu, the radial menu items correspond to 8 icons arranged in a circle within the menuEditor. Overflow items in the Marking Menu (or linear items in a normal menu) are displayed in a column below the radial items.
To edit a submenu of a popup menu, a new menuEditor instance must be created (typically within its own window) and attached to its parent menuEditor.
Some flags require the position of a menu item to be passed in as an argument. For these, positions are specified with a (string,int) pair, where the string corresponds to a radial position (possibily "None") and the int corresponds to a linear position (possibly equal to 0 for none). Radial positions are specified by one of ("N",0), ("NE",0), ("E",0), ("SE",0), ("S",0), ("SW",0), ("W",0) or ("NW",0). Overflow, or linear positions, are specified with ("None",i), where i is a 1-based index giving the position of the item within the overflow column.
Note: This command is not meant to be called explicitly. It was created to support the Marking Menu editor. It is recommended that you use that editor to modify marking menus.

    """
    pass
    


def menuItem(string, tearOff=bool, docTag="string", isCheckBox=bool, defineTemplate="string", dragDoubleClickCommand="string", longDivider=bool, image="string", useTemplate="string", altModifier=bool, label="string", italicized=bool, data=int, imageOverlayLabel="string", annotation="string", enable=bool, postMenuCommandOnce=bool, familyImage="string", parent="string", insertAfter="string", exists=bool, optionModifier=bool, optionBoxIcon="string", isRadioButton=bool, echoCommand=bool, subMenu=bool, ltVersion="string", collection="string", shiftModifier=bool, radialPosition="string", boldFont=bool, allowOptionBoxes=bool, sourceType="string", checkBox=bool, enableCommandRepeat=bool, dragMenuCommand="string", radioButton=bool, postMenuCommand="string", dividerLabel="string", divider=bool, commandModifier=bool, command="string", isOptionBox=bool, version="string", optionBox=bool, keyEquivalent="string", ctrlModifier=bool):
    """
    menuItem is undoable, queryable, and editable.
    

    
This command creates/edits/queries menu items.

    """
    pass
    


def menuSet(object, allMenuSets=bool, removeMenuSet="string", moveMenu="string", numberOfMenuSets=bool, moveMenuSet="string", exists="string", addMenu="string", permanent=bool, label="string", insertMenu="string", hotBoxVisible=bool, numberOfMenus=bool, removeMenu="string", currentMenuSet="string", menuArray="string"):
    """
    menuSet is undoable, queryable, and editable.
    

    
Create a menu set which is used to logically order menus for display in the main menu bar. Such menu sets can be edited and reordered dynamically.

    """
    pass
    


def menuSetPref(object, version=bool, removeAll=bool, force=bool, saveBackup=bool, loadAll=bool, saveAll=bool, exists=bool):
    """
    menuSetPref is undoable, queryable, and editable.
    

    
Provides the functionality to save and load menuSets between sessions of Maya. For Internal Use Only!

    """
    pass
    


def messageLine(name, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", backgroundColor=float, noBackground=bool, manage=bool, isObscured=bool):
    """
    messageLine is undoable, queryable, and editable.
    

    
This command creates a message line where tool feedback is shown.

    """
    pass
    


def minimizeApp():
    """
    minimizeApp is undoable, NOT queryable, and NOT editable.
    

    
This command minimizes (iconifies) all of the application's windows into a single desktop icon. To restore the application click on the desktop icon.

    """
    pass
    


def mirrorJoint(mirrorYZ=bool, mirrorXZ=bool, searchReplace="string", mirrorBehavior=bool, mirrorXY=bool):
    """
    mirrorJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will duplicate a branch of the skeleton from the selected joint symmetrically about a plane in world space. There are three mirroring modes(xy-, yz-, xz-plane).

    """
    pass
    


def modelCurrentTimeCtx(image1="string", history=bool, exists=bool, percent=float, image2="string", name="string", image3="string"):
    """
    modelCurrentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the model views.

    """
    pass
    


def modelEditor(editorName, docTag="string", height=int, hairSystems=bool, textureDisplay="string", joints=bool, setSelected=bool, useTemplate="string", toggleGamma=bool, fogStart=float, cullingOverride="string", occlusionCulling=bool, panel="string", cameraSetup=bool, shadows=bool, jointXray=bool, updateColorMode=bool, smoothWireframe=bool, fogEnd=float, viewType=bool, fogColor=float, selectionHiliteDisplay=bool, textures=bool, isFiltered=bool, grid=bool, addObjects="string", resetCustomCamera=bool, textureAnisotropic=bool, noUndo=bool, forceMainConnection="string", displayTextures=bool, fogSource="string", dynamics=bool, wireframeOnShaded=bool, textureSampling=int, defineTemplate="string", parent="string", bumpResolution=int, motionTrails=bool, sceneRenderFilter="string", rendererOverrideListUI=bool, nCloths=bool, fluids=bool, ikHandles=bool, xray=bool, transpInShadows=bool, toggleExposure=bool, lowQualityLighting=bool, displayLights="string", exposure=float, stateString=bool, deformers=bool, textureMaxSize=int, maxConstantTransparency=float, fogMode="string", control=bool, hulls=bool, colorMap=bool, useBaseRenderer=bool, activeCustomOverrideGeometry="string", selectionConnection="string", useColorIndex=bool, objectFilter="string", userNode="string", viewTransformName="string", manipulators=bool, objectFilterUI="string", sortTransparent=bool, twoSidedLighting=bool, interactive=bool, colorResolution=int, rendererOverrideName="string", viewObjects=bool, controlVertices=bool, allObjects=bool, objectFilterShowInHUD=bool, lockMainConnection=bool, editorChanged="string", removeSelected=bool, pluginObjects="string", dynamicConstraints=bool, modelPanel="string", mainListConnection="string", activeCustomLighSet="string", objectFilterList="string", nRigids=bool, updateMainConnection=bool, transparencyAlgorithm="string", polymeshes=bool, textureMemoryUsed=bool, ignorePanZoom=bool, fogDensity=float, follicles=bool, addSelected=bool, activeCustomGeometry="string", lineWidth=float, locators=bool, unlockMainConnection=bool, pivots=bool, fogging=bool, objectFilterListUI="string", nurbsCurves=bool, lights=bool, cameras=bool, bufferMode="string", rendererListUI=bool, rendererDeviceName=bool, activeCustomEnvironment="string", width=int, filteredObjectList=bool, unParent=bool, planes=bool, activeView=bool, camera="string", nurbsSurfaces=bool, headsUpDisplay=bool, highlightConnection="string", dimensions=bool, handles=bool, subdivSurfaces=bool, exists=bool, imagePlane=bool, rendererList=bool, viewSelected=bool, pluginShapes=bool, captureSequenceNumber=int, nParticles=bool, gamma=float, useDefaultMaterial=bool, strokes=bool, activeCustomRenderer="string", activeOnly=bool, backfaceCulling=bool, activeShadingGraph="string", wireframeBackingStore=bool, useInteractiveMode=bool, useRGBImagePlane=bool, queryPluginObjects="string", rendererOverrideList=bool, activeComponentsXray=bool, default=bool, capture="string", cmEnabled=bool, textureHilight=bool, cameraName="string", rendererName="string", filter="string", displayAppearance="string"):
    """
    modelEditor is undoable, queryable, and editable.
    

    
Create, edit or query a model editor.
Note that some of the flags of this command may have different settings for normal mode and for interactive/playback mode. For example, a modelEditor can be set to use shaded mode normally, but to use wireframe during playback for greater speed. Some flags also support having defaults set so that new model editors will be created with those settings.

    """
    pass
    


def modelPanel(barLayout=bool, docTag="string", defineTemplate="string", parent="string", useTemplate="string", tearOff=bool, label="string", replacePanel="string", unParent=bool, tearOffCopy="string", camera="string", isUnique=bool, createString=bool, needsInit=bool, exists=bool, control=bool, menuBarVisible=bool, init=bool, modelEditor=bool, tearOffRestore=bool, popupMenuProcedure="string", editString=bool, copy="string"):
    """
    modelPanel is undoable, queryable, and editable.
    

    
This command creates a panel consisting of a model editor. See the modelEditor command documentation for more information.

    """
    pass
    


def moduleInfo(moduleName="string", version=bool, definition=bool, listModules=bool, path=bool):
    """
    moduleInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns information on modules found by Maya.

    """
    pass
    


def mouse(mouseButtonTracking=int, scrollWheelStatus=bool, enableScrollWheel=bool, mouseButtonTrackingStatus=bool):
    """
    mouse is undoable, NOT queryable, and NOT editable.
    

    
This command allows to configure mouse.

    """
    pass
    


def move(floatfloatfloatobjects, reflectionAboutZ=bool, moveXZ=bool, symNegative=bool, scalePivotRelative=bool, localSpace=bool, reflectionAboutBBox=bool, rotatePivotRelative=bool, relative=bool, reflectionTolerance=float, reflectionAboutX=bool, xformConstraint="string", secondaryAxisOrient="string", moveY=bool, parameter=bool, objectSpace=bool, moveX=bool, orientJoint="string", moveXY=bool, constrainAlongNormal=bool, moveXYZ=bool, componentSpace=bool, preserveGeometryPosition=bool, worldSpaceDistance=bool, absolute=bool, preserveUV=bool, worldSpace=bool, reflection=bool, deletePriorHistory=bool, moveZ=bool, preserveChildPosition=bool, reflectionAboutOrigin=bool, moveYZ=bool, reflectionAboutY=bool):
    """
    move is undoable, NOT queryable, and NOT editable.
    

    
The move command is used to change the positions of geometric objects.
The default behaviour, when no objects or flags are passed, is to do a absolute move on each currently selected object in the world space. The value of the coordinates are interpreted as being defined in the current linear unit unless the unit is explicitly mentioned.
When using -objectSpace there are two ways to use this command. If numbers are typed without units then the internal values of the object are set to these values. If, on the other hand a unit is specified then the internal value is set to the equivalent internal value that represents that world-space distance.
The -localSpace flag moves the object in its parent space. In this space the x,y,z values correspond directly to the tx, ty, tz channels on the object.
The -rotatePivotRelative/-scalePivotRelative flags can be used with the -absolute flag to translate an object so that its pivot point ends up at the given absolute position. These flags will be ignored if components are specified.
The -worldSpaceDistance flag is a modifier flag that may be used in conjunction with the -objectSpace/-localSpace flags. When this flag is specified the command treats the x,y,z values as world space units so the object will move the specified world space distance but it will move along the axis specified by the -objectSpace/-localSpace flag. The default behaviour, without this flag, is to treat the x,y,z values as units in object space or local space. In other words, the worldspace distance moved will depend on the transformations applied to the object unless this flag is specified.

    """
    pass
    


def moveKeyCtx(image1="string", moveFunction="string", history=bool, exists=bool, option="string", image2="string", name="string", image3="string"):
    """
    moveKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to move keyframes within the graph editor

    """
    pass
    


def moveVertexAlongDirection(vDirection="string", magnitude="string", uDirection="string", uvNormalDirection="string", normalDirection="string", direction=float):
    """
    moveVertexAlongDirection is undoable, NOT queryable, and NOT editable.
    

    
The command moves the selected vertex ( control vertex ) in the specified unit direction by the given magnitude. The vertex(ices) may also be moved in the direction of unit normal ( -n flag ). For NURBS surface vertices the direction of movement could also be either in tangent along U or tangent along V. The flags -n, -u, -v and -d are mutually exclusive, ie. the selected vertices can be all moved in only -n or -u or -v or -d.

    """
    pass
    


def movieInfo(numFrames=bool, frameCount=bool, negTimesOK=bool, quickTime=bool, width=bool, timeCode=bool, dropFrame=bool, timeScale=bool, movieTexture=bool, height=bool, timeCodeTrack=bool, twentyFourHourMax=bool, counter=bool, frameDuration=bool):
    """
    movieInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
movieInfo provides a mechanism for querying information about movie files.

    """
    pass
    


def movIn(attributeList, file="string", startTime=()):
    """
    movIn is undoable, NOT queryable, and NOT editable.
    

    
Imports a .mov file into animation curves connected to the listed attributes. The attribute must be writable, since an animation curve will be created and connected to the attribute. If an animation curve already is connected to the attribute, the imported data is pasted onto that curve.
The starting time used for the .mov file importation is the current time when the command is executed.
Valid attribute types are numeric attributes; time attributes; linear attributes; angular attributes; compound attributes made of the types listed previously; and multi attributes composed of the types listed previously. If an unsuppoted attribute type is requested, the command will fail and no data will be imported. It is important that your user units are set to the same units used in the .mov file, otherwise linear and angular values will be incorrect.
To export a .mov file, use the movOut command.

    """
    pass
    


def movOut(targetList, time=(), precision=int, file="string", comment=bool):
    """
    movOut is undoable, NOT queryable, and NOT editable.
    

    
Exports a .mov file from the listed attributes. Valid attribute types are numeric attributes; time attributes; linear attributes; angular attributes; compound attributes made of the types listed previously; and multi attributes composed of the types listed previously.
Length, angle, and time values will be written to the file in the user units.
If an unsupported attribute type is requested, the action will fail. The .mov file may be read back into Maya using the movIn command.

    """
    pass
    


def multiProfileBirailSurface(transformMode=int, polygon=int, object=bool, tangentContinuityProfile2=bool, nodeState=int, constructionHistory=bool, tangentContinuityProfile1=bool, caching=bool, name="string"):
    """
    multiProfileBirailSurface is undoable, queryable, and editable.
    

    
The cmd creates a railed surface by sweeping the profiles using two rail curves. The two rails are the last two arguments. For examples, if 5 curves are specified, they will correspond to "curve1" "curve2" "curve3" "rail1" "rail2".
In this case, the cmd creates a railed surface by sweeping the profile "curve1" to profile "curve2", profile "curve2" to profile "curve3" along the two rail curves "rail1", "rail2". There must be atleast 3 profile curves followed by the two rail curves. The profile curves must intersect the two rail curves. The constructed may be made tangent continuous to the first and last profile using the flags -tp1, -tp2 provided the profiles are surface curves i.e. isoparms, curve on surface or trimmed edge.

    """
    pass
    


def multiTouch(trackpad=int, gestures=bool):
    """
    multiTouch is undoable, queryable, and NOT editable.
    

    
Used to interact with the Gestura (multi-touch) library.

    """
    pass
    


def mute(force=bool, disable=bool):
    """
    mute is undoable, queryable, and NOT editable.
    

    
The mute command is used to disable and enable playback on a channel. When a channel is muted, it retains the value that it was at prior to being muted.

    """
    pass
    


def nameCommand(string, data2="string", data3="string", default=bool, command="string", sourceType="string", annotation="string", data1="string"):
    """
    nameCommand is undoable, NOT queryable, and NOT editable.
    

    
This command creates a nameCommand object. Each nameCommand object can be connected to a hotkey. Thereafter, the nameCommand's command string will be executed whenever the hotkey is pressed (or released, as specified by the user).

    """
    pass
    


def nameField(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, nameChangeCommand="string", popupMenuArray=bool, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, object="string", drawInactiveFrame=bool, manage=bool, isObscured=bool, receiveFocusCommand="string"):
    """
    nameField is undoable, queryable, and editable.
    

    
This command creates an editable field that can be linked to the name of a Maya object. The field will always show the name of the object.

    """
    pass
    


def namespace(string, rename="string", relativeNames=bool, exists="string", force=bool, setNamespace="string", isRootNamespace="string", removeNamespace="string", deleteNamespaceContent=bool, mergeNamespaceWithRoot=bool, validateName="string", moveNamespace="string", recurse=bool, absoluteName=bool, addNamespace="string", parent="string", collapseAncestors="string", mergeNamespaceWithParent=bool):
    """
    namespace is undoable, queryable, and NOT editable.
    

    
This command allows a namespace to be created, set or removed.
A namespace is a simple grouping of objects under a given name. Namespaces are primarily used to resolve name-clash issues in Maya, where a new object has the same name as an existing object (from importing a file, for example). Using namespaces, you can have two objects with the same name, as long as they are contained in differenct namespaces.
Namespaces are reminiscent of hierarchical structures like file systems where namespaces are analogous to directories and objects are analogous to files. The colon (':') character is the separator used to separate the names of namespaces and nodes instead of the slash ('/') or backslash ('\') character. Namespaces can contain other namespaces as well as objects. Like objects, the names of namespaces must be unique within another namespace. Objects and namespaces can be in only one namespace. Namespace names and object names don't clash so a namespace and an object contained in another namespace can have the same name.
There is an unnamed root namespace specified with a leading colon (':'). Any object not in a named namespace is in the root namespace. Normally, the leading colon is omitted from the name of an object as it's presence is implied. The presence of a leading colon is important when moving objects between namespaces using the 'rename' command. For the 'rename' command, the new name is relative to the current namespace unless the new name is fully qualified with a leading colon.
Namespaces are created using the 'add/addNamespace' flag. By default they are created under the current namespace. Changing the current namespace is done with the 'set/setNamespace' flag. To reset the current namespace to the root namespace, use 'namespace -set ":";'. Whenever an object is created, it is added by default to the current namespace.
When creating a new namespace using a qualified name, any intervening namespaces which do not yet exist will be automatically created. For example, if the name of the new namespace is specified as "A:B" and the current namespace already has a child namespace named "A" then a new child namespace named "B" will be created under "A". But if the current namespace does not yet have a child named "A" then it will be created automatically. This applies regardless of the number of levels in the provided name (e.g. "A:B:C:D").
The 'p/parent' flag can be used to explicitly specify the parent namespace under which the new one should be created, rather than just defaulting to the current namespace.
If the name given for the new namespace is absolute (i.e. it begins with a colon, as in ":A:B") then both the current namespace and the 'parent' flag will be ignored and the new namespace will be created under the root namespace.
The relativeNamespace flag can be used to change the way node names are displayed in the UI and returned by the 'ls' command. Here are some specific details on how the return from the 'ls' command works in relativeNamespace mode:
List all mesh objects in the scene:
ls -type "mesh";
The above command lists all mesh objects in the root and any child namespaces. In relative name lookup mode, all names will be displayed relative to the current namespace. When not in relative name lookup mode (the default behaviour in Maya), results are printed relative to the root namespace.

Using a "*" wildcard:
namespace -set myNS;
ls -type "mesh "*";


In relative name lookup mode, the "*" will match to the current namespace and thus the ls command will list only those meshes defined within the current namespace (i.e. myNs). If relative name lookup is off (the default behaviour in Maya), names are root-relative and thus "*" matches the root namespace, with the net result being that only thoses meshes defined in the root namespace will be listed.

You can force the root namespace to be listed when in relative name lookup mode by specifying ":*" as your search pattern (i.e. ls -type mesh ":*" which lists those meshes defined in the root namespace only). Note that you can also use ":*" when relative name lookup mode is off to match the root if you want a consistent way to list the root.

Listing child namespace contents:
ls -type mesh "*:*";


For an example to list all meshes in immediate child namespaces, use "*:*". In relative name lookup mode "*:*" lists those meshes in immediate child namespaces of the current namespaces. When not in relative name lookup mode, "*:*" lists meshes in namespaces one level below the root.

Recursive listing of namespace contents:
Example: ls -type mesh -recurse on "*"


The 'recurse' flag is provided on the "ls" command to recursively traverse any child namespaces. In relative name lookup mode, the above example command will list all meshes in the current and any child namespaces of current. When not in relative name lookup mode, the above example command works from the root downwards and is thus equivalent to "ls -type mesh".

    """
    pass
    


def namespaceInfo(shortName=bool, listNamespace=bool, baseName=bool, isRootNamespace="string", internal=bool, listOnlyNamespaces=bool, currentNamespace=bool, fullName=bool, recurse=bool, listOnlyDependencyNodes=bool, absoluteName=bool, parent=bool, dagPath=bool):
    """
    namespaceInfo is undoable, NOT queryable, and NOT editable.
    

    
This command displays information about a namespace. The target namespace can optionally be specified on the command line. If no namespace is specified, the command will display information about the current namespace.
A namespace is a simple grouping of objects under a given name. Each item in a namespace can then be identified by its own name, along with what namespace it belongs to. Namespaces can contain other namespaces like sets, with the restriction that all namespaces are disjoint.
Namespaces are primarily used to resolve name-clash issues in Maya, where a new object has the same name as an existing object (from importing a file, for example). Using namespaces, you can have two objects with the same name, as long as they are contained in different namespaces.
Note that namespaces are a simple grouping of names, so they do not effect selection, the DAG, the Dependency Graph, or any other aspect of Maya. All namespace names are colon-separated.
The namespace format flags are: "baseName"("shortName"), "fullName" and "absoluteName". The flags are used in conjunction with the main query flags to specify the desired namespace format of the returned result. They can also be used to return the different formats of a specified namespace. By default, when no format is specified, the result will be returned as a full name.

    """
    pass
    


def nBase(stuffStart=bool, clearStart=bool, clearCachedTextureMap="string", textureToVertex="string"):
    """
    nBase is undoable, queryable, and editable.
    

    
Edits one or more nBase objects. Note that nBase objects include nCloth, nRigid and nParticle objects, but the options on this command do not currently apply to nParticle objects.

    """
    pass
    


def newton(magnitude=float, position="string", perVertex=bool, attenuation=float, maxDistance="string", minDistance=float, name="string"):
    """
    newton is undoable, queryable, and editable.
    

    
A Newton field pulls an object towards the exerting object with force dependent on the exerting object's mass, using Newton's universal law of gravitation.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def nodeCast(disableScriptJobCallbacks=bool, force=bool, disconnectUnmatchedAttrs=bool, copyDynamicAttrs=bool, swapValues=bool, swapNames=bool, disableAPICallbacks=bool):
    """
    nodeCast is undoable, NOT queryable, and NOT editable.
    

    
Given two nodes, a source node of type A and a target node of type B, where type A is either type B or a sub-type of B, this command will replace the target node with the source node. That is, all node connections, DAG hierarchy and attribute values on the target node will be removed from the target node and placed on the source node. This operation will fail if either object is referenced, locked or if the nodes do not share a common sub-type. This operation is atomic. If the given parameters fail, then the source and target nodes will remain in their initial state prior to execution of the command. IMPORTANT: the command will currently ignore instance connections and instance objects. It will also ignore reference nodes.

    """
    pass
    


def nodeEditor( string, docTag="string", feedbackTabIndex=bool, graphSelection=bool, useTemplate="string", downstream=bool, panel="string", selectFeedbackConnection=bool, dotFormat="string", toggleSelectedPins=bool, layout=bool, rootsFromSelection=bool, showShapes=bool, allowTabTearoff=bool, useAssets=bool, removeUnselected=bool, allowNewTabs=bool, tabChangeCommand="string", shaderNetworks=bool, toggleAttrFilter=bool, forceMainConnection="string", selectUpstream=bool, pinSelectedNodes=bool, backToParentView=bool, island=bool, ignoreAssets=bool, panView=float, beginNewConnection="string", scaleView=float, selectNode="string", restoreLastClosedTab=bool, popupMenuScript="string", addNode="string", settingsChangedCallback="string", defineTemplate="string", parent="string", selectDownstream=bool, vnnRuntime=bool, beginCreateNode=bool, renameTab=int, selectAll=bool, stateString=bool, renameNode="string", defaultPinnedState=bool, cycleHUD=bool, control=bool, nodeViewMode="string", feedbackType=bool, createInfo="string", unParent=bool, selectionConnection="string", autoSizeNodes=bool, removeNode="string", nodeTitleMode="string", closeAllTabs=bool, allAttributes=bool, keyPressCommand="string", showNamespace=bool, addNewNodes=bool, removeDownstream=bool, lockMainConnection=bool, feedbackConnection=bool, selectConnectionNodes=bool, showAllNodeAttributes="string", consistentNameSize=bool, mainListConnection="string", activeTab=int, focusCommand="string", primary=bool, openContainerView="string", allNodes=bool, nodeSwatchSize="string", showTabs=bool, customAttributeListEdit="string", feedbackPlug=bool, createNodeCommand="string", getNodeList=bool, toolTipCommand="string", contentsChangedCommand="string", updateMainConnection=bool, frameModelSelection=bool, gridVisibility=bool, graphSelectedConnections=bool, additiveGraphingMode=bool, traversalDepthLimit=int, breakSelectedConnections=bool, hudMessage="string", filterCreateNodeTypes="string", keyReleaseCommand="string", vnnDgContainer=bool, inContainerView=bool, feedbackNode=bool, upstream=bool, unlockMainConnection=bool, showTransforms=bool, isContainerNode="string", removeUpstream=bool, highlightConnection="string", restoreInfo="string", extendToShapes=bool, exists=bool, redockTab=bool, frameAll=bool, showSGShapes=bool, createTab=int, vnnCompound=bool, frameSelected=bool, duplicateTab=int, deleteSelected=bool, rootNode="string", toggleSwatchSize="string", layoutCommand="string", syncedSelection=bool, closeTab=int, gridSnap=bool, filter="string"):
    """
    nodeEditor is undoable, queryable, and editable.
    

    
This command creates/edits/queries a nodeEditor editor. The optional argument is the name of the control.

    """
    pass
    


def nodeIconButton(string, docTag="string", height=int, useAlpha=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", image3="string", highlightColor=float, imageOverlayLabel="string", overlayLabelBackColor=float, disabledImage="string", annotation="string", enable=bool, image1="string", popupMenuArray=bool, labelOffset=int, flipX=bool, font="string", exists=bool, rotation=float, flipY=bool, marginHeight=int, ltVersion="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, marginWidth=int, preventOverride=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, align="string", manage=bool, command="string", style="string", version="string", image2="string", isObscured=bool, overlayLabelColor=float):
    """
    nodeIconButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates a button that can be displayed with different icons, with or without a text label. If the button is drag and dropped onto other controls (e.g., HyperShade), the command will be executed and the return string will be used as the name of a dropped node.

    """
    pass
    


def nodeOutliner(string, replace="string", docTag="string", height=int, defineTemplate="string", parent="string", lastMenuChoice="string", numberOfPopupMenus=bool, connectivity="string", width=int, dragCallback="string", showConnectedOnly=bool, highlightColor=float, annotation="string", enable=bool, longNames=bool, preventOverride=bool, nodesDisplayed=bool, showNonKeyable=bool, showInputs=bool, showOutputs=bool, attrAlphaOrder="string", pressHighlightsUnconnected=bool, menuCommand="string", exists=bool, showPublished=bool, showNonConnectable=bool, showHidden=bool, multiSelect=bool, addObject="string", niceNames=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, useTemplate="string", noBackground=bool, fullPathName=bool, dropCallback="string", selectCommand="string", popupMenuArray=bool, addCommand="string", removeAll=bool, backgroundColor=float, noConnectivity=bool, manage=bool, showReadOnly=bool, menuMultiOption=bool, isObscured=bool, currentSelection=bool, remove="string"):
    """
    nodeOutliner is undoable, queryable, and editable.
    

    
The nodeOutliner command creates, edits and queries an outline control that shows dependency nodes and their attributes. Compound attributes are further expandable to show their children. Additional configure flags allow multi selection, customizable commands to issue upon selection, and showing connections (and connectability) to a single input attribute. There are also the abilities to add/remove/replace nodes through the command line interface, and drag/add.
In some configurations, dragging a connected attribute of a node will load the node at the other end of the connection.
There is a right mouse button menu and a flag to attach a command to it. The menu is used to list the specific connections of a connected attribute. Clicking over any spot but the row of a connected attribute will show an empty menu. By default, there is no command attached to the menu.

    """
    pass
    


def nodePreset(delete="string", exists="string", isValidName="string", attributes="string", custom="string", save="string", load="string", list="string"):
    """
    nodePreset is NOT undoable, NOT queryable, and NOT editable.
    

    
Command to save and load preset settings for a node. This command allows you to take a snapshot of the values of all attributes of a node and save it to disk as a preset with user specified name. Later the saved preset can be loaded and applied onto a different node of the same type. The end result is that the node to which the preset is applied takes on the same values as the node from which the preset was generated had at the time of the snapshot.

    """
    pass
    


def nodeTreeLister(string, vnnString=bool, docTag="string", height=int, defineTemplate="string", parent="string", clearContents=bool, addVnnItem="string", numberOfPopupMenus=bool, useTemplate="string", favoritesList=bool, width=int, highlightColor=float, dragCallback="string", favoritesCallback="string", collapsePath="string", annotation="string", preventOverride=bool, popupMenuArray=bool, refreshCommand="string", addFavorite="string", exists=bool, resultsPathUnderCursor=bool, nodeLibrary="string", executeItem="string", enable=bool, enableBackground=bool, selectPath="string", visibleChangeCommand="string", visible=bool, expandPath="string", itemScript="string", removeItem="string", fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, removeFavorite="string", addItem="string", manage=bool, expandToDepth=int, isObscured=bool):
    """
    nodeTreeLister is undoable, queryable, and editable.
    

    
This command creates/edits/queries the node tree lister control. nodeTreeLister is a treeLister, but items are assumed to have commands which return dependency node names. Dragging from the results pane is supported.
The optional argument is the name of the control.

    """
    pass
    


def nodeType(derived=bool, inherited=bool, apiType=bool, isTypeName=bool):
    """
    nodeType is undoable, NOT queryable, and NOT editable.
    

    
This command returns a string which identifies the given node's type.
When no flags are used, the unique type name is returned. This can be useful for seeing if two nodes are of the same type.
When the api flag is used, the MFn::Type of the node is returned. This can be useful for seeing if a plug-in node belongs to a given class. The api flag cannot be used in conjunction with any other flags.
When the derived flag is used, the command returns a string array containing the names of all the currently known node types which derive from the node type of the given object.
When the inherited flag is used, the command returns a string array containing the names of all the base node types inherited by the the given node.
If the isTypeName flag is present then the argument provided to the command is taken to be the name of a node type rather than the name of a specific node. This makes it possible to query the hierarchy of node types without needing to have instances of each node type.

    """
    pass
    


def nonLinear(before=bool, exclusive="string", geometryIndices=bool, after=bool, type="string", autoParent=bool, ignoreSelected=bool, split=bool, commonParent=bool, afterReference=bool, deformerTools=bool, parallel=bool, includeHiddenSelections=bool, frontOfChain=bool, geometry="string", remove=bool, prune=bool, defaultScale=bool, name="string"):
    """
    nonLinear is undoable, queryable, and editable.
    

    
This command creates a functional deformer of the specified type that will deform the selected objects. The deformer consists of three nodes: The deformer driver that gets connected to the history of the selected objects, the deformer handle transform that controls position and orientation of the axis of the deformation and the deformer handle that maintains the deformation parameters. The type of the deformer handle shape created depends on the specified type of the deformer. The deformer handle will be positioned at the center of the selected objects' bounding box and oriented to match the orientation of the leading object in the selection list. The deformer handle transform will be selected when the command is completed.
The nonLinear command has some flags which are specific to the nonLinear type specified with the -type flag. The flags correspond to the primary keyable attributes related to the specific type of nonLinear node. For example, if the type is "bend", then the flags "-curvature", "-lowBound" and "-highBound" may be used to initialize, edit or query those attribute values on the bend node. Examples of this are covered in the example section below.

    """
    pass
    


def normalConstraint(targetobject, worldUpObject="string", worldUpVector=float, remove=bool, worldUpType="string", weightAliasList=bool, layer="string", targetList=bool, upVector=float, aimVector=float, weight=float, name="string"):
    """
    normalConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation based on the normal of the target surface(s) at the closest point(s) to the object.
A normalConstraint takes as input one or more surface shapes (the targets) and a DAG transform node (the object). The normalConstraint orients the constrained object such that the aimVector (in the object's local coordinate system) aligns in world space to combined normal vector. The upVector (again the the object's local coordinate system) is aligned in world space with the worldUpVector. The combined normal vector is a weighted average of the normal vector for each target surface at the point closest to the constrained object.

    """
    pass
    


def nParticle(upperRight="string", particleId=int, perParticleDouble=bool, inherit=float, vectorValue=float, order=int, conserve=float, name="string", numJitters=int, dynamicAttrList=bool, deleteCache=bool, jitterRadius="string", shapeName="string", attribute="string", jitterBasePoint="string", count=bool, cache=bool, lowerLeft="string", perParticleVector=bool, position="string", floatValue=float, gridSpacing="string"):
    """
    nParticle is undoable, queryable, and editable.
    

    
The nParticle command creates a new nParticle object from a list of world space points. If an nParticle object is created, the command returns the names of the new particle shape and its associated particle object dependency node. If an object was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.

    """
    pass
    


def nSoft(goal=float, convert=bool, hideOriginal=bool, duplicate=bool, duplicateHistory=bool):
    r"""
    nSoft is undoable, queryable, and NOT editable.
    

    
Makes a nSoft body from the object(s) passed on the command line or in the selection list. The geometry can be a NURBS, polygonal, lattice object. The resulting nSoft body is made up of a hierarchy with a particle shape and a geometry shape, thus:
                              T    
            / \  
           T   G 
          /      
        P        
                  Dynamics are applied to the particle shape and the resulting particle positions then drive the locations of the geometry's CVs, vertices, or lattice points.
With the convert option, the particle shape and its transform are simply inserted below the original shape's hierarchy. With the duplicate option, the original geometry's transform and shape are duplicated underneath its parent, and the particle shape is placed under the duplicate. Note that any animation on the hierarchy will affect the particle shape as well. If you do not want them, then reparent the structure outside the hierarchy.
When duplicating, the nSoft portion (the duplicate) is given the name "copyOf" + "original object name". The particle portion is always given the name "original object name" + "Particles."
None of the flags of the nSoft command can be queried. The nSoft -q command is used only to identify when an object is a nSoft body, or when two objects are part of the same nSoft body. See the examples.

    """
    pass
    


def nurbsBoolean(smartConnection=bool, caching=bool, object=bool, nodeState=int, constructionHistory=bool, operation=int, nsrfsInFirstShell=int, tolerance="string", name="string"):
    """
    nurbsBoolean is undoable, queryable, and editable.
    

    
This command performs a boolean operation.

    """
    pass
    


def nurbsCopyUVSet():
    """
    nurbsCopyUVSet is undoable, queryable, and editable.
    

    
This is only a sample command for debugging purposes, which makes a copy of the implicit st parameterization on a nurbs surface to be the 1st explicit uvset.

    """
    pass
    


def nurbsCube(degree=int, axis="string", pivot="string", width="string", lengthRatio=float, object=bool, nodeState=int, patchesV=int, name="string", heightRatio=float, patchesU=int, caching=bool, constructionHistory=bool, polygon=int):
    """
    nurbsCube is undoable, queryable, and editable.
    

    
The nurbsCube command creates a new NURBS Cube made up of six planes. It creates an unit cube with center at origin by default.

    """
    pass
    


def nurbsCurveToBezier():
    """
    nurbsCurveToBezier is undoable, NOT queryable, and NOT editable.
    

    
The nurbsCurveToBezier command attempts to convert an existing NURBS curve to a Bezier curve.

    """
    pass
    


def nurbsEditUV(angle=float, pivotU=float, uValue=float, scaleU=float, vValue=float, pivotV=float, scaleV=float, relative=bool, rotation=bool, scale=bool):
    """
    nurbsEditUV is undoable, queryable, and NOT editable.
    

    
Command edits uvs on NURBS objects. When used with the query flag, it returns the uv values associated with the specified components.

    """
    pass
    


def nurbsPlane(degree=int, axis="string", pivot="string", width="string", lengthRatio=float, object=bool, nodeState=int, patchesV=int, name="string", patchesU=int, caching=bool, constructionHistory=bool, polygon=int):
    """
    nurbsPlane is undoable, queryable, and editable.
    

    
The nurbsPlane command creates a new NURBS Plane and return the name of the new surface. It creates an unit plane with center at origin by default.

    """
    pass
    


def nurbsSelect(leftBorder=bool, bottomBorder=bool, growSelection=int, borderSelection=bool, topBorder=bool, shrinkSelection=int, rightBorder=bool):
    """
    nurbsSelect is NOT undoable, NOT queryable, and NOT editable.
    

    
Performs selection operations on NURBS objects.
If any of the border flags is set, then the appropriate borders are selected. Otherwise the current CV selection is used, or all CVs if the surfaces is selected as an object.
The growSelection, shrinkSelection, borderSelection flags are then applied in that order.
In practice, it is recommended to use one flag at a time, except for the border flags.

    """
    pass
    


def nurbsSquare(degree=int, normalY="string", spansPerSide=int, centerY="string", normal="string", object=bool, name="string", sideLength1="string", centerZ="string", nodeState=int, centerX="string", center="string", sideLength2="string", normalX="string", normalZ="string", caching=bool, constructionHistory=bool):
    """
    nurbsSquare is undoable, queryable, and editable.
    

    
The nurbsSquare command creates a square

    """
    pass
    


def nurbsToPoly(surface, name="string", matchNormalDir=bool, uNumber=int, delta="string", useChordHeight=bool, fractionalTolerance=float, uType=int, chordHeight="string", edgeSwap=bool, chordHeightRatio=float, normalizeTrimmedUVRange=bool, polygonCount=int, vType=int, vNumber=int, minEdgeLength="string", polygonType=int, format=int, useChordHeightRatio=bool, object=bool, constructionHistory=bool):
    """
    nurbsToPoly is undoable, queryable, and editable.
    

    
This command tesselates a NURBS surface and produces a polygonal surface. The name of the new polygonal surface is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def nurbsToPolygonsPref(chordHeight=float, uNumber=int, polyCount=int, useChordHeightRatio=bool, fraction=float, matchRenderTessellation=int, uType=int, merge=int, edgeSwap=bool, chordHeightRatio=float, polyType=int, useChordHeight=bool, vNumber=int, minEdgeLen=float, format=int, mergeTolerance=float, vType=int, delta3D=float):
    """
    nurbsToPolygonsPref is undoable, queryable, and NOT editable.
    

    
This command sets the values used by the nurbs-to-polygons (or "tesselate") preference. This preference is used by Maya menu items and is saved between Maya sessions. To query any of the flags, use the "-query" flag. For more information on the flags, see the node documentation for the "nurbsTessellate" node.

    """
    pass
    


def nurbsToSubdiv(surface, object=bool, constructionHistory=bool, name="string"):
    """
    nurbsToSubdiv is undoable, queryable, and editable.
    

    
This command converts a NURBS surface and produces a subd surface. The name of the new subdivision surface is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def nurbsToSubdivPref(trans32=float, matchPeriodic=bool, trans20=float, trans31=float, trans11=float, bridge=int, trans12=float, offset="string", maxPolyCount=int, trans21=float, solidType=int, collapsePoles=bool, capType=int, trans01=float, trans22=float, trans02=float, reverseNormal=bool, trans30=float, trans00=float, trans10=float):
    """
    nurbsToSubdivPref is undoable, queryable, and NOT editable.
    

    
This command sets the values used by the nurbs-to-subdivision surface preference. This preference is used by the nurbs creation commands and is saved between Maya sessions.
To query any of the flags, use the "-query" flag.
For more information on the flags, see the node documentation for the "nurbsToSubdivProc" node.

    """
    pass
    


def nurbsUVSet(useExplicit=bool, create=bool):
    """
    nurbsUVSet is undoable, queryable, and editable.
    

    
Allows user to toggle between implicit and explicit UVs on a NURBS object. Also provides a facility to create, delete, rename and set the current explicit UVSet. An implicit UVSet is non-editable. It uses the parametric make-up of the NURBS object to determine the location of UVs (isoparm intersections). NURBS objects also support explicit UVSets which are similar to the UVs of a polygonal object. UVs are created at the knots (isoparm intersections) of the object and are fully editable. In order to access UV editing capabilities on a NURBS object an explicit UVSet must be created and set as the current UVSet.

    """
    pass
    


def objectCenter(local=bool, z=bool, y=bool, gl=bool, x=bool):
    """
    objectCenter is undoable, NOT queryable, and NOT editable.
    

    
This command returns the coordinates of the center of the bounding box of the specified object. If one coordinate only is specified, it will be returned as a float. If no coordinates are specified, an array of floats is returned, containing x, y, and z. If you specify multiple coordinates, only one will be returned.

    """
    pass
    


def objectType(typeTag=bool, isAType="string", tagFromType="string", typeFromTag=int, isType="string"):
    """
    objectType is undoable, NOT queryable, and NOT editable.
    

    
This command returns the type of elements. Warning: This command is incomplete and may not be supported by all object types.

    """
    pass
    


def objectTypeUI(superClasses=bool, listAll=bool, isType="string"):
    """
    objectTypeUI is undoable, NOT queryable, and NOT editable.
    

    
This command returns the type of UI element such as button, sliders, etc.

    """
    pass
    


def objExists():
    """
    objExists is undoable, NOT queryable, and NOT editable.
    

    
This command simply returns true or false depending on whether an object with the given name exists.

    """
    pass
    


def offsetCurve(curve, subdivisionDensity=int, normal="string", distance="string", connectBreaks=int, object=bool, useGivenNormal=bool, reparameterize=bool, nodeState=int, range=bool, cutRadius="string", name="string", stitch=bool, caching=bool, tolerance="string", constructionHistory=bool, cutLoop=bool):
    """
    offsetCurve is undoable, queryable, and editable.
    

    
The offset command creates new offset curves from the selected curves. The connecting type for breaks in offsets is off (no connection), circular (connect with an arc) or linear (connect linearly resulting in a sharp corner). If loop cutting is on then any loops in the offset curves are trimmed away. For the default cut radius of 0.0 a sharp corner is created at each intersection. For values greater than 0.0 a small arc of that radius is created at each intersection. The cut radius value is only valid when loop cutting is on. Offsets (for planar curves) are calculated in the plane of that curve and 3d curves are offset in 3d. The subdivisionDensity flag is the maximum number of times the offset object can be subdivided (i.e. calculate the offset until the offset comes within tolerance or the iteration reaches this maximum.) The reparameterize option allows the offset curve to have a different parameterization to the original curve. This avoids uneven parameter distributions in the offset curve that can occur with large offsets of curves, but is more expensive to compute.

    """
    pass
    


def offsetCurveOnSurface(curve, subdivisionDensity=int, distance="string", connectBreaks=int, object=bool, nodeState=int, range=bool, name="string", stitch=bool, checkPoints=int, caching=bool, tolerance="string", constructionHistory=bool, cutLoop=bool):
    """
    offsetCurveOnSurface is undoable, queryable, and editable.
    

    
The offsetCurveOnSurface command offsets a curve on surface resulting in another curve on surface. The connecting type for breaks in offsets is off (no connection), circular (connect with an arc) or linear (connect linearly resulting in a sharp corner). If loop cutting is on then any loops in the offset curves are trimmed away and a sharp corner is created at each intersection. The subdivisionDensity flag is the maximum number of times the offset object can be subdivided (i.e. calculate the offset until the offset comes within tolerance or the iteration reaches this maximum.) The checkPoints flag sets the number of points per span at which the distance of the offset curve from the original curve is determined. The tolerance flag determines how accurately the offset curve should satisfy the required offset distance. A satisfactory offset curve is one for which all of the checkpoints are within the given tolerance of the required offset.

    """
    pass
    


def offsetSurface(surface, method=int, distance="string", object=bool, nodeState=int, constructionHistory=bool, caching=bool, name="string"):
    """
    offsetSurface is undoable, queryable, and editable.
    

    
The offset command creates new offset surfaces from the selected surfaces. The default method is a surface offset, which offsets relative to the surface itself. The CV offset method offsets the CVs directly rather than the surface, so is usually slightly less accurate but is faster. The offset surface will always have the same degree, number of CVs and knot spacing as the original surface.

    """
    pass
    


def ogs(reloadTextures=bool, reset=bool, fragmentXML="string", toggleTexturePaging=bool, regenerateUVTilePreview="string", rebakeTextures=bool, gpuMemoryUsed=bool, shaderSource="string", enableHardwareInstancing=bool, fragmentEditor="string", disposeReleasableTextures=bool, traceRenderPipeline=bool, deviceInformation=bool, pause=bool, dumpTexture="string"):
    """
    ogs is NOT undoable, queryable, and NOT editable.
    

    
OGS is one of the viewport renderers. As there is a lot of effort involved in migrating functionality it will evolve over several releases. As it evolves it is prudent to provide safeguards to get the database back to a known state. That is the function of this command, similar to how 'dgdirty' is used to restore state to the dependency graph.

    """
    pass
    


def ogsRender(camera="string", activeRenderOverride="string", noRenderView=bool, enableFloatingPointRenderTarget=bool, enableMultisample=bool, currentFrame=bool, width=int, activeRenderTargetFormat="string", height=int, frame=float, availableMultisampleType=bool, availableRenderOverrides=bool, currentView=bool, layer="string", availableFloatingPointTargetFormat=bool, activeMultisampleType="string"):
    """
    ogsRender is NOT undoable, queryable, and editable.
    

    
Renders an image or a sequence using the OGS rendering engine

    """
    pass
    


def openGLExtension(vendor=bool, version=bool, renderer=bool, extension="string"):
    """
    openGLExtension is NOT undoable, NOT queryable, and NOT editable.
    

    
Command returns the extension name depending on whether a given OpenGL extension is supported or not. The input is the extension string to the -extension flag. If the -extension flag is not used, or if the string argument to this flag is an empty string than all extension names are returned in a single string. If the extension exists it is not necessary true that the extension is supported. This command can only be used when a modeling view has been created. Otherwise no extensions will have been initialized and the resulting string will always be the empty string.

    """
    pass
    


def openMayaPref(lazyLoad=bool, errlog=bool, oldPluginWarning=bool):
    """
    openMayaPref is undoable, queryable, and editable.
    

    
Set or query API preferences.

    """
    pass
    


def optionMenu(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfItems=bool, numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", value="string", highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, itemListLong=bool, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, select=int, dropCallback="string", beforeShowPopup="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool, itemListShort=bool):
    """
    optionMenu is undoable, queryable, and editable.
    

    
This command creates a popup menu control. The command creates the control and provides its menu. Subsequent calls to the menuItem command will place them in the popup. Note that commands attached to menu items will not get called. Attach any commands via the -cc/changedCommand flag.

    """
    pass
    


def optionMenuGrp(groupName, docTag="string", height=int, columnWidth4=int, extraLabel="string", popupMenuArray=bool, numberOfItems=bool, numberOfPopupMenus=bool, noBackground=bool, defineTemplate="string", width=int, label="string", highlightColor=float, value="string", dragCallback="string", columnOffset2=int, parent="string", annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, itemListLong=bool, exists=bool, columnAttach4="string", adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, select=int, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", columnAttach6="string", isObscured=bool, itemListShort=bool, columnOffset6=int):
    """
    optionMenuGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text, option menu and an extra label. Both the label and extra label are optional. Subsequent calls to the menuItem command will place them in the option menu. When adding menu items to the option menu after the initialization step, use the name of the options menu itself. See the example below for more details. Note that commands attached to menu items will not get called. Use the -cc/changedCommand flag to be notified when the user changes the value of the option menu.

    """
    pass
    


def optionVar(floatValue="string", list=bool, removeFromArray="string", exists="string", floatValueAppend="string", clearArray="string", intValueAppend="string", stringValue="string", version=int, stringValueAppend="string", remove="string", arraySize="string", intValue="string"):
    """
    optionVar is undoable, queryable, and NOT editable.
    

    
This command allows you to set and query variables which are persistent between different invocations of Maya. These variables are stored as part of the preferences.

    """
    pass
    


def orbit(camera, rotationAngles=int, pivotPoint="string", horizontalAngle=int, verticalAngle=int):
    """
    orbit is undoable, NOT queryable, and NOT editable.
    

    
The orbit command revolves the camera(s) horizontally and/or vertically in the perspective window. The rotation axis is with respect to the camera.
To revolve horizontally: the rotation axis is the camera up direction vector. To revolve vertically: the rotation axis is the camera left direction vector.
When both the horizontal and the vertical angles are supplied on the command line, the camera is firstly revolved horizontally, then revolved vertically.
This command may be applied to more than one camera; objects that are not cameras are ignored. When no camera name supplied, this command is applied to all currently active cameras.

    """
    pass
    


def orbitCtx(image1="string", orbitScale=float, alternateContext=bool, history=bool, localOrbit=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    orbitCtx is undoable, queryable, and editable.
    

    
Create, edit, or query an orbit context.

    """
    pass
    


def orientConstraint(targetobject, remove=bool, skip="string", deleteCache=bool, maintainOffset=bool, weightAliasList=bool, layer="string", offset=float, name="string", targetList=bool, createCache=float, weight=float):
    """
    orientConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation to match the orientation of the target or the average of a number of targets.
An orientConstraint takes as input one or more "target" DAG transform nodes to control the orientation of the single "constraint object" DAG transform The orientConstraint orients the constrained object to match the weighted average of the target world space orientations.

    """
    pass
    


def outlinerEditor(expandAllSelectedItems=bool, docTag="string", isSetMember=int, ignoreOutlinerColor=bool, useTemplate="string", ignoreHiddenAttribute=bool, renderFilterIndex=int, showAssignedMaterials=bool, showTimeEditor=bool, panel="string", attrFilter="string", feedbackRowNumber=bool, attrAlphaOrder="string", ignoreDagHierarchy=bool, removeFromCurrentSet=int, unlockMainConnection=bool, showSelected=bool, renameSelectedItem=bool, organizeByLayer=bool, showAnimCurvesOnly=bool, containersIgnoreFilters=bool, forceMainConnection="string", selectCommand="string", showAnimLayerWeight=bool, renderFilterActive=bool, directSelect=bool, defineTemplate="string", parent="string", expandObjects=bool, sortOrder="string", longNames=bool, showAttributes=bool, doNotSelectNewObjects=bool, isChildSelected="string", mapMotionTrails=bool, stateString=bool, setFilter="string", autoExpandLayers=bool, control=bool, feedbackItemName=bool, renderFilterVisible=bool, showPinIcons=bool, editAttrName=bool, selectionConnection="string", showConnected=bool, alwaysToggleSelect=bool, showLeafs=bool, highlightActive=bool, showNamespace=bool, highlightSecondary=bool, selectionOrder="string", displayMode="string", lockMainConnection=bool, showDagOnly=bool, showReferenceMembers=bool, renameItem=int, expandAllItems=bool, mainListConnection="string", expandConnections=bool, expandAttribute=bool, showUVAttrsOnly=bool, showContainedOnly=bool, masterOutliner="string", updateMainConnection=bool, setsIgnoreFilters=bool, parentObject=bool, animLayerFilterOptions="string", object="string", dropIsParent=bool, showAttrValues=bool, showShapes=bool, isSet=int, allowMultiSelection=bool, showUnitlessCurves=bool, refresh=bool, unParent=bool, showAssets=bool, highlightConnection="string", showCompounds=bool, autoSelectNewObjects=bool, showNumericAttrsOnly=bool, showPublishedAsConnected=bool, showContainerContents=bool, exists=bool, niceNames=bool, unpinPlug="string", showSetMembers=bool, getCurrentSetOfItem=int, transmitFilters=bool, autoExpand=bool, pinPlug="string", showUpstreamCurves=bool, showTextureNodesOnly=bool, showReferenceNodes=bool, filter="string"):
    """
    outlinerEditor is undoable, queryable, and editable.
    

    
This command creates an outliner editor which can be used to display a list of objects.
WARNING: some flag combinations may not behave as you expect. The command is really intended for internal use for creating the outliner used by the various editors.

    """
    pass
    


def outlinerPanel(panelName, tearOff=bool, docTag="string", parent="string", useTemplate="string", label="string", replacePanel="string", unParent=bool, tearOffCopy="string", isUnique=bool, defineTemplate="string", createString=bool, needsInit=bool, exists=bool, control=bool, menuBarVisible=bool, init=bool, tearOffRestore=bool, popupMenuProcedure="string", editString=bool, copy="string", outlinerEditor=bool):
    """
    outlinerPanel is undoable, queryable, and editable.
    

    
This command creates, edit and queries outliner panels which contain only an outliner editor.

    """
    pass
    


def overrideModifier(press="string", clear=bool, release="string"):
    """
    overrideModifier is undoable, NOT queryable, and NOT editable.
    

    
This command allows you to assign modifier key behaviour to other parts of the system. For example you can use a hotkey or input device instead of a modifer key to perform the same action.
Note that the original modifier key behaviour is not altered in anyway. For example, if you've assigned "Ctrl" key behaviour to the "c" key then the "Ctrl" key will still work as you expect, all you've done is allowed yourself to use the "c" key as an alternative to the "Ctrl" key.

    """
    pass
    


def paintEffectsDisplay(meshDrawEnable=bool):
    """
    paintEffectsDisplay is NOT undoable, queryable, and NOT editable.
    

    
Command to set the global display methods for paint effects items

    """
    pass
    


def pairBlend(node="string", attribute="string", input2=bool, input1=bool):
    """
    pairBlend is undoable, queryable, and editable.
    

    
The pairBlend node allows a weighted combinations of 2 inputs to be blended together. It is created automatically when keying or constraining an attribute which is already connected.
Alternatively, the pairBlend command can be used to connect a pairBlend node to connected attributes of a node. The previously existing connections are rewired to input1 of the pairBlend node. Additional connections can then be made manually to input2 of the pairBlend node.
The pairBlend command can also be used to query the inputs to an existing pairBlend node.

    """
    pass
    


def palettePort(docTag="string", height=int, defineTemplate="string", parent="string", topDown=bool, numberOfPopupMenus=bool, transparent=int, width=int, dragCallback="string", rgbValue=int, highlightColor=float, setCurCell=int, redraw=bool, annotation="string", changeCommand="string", preventOverride=bool, popupMenuArray=bool, dimensions=int, exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, useTemplate="string", colorEditable=bool, fullPathName=bool, dropCallback="string", actualTotal=int, noBackground=bool, backgroundColor=float, hsvValue=int, manage=bool, editable=bool, isObscured=bool, colorEdited="string"):
    """
    palettePort is undoable, queryable, and editable.
    

    
This command creates an array of color cells. It could be used to to store an retrieve some colors you want to manage during your working session.

    """
    pass
    


def panel(tearOff=bool, docTag="string", isUnique=bool, control=bool, tearOffRestore=bool, defineTemplate="string", parent="string", createString=bool, unParent=bool, needsInit=bool, useTemplate="string", init=bool, label="string", replacePanel="string", popupMenuProcedure="string", editString=bool, copy="string", exists=bool, menuBarVisible=bool, tearOffCopy="string"):
    """
    panel is undoable, queryable, and editable.
    

    
This command allows editing or querying properties of any panels. Not all of the common properites of panels can be used with this command. Flags such as -tearOff and -replacePanel require that you use the explicit panel command. The command 'getPanel -typeOf panelName' will return the explicit type of a panel.

    """
    pass
    


def paneLayout(string, docTag="string", height=int, pane3=bool, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", numberOfChildren=bool, highlightColor=float, activePaneIndex=int, annotation="string", pane4=bool, preventOverride=bool, popupMenuArray=bool, childArray=bool, staticHeightPane=int, pane2=bool, paneSize=int, exists=bool, visibleChangeCommand="string", pane1=bool, configuration="string", enable=bool, enableBackground=bool, activeFrameThickness=int, separatorThickness=int, visible=bool, staticWidthPane=int, fullPathName=bool, dropCallback="string", numberOfVisiblePanes=bool, paneUnderPointer=bool, noBackground=bool, backgroundColor=float, separatorMovedCommand="string", manage=bool, setPane="string", isObscured=bool, activePane="string"):
    """
    paneLayout is undoable, queryable, and editable.
    

    
This command creates a pane layout. A pane layout may have any number of children but at any one time only certain children may be visible, as determined by the current layout configuration. For example a horizontally split pane shows only two children, one on top of the other and a visible separator between the two. The separator may be moved to vary the size of each pane. Various other pane configurations are available and all display a moveable separator that define the size of each pane in the layout.

    """
    pass
    


def panelConfiguration(name, defineTemplate="string", isFixedState=bool, image="string", useTemplate="string", label="string", numberOfPanels=bool, createStrings=bool, replaceLabel=int, replaceCreateString=int, replacePanel=int, sceneConfig=bool, labelStrings=bool, userCreated=bool, exists=bool, typeStrings=bool, removeLastPanel=bool, replaceFixedState=int, addPanel=bool, editStrings=bool, configString="string", removeAllPanels=bool, replaceTypeString=int, replaceEditString=int, defaultImage="string"):
    """
    panelConfiguration is undoable, queryable, and editable.
    

    
This command creates a panel configuration object. Typically you would not call this method command directly. Instead use the Panel Editor.
Once a panel configuration is created you can make it appear in the main Maya window by selecting it from any panel's "Panels->Saved Layouts" menu.

    """
    pass
    


def panelHistory(name, isEmpty=bool, defineTemplate="string", targetPane="string", clear=bool, historyDepth=int, wrap=bool, useTemplate="string", suspend=bool, back=bool, exists=bool, forward=bool):
    """
    panelHistory is undoable, queryable, and editable.
    

    
This command creates a panel history object. The object is targeted on a particular paneLayout and thereafter notes changes in panel configurations within that paneLayout, building up a history list. The list can be stepped through backwards or forwards.

    """
    pass
    


def panZoom(camera, zoomRatio=float, downDistance="string", relative=bool, absolute=bool, rightDistance="string", upDistance="string", leftDistance="string"):
    """
    panZoom is undoable, NOT queryable, and NOT editable.
    

    
The panZoom command pans/zooms the 2D film.
The panZoom command can be applied to either a perspective or an orthographic camera.
When no camera name is supplied, this command is applied to the camera in the active view.

    """
    pass
    


def panZoomCtx(image1="string", zoomScale=float, panMode=bool, alternateContext=bool, history=bool, zoomMode=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    panZoomCtx is undoable, queryable, and editable.
    

    
This command can be used to create camera 2D pan/zoom context.

    """
    pass
    


def paramDimContext(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    paramDimContext is undoable, queryable, and editable.
    

    
Command used to register the paramDimCtx tool.

    """
    pass
    


def paramDimension(curve ,surface):
    """
    paramDimension is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create a param dimension to display the parameter value of a curve/surface at a specified point on the curve/surface.

    """
    pass
    


def paramLocator(object, position=bool):
    """
    paramLocator is undoable, queryable, and editable.
    

    
The command creates a locator in the underworld of a NURBS curve or NURBS surface at the specified parameter value. If no object is specified, then a locator will be created on the first valid selected item (either a curve point or a surface point).

    """
    pass
    


def parent(dagObjectdagObject, addObject=bool, noInvScale=bool, noConnections=bool, shape=bool, relative=bool, absolute=bool, world=bool, removeObject=bool):
    """
    parent is undoable, NOT queryable, and NOT editable.
    

    
This command parents (moves) objects under a new group, removes objects from an existing group, or adds/removes parents.
If the -w flag is specified all the selected or specified objects are parented to the world (unparented first).
If the -rm flag is specified then all the selected or specified instances are removed.
If there are more than two objects specified all the objects are parented to the last object specified.
If the -add flag is specified, the objects are not reparented but also become children of the last object specified.
If there is only a single object specified then the selected objects are parented to that object.
If an object is parented under a different group and there is an object in that group with the same name then this command will rename the parented object.

    """
    pass
    


def parentConstraint(targetobject, decompRotationToChild=bool, skipTranslate="string", remove=bool, deleteCache=bool, maintainOffset=bool, weightAliasList=bool, layer="string", name="string", targetList=bool, createCache=float, weight=float, skipRotate="string"):
    """
    parentConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s). In the case of multiple targets, the overall position and rotation of the constrained object is the weighted average of each target's contribution to the position and rotation of the object.
A parentConstraint takes as input one or more "target" DAG transform nodes at which to position and rotate the single "constraint object" DAG transform node. The parentConstraint positions and rotates the constrained object at the weighted average of the world space position, rotation and scale target objects.

    """
    pass
    


def particle(upperRight="string", particleId=int, perParticleDouble=bool, inherit=float, vectorValue=float, order=int, conserve=float, name="string", numJitters=int, dynamicAttrList=bool, deleteCache=bool, jitterRadius="string", shapeName="string", attribute="string", jitterBasePoint="string", count=bool, cache=bool, lowerLeft="string", perParticleVector=bool, position="string", floatValue=float, gridSpacing="string"):
    """
    particle is undoable, queryable, and editable.
    

    
The particle command creates a new particle object from a list of world space points. If a particle object is created, the command returns the names of the new particle shape and its associated particle object dependency node. If an object was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.

    """
    pass
    


def particleExists():
    """
    particleExists is undoable, NOT queryable, and NOT editable.
    

    
This command is used to query if a particle or soft object with the given name exists. Either the transform or shape name can be used as well as the name of the soft object.

    """
    pass
    


def particleFill(minZ=float, minX=float, resolution=int, closePacking=bool, maxY=float, particleDensity=float, doubleWalled=bool, maxX=float, maxZ=float, minY=float):
    """
    particleFill is NOT undoable, NOT queryable, and NOT editable.
    

    
This command generates an nParticle system that fills the selected object with a grid of particles.

    """
    pass
    


def particleInstancer(aimAxis="string", aimWorldUp="string", shear="string", cycleStartObject="string", cycle="string", rotationType="string", rotationOrder="string", visibility="string", addObject=bool, particleAge="string", aimDirection="string", name="string", cycleStep=float, instanceId="string", aimUpAxis="string", scale="string", levelOfDetail="string", objectIndex="string", cycleStepUnits="string", attributeMapping=bool, rotation="string", index=int, object="string", aimPosition="string", removeObject=bool, position="string", rotationUnits="string"):
    """
    particleInstancer is undoable, queryable, and editable.
    

    
This command is used to create a particle instancer node and set the proper attributes in the particle shape and in the instancer node. It will also create the connections needed between the particle shape and the instancer node.

    """
    pass
    


def particleRenderInfo(name=int, renderTypeCount=bool, attrListAll=bool, attrList=int):
    """
    particleRenderInfo is undoable, queryable, and NOT editable.
    

    
This action provides information access to the particle render subclasses. These are derived from TdynRenderBase. This action is used primarily by the Attribute Editor to gather information about attributes used for rendering.

    """
    pass
    


def partition(stringstring, removeSet="string", render=bool, name="string", addSet="string"):
    """
    partition is undoable, queryable, and editable.
    

    
This command is used to create, query or add/remove sets to a partition. If a partition name needs to be specified, it is the first argument, other arguments represent the set names.
Without any flags, the command will create a partition with a default name. Any sets which are arguments to the command will be added to the partition.
A set can be added to a partition only if none of its members are in any of the other sets in the partition. If the -re/render flag is specified when the partition is created, only 'renderable' sets can be added to the partition.
Sets can be added and removed from a partition by using the -addSet or -removeSet flags.
Note: If a set is already selected, and the partition command is executed, the set will be added to the created partition.

    """
    pass
    


def pasteKey(objects, time=(), animLayer="string", float=(), includeUpperBound=bool, clipboard="string", floatOffset=float, matchByName=bool, valueOffset=float, copies=int, connect=bool, attribute="string", animation="string", index=int, option="string", timeOffset=()):
    """
    pasteKey is undoable, queryable, and editable.
    

    
The pasteKey command pastes curve segment hierarchies from the clipboard onto other objects or curves. If the object hierarchy from which the curve segments were copied or cut does not match the object hierarchy being pasted to, pasteKey will paste as much as it can match in the hierarchy. If animation from only one object is on the clipboard, it will be pasted to each of the target objects. If animation from more than one object is on the clipboard, selection list order determines what animation is pasted to which object.
Valid operations include:
One attribute to one or more attributes (Clipboard animation is pasted onto all target attributes.
One attribute to one or more objects (Clipboard animation pasted onto target object, when attribute names match.)
Many attributes to one or more objects
Clipboard animation pasted onto targets when attribute names match.
TbaseKeySetCmd.h
The way the keyset clipboard will be pasted to the specified object's attributes depends on the paste "-option" specified. Each of these options below will be explained using an example. For all the explanations, let us assume that there is a curve segment with 20 frames of animation on the keyset clipboard (you can put curve segments onto the clipboard using the cutKey or copyKey commands). We will call the animation curve that we are pasting to the target curve:
pasteKey -time 5 -option insert
1. Shift all keyframes on the target curve after time 5 to the right by 20 frames (to make room for the 20-frame clipboard segment).
2. Paste the 20-frame clipboard segment starting at time 5.
pasteKey -time "5:25" -option replace
1. Remove all keys on the target curve from 5 to 25.
2. Paste the 20-frame clipboard curve at time 5.
pasteKey -option replaceCompletely
1. Remove all keys on the target curve.
2. Paste the 20-frame clipboard curve, preserving the clipboard curve's original keyframe times.
pasteKey -time 5 -option merge
1.The clipboard curve segment will be pasted starting at time 5 for its full 20-frame range until frame 25.
2. If a keyframe on the target curve has the same time as a keyframe on the clipboard curve, it is overwritten. Otherwise, any keys that existed in the 5:25 range before the paste, will remain untouched
pasteKey -time "3:10" -option scaleInsert
1. Shift all keyframes on the target curve after time 3 to the right by 7 frames (to clear the range 3:10 to paste in)
2. The clipboard curve segment will be scaled to fit the specified time range (i.e. the 20 frames on the clipboard will be scaled to fit into 7 frames), and then pasted into the range 3:10.
pasteKey -time "3:10" -option scaleReplace
1. Any existing keyframes in the target curve in the range 3:10 are removed.
2. The clipboard curve segment will be scaled to fit the specified time range (i.e. the 20 frames on the clipboard will be scaled to fit into 7 frames), and then pasted into the range 3:10.
pasteKey -time "3:10" -option scaleMerge
1. The clipboard curve segment will be scaled to fit the specified time range (i.e. the 20 frames on the clipboard will be scaled to fit into 7 frames).
2. If there are keys on the target curve at the same time as keys on the clipboard curve, they are overwritten. Otherwise, keyframes on the target curve that existed in the 3:10 range before the paste, will remain untouched.
pasteKey -time "3:10" -option fitInsert
1. Shift all the keyframes on the target curve after time 3 to the right by 7 frames (to clear the range 3:10 to paste in)
2. The first 7 frames of the clipboard curve segment will be pasted into the range 3:10.
pasteKey -time "3:10" -option fitReplace
1. Any existing frames in the target curve in the range 3:10 are removed.
2. The first 7 frames of the clipboard curve segment will be pasted into the range 3:10.
pasteKey -time "3:10" -option fitMerge
1. The first 7 frames of the clipboard curve segment will be pasted into the range 3:10.
2. If there are keys on the target curve at the same time as keys on the clipboard curve, they are overwritten. Otherwise, keyframes on the target curve that existed in the 3:10 range before the paste, will remain untouched.

    """
    pass
    


def pathAnimation(objects, worldUpObject="string", worldUpVector=float, bankScale=float, follow=bool, upAxis="string", fractionMode=bool, bankThreshold=int, useNormal=bool, inverseUp=bool, inverseFront=bool, startU=float, startTimeU=(), endTimeU=(), curve="string", followAxis="string", bank=bool, endU=float, worldUpType="string", name="string"):
    """
    pathAnimation is undoable, queryable, and editable.
    

    
The pathAnimation command constructs the necessary graph nodes and their interconnections for a motion path animation. Motion path animation requires a curve and one or more other objects. During the animation, the objects will be moved along the 3D curve or the curveOnSurface.
There are two ways to specify the moving objects:
by explicitly specifying their names in the command line, or
by making the objects selected (interactively, or through a MEL command).
Likewise, there are two ways to specify a motion curve:
by explicitly specifying the name of the motion curve in the command line (i.e. using the -c curve_name option), or
by selecting the moving objects first before selecting the motion curve. I.e. if the name of the motion curve is not provided in the command line, the curve will be taken to be the last selected object in the selection list.
When the end time is not specified: only one keyframe will be created either at the current time, or at the specified start time.

    """
    pass
    


def pause(seconds=int):
    """
    pause is undoable, NOT queryable, and NOT editable.
    

    
Pause for a specified number of seconds for canned demos or for test scripts to allow user to view results.

    """
    pass
    


def perCameraVisibility(camera="string", remove=bool, removeAll=bool, exclusive=bool, removeCamera=bool, hide=bool):
    """
    perCameraVisibility is NOT undoable, queryable, and NOT editable.
    

    
The perCameraVisibility command creates, queries and removes visibility relationships between DAG objects and cameras. These relationships are applied in any viewport that uses the cameras involved. (They are not used e.g. in rendering.) Objects can be set to be exclusive to a camera (meaning they will only be displayed in viewports using that camera; they will be hidden in other viewports) or hidden from a camera (meaning they will be not visible in any viewport using the camera).

    """
    pass
    


def percent(nodeobjects, dropoffType="string", dropoffCurve="string", dropoffPosition="string", dropoffAxis="string", multiplyPercent=bool, value=float, dropoffDistance="string", addPercent=bool):
    """
    percent is undoable, queryable, and NOT editable.
    

    
This command sets percent values on members of a weighted node such as a cluster or a jointCluster. With no flags specified the command sets the percent value for selected components of the specified node to the specified percent value. A dropoff from the specified percent value to 0 can be specified from a point, plane or curve using a dropoff distance around that shape. The percent value can also be added or multiplied with existing percent values of the node components.

    """
    pass
    


def performanceOptions(passThroughFlexors="string", passThroughSculpt="string", useClusterResolution="string", passThroughBindSkinAndFlexors="string", passThroughWire="string", passThroughLattice="string", useLatticeResolution="string", disableTrimDisplay="string", passThroughDeltaMush="string", skipHierarchyTraversal=bool, passThroughCluster="string", passThroughPaintEffects="string", latticeResolution=float, passThroughBlendShape="string", disableStitch="string", clusterResolution=float):
    """
    performanceOptions is undoable, queryable, and NOT editable.
    

    
Sets the global performance options for the application. The options allow the disabling of features such as stitch surfaces or deformers to cut down on computation time in the scene.
Performance options that are in effect may be on all the time, or they can be turned on only for interaction. In the latter case, the options will only take effect during UI interaction or playback.
Note that none of these performance options will affect rendering.

    """
    pass
    


def pfxstrokes(postCallback=bool, filename="string", selected=bool):
    """
    pfxstrokes is NOT undoable, NOT queryable, and NOT editable.
    

    
This command will loop through all the Paint Effects strokes, including pfxHair nodes, and write the current state of all the tubes to a file. For normal stroke nodes tubes must be ON in the brush or there will be no output. For pfxHair nodes there will always be output, but the format is different than for stroke nodes(however one can assign a brush with tubes = ON to a pfxHair node, in which case it will output the same format as strokes). The general file format is ASCII, using commas to separate numerical values and newlines between blocks of data. The format used for pfxHair nodes presents the hair curves points in order from root to tip of the hair. The hairs follow sequentially in the following fashion: NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc... NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc.. The format used to output files for brushes with tubes=ON is more complex. The tubes can branch and the order the segments are written is the same order they are drawn in. Slowly drawing a tall grass brush in the paint effects panel can help to illustrate the order the segments will appear in the file. New tubes can start "growing" before others are finished. There is no line for "NumCvs". Instead all data for each segment appears on each line. The data on each line is the same as passed into the paint effects runtime function. See the argument list of paintRuntimeFunc.mel for the order and a description of these parameters. The parameters match up exactly in the order they appear on a line of the output file with the order of arguments to this function. If one wishes to parse the output file and connect the segments together into curves the branchId, parentId and siblingCnt parameters can help when sorting which segment connects to which line. Using the -postCallback option will write out the tubes data after it has been proessed by the runTime callback.

    """
    pass
    


def pickWalk(objects, type="string", direction="string"):
    """
    pickWalk is undoable, NOT queryable, and NOT editable.
    

    
The pickWalk command allows you to quickly change the selection list relative to the nodes that are currently selected. It is called pickWalk, because it walks from one selection list to another by unselecting what's currently selected, and selecting nodes that are in the specified direction from the currently selected list. If you specify objects on the command line, the pickWalk command will walk from those objects instead of the selected list.
If the -type flag is instances, then the left and right direction will walk to the previous or next instance of the same selected dag node.

    """
    pass
    


def picture(string, docTag="string", height=int, defineTemplate="string", parent="string", image="string", tile=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", exists=bool, enableBackground=bool, numberOfPopupMenus=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    picture is undoable, queryable, and editable.
    

    
This command creates a static image.

    """
    pass
    


def pixelMove():
    """
    pixelMove is undoable, NOT queryable, and NOT editable.
    

    
The pixelMove command moves objects by what appears as pixel units based on the current view. It takes two integer arguments which specify the direction in screen space an object should appear to move. The vector between the center pixel of the view and the specified offset is mapped to some world space vector which defines the relative amount to move the selected objects. The mapping is dependent upon the view.

    """
    pass
    


def planarSrf(keepOutside=bool, degree=int, object=bool, polygon=int, nodeState=int, range=bool, constructionHistory=bool, caching=bool, tolerance="string", name="string"):
    """
    planarSrf is undoable, queryable, and editable.
    

    
This command computes a planar trimmed surface given planar boundary curves that form a closed region.

    """
    pass
    


def plane(size="string", width="string", length="string", position="string", rotation=int, name="string"):
    """
    plane is undoable, NOT queryable, and NOT editable.
    

    
The command creates a sketch plane (also known as a "construction plane") in space. To create an object (such as a NURBS curve, joint chain or polygon) on a construction plane, you need to first make the plane live. See also the makeLive command.

    """
    pass
    


def play(playSound=bool, wait=bool, sound="string", state=bool, record=bool, forward=bool):
    """
    play is undoable, queryable, and NOT editable.
    

    
This command starts and stops playback. In order to change the frame range of playback, see the playbackOptions command.

    """
    pass
    


def playbackOptions(maxTime=(), loop="string", playbackSpeed=float, maxPlaybackSpeed=float, by=float, blockingAnim=bool, minTime=(), framesPerSecond=bool, animationEndTime=(), view="string", animationStartTime=()):
    """
    playbackOptions is undoable, queryable, and editable.
    

    
This command sets/queries certain values associated with playback: looping style, start/end times, etc. Only commands modifying the -minTime/maxTime, the -animationStartTime/animationEndTime, or the -by value are undoable.

    """
    pass
    


def playblast(height=int, quality=int, sequenceTime=bool, framePadding=int, replaceAudioOnly=bool, showOrnaments=bool, activeEditor=bool, format="string", replaceStartTime=(), compression="string", codecOptions=bool, frame=(), editorPanelName="string", clearCache=bool, sound="string", widthHeight=int, completeFilename="string", startTime=(), viewer=bool, percent=int, indexFromZero=bool, offScreen=bool, cameraSetup="string", endTime=(), options=bool, replaceEndTime=(), filename="string", width=int, combineSound=bool, replaceFilename=bool, rawFrameNumbers=bool, forceOverwrite=bool):
    """
    playblast is undoable, NOT queryable, and NOT editable.
    

    
This command playblasts the current playback range. Sound is optional.
Note that the playblast command registers a condition called "playblasting" so that users can monitor whether playblasting is occurring. You may monitor the condition using the API (MConditionMessage) or a script (scriptJob and condition commands).

    """
    pass
    


def pluginDisplayFilter(exists="string", listFilters=bool, classification="string", deregister=bool, label="string", register=bool):
    """
    pluginDisplayFilter is NOT undoable, queryable, and NOT editable.
    

    
Register, deregister or query a plugin display filter. Plug-ins can use this command to register their own display filters which will appear in the 'Show' menus on Maya's model panels.

    """
    pass
    


def pluginInfo(string, animCurveInterp="string", autoload=bool, controlCommand="string", listPlugins=bool, changedCommand="string", loadPluginPrefs=bool, unloadOk=bool, apiVersion=bool, device=bool, writeRequires=bool, vendor="string", path="string", version=bool, activeFile=bool, tool="string", pluginsInUse=bool, userNamed=bool, cacheFormat=bool, dragAndDropBehavior=bool, dependNode=bool, dependNodeId="string", renderer=bool, translator=bool, name="string", serviceDescriptions=bool, dependNodeByType="string", data="string", listPluginsPath=bool, loaded=bool, remove=bool, modelEditorCommand="string", settings=bool, command="string", constraintCommand="string", savePluginPrefs=bool, registered=bool, iksolver=bool):
    """
    pluginInfo is undoable, queryable, and editable.
    

    
This command provides access to the plug-in registry of the application. It is used mainly to query the characteristics of registered plug-ins. Plugins automatically become registered the first time that they are loaded.
The argument is either the internal name of the plug-in or the path to access it.

    """
    pass
    


def pointConstraint(targetobject, remove=bool, skip="string", maintainOffset=bool, weightAliasList=bool, layer="string", offset=float, targetList=bool, weight=float, name="string"):
    """
    pointConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position to the position of the target object or to the average position of a number of targets.
A pointConstraint takes as input one or more "target" DAG transform nodes at which to position the single "constraint object" DAG transform node. The pointConstraint positions the constrained object at the weighted average of the world space position target objects.

    """
    pass
    


def pointCurveConstraint(pointConstraintUVW=float, object=bool, nodeState=int, replaceOriginal=bool, constructionHistory=bool, position=float, pointWeight=float, caching=bool, weight=float, name="string"):
    """
    pointCurveConstraint is undoable, queryable, and editable.
    

    
The command enables direct manipulation of a NURBS curve. It does so by apply a position constraint at the specified parameter location on the NURBS curve.
If construction history for the cmd is enabled, a locator is created to enable subsequent interactive manipulation of the curve. The locator position may be key framed or transformed and the "curve1" will try to match the position of the locator.
The argument is a curve location

    """
    pass
    


def pointLight(discRadius="string", decayRate=int, softShadow=bool, exclusive=bool, useRayTraceShadows=bool, shadowColor=float, intensity=float, rgb=float, position="string", shadowSamples=int, shadowDither=float, rotation=int, name="string"):
    """
    pointLight is undoable, queryable, and editable.
    

    
The pointLight command is used to edit the parameters of existing pointLights, or to create new ones. The default behaviour is to create a new pointlight.

    """
    pass
    


def pointOnCurve(objects, tangent=bool, curvatureCenter=bool, curvatureRadius=bool, normal=bool, turnOnPercentage=bool, normalizedTangent=bool, normalizedNormal=bool, parameter=float, constructionHistory=bool, position=bool):
    """
    pointOnCurve is undoable, queryable, and editable.
    

    
This command returns information for a point on a NURBS curve. If no flag is specified, it assumes p/position by default.

    """
    pass
    


def pointOnPolyConstraint(targetobject, remove=bool, skip="string", maintainOffset=bool, weightAliasList=bool, layer="string", offset=float, targetList=bool, weight=float, name="string"):
    """
    pointOnPolyConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position to the position of the target object or to the average position of a number of targets.
A pointOnPolyConstraint takes as input one or more "target" DAG transform nodes at which to position the single "constraint object" DAG transform node. The pointOnPolyConstraint positions the constrained object at the weighted average of the world space position target objects.

    """
    pass
    


def pointOnSurface(objects, normalizedTangentU=bool, normal=bool, turnOnPercentage=bool, parameterU=float, tangentV=bool, parameterV=float, normalizedTangentV=bool, tangentU=bool, normalizedNormal=bool, constructionHistory=bool, position=bool):
    """
    pointOnSurface is undoable, queryable, and editable.
    

    
This command returns information for a point on a surface. If no flag is specified, this command assumes p/position by default. If more than one flag is specifed, then a string array is returned.

    """
    pass
    


def pointPosition(object, local=bool, world=bool):
    """
    pointPosition is undoable, NOT queryable, and NOT editable.
    

    
This command returns the world or local space position for any type of point object. Valid selection items are: - curve and surface CVs - poly vertices - lattice points - particles - curve and surface edit points - curve and surface parameter points - poly uvs - rotate/scale/joint pivots - selection handles - locators, param locators and arc length locators
It works on the selected object or you can specify the object in the command. By default, if no flag is specified then the world position is returned.

    """
    pass
    


def poleVectorConstraint(targetobject, remove=bool, weightAliasList=bool, layer="string", targetList=bool, weight=float, name="string"):
    """
    poleVectorConstraint is undoable, queryable, and editable.
    

    
Constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number of targets.
An poleVectorConstraint takes as input one or more "target" DAG transform nodes at which to aim pole vector for an IK handle using the rotate plane solver. The pole vector is adjust such that the in weighted average of the world space position target objects lies is the "rotate plane" of the handle.

    """
    pass
    


def polyAppend(texture=int, point=float, append=(), subdivision=int, name="string", hole=bool, edge=int, constructionHistory=bool):
    """
    polyAppend is undoable, queryable, and editable.
    

    
Appends a new face to the selected polygonal object. The first argument must be a border edge. The new face will be automatically closed.
Only works with one object selected.

    """
    pass
    


def polyAppendFacetCtx(rotate=float, planarConstraint=bool, append=bool, subdivision=int, isRotateAvailable=bool, maximumNumberOfPoints=int):
    """
    polyAppendFacetCtx is undoable, queryable, and editable.
    

    
Create a new context to append facets on polygonal objects

    """
    pass
    


def polyAppendVertex(texture=int, point=float, append=(), vertex=int, name="string", hole=bool, constructionHistory=bool):
    """
    polyAppendVertex is undoable, queryable, and editable.
    

    
Appends a new face to the selected polygonal object. The direction of the normal is given by the vertex order: the face normal points towards the user when the vertices rotate counter clockwise. Note that holes must be described in the opposite direction.
Only works with one object selected.

    """
    pass
    


def polyAutoProjection(uvSetName="string", optimize=int, scale=float, rotateX=int, layoutMethod=int, insertBeforeDeformers=bool, scaleZ=float, pivotY="string", planes=int, layout=int, worldSpace=bool, pivotX="string", translate="string", translateX="string", caching=bool, name="string", skipIntersect=bool, scaleX=float, translateY="string", pivot="string", pivotZ="string", percentageSpace=float, rotate=int, rotateY=int, createNewMap=bool, translateZ="string", nodeState=int, scaleY=float, rotateZ=int, projectBothDirections=bool, scaleMode=int, constructionHistory=bool):
    """
    polyAutoProjection is undoable, queryable, and editable.
    

    
Projects a map onto an object, using several orthogonal projections simultaneously.

    """
    pass
    


def polyAverageNormal(prenormalize=bool, postnormalize=bool, allowZeroNormal=bool, distance=float, replaceNormalXYZ=float):
    """
    polyAverageNormal is undoable, NOT queryable, and NOT editable.
    

    
Set normals of vertices or vertex-faces to an average value when the vertices within a given threshold. First, it sorts out the containing edges, and set them to be soft, if it is possible, so to let the normals appear to be "merged". The remained components then are sorted into lumps where vertices in each lump are within the given threshold. For all vertices and vertex-faces, set their normals to the average normal in the lump. Selected vertices may or may not on the same object. If objects are selected, it is assumed that all vertices are selected. If edges or faces are selected, it is assumed that the related vertex-faces are selected.

    """
    pass
    


def polyAverageVertex(iterations=int, worldSpace=bool, nodeState=int, constructionHistory=bool, caching=bool, name="string"):
    """
    polyAverageVertex is undoable, queryable, and editable.
    

    
Moves the selected vertices of a polygonal object to round its shape. Translate, move, rotate or scale vertices.

    """
    pass
    


def polyBevel(segments=int, offset="string", autoFit=bool, worldSpace=bool, nodeState=int, angleTolerance=float, constructionHistory=bool, roundness=float, offsetAsFraction=bool, caching=bool, name="string"):
    """
    polyBevel is undoable, queryable, and editable.
    

    
Bevel edges.

    """
    pass
    


def polyBevel3(segments=int, offset="string", autoFit=bool, worldSpace=bool, nodeState=int, angleTolerance=float, constructionHistory=bool, roundness=float, offsetAsFraction=bool, caching=bool, name="string"):
    """
    polyBevel3 is undoable, queryable, and editable.
    

    
Bevel edges.

    """
    pass
    


def polyBlendColor(nodeState=int, blendWeightD=float, dstColorName="string", baseColorName="string", blendWeightC=float, blendFunc=int, name="string", blendWeightB=float, srcColorName="string", blendWeightA=float, caching=bool, constructionHistory=bool):
    """
    polyBlendColor is undoable, queryable, and editable.
    

    
Takes two color sets and blends them together into a third specified color set.

    """
    pass
    


def polyBlindData(longDataName="string", delete=bool, int64Data=int, booleanData=bool, shortDataName="string", typeId=int, stringData="string", doubleData=float, reset=bool, shape=bool, binaryData="string", intData=int, rescan=bool, associationType="string"):
    """
    polyBlindData is undoable, NOT queryable, and editable.
    

    
Command creates blindData types (basically creates an instance of TdnPolyBlindData). When used with the query flag, it returns the data types that define this blindData type. This command is to be used create a blindData node *and* to edit the same.. The associationType flag *has* to be specified at all times.. This is because if an instance of the specified BD typeId exists in the history chain but if the associationType is not the same, then a new polyBlindData node is created.. For object level blind data, only the object itself must be specified. A new compound attribute BlindDataNNNN will be created on the object. Blind data attribute names must be unique across types for object level blind data. So, the command will require the following to be specified: - typeId, - associationType - longDataName or shortDataName of data being edited. - The actual data being specified. - The components that this data is to be attached to.

    """
    pass
    


def polyBoolOp(object=bool, nodeState=int, constructionHistory=bool, operation=int, caching=bool, name="string"):
    """
    polyBoolOp is undoable, queryable, and editable.
    

    
This command creates a new poly as the result of a boolean operation on input polys : union, intersection, difference.
Only for difference, the order of the selected objects is important :
result = object1 - object2.
If no objects are specified in the command line, then the objects from the active list are used.

    """
    pass
    


def polyBridgeEdge(worldSpace=bool, nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyBridgeEdge is undoable, queryable, and editable.
    

    
Bridges two sets of edges.

    """
    pass
    


def polyCacheMonitor(cacheValue=bool, nodeName="string"):
    """
    polyCacheMonitor is NOT undoable, NOT queryable, and NOT editable.
    

    
When the cacheInput attribute has a positive value the midModifier node caches the output mesh improving performance in computations of downstream nodes. When the counter has a zero value the midModifier releases the cached data.

    """
    pass
    


def polyCBoolOp(object=bool, nodeState=int, constructionHistory=bool, operation=int, caching=bool, name="string"):
    """
    polyCBoolOp is undoable, queryable, and editable.
    

    
This command creates a new poly as the result of a boolean operation on input polys : union, intersection, difference.
Only for difference, the order of the selected objects is important :
result = object1 - object2.
If no objects are specified in the command line, then the objects from the active list are used.

    """
    pass
    


def polyCheck(edge=bool, face=bool, openFile="string"):
    """
    polyCheck is undoable, NOT queryable, and NOT editable.
    

    
Dumps a description of internal memory representation of poly objects.
If no objects are specified in the command line, the objects from the active list are used.
Default behaviour is to print only a summary. Use the flags above to get more details on a specific part of the object.

    """
    pass
    


def polyChipOff(localRotateY=int, translateZ="string", keepFacesTogether=bool, gravity="string", localRotateX=int, localDirectionZ="string", localScaleX=float, scale=float, magnZ="string", magnX="string", localScale=float, localTranslateX="string", localScaleY=float, localTranslateZ="string", weight=float, localTranslateY="string", worldSpace=bool, gravityZ="string", pivotY="string", random=float, pivotX="string", offset=float, localRotateZ=int, translate="string", caching=bool, name="string", localDirectionX="string", scaleZ=float, magnY="string", gravityX="string", rotateX=int, translateY="string", translateX="string", localDirection="string", localDirectionY="string", localScaleZ=float, pivot="string", pivotZ="string", rotate=int, rotateY=int, duplicate=bool, gravityY="string", attraction=float, localRotate=int, nodeState=int, scaleY=float, rotateZ=int, scaleX=float, localTranslate="string", magnet="string", constructionHistory=bool):
    """
    polyChipOff is undoable, queryable, and editable.
    

    
Extract facets. Faces can be extracted separately or together, and manipulations can be performed either in world or object space.

    """
    pass
    


def polyClean(cleanEdges=bool, name="string", nodeState=int, cleanVertices=bool, cleanPartialUVMapping=bool, caching=bool, constructionHistory=bool):
    """
    polyClean is undoable, queryable, and editable.
    

    
polyClean will attempt to remove components that are invalid in the description of a poly mesh.

    """
    pass
    


def polyClipboard(paste=bool, clear=bool, color=bool, copy=bool, uvCoordinates=bool, shader=bool):
    """
    polyClipboard is undoable, NOT queryable, and NOT editable.
    

    
The command allows the user to copy and paste certain polygonal attributes to a clipboard. These attributes are: 1) Shader (shading engine) assignment. 2) Texture coordinate (UV) assignment. 3) Color value assignment. Any combination of attributes can be chosen for the copy or paste operation. If the attribute has not been copied to the clipboard, then naturally it cannot be pasted from the clipboard. The copy option will copy the attribute assignments from a single source polygonal dag object or polygon component. If the source does not have the either UV or color attributes, then nothing will be copied to the clipboard. The paste option will paste the attribute assignments to one or more polygon components or polygonal dag objects. If the destination does not have either UV or color attributes, then new values will be assigned as needed. Additionally, there is the option to clear the clipboard contents

    """
    pass
    


def polyCloseBorder(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyCloseBorder is undoable, queryable, and editable.
    

    
Closes open borders of objects. For each border edge given, a face is created to fill the hole the edge lies on.

    """
    pass
    


def polyCollapseEdge(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyCollapseEdge is undoable, queryable, and editable.
    

    
Turns each selected edge into a point.

    """
    pass
    


def polyCollapseFacet(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyCollapseFacet is undoable, queryable, and editable.
    

    
Turns each selected facet into a point.

    """
    pass
    


def polyCollapseTweaks(hasVertexTweaks=bool):
    """
    polyCollapseTweaks is undoable, queryable, and NOT editable.
    

    
A command that updates a mesh's vertex tweaks by applying its tweak data (stored on the mesh node) onto its respective vertex data.
This command is only useful in cases where no construction history is associated with the shape node.
If a mesh name is not specified as input, a singly selected mesh (if any) will have its tweaked vertices baked.

    """
    pass
    


def polyColorBlindData(useMin=bool, aboveMaxColorBlue=float, minColorGreen=float, noColorBlue=float, minColorBlue=float, maxColorBlue=float, colorRed=float, noColorRed=float, value="string", dataType="string", belowMinColorGreen=float, maxColorRed=float, enableFalseColor=bool, belowMinColorRed=float, mode=int, minColorRed=float, clashColorGreen=float, aboveMaxColorRed=float, typeId=int, aboveMaxColorGreen=float, maxColorGreen=float, clashColorRed=float, useMax=bool, numIdTypes=int, noColorGreen=float, queryMode=bool, colorGreen=float, minValue=float, maxValue=float, attrName="string", clashColorBlue=float, colorBlue=float, belowMinColorBlue=float):
    """
    polyColorBlindData is NOT undoable, NOT queryable, and NOT editable.
    

    
This command applies false color to the selected polygonal components and objects, depending on whether or not blind data exists for the selected components (or, in the case of poly objects, dynamic attributes), and, depending on the color mode indicated, what the values are. It is possible to color objects based on whether or not the data exists, if the data matches a specific value or range of values, or grayscale color the data according to what the actual value is in relation to the specified min and max. This command also has a query mode in which the components and/or objects are returned in a string array to allow for selection filtering.

    """
    pass
    


def polyColorDel(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyColorDel is undoable, queryable, and editable.
    

    
Deletes color from selected components.

    """
    pass
    


def polyColorMod(satv=float, huev=float, baseColorName="string", nodeState=int, name="string", value=float, caching=bool, constructionHistory=bool):
    """
    polyColorMod is undoable, queryable, and editable.
    

    
Modifies the attributes of a poly color set.

    """
    pass
    


def polyColorPerVertex(representation=int, remove=bool, notUndoable=bool, colorB=float, alpha=float, colorDisplayOption=bool, relative=bool, colorRGB=float, colorR=float, colorG=float, clamped=bool):
    """
    polyColorPerVertex is undoable, queryable, and editable.
    

    
Command associates color(rgb and alpha) with vertices on polygonal objects. When used with the query flag, it returns the color associated with the specified components.

    """
    pass
    


def polyColorSet(delete=bool, currentPerInstanceSet=bool, allColorSets=bool, colorSet="string", perInstance=bool, shareInstances=bool, unshared=bool, currentColorSet=bool, newColorSet="string", copy=bool, representation="string", rename=bool, create=bool, clamped=bool):
    """
    polyColorSet is undoable, queryable, and editable.
    

    
Command to do the following to color sets: - delete an existing color set. - rename an existing color set. - create a new empty color set. - set the current color set to a pre-existing color set. - modify sharing between instances of per-instance color sets - query the current color set. - query the names of all color sets. - query the name(s) along with representation value(s) or clamped value(s) of all color sets - query the representation value or clamped value of the current color set

    """
    pass
    


def polyCompare(colorSets=bool, vertices=bool, edges=bool, faceDesc=bool, uvSets=bool, userNormals=bool, uvSetIndices=bool, colorSetIndices=bool):
    """
    polyCompare is undoable, NOT queryable, and NOT editable.
    

    
Compares two Polygonal Geometry objects with a fine control on what to compare.
If no objects are specified in the command line, then the objects from the active list are used.
Default behaviour is to compare all flags.
Use MEL script polyCompareTwoObjects.mel to get formatted output from this command.

    """
    pass
    


def polyCone(axis="string", texture=bool, radius="string", createUVs=int, height="string", constructionHistory=bool, subdivisionsY=int, subdivisionsX=int, subdivisionsZ=int, name="string"):
    """
    polyCone is undoable, queryable, and editable.
    

    
The cone command creates a new polygonal cone.

    """
    pass
    


def polyConnectComponents(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyConnectComponents is undoable, queryable, and editable.
    

    
Splits polygon edges according to the selected components. The selected components are gathered into connected 'paths' that define continuous splits. Mixed components (vertices, edges and faces) can be used at once. The connection rules are: * Edges can connect to other edges in the same face or to vertices in the same face (that are not in the edge itself) or to faces connected to other edges in the same face. * Vertices can connect to edges (as above) or to vertices in the same face (that are not joined to the first vertex by an edge) or to faces adjacent to a face that uses the vertex (except those that also use the vertex). * Faces can connect to vertices or edges (as above) or to adjacent faces.

    """
    pass
    


def polyContourProjection(offset0="string", offset2="string", method=int, offset1="string", reduceShear=float, smoothness1=float, smoothness2=float, createNewMap=bool, name="string", worldSpace=bool, nodeState=int, userDefinedCorners=bool, constructionHistory=bool, flipRails=bool, offset3="string", smoothness3=float, caching=bool, insertBeforeDeformers=bool, smoothness0=float):
    """
    polyContourProjection is undoable, queryable, and editable.
    

    
Performs a contour stretch UV projection onto an object.

    """
    pass
    


def polyCopyUV(selectionList, uvSetName="string", createNewMap=bool, uvSetNameInput="string", nodeState=int, constructionHistory=bool, caching=bool, name="string"):
    """
    polyCopyUV is undoable, queryable, and editable.
    

    
Copy some UVs from a UV set into another.

    """
    pass
    


def polyCrease(relativeValue=float, operation=int, vertexValue=float, value=float, createHistory=bool):
    """
    polyCrease is undoable, queryable, and editable.
    

    
Command to set the crease values on the edges or vertices of a poly. The crease values are used by the smoothing algorithm.

    """
    pass
    


def polyCreaseCtx(relative=bool, createSet="string", extendSelection=bool):
    """
    polyCreaseCtx is undoable, queryable, and editable.
    

    
Create a new context to crease components on polygonal objects

    """
    pass
    


def polyCreateFacet(texture=int, subdivision=int, name="string", hole=bool, point=(), constructionHistory=bool):
    """
    polyCreateFacet is undoable, queryable, and editable.
    

    
Create a new polygonal object with the specified face, which will be closed. List of arguments must have at least 3 points.

    """
    pass
    


def polyCreateFacetCtx(append=bool, subdivision=int, maximumNumberOfPoints=int, planarConstraint=bool):
    """
    polyCreateFacetCtx is undoable, queryable, and editable.
    

    
Create a new context to create polygonal objects

    """
    pass
    


def polyCube(texture=int, depth="string", axis="string", width="string", createUVs=int, height="string", constructionHistory=bool, subdivisionsY=int, subdivisionsX=int, subdivisionsZ=int, name="string"):
    """
    polyCube is undoable, queryable, and editable.
    

    
The cube command creates a new polygonal cube.

    """
    pass
    


def polyCut(deleteFaces=bool, extractOffsetZ="string", cutPlaneCenterY="string", cutPlaneSize="string", cutPlaneCenter="string", extractOffset="string", cutPlaneRotate=int, worldSpace=bool, extractOffsetX="string", cutPlaneRotateZ=int, cutPlaneCenterX="string", name="string", extractFaces=bool, extractOffsetY="string", cutPlaneWidth="string", cuttingDirection="string", cutPlaneCenterZ="string", cutPlaneRotateY=int, caching=bool, cutPlaneRotateX=int, nodeState=int, cutPlaneHeight="string", constructionHistory=bool):
    """
    polyCut is undoable, queryable, and editable.
    

    
This command splits a mesh, or a set of poly faces, along a plane. The position and orientation of the plane can be adjusted using the appropriate flags listed above. In addition, the cut operation can also delete the faces lying on one side of the cutting plane, or extract those faces by an offset amount.

    """
    pass
    


def polyCutCtx():
    """
    polyCutCtx is undoable, queryable, and editable.
    

    
Create a new context to cut facets on polygonal objects

    """
    pass
    


def polyCylinder(texture=int, axis="string", radius="string", createUVs=int, height="string", constructionHistory=bool, subdivisionsY=int, subdivisionsX=int, subdivisionsZ=int, name="string"):
    """
    polyCylinder is undoable, queryable, and editable.
    

    
The cylinder command creates a new polygonal cylinder.

    """
    pass
    


def polyCylindricalProjection(projectionScaleU=float, imageScaleU=float, imageCenter=float, rotateX=int, insertBeforeDeformers=bool, projectionCenterZ="string", projectionCenter="string", imageScaleV=float, worldSpace=bool, projectionCenterY="string", rotationAngle=int, caching=bool, name="string", seamCorrect=bool, imageCenterY=float, smartFit=bool, imageScale=float, projectionScale=float, rotate=int, rotateY=int, createNewMap=bool, projectionScaleV=float, nodeState=int, constructionHistory=bool, rotateZ=int, projectionCenterX="string", imageCenterX=float):
    """
    polyCylindricalProjection is undoable, queryable, and editable.
    

    
Projects a cylindrical map onto an object.

    """
    pass
    


def polyDelEdge(nodeState=int, caching=bool, cleanVertices=bool, constructionHistory=bool, name="string"):
    """
    polyDelEdge is undoable, queryable, and editable.
    

    
Deletes selected edges, and merges neighboring faces. If deletion leaves winged vertices, they may be deleted as well.
Notice : only non border edges can be deleted.

    """
    pass
    


def polyDelFacet(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyDelFacet is undoable, queryable, and editable.
    

    
Deletes faces. If the result is split into disconnected pieces, the pieces (so-called shells) are still considered to be one object.
Notice : The last face cannot be deleted.

    """
    pass
    


def polyDelVertex(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyDelVertex is undoable, queryable, and editable.
    

    
Deletes vertices. Joins two edges which have a common vertex. The vertices must be connected to exactly two edges (so-called "winged").

    """
    pass
    


def polyDuplicateAndConnect(removeOriginalFromShaders=bool, renameChildren=bool):
    """
    polyDuplicateAndConnect is undoable, NOT queryable, and NOT editable.
    

    
This command duplicates the input polygonal object, connects up the outMesh attribute of the original polygonal shape to the inMesh attribute of the newly created duplicate shape and copies over the shader assignments from the original shape to the new duplicated shape.
The command will fail if no objects are selected or sent as argument or if the object sent as argument is not a polygonal object.

    """
    pass
    


def polyDuplicateEdge(splitType=int, nodeState=int, offset=float, constructionHistory=bool, caching=bool, smoothingAngle=int, name="string"):
    """
    polyDuplicateEdge is undoable, queryable, and editable.
    

    
Duplicates a series of connected edges (edgeLoop)

    """
    pass
    


def polyEditEdgeFlow(constructionHistory=bool, adjustEdgeFlow=float, nodeState=int, edgeFlow=bool, caching=bool, name="string"):
    """
    polyEditEdgeFlow is undoable, queryable, and editable.
    

    
Edit edges of a polygonal object to respect surface curvature.

    """
    pass
    


def polyEditUV(uvSetName="string", angle=float, pivotU=float, uValue=float, scaleU=float, vValue=float, pivotV=float, scaleV=float, relative=bool, rotation=bool, scale=bool):
    """
    polyEditUV is undoable, queryable, and NOT editable.
    

    
Command edits uvs on polygonal objects. When used with the query flag, it returns the uv values associated with the specified components.

    """
    pass
    


def polyEditUVShell(uvSetName="string", angle=float, pivotU=float, uValue=float, scaleU=float, vValue=float, pivotV=float, scaleV=float, relative=bool, rotation=bool, scale=bool):
    """
    polyEditUVShell is undoable, queryable, and NOT editable.
    

    
Command edits uv shells on polygonal objects. When used with the query flag, it returns the transformation values associated with the specified components.

    """
    pass
    


def polyEvaluate(polypoly, uvSetName="string", boundingBoxComponent=bool, accurateEvaluation=bool, uvcoord=bool, vertexComponent=bool, triangle=bool, boundingBox2d=bool, format=bool, boundingBoxComponent2d=bool, edge=bool, area=bool, displayStats=bool, boundingBox=bool, edgeComponent=bool, triangleComponent=bool, uvComponent=bool, face=bool, worldArea=bool, vertex=bool, faceComponent=bool, shell=bool):
    """
    polyEvaluate is undoable, NOT queryable, and NOT editable.
    

    
Returns the required counts on the specified objects.
If no objects are specified in the command line, then the objects from the active list are used.
In MEL, the values are returned in the same order as the flags are set. Under Python, there is no concept of argument ordering, so the items are returned in a dictionary keyed by the name of the flag. In Python, if only one item is requested, then it will not be returned in a dictionary.
For user convenience, if no flag is set, then all values are echoed.
All flags (except -fmt/format) are in fact query-flags. For user convenience, the -q flag may be ommitted.
Some comments for non-formatted output :
3d bounding boxes are returned as 3 couples of floats, 2d ones as 2 couples of floats.
if a bounding box is queried and cannot be computed (for example the component bounding box when no component is selected, or 2d bounding box for and unmapped object) 0 is returned for each array element, so that indices in the output array remain consistent.
int values (queried by topological flags) cannot be mixed with float values (queried by bounding box flags). Thus if no flag is set, only int values are returned.

    """
    pass
    


def polyExtrudeEdge(localRotateY=int, keepFacesTogether=bool, rotateX=int, localRotateX=int, localDirectionZ="string", localScaleX=float, scale=float, translateZ="string", localScale=float, localTranslateX="string", localScaleY=float, localTranslateZ="string", localTranslateY="string", worldSpace=bool, scaleZ=float, pivotY="string", divisions=int, random=float, pivotX="string", translate="string", localRotateZ=int, translateX="string", caching=bool, name="string", localDirectionX="string", scaleX=float, translateY="string", localDirection="string", smoothingAngle=int, localDirectionY="string", localScaleZ=float, pivot="string", pivotZ="string", rotate=int, inputCurve="string", localRotate=int, nodeState=int, scaleY=float, rotateZ=int, rotateY=int, localTranslate="string", constructionHistory=bool):
    """
    polyExtrudeEdge is undoable, queryable, and editable.
    

    
Extrude edges separately or together.

    """
    pass
    


def polyExtrudeFacet(localRotateY=int, translateZ="string", keepFacesTogether=bool, gravity="string", localRotateX=int, attraction=float, localScaleX=float, scale=float, magnX="string", localScale=float, localTranslateX="string", localScaleY=float, localTranslateZ="string", weight=float, localTranslateY="string", worldSpace=bool, gravityZ="string", pivotY="string", divisions=int, random=float, pivotX="string", offset=float, localRotateZ=int, translate="string", inputCurve="string", name="string", localDirectionX="string", scaleZ=float, scaleX=float, magnY="string", gravityX="string", rotateX=int, translateY="string", translateX="string", localDirection="string", smoothingAngle=int, localDirectionY="string", localScaleZ=float, pivot="string", pivotZ="string", rotate=int, caching=bool, gravityY="string", localDirectionZ="string", localRotate=int, nodeState=int, scaleY=float, rotateZ=int, rotateY=int, localTranslate="string", magnet="string", constructionHistory=bool):
    """
    polyExtrudeFacet is undoable, queryable, and editable.
    

    
Extrude faces. Faces can be extruded separately or together, and manipulations can be performed either in world or object space.

    """
    pass
    


def polyExtrudeVertex(length=float, width=float, divisions=int, worldSpace=bool, nodeState=int, name="string", caching=bool, constructionHistory=bool):
    """
    polyExtrudeVertex is undoable, queryable, and editable.
    

    
Command that extrudes selected vertices outwards.

    """
    pass
    


def polyFlipEdge():
    """
    polyFlipEdge is undoable, queryable, and editable.
    

    
Command to flip the edges shared by 2 adjacent triangles. When used with the edit flag, new edges can be added to the same node, instead of creating a separate node in the chain.

    """
    pass
    


def polyFlipUV(local=bool, uvSetName="string", createNewMap=bool, name="string", nodeState=int, constructionHistory=bool, caching=bool, flipType=int, insertBeforeDeformers=bool):
    """
    polyFlipUV is undoable, queryable, and editable.
    

    
Flip (mirror) the UVs (in texture space) of input polyFaces, about either the U or V axis..

    """
    pass
    


def polyForceUV(local=bool, flipVertical=bool, preserveAspectRatio=bool, unshare=bool, unitize=bool, uvSetName="string", normalize="string", createNewMap=bool, g=bool, numItems=int, flipHorizontal=bool, cameraProjection=bool):
    """
    polyForceUV is undoable, NOT queryable, and NOT editable.
    

    
A set of functionalities can be called through this command. The input for this command is a set of faces. Based on the arguments passed, the UVs for these selected faces can be created.
Project UVs based on the camera: (UV creation)
Based on the current view direction/orientation, the UVs are generated and assigned to the faces. Any previously assigned UV information will be lost.
Best Plane Projection: (UV creation)
The UVs are computed based on the plane defined by the user, and is applied to the selected faces. This tool has 2 phases. In the first phase, the faces to be mapped (faces to which UVs are to be created) are selected. In the second phase, the points (vertices, CVs) that define the projecting plane are selected. Any previously assigned UV information will be lost.
Unitize: (UV creation)
A new set of unitized UVs are generated and assigned to the faces. Any previously assigned UV information will be lost.
Unshare: (UV creation)
Force the specified UV to be unshared by possibly creating new UVs. Any previously assigned UV information will be lost.

    """
    pass
    


def polyGeoSampler(displaceGeometry=bool, clampAlphaMax=float, scaleFactor=float, colorDisplayOption=bool, shareUV=bool, averageColor=bool, useLightShadows=bool, clampRGBMin=float, lightingOnly=bool, clampAlphaMin=float, alphaBlend="string", flatShading=bool, sampleByFace=bool, ignoreDoubleSided=bool, clampRGBMax=float, reuseShadows=bool, computeShadows=bool, colorBlend="string"):
    """
    polyGeoSampler is undoable, NOT queryable, and editable.
    

    
This command performs a render sampling of surface color and transparency for each selected vertex or face and stores the sampled data as either the color value, or uses the sampled data to displace the affected vertices or faces by a sampled data value. Transparency is not used for displacement, and displacement is performed along vertex normals. The sampled data value used can be pre-scaled by a user defined amount. Additionally, the normals chosen for sampling can be overridden using a "flat" shading option. This option basically means to always use the normals of the faces when computing sampling values. This may be a desired if the user wishes to override an edge smoothness factor. Basically with the "flat" shading option on, edges are always considered to be hard. Note that displacement sampling will result in the -sampleByFace option to be turned off, since a displacement of a vertex always affects the faces the vertex is connected to. Finally, it is possible to force the storage of shared colors per vertex, and / or force the usage of unshared UV values. The computation of the resulting color is as follows:
        resulting-RGB = (sampled-RGB * scale-factor);
        if (color blend is none)
                resulting-RGB = geometry-RGB
        else if (color blend is add)
                resulting-RGB = geometry-RGB + sampled-RGB;
        else if (color blend is subtract)
                resulting-RGB = geometry-RGB - sampled-RGB;
        else if (color blend is multiply)
                resulting-RGB = geometry-RGB * sampled-RGB;
        else if (color blend is divide)
                resulting-RGB = geometry-RGB / sampled-RGB;
        else if (color blend is average)
                resulting-RGB = (geometry-RGB * 1/2) + (sampled-RGB * 1/2);
        if (clamp option set)
                clamp resulting-RGB between minimum-RGB and maximum-RGB,
The analogous computation is done for computing the resulting alpha value. The command requires that there be a camera selected in your scene in order to work properly in -batch or -prompt mode.

    """
    pass
    


def polyHelix(texture=int, axis="string", radius="string", width="string", subdivisionsCaps=int, createUVs=int, direction=int, subdivisionsCoil=int, height="string", name="string", coils=float, subdivisionsAxis=int, constructionHistory=bool):
    """
    polyHelix is undoable, queryable, and editable.
    

    
The polyHelix command creates a new polygonal helix.

    """
    pass
    


def polyHole(assignHole=bool, createHistory=bool):
    """
    polyHole is undoable, queryable, and editable.
    

    
Command to set and clear holes on given faces.

    """
    pass
    


def polyInfo(invalidVertices=bool, faceToVertex=bool, nonManifoldUVs=bool, edgeToVertex=bool, faceNormals=bool, faceToEdge=bool, nonManifoldEdges=bool, vertexToEdge=bool, laminaFaces=bool, nonManifoldUVEdges=bool, edgeToFace=bool, nonManifoldVertices=bool, vertexToFace=bool, invalidEdges=bool):
    """
    polyInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
Command queries topological information on polygonal objects and components. So, the command will require the following to be specified: - selection list to query

    """
    pass
    


def polyInstallAction(installDisplay=bool, keepInstances=bool, installConstraint=bool, uninstallDisplay=bool, commandName=bool, uninstallConstraint=bool, convertSelection=bool):
    """
    polyInstallAction is undoable, queryable, and NOT editable.
    

    
Installs/uninstalls several things to help the user to perform the specified action :
Pickmask
Internal selection constraints
Display attributes

    """
    pass
    


def polyLayoutUV(uvSetName="string", rotateForBestFit=int, flipReversed=bool, percentageSpace=float, layout=int, worldSpace=bool, nodeState=int, constructionHistory=bool, separate=int, layoutMethod=int, scale=int, caching=bool, name="string"):
    """
    polyLayoutUV is undoable, queryable, and editable.
    

    
Move UVs in the texture plane to avoid overlaps.

    """
    pass
    


def polyListComponentConversion(selectionItem, toVertexFace=bool, internal=bool, fromVertex=bool, vertexFaceAllEdges=bool, fromUV=bool, toUV=bool, fromEdge=bool, toVertex=bool, border=bool, fromFace=bool, toEdge=bool, toFace=bool, fromVertexFace=bool):
    """
    polyListComponentConversion is undoable, NOT queryable, and NOT editable.
    

    
This command converts poly components from one or more types to another one or more types, and returns the list of the conversion. It doesn't change anything of the current database.

    """
    pass
    


def polyMapCut(nodeState=int, moveratio=float, caching=bool, name="string", constructionHistory=bool):
    """
    polyMapCut is undoable, queryable, and editable.
    

    
Cut along edges of the texture mapping. The cut edges become map borders.

    """
    pass
    


def polyMapDel(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyMapDel is undoable, queryable, and editable.
    

    
Deletes texture coordinates (UVs) from selected faces.

    """
    pass
    


def polyMapSew(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyMapSew is undoable, queryable, and editable.
    

    
Sew border edges in texture space. Selected edges must be map borders.

    """
    pass
    


def polyMapSewMove(numberFaces=int, uvSetName="string", nodeState=int, limitPieceSize=bool, constructionHistory=bool, caching=bool, name="string"):
    """
    polyMapSewMove is undoable, queryable, and editable.
    

    
This command can be used to Move and Sew together separate UV pieces along geometric edges. UV pieces that correspond to the same geometric edge, are merged together by moving the smaller piece to the larger one.

    """
    pass
    


def polyMergeEdge(secondEdge=int, mergeMode=int, nodeState=int, constructionHistory=bool, firstEdge=int, caching=bool, name="string"):
    """
    polyMergeEdge is undoable, queryable, and editable.
    

    
Sews two border edges together.
The new edge is located either on the first, last, or between both selected edges, depending on the mode.
Both edges must belong to the same object, and orientations must match (i.e. normals on corresponding faces must point in the same direction).
Edge flags are mandatory.

    """
    pass
    


def polyMergeEdgeCtx(image1="string", reset=bool, toolNode=bool, immediate=bool, name="string", mergeMode=int, image3="string", exists=bool, image2="string", activeNodes=bool, previous=bool):
    """
    polyMergeEdgeCtx is undoable, queryable, and editable.
    

    
Create a new context to merge edges on polygonal objects

    """
    pass
    


def polyMergeFacet(firstFacet=int, mergeMode=int, nodeState=int, constructionHistory=bool, secondFacet=int, caching=bool, name="string"):
    """
    polyMergeFacet is undoable, queryable, and editable.
    

    
The second face becomes a hole in the first face.
The new holed face is located either on the first, last, or between both selected faces, depending on the mode.
Both faces must belong to the same object.
Facet flags are mandatory.

    """
    pass
    


def polyMergeFacetCtx(image1="string", reset=bool, toolNode=bool, immediate=bool, name="string", mergeMode=int, image3="string", exists=bool, image2="string", activeNodes=bool, previous=bool):
    """
    polyMergeFacetCtx is undoable, queryable, and editable.
    

    
Create a new context to merge facets on polygonal objects

    """
    pass
    


def polyMergeUV(uvSetName="string", distance=float, nodeState=int, name="string", caching=bool, constructionHistory=bool):
    """
    polyMergeUV is undoable, queryable, and editable.
    

    
Merge UVs of an object based on their distance. UVs are merge only if they belong to the same 3D vertex.

    """
    pass
    


def polyMergeVertex(distance="string", mergeToComponents="string", nodeState=int, name="string", texture=bool, alwaysMergeTwoVertices=bool, caching=bool, constructionHistory=bool):
    """
    polyMergeVertex is undoable, queryable, and editable.
    

    
Merge vertices within a given threshold.
Since this allows merging any vertices that lie on the same object it is possible for the resulting geometry to be non-manifold.
First, perform comparison of pairs of selected vertices. Pairs that lie within given distance of one another are merged, along with the edge between them.
Second, any selected vertices which share an edge are merged if the distance between them is within the specified distance.
Unlike Merge Edges, Merge Vertices will perform the merge even if the edges adjoining the vertices do not have matching orientation (i.e. normals of adjacent faces do not point in the same direction). As this restriction is not enforced while merging vertices, resulting geometry can be non-manifold.
If alwaysMergeTwoVertices is set and there are only two vertices, tolerance is ignored and the vertices will be merged.
Resulting mesh may have extra vertices or edges to ensure geometry is valid.

    """
    pass
    


def polyMirrorFace(mirrorAxis=int, worldSpace=bool, pivot="string", pivotZ="string", pivotY="string", nodeState=int, mirrorPosition="string", mergeMode=int, direction=int, mergeThresholdType=int, name="string", mergeThreshold="string", pivotX="string", caching=bool, constructionHistory=bool):
    """
    polyMirrorFace is undoable, queryable, and editable.
    

    
Mirror all the faces of the selected object.

    """
    pass
    


def polyMoveEdge(localCenter=int, localRotateY=int, rotateX=int, localRotateX=int, localDirectionZ="string", localScaleX=float, scale=float, translateZ="string", localScale=float, localTranslateX="string", localScaleY=float, localTranslateZ="string", localTranslateY="string", worldSpace=bool, scaleZ=float, pivotY="string", random=float, pivotX="string", translate="string", localRotateZ=int, translateX="string", caching=bool, name="string", localDirectionX="string", translateY="string", localDirection="string", localDirectionY="string", localScaleZ=float, pivot="string", pivotZ="string", rotate=int, rotateY=int, localRotate=int, nodeState=int, scaleY=float, rotateZ=int, scaleX=float, localTranslate="string", constructionHistory=bool):
    """
    polyMoveEdge is undoable, queryable, and editable.
    

    
Modifies edges of a polygonal object. Translate, move, rotate or scale edges.

    """
    pass
    


def polyMoveFacet(localRotateY=int, translateZ="string", gravity="string", localRotateX=int, localDirectionZ="string", localScaleX=float, scale=float, magnZ="string", magnX="string", localScale=float, localTranslateX="string", localScaleY=float, localTranslateZ="string", weight=float, localTranslateY="string", worldSpace=bool, gravityZ="string", pivotY="string", random=float, pivotX="string", offset=float, localRotateZ=int, translate="string", caching=bool, name="string", localDirectionX="string", scaleZ=float, magnY="string", gravityX="string", rotateX=int, translateY="string", translateX="string", localDirection="string", localDirectionY="string", localScaleZ=float, pivot="string", pivotZ="string", rotate=int, rotateY=int, gravityY="string", attraction=float, localRotate=int, nodeState=int, scaleY=float, rotateZ=int, scaleX=float, localTranslate="string", magnet="string", constructionHistory=bool):
    """
    polyMoveFacet is undoable, queryable, and editable.
    

    
Modifies facet of a polygonal object. Translate, move, rotate or scale facets.

    """
    pass
    


def polyMoveFacetUV(translateV=float, pivotU=float, translate=float, scaleU=float, pivot=float, axisLenX=float, random=float, scaleV=float, nodeState=int, axisLen=float, constructionHistory=bool, axisLenY=float, scale=float, rotationAngle=int, pivotV=float, caching=bool, translateU=float, name="string"):
    """
    polyMoveFacetUV is undoable, queryable, and editable.
    

    
Modifies the map by moving all UV values associated with the selected face(s).
The UV coordinates of the model are manipulated without changing the vertices of the 3D object.

    """
    pass
    


def polyMoveUV(translateV=float, pivotU=float, translate=float, scaleU=float, pivot=float, pivotV=float, random=float, scaleV=float, nodeState=int, scale=float, constructionHistory=bool, rotationAngle=int, caching=bool, translateU=float, name="string"):
    """
    polyMoveUV is undoable, queryable, and editable.
    

    
Moves selected UV coordinates in 2D space. As the selected UVs are adjusted, the way the image is mapped onto the object changes accordingly. This command manipulates the UV values without changing the 3D geometry of the object.

    """
    pass
    


def polyMoveVertex(localDirectionZ="string", scale=float, rotateX=int, localTranslateX="string", localTranslateZ="string", localTranslateY="string", worldSpace=bool, scaleZ=float, pivotY="string", random=float, pivotX="string", translate="string", translateX="string", caching=bool, name="string", localDirectionX="string", translateY="string", localDirection="string", localDirectionY="string", pivot="string", pivotZ="string", rotate=int, rotateY=int, translateZ="string", nodeState=int, scaleY=float, rotateZ=int, scaleX=float, localTranslate="string", constructionHistory=bool):
    """
    polyMoveVertex is undoable, queryable, and editable.
    

    
Modifies vertices of a polygonal object. Translate, rotate or scale vertices in local or world space.

    """
    pass
    


def polyMultiLayoutUV(uvSetName="string", rotateForBestFit=int, scale=int, gridU=int, flipReversed=bool, percentageSpace=float, prescale=int, offsetV=float, layout=int, sizeV=float, offsetU=float, sizeU=float, layoutMethod=int, gridV=int):
    """
    polyMultiLayoutUV is undoable, NOT queryable, and NOT editable.
    

    
place the UVs of the selected polygonal objects so that they do not overlap.

    """
    pass
    


def polyNormal(nodeState=int, normalMode=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyNormal is undoable, queryable, and editable.
    

    
Control the normals of an object. This command works on faces or polygonal objects.

    """
    pass
    


def polyNormalizeUV(normalizeType=int, uvSetName="string", preserveAspectRatio=bool, createNewMap=bool, name="string", nodeState=int, constructionHistory=bool, caching=bool, insertBeforeDeformers=bool):
    """
    polyNormalizeUV is undoable, queryable, and editable.
    

    
Normalizes the UVs of input polyFaces. The existing UVs of the faces are normalized between 0 and 1.

    """
    pass
    


def polyNormalPerVertex(freezeNormal=bool, unFreezeNormal=bool, normalY=float, normalXYZ=float, normalX=float, deformable=bool, relative=bool, normalZ=float, allLocked=bool):
    """
    polyNormalPerVertex is undoable, queryable, and editable.
    

    
Command associates normal(x, y, z) with vertices on polygonal objects. When used with the query flag, it returns the normal associated with the specified components. However, when queried, the command returns all normals (all vtx-face combinations) on the vertex, regardless of whether they are shared or not.

    """
    pass
    


def polyOptions(sizeBorder=float, reuseTriangles=bool, hardEdge=bool, smoothDrawType=int, pointFacet=bool, gl=bool, displayMapBorder=bool, displayUVTopology=bool, relative=bool, displayTriangle=bool, displaySubdComps=bool, point=bool, displayInvisibleFaces=bool, displayCreaseEdge=bool, displayCreaseVertex=bool, activeObjects=bool, displayBorder=bool, newPolymesh=bool, colorShadedDisplay=bool, fullBack=bool, colorMaterialChannel="string", displayWarp=bool, displayVertex=bool, displayGeometry=bool, facet=bool, displayMetadata=bool, softEdge=bool, sizeVertex=float, hardBack=bool, hardEdgeColor=bool, sizeNormal=float, backCullVertex=bool, displayCenter=bool, displayNormal=bool, sizeUV=float, allEdges=bool, displayAlphaAsGreyScale=bool, displayItemNumbers=bool, backCulling=bool, vertexNormalMethod=int, wireBackCulling=bool, displayUVs=bool, materialBlend="string"):
    """
    polyOptions is undoable, queryable, and NOT editable.
    

    
Changes the global display polygonal attributes.

    """
    pass
    


def polyOptUvs(uvSetName="string", optimizeAxis=int, nodeState=int, name="string", iterations=int, pinSelected=bool, scale=float, areaWeight=float, useScale=bool, globalMethodBlend=float, globalBlend=float, pinUvBorder=bool, caching=bool, applyToShell=bool, constructionHistory=bool, stoppingThreshold=float):
    """
    polyOptUvs is undoable, queryable, and editable.
    

    
Optimizes selected UVs.

    """
    pass
    


def polyOutput(edgeFace=bool, vertNorm=bool, allValues=bool, normDesc=bool, uvValue=bool, force=bool, group=bool, vert=bool, color=bool, vertEdge=bool, uvDesc=bool, edge=bool, triangle=bool, colorDesc=bool, noOutput=bool, face=bool, faceNorm=bool):
    """
    polyOutput is undoable, NOT queryable, and NOT editable.
    

    
Dumps a description of internal memory representation of poly objects. If no objects are specified in the command line, then the objects from the active list are used. If information on the geometry in the history of a poly shape is desired, then the plug of interest needs to be specified in the command line. Default behaviour is to print only a summary. Use the flags above to get more details on a specific part of the object.

    """
    pass
    


def polyPinUV(uvSetName="string", value=float, operation=int, createHistory=bool):
    """
    polyPinUV is undoable, queryable, and editable.
    

    
This command is used to pin and unpin UVs. A "pinned" UV is one which should not be modified.
Each UV has an associated pin weight, that defaults to 0.0 meaning that the UV is not pinned. If pin weight is set to 1.0 then it becomes fully pinned and UV tools should not modify that UV. If the pin weight is set to a value between 0.0 and 1.0 then UV tools should weight their changes to that UV accordingly.
UV pinning is not enforced by the shape node: it is up to each tool to decide whether it will obey the pin weights.

    """
    pass
    


def polyPipe(subdivisionsHeight=int, axis="string", radius="string", createUVs=bool, subdivisionsCaps=int, thickness="string", height="string", constructionHistory=bool, texture=bool, name="string"):
    """
    polyPipe is undoable, queryable, and editable.
    

    
The polyPipe command creates a new polygonal pipe.

    """
    pass
    


def polyPlanarProjection(imageScaleU=float, projectionScaleU="string", imageCenter=float, rotateX=int, insertBeforeDeformers=bool, projectionCenterZ="string", projectionCenter="string", mapDirection="string", imageScaleV=float, worldSpace=bool, projectionCenterY="string", rotationAngle=int, caching=bool, name="string", imageCenterY=float, projectionScale="string", imageScale=float, rotate=int, rotateY=int, createNewMap=bool, nodeState=int, constructionHistory=bool, rotateZ=int, projectionScaleV="string", projectionCenterX="string", imageCenterX=float):
    """
    polyPlanarProjection is undoable, queryable, and editable.
    

    
Projects a map onto an object, using an orthogonal projection. The piece of the map defined from isu, isv, icx, icy area, is placed at pcx, pcy, pcz location.

    """
    pass
    


def polyPlane(texture=int, axis="string", width="string", createUVs=int, height="string", constructionHistory=bool, subdivisionsY=int, subdivisionsX=int, name="string"):
    """
    polyPlane is undoable, queryable, and editable.
    

    
The mesh command creates a new polygonal plane.

    """
    pass
    


def polyPlatonicSolid(sideLength="string", texture=int, axis="string", radius="string", solidType=int, createUVs=int, constructionHistory=bool, name="string"):
    """
    polyPlatonicSolid is undoable, queryable, and editable.
    

    
The polyPlatonicSolid command creates a new polygonal platonic solid.

    """
    pass
    


def polyPoke(translateZ="string", caching=bool, name="string", worldSpace=bool, nodeState=int, translate="string", constructionHistory=bool, translateY="string", translateX="string", localTranslateX="string", localTranslateZ="string", localTranslate="string", localTranslateY="string"):
    """
    polyPoke is undoable, queryable, and editable.
    

    
Introduces a new vertex in the middle of the selected face, and connects it to the rest of the vertices of the face.

    """
    pass
    


def polyPrimitive(sideLength="string", axis="string", radius="string", polyType=int, constructionHistory=bool, name="string"):
    """
    polyPrimitive is undoable, queryable, and editable.
    

    
Create a polygon primative

    """
    pass
    


def polyPrism(sideLength="string", subdivisionsHeight=int, texture=int, axis="string", length="string", numberOfSides=int, subdivisionsCaps=int, createUVs=int, constructionHistory=bool, name="string"):
    """
    polyPrism is undoable, queryable, and editable.
    

    
The prism command creates a new polygonal prism.

    """
    pass
    


def polyProjectCurve(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyProjectCurve is undoable, queryable, and editable.
    

    
The polyProjectCurve command creates curves by projecting a selected curve onto a selected poly mesh. The direction of projection will be the current view direction unless the direction vector is specified with the -direction/-d flag.

    """
    pass
    


def polyProjection(uvSetName="string", projectionScaleU=float, imageScaleU=float, rotateX=float, insertBeforeDeformers=bool, keepImageRatio=bool, projectionScaleV=float, type="string", mapDirection="string", imageScaleV=float, rotationAngle=float, projectionCenterY=float, seamCorrect=bool, imageCenterY=float, smartFit=bool, rotateZ=float, rotateY=float, createNewMap=bool, projectionCenterZ=float, projectionCenterX=float, constructionHistory=bool, imageCenterX=float):
    """
    polyProjection is undoable, NOT queryable, and NOT editable.
    

    
Creates a mapping on the selected polygonal faces. When construction history is created, the name of the new node is returned. In other cases, the command returns nothing.

    """
    pass
    


def polyPyramid(sideLength="string", subdivisionsHeight=int, axis="string", numberOfSides=int, subdivisionsCaps=int, createUVs=int, constructionHistory=bool, texture=bool, name="string"):
    """
    polyPyramid is undoable, queryable, and editable.
    

    
The pyramid command creates a new polygonal pyramid.

    """
    pass
    


def polyQuad(keepTextureBorders=bool, keepHardEdges=bool, worldSpace=bool, nodeState=int, name="string", angle=int, caching=bool, constructionHistory=bool, keepGroupBorder=bool):
    """
    polyQuad is undoable, queryable, and editable.
    

    
Merges selected triangles of a polygonal object into four-sided faces.

    """
    pass
    


def polyQueryBlindData(longDataName="string", showComp=bool, intData=int, booleanData=bool, shortDataName="string", minValue=float, typeId=int, maxValue=float, doubleData=float, stringData="string", binaryData="string", subString="string", associationType="string"):
    """
    polyQueryBlindData is NOT undoable, NOT queryable, and NOT editable.
    

    
Command query's blindData associated with particular polygonal components. So, the command will require the following to be specified: - selection list to query Optional are the: - typeId - associationType - longDataName or shortDataName of data being queried. - The actual data being specified. - showComponent flag Note that for object level blind data, the showComponent flag will be ignored. If no components are selected, the assocation flag will be ignored and object level data will be queried.

    """
    pass
    


def polyReduce(keepHardEdgeWeight=float, sharpness=float, triangulate=bool, keepOriginalVertices=bool, keepCreaseEdgeWeight=float, colorWeights=float, keepColorBorderWeight=float, vertexWeightCoefficient=float, keepHardEdge=bool, symmetryTolerance=float, keepFaceGroupBorder=bool, keepQuadsWeight=float, geomWeights=float, replaceOriginal=bool, symmetryPlaneY=float, uvWeights=float, compactness=float, triangleCount=int, keepBorderWeight=float, caching=bool, keepCreaseEdge=bool, name="string", symmetryPlaneZ=float, symmetryPlaneW=float, keepMapBorderWeight=float, preserveLocation=bool, percentage=float, invertVertexWeights=bool, keepBorder=bool, keepFaceGroupBorderWeight=float, vertexCount=int, weightCoefficient=float, cachingReduce=bool, keepColorBorder=bool, useVirtualSymmetry=int, version=int, vertexMapName="string", nodeState=int, preserveTopology=bool, symmetryPlaneX=float, termination=int, keepMapBorder=bool, constructionHistory=bool):
    """
    polyReduce is undoable, queryable, and editable.
    

    
Simplify a polygonal object by reducing geometry while preserving the overall shape of the mesh.
The algorithm for polyReduce was changed in 2014 to use a new algorithm derived from Softimage. However, the command still defaults to using the old algorithm for backwards compatibility. Therefore, we recommend setting the version flag to 1 for best results as the new algorithm is better at preserving geometry features. Additionally, some flags only apply to a specific algorithm and this is documented for each flag.

    """
    pass
    


def polyRemesh(refineThreshold=float, reduceThreshold=float, smoothStrength=float, nodeState=int, interpolationType=int, tessellateBorders=bool, constructionHistory=bool, caching=bool, name="string"):
    """
    polyRemesh is undoable, queryable, and editable.
    

    
Triangulates, then remeshes the given mesh through edge splitting and collapsing. Edges longer than the specified refinement threshold are split, and edges shorter than the reduction threshold are collapsed.

    """
    pass
    


def polySelect(shortestEdgePathUV=int, edgeRingPath=int, replace=bool, toggle=bool, asSelectString=bool, edgeLoopOrBorderPattern=int, extendToShell=int, edgeLoopPattern=int, edgeBorderPattern=int, edgeLoopPath=int, edgeRing=int, addFirst=bool, shortestEdgePath=int, edgeLoop=int, noSelection=bool, edgeRingPattern=int, deselect=bool, add=bool, edgeBorder=int, shortestFacePath=int, edgeBorderPath=int, edgeUVLoopOrBorder=int, edgeLoopOrBorder=int):
    """
    polySelect is undoable, queryable, and NOT editable.
    

    
This command makes different types of poly component selections. The return value is an integer array containing the id's of the components in the selection in order. If a given type of selection loops back on itself then this is indicated by the start id appearing twice, once at the start and once at the end.

    """
    pass
    


def polySelectConstraint(orientaxis=float, max3dAngle=float, distbound=float, size=int, orderbound=int, borderPropagation=bool, crease=bool, orientbound=float, nonmanifold=int, max2dAngle=float, orient=int, texturedarea=int, loopPropagation=bool, texturedareabound=float, distpoint=float, planarity=int, length=int, wholeSensitive=bool, where=int, edgeDistance=int, textureshared=int, returnSelection=bool, propagate=int, order=int, lengthbound=float, smoothness=int, convexity=int, topology=int, disable=bool, visibilitypoint=float, type=int, uvShell=bool, holes=int, stateString=bool, geometricarea=int, shell=bool, anglePropagation=bool, dist=int, textured=int, distaxis=float, randomratio=float, random=int, geometricareabound=float, angle=int, angleTolerance=float, visibilityangle=int, mode=int, border=bool, anglebound=int, visibility=int, ringPropagation=bool):
    """
    polySelectConstraint is undoable, queryable, and NOT editable.
    

    
Changes the global polygonal selection constraints.

    """
    pass
    


def polySelectConstraintMonitor(delete=bool, create=bool, changeCommand="string"):
    """
    polySelectConstraintMonitor is undoable, NOT queryable, and NOT editable.
    

    
Manage the window to display/edit the polygonal selection constraint parameters

    """
    pass
    


def polySelectCtx(mode=int):
    """
    polySelectCtx is undoable, queryable, and editable.
    

    
Create a new context to select polygon components

    """
    pass
    


def polySelectEditCtx(mode=int):
    """
    polySelectEditCtx is undoable, queryable, and editable.
    

    
Create a new context to select and edit polygonal objects

    """
    pass
    


def polySeparate(poly, object=bool, nodeState=int, name="string", caching=bool, constructionHistory=bool):
    """
    polySeparate is undoable, queryable, and editable.
    

    
This command creates new objects from the given poly. A new object will be created for each section of the mesh that is distinct (no edges connect it to the rest of the mesh).
This command can only separate one object at a time.

    """
    pass
    


def polySetToFaceNormal(setUserNormal=bool):
    """
    polySetToFaceNormal is undoable, NOT queryable, and NOT editable.
    

    
This command takes selected polygonal vertices or vertex-faces and changes their normals. If the option userNormal is used, the new normal values will be the face normals arround the vertices/vertex-faces. Otherwise the new normal values will be default values according to the internal calculation.

    """
    pass
    


def polySewEdge(worldSpace=bool, nodeState=int, constructionHistory=bool, texture=bool, caching=bool, tolerance="string", name="string"):
    """
    polySewEdge is undoable, queryable, and editable.
    

    
Merge border edges within a given threshold.
Perform pair-wise comparison of selected edges. Pairs whose corresponding vertices meet threshold conditions and whose orientations are aligned (i.e. their respective normals point in the same direction) are merged, as are the vertices (in other words, vertices are shared).
Resulting mesh may have extra vertices or edges to ensure geometry is valid.
Edges must be on the same object to be merged.
Default : share only vertices lying exactly at the same place. (polySewEdge -t 0.0)

    """
    pass
    


def polyShortestPathCtx():
    """
    polyShortestPathCtx is undoable, queryable, and editable.
    

    
Creates a new context to select shortest edge path between two vertices or UVs in the 3d viewport.

    """
    pass
    


def polySlideEdge(direction=int, edgeDirection=float, absolute=bool, symmetry=bool):
    """
    polySlideEdge is undoable, NOT queryable, and NOT editable.
    

    
Moves an edge loop selection along the edges connected to the sides of its vertices.

    """
    pass
    


def polySmooth(subdivisionType=int, osdSmoothTriangles=bool, keepTessellation=bool, osdVertBoundary=int, osdFvarPropagateCorners=bool, continuity=float, divisions=int, name="string", propagateEdgeHardness=bool, nodeState=int, keepBorder=bool, osdFvarBoundary=int, osdCreaseMethod=int, keepHardEdge=bool, keepSelectionBorder=bool, caching=bool, constructionHistory=bool):
    """
    polySmooth is undoable, queryable, and editable.
    

    
Smooth a polygonal object. This command works on polygonal objects or faces.

    """
    pass
    


def polySoftEdge(worldSpace=bool, nodeState=int, constructionHistory=bool, angle=int, caching=bool, name="string"):
    """
    polySoftEdge is undoable, queryable, and editable.
    

    
Selectively makes edges soft or hard.

An edge will be made hard if the angle between two owning faces is sharper (larger) than the smoothing angle.
An edge wil be made soft if the angle between two owning facets is flatter (smaller) than the smoothing angle.

    """
    pass
    


def polySphere(texture=int, axis="string", radius="string", createUVs=int, constructionHistory=bool, subdivisionsY=int, subdivisionsX=int, name="string"):
    """
    polySphere is undoable, queryable, and editable.
    

    
The sphere command creates a new polygonal sphere.

    """
    pass
    


def polySphericalProjection(imageScaleU=float, projectionScaleU="string", imageCenter=float, rotateX=int, insertBeforeDeformers=bool, projectionCenterZ="string", projectionCenter="string", imageScaleV=float, worldSpace=bool, projectionCenterY="string", rotationAngle=int, caching=bool, name="string", seamCorrect=bool, imageCenterY=float, smartFit=bool, projectionScale="string", imageScale=float, rotate=int, rotateY=int, createNewMap=bool, nodeState=int, constructionHistory=bool, rotateZ=int, projectionScaleV="string", projectionCenterX="string", imageCenterX=float):
    """
    polySphericalProjection is undoable, queryable, and editable.
    

    
Projects a spherical map onto an object.

    """
    pass
    


def polySplit( edgepoint=int, facepoint=int, insertpoint=int, subdivision=int, name="string", smoothingangle=int, constructionHistory=bool):
    """
    polySplit is undoable, queryable, and editable.
    

    
Split facets/edges of a polygonal object.
The first and last arguments must be edges. Intermediate points may lie on either a shared face or an edge which neighbors the previous point.

    """
    pass
    


def polySplitCtx(precsnap=float, snaptoedge=bool, subdivision=int, magnetsnap=int, enablesnap=bool, smoothingangle=int):
    """
    polySplitCtx is undoable, queryable, and editable.
    

    
Create a new context to split facets on polygonal objects

    """
    pass
    


def polySplitCtx2(constrainToEdges=bool, edgeMagnets=int, snapTolerance=float):
    """
    polySplitCtx2 is undoable, queryable, and editable.
    

    
Create a new context to split facets on polygonal objects

    """
    pass
    


def polySplitEdge(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polySplitEdge is undoable, queryable, and editable.
    

    
Split Edges.
There are two operations for this command depending on the value of the -operation flag.
If -operation is set to 1 then this command will split apart faces along all selected manifold edges.
If -operation is set to 0 then this command will split non-manifold edges so as to make them manifold edges. It creates the minimum number of edges that can be created to make the edge manifold.
The default value for -operation is 1, operate on manifold edges.
Resulting mesh may have extra vertices or edges to ensure geometry is valid.

    """
    pass
    


def polySplitRing(divisions=int, splitType=int, weight=float, nodeState=int, name="string", rootEdge=int, direction=bool, caching=bool, smoothingAngle=int, constructionHistory=bool):
    """
    polySplitRing is undoable, queryable, and editable.
    

    
Splits a series of ring edges of connected quads and inserts connecting edges between them.

    """
    pass
    


def polySplitVertex(worldSpace=bool, nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polySplitVertex is undoable, queryable, and editable.
    

    
Use this command to split one or more vertices.
A mesh is made up of one or more faces. The faces are defined by edges which connect vertices together. Typically a face will share vertices and edges with adjacent faces in the same mesh. Sharing vertices and edges helps reduce the amount of memory used by a mesh. It also ensures that when a face is moved, all the connected faces move together.
Sometimes you may want to separate a face from its connected faces so that it may be moved in isolation. There are three ways to accomplish this depending upon which parts of the face you want to extract:
polySplitVertex split one or more vertices so that each face that shared the vertex acquires its own copy of the vertex
polySplitEdge split one or more edges so that each face that shared the vertex acquires its own copy of the edge
polyChipOff completely extract the face so that it has its own vertices and edges

Notice that the area of affect of each operation is different. polySplitVertex will affect all the edges and faces that shared the vertex. This is the broadest effect. polySplitEdge will only affect the faces which shared the edge and polyChipOff will affect a specific face. If we just count vertices to measure the effect of each command when splitting all components of a face, starting from a 3x3 plane which has 16 vertices and we were to split the middle face:
polySplitVertex applied to the four vertices would end up creating 12 new vertices
polySplitEdge applied to the four edges would end up creating 4 new vertices
polyChipOff applied to the middle face would end up creating 4 new vertices

Note that polySplitVertex may create non-manifold geometry as a part of this operation. You can use Polygons->Cleanup afterwards to to clean up any non-manifold geometry.

    """
    pass
    


def polyStraightenUVBorder(uvSetName="string", preserveLength=float, blendOriginal=float, curvature=float, nodeState=int, constructionHistory=bool, gapTolerance=int, caching=bool, name="string"):
    """
    polyStraightenUVBorder is undoable, queryable, and editable.
    

    
Move border UVs along a simple curve.

    """
    pass
    


def polySubdivideEdge(size="string", divisions=int, worldSpace=bool, nodeState=int, name="string", caching=bool, constructionHistory=bool):
    """
    polySubdivideEdge is undoable, queryable, and editable.
    

    
Subdivides an edge into two or more subedges.

Default : divide edge into two edges of equal length.

    """
    pass
    


def polySubdivideFacet(mode=int, divisions=int, nodeState=int, name="string", caching=bool, constructionHistory=bool):
    """
    polySubdivideFacet is undoable, queryable, and editable.
    

    
Subdivides a face into quads or triangles.

In quad mode, a center point is introduced at the center of each face and midpoints are inserted on all the edges of each face. New faces (all quadrilaterals) are built by adding edges from the midpoints towards the center.
In triangle mode, only the center point is created; new faces (all triangles) are created by connecting the center point to all the existing vertices of the face.
Default : one subdivision step in quad mode (polySubdFacet -dv 1 -m 0;)

    """
    pass
    


def polyTorus(axis="string", texture=bool, radius="string", createUVs=bool, twist=int, constructionHistory=bool, subdivisionsY=int, subdivisionsX=int, sectionRadius="string", name="string"):
    """
    polyTorus is undoable, queryable, and editable.
    

    
The torus command creates a new polygonal torus.

    """
    pass
    


def polyToSubdiv(poly, applyMatrixToResult=bool, uvPointsU=float, quickConvert=bool, preserveVertexOrdering=bool, absolutePosition=bool, maxEdgesPerVert=int, maxPolyCount=int, object=bool, uvPointsV=float, nodeState=int, uvTreatment=int, name="string", uvPoints=float, caching=bool, constructionHistory=bool):
    """
    polyToSubdiv is undoable, queryable, and editable.
    

    
This command converts a polygon and produces a subd surface. The name of the new subdivision surface is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def polyTransfer(vertices=bool, alternateObject="string", nodeState=int, vertexColor=bool, name="string", uvSets=bool, caching=bool, constructionHistory=bool):
    """
    polyTransfer is undoable, queryable, and editable.
    

    
Transfer information from one polygonal object to another one. Both objects must have identical topology, that is same vertex, edge, and face numbering. The flags specify which of the vertices, UV sets or vertex colors will be copied.

    """
    pass
    


def polyTriangulate(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyTriangulate is undoable, queryable, and editable.
    

    
Triangulation breaks polygons down into triangles, ensuring that all faces are planar and non-holed. Triangulation of models can be beneficial in many areas.

    """
    pass
    


def polyUnite(polypolypoly, mergeUVSets=int, nodeState=int, constructionHistory=bool, caching=bool, name="string"):
    """
    polyUnite is undoable, queryable, and editable.
    

    
This command creates a new poly as an union of a list of polys If no objects are specified in the command line, then the objects from the active list are used.

    """
    pass
    


def polyUniteSkinned(objectPivot=bool, centerPivot=bool, mergeUVSets=int, constructionHistory=bool):
    """
    polyUniteSkinned is undoable, queryable, and editable.
    

    
Command to combine poly mesh objects (as polyUnite) while retaining the smooth skinning setup on the combined object.

    """
    pass
    


def polyUVRectangle(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    polyUVRectangle is undoable, queryable, and editable.
    

    
Given two vertices, does one of the following: 1) If the vertices define opposite corners of a rectangular area of quads, assigns a grid of UVs spanning the 0-1 area to that rectangle. 2) If the vertices define an edge in a rectangular and topologically cylindrical area of quads, assigns UVs spanning the 0-1 area to that cylindrical patch, using the defined edge as the U=0 edge.

    """
    pass
    


def polyUVSet(delete=bool, allUVSetsIndices=bool, allUVSets=bool, currentLastUVSet=bool, shareInstances=bool, unshared=bool, projections=bool, currentUVSet=bool, newUVSet="string", allUVSetsWithCount=bool, perInstance=bool, copy=bool, uvSet="string", rename=bool, create=bool, currentPerInstanceUVSet=bool):
    """
    polyUVSet is undoable, queryable, and editable.
    

    
Command to do the following to uv sets: - delete an existing uv set. - rename an existing uv set. - create a new empty uv set. - copy the values from one uv set to a another pre-existing uv set. - set the current uv set to a pre-existing uv set. - modify sharing between instances of per-instance uv sets - query the current uv set. - set the current uv set to the last uv set added to an object. - query the names of all uv sets.

    """
    pass
    


def polyWedgeFace(axis=float, wedgeAngle=int, divisions=int, worldSpace=bool, nodeState=int, name="string", center=float, edge=int, caching=bool, constructionHistory=bool):
    """
    polyWedgeFace is undoable, queryable, and editable.
    

    
Extrude faces about an axis. The axis is the average of all the selected edges. If the edges are not aligned, the wedge may not look intuitive. To separately wedge faces about different wedge axes, the command should be issued as many times as the wedge axes. (as in the second example)

    """
    pass
    


def popupMenu(markingMenu=bool, postMenuCommand="string", button=int, defineTemplate="string", parent="string", ctrlModifier=bool, shiftModifier=bool, numberOfItems=bool, useTemplate="string", altModifier=bool, itemArray=bool, allowOptionBoxes=bool, exists=bool, postMenuCommandOnce=bool, deleteAllItems=bool):
    """
    popupMenu is undoable, queryable, and editable.
    

    
This command creates a popup menu and attaches it to the current control if no parent is specified. The popup menu is posted with the right mouse button by default.
Popup menus can be added to any kind of control, however, on some widgets, only the standard menu button (3rd mouse button) can be used to trigger popup menus. This is to meet generally accepted UI guidelines that assign the 3rd mouse button and only this one to popup menus, and also to prevent unexpected behavior of controls like text fields, that expect 1st and 2nd button to be reserved for contextual operations like text or item selection...

    """
    pass
    


def pose(apply=bool, name="string", allPoses=bool):
    """
    pose is undoable, queryable, and editable.
    

    
This command is used to create character poses.

    """
    pass
    


def poseEditor(panel="string", docTag="string", control=bool, mainListConnection="string", defineTemplate="string", parent="string", highlightConnection="string", useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", unParent=bool, stateString=bool, exists=bool, updateMainConnection=bool, forceMainConnection="string", unlockMainConnection=bool):
    """
    poseEditor is undoable, queryable, and editable.
    

    
This command creates an editor that derives from the base editor class that has controls for deformer and control nodes.

    """
    pass
    


def posePanel(tearOff=bool, docTag="string", isUnique=bool, control=bool, tearOffRestore=bool, defineTemplate="string", parent="string", createString=bool, unParent=bool, needsInit=bool, useTemplate="string", init=bool, label="string", replacePanel="string", popupMenuProcedure="string", editString=bool, copy="string", exists=bool, menuBarVisible=bool, tearOffCopy="string", poseEditor=bool):
    """
    posePanel is undoable, queryable, and editable.
    

    
This command creates a panel that derives from the base panel class that houses a poseEditor.

    """
    pass
    


def preferredRenderer(string, makeCurrent=bool, fallback="string"):
    """
    preferredRenderer is NOT undoable, queryable, and NOT editable.
    

    
Command to set the preferred renderer. This command can be used to query the preferred renderer and to set the current renderer as the preferred one. It also allows users to specify a preferred fallback renderer.

    """
    pass
    


def preloadRefEd(panel="string", docTag="string", control=bool, mainListConnection="string", defineTemplate="string", parent="string", updateMainConnection=bool, highlightConnection="string", useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", unParent=bool, stateString=bool, exists=bool, selectFileNode=bool, forceMainConnection="string", unlockMainConnection=bool):
    """
    preloadRefEd is undoable, queryable, and editable.
    

    
This creates an editor for managing which references will be read in (loaded) and which deferred (unloaded) upon opening a file.

    """
    pass
    


def prepareRender(settingsUI="string", preRenderFrame="string", postRenderLayer="string", deregister="string", label="string", saveAssemblyConfig=bool, invokePreRenderLayer=bool, postRender="string", traversalSet="string", restore=bool, defaultTraversalSet="string", traversalSetInit="string", preRender="string", listTraversalSets=bool, preRenderLayer="string", invokePostRenderFrame=bool, invokePostRender=bool, invokeSettingsUI=bool, invokePostRenderLayer=bool, invokePreRender=bool, postRenderFrame="string", setup=bool, invokePreRenderFrame=bool):
    """
    prepareRender is undoable, queryable, and editable.
    

    
This command is used to register, manage and invoke render traversals. Render traversals are used to configure a scene to prepare it for rendering.
This command has special support for scene assembly nodes. To render scene assembly nodes, a rendering traversal can activate an appropriate representation, for each assembly node in the scene. When rendering is done, this command can correspondingly restore the representation that was active before rendering on each assembly. Render traversals are grouped into traversal sets. A render traversal set includes callbacks, or render traversals, for one or more of the following steps of rendering, ordered by decreasing level of granularity. A render traversal callback is an arbitrary script, either MEL or Python, that can transform the Maya scene for rendering purposes.
preRender
Traversal run once per render, before any rendering is performed.
postRender
Traversal run once per render, after all rendering has been performed.
preRenderLayer
Traversal run before rendering each render layer.
postRenderLayer
Traversal run after rendering each render layer.
preRenderFrame
Traversal run before rendering each frame.
postRenderFrame
Traversal run after rendering each frame.
During a render view or batch render, Maya will run the render traversals from the same traversal set, the default traversal set. Traversal sets are named, so multiple traversal sets can be registered with this command, and the default render traversal set can be switched to any one of these registered traversal sets. When changing the default traversal set, the different render traversal callbacks (preRender, preRenderLayer, preRenderFrame, postRender, postRenderLayer, postRenderFrame) are switched as a unit.
At render time, the software rendering code invokes the callbacks of the default traversal set. The prepareRender scripting capability allows for the development of multiple rendering preparation scripts, including from plugins, to provide extensibility rather than being constrained to a single implementation.
A special traversal set is the "null" traversal set. It is the initial default traversal set, and cannot be deregistered. It performs no work, and does not save and restore the assembly node active representation configuration. It will provide WYSIWYG (What You See Is What You Get) rendering of assembly nodes, without switching to a different representation to render.
Render traversals are invoked by Maya using this command's create mode. This is done by Maya's rendering infrastructure, and should not be required unless developing new render views or batch render code. Most uses of this command will simply use the edit mode to register render traversals into a render traversal set, or the query mode to query the names of the render traversals in a render traversal set.
Render Traversals versus Render MEL Scripts
Render traversals are similar in intent to the user-specified pre- and post-render, pre- and post-render layer, pre- and post-render frame MEL script capability. The difference with the user MEL scripts is that prepareRender is in addition to, and does not replace, the user MEL scripts, can register multiple render traversal sets and switch them, and supports both MEL and Python. The MEL render scripts are run inside the scope of the render traversals, that is, the preRender traversal is run before the pre-render MEL script and the postRender traversal is run after the post-render MEL script, the preRenderLayer traversal is run before the pre-render layer MEL script and the postRenderLayer traversal is run after the post-render layer MEL script, and finally the preRenderFrame traversal is run before the pre-render frame MEL script and the postRenderFrame traversal is run after the post-render frame MEL script.
Saving and Restoring State
The prepareRender command has support for saving and restoring the active representation of assembly nodes in the scene. Use the saveAssemblyConfig flag to indicate that the render traversal set requires saving the assembly node active representation before rendering begins, and should restore the assembly node active representation after rendering ends.
It is the responsibility of render traversals that modify the scene in ways other than changing the active representation on assembly nodes to restore the scene to its previous state, most likely using the postRender, postRenderLayer, and postRenderFrame traversals.
Note that Maya does not call the prepareRender -restore command on batch render completion, since batch rendering is done on a copy of the scene which is discarded once rendering terminates. Implementors of render traversals may wish to check whether they are running in batch mode, to implement the same optimization.

    """
    pass
    


def profiler(procedureName="string", eventColor=bool, instrumentMel=bool, eventCount=bool, removeCategory="string", categoryRecording=bool, colorIndex=int, load="string", output="string", eventStartTime=bool, addCategory="string", eventName=bool, eventThreadId=bool, eventDuration=bool, eventCPUId=bool, procedureDescription="string", signalEvent=bool, sampling=bool, categoryNameToIndex="string", bufferSize=int, signalMelEvent=bool, eventDescription=bool, clearAllMelInstrumentation=bool, allCategories=bool, categoryIndex=int, eventCategory=bool, reset=bool, categoryIndexToName=int, categoryName="string", eventIndex=int):
    """
    profiler is NOT undoable, queryable, and NOT editable.
    

    
The profiler is used to record timing information from key events within Maya, as an aid in tuning the performance of scenes, scripts and plug-ins. User written plug-ins and Python scripts can also generate profiling information for their own code through the MProfilingScope and MProfiler classes in the API.
This command provides the ability to control the collection of profiling data and to query information about the recorded events. The recorded information can also be viewed graphically in the Profiler window.
The buffer size cannot be changed while sampling is active, it will return an error The reset flag cannot be called while sampling is active, it will return an error. Any changes to the buffer size will only be applied on start of the next recording. You can't save and load in the same command, save has priority, load would be ignored.

    """
    pass
    


def profilerTool(frameAll=bool, findPrevious=bool, threadView=bool, unisolateSegment=bool, make=bool, isolateSegment=int, showAllEvent=bool, matchWholeWord=bool, showSelectedEvents=bool, categoryView=bool, searchEvent="string", destroy=bool, showSelectedEventsRepetition=bool, segmentCount=bool, exists=bool, frameSelected=bool, findNext=bool, cpuView=bool):
    """
    profilerTool is NOT undoable, queryable, and editable.
    

    
This script is intended to be used by the profilerPanel to interact with the profiler tool's view (draw region). It can be used to control some behaviors about the profiler Tool.

    """
    pass
    


def progressBar(string, docTag="string", height=int, defineTemplate="string", parent="string", step=int, numberOfPopupMenus=bool, useTemplate="string", progress=int, highlightColor=float, status="string", isMainProgressBar=bool, isCancelled=bool, endProgress=bool, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, width=int, minValue=int, exists=bool, maxValue=int, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", dragCallback="string", isInterruptable=bool, noBackground=bool, backgroundColor=float, manage=bool, beginProgress=bool, isObscured=bool):
    """
    progressBar is undoable, queryable, and editable.
    

    
Creates a progress bar control that graphically fills in as its progress value increases.

    """
    pass
    


def progressWindow(maxValue=int, isInterruptable=bool, step=int, progress=int, minValue=int, status="string", title="string", isCancelled=bool, endProgress=bool):
    """
    progressWindow is undoable, queryable, and editable.
    

    
The progressWindow command creates a window containing a status message, a graphical progress gauge, and optionally a "Hit ESC to Cancel" label for interruptable operations.
Only one progress window is allowed on screen at a time. While the window is visible, the busy cursor is shown.

    """
    pass
    


def projectCurve(curvesurface, useNormal=bool, direction="string", object=bool, name="string", nodeState=int, directionY="string", range=bool, directionX="string", directionZ="string", caching=bool, tolerance="string", constructionHistory=bool):
    """
    projectCurve is undoable, queryable, and editable.
    

    
The projectCurve command creates curves on surface where all selected curves project onto the selected surfaces. Projection can be done using the surface normals or the user can specify the vector to project along. Note: the user does not have to specify the curves and surfaces in any particular order in the command line.

    """
    pass
    


def projectionContext(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    projectionContext is undoable, queryable, and editable.
    

    
Set the context for projection manips

    """
    pass
    


def projectionManip(switchType=bool, fitBBox=bool, projType=int):
    """
    projectionManip is undoable, queryable, and NOT editable.
    

    
Various commands to set the manipulator to interesting positions.

    """
    pass
    


def projectTangent(curvecurvecurve ,surface, curvature=bool, rotate=int, ignoreEdges=bool, object=bool, curvatureScale="string", reverseTangent=bool, tangentScale="string", nodeState=int, replaceOriginal=bool, name="string", tangentDirection=int, caching=bool, constructionHistory=bool):
    """
    projectTangent is undoable, queryable, and editable.
    

    
The project tangent command is used to align (for tangents) a curve to two other curves or a surface. A surface isoparm may be selected to define the direction (U or V) to align to. The end of the curve must intersect with these other objects. Curvature continuity may also be applied if required.
Tangent continuity means the end of the curve is modified to be tangent at the point it meets the other objects.
Curvature continuity means the end of the curve is modified to be curvature continuous as well as tangent.
If the normal tangent direction is used, the curvature continuity and rotation do not apply. Also, curvature continuity is only available if align to a surface (not with 2 curves).

    """
    pass
    


def promptDialog(messageAlign="string", backgroundColor=float, defaultButton="string", text="string", message="string", style="string", button="string", cancelButton="string", title="string", dismissString="string", parent="string", scrollableField=bool):
    """
    promptDialog is undoable, queryable, and NOT editable.
    

    
The promptDialog command creates a modal dialog with a message to the user, a text field in which the user may enter a response, and a variable number of buttons to dismiss the dialog. The dialog is dismissed when the user presses any button or chooses the close item from the window menu. In the case where a button is pressed then the name of the button selected is returned. If the dialog is dismissed via the close item then the string returned is specified by the -ds/dismissString flag.
The default behaviour when no arguments are specified is to create an empty single button dialog.
To obtain the text entered by the user simply query the -tx/text flag.

    """
    pass
    


def propModCtx(animCurveFalloff=float, image1="string", nurbsCurve="string", scriptParam="string", powerCutoff=float, exists=bool, worldspace=bool, type=int, linearParam=float, image2="string", linear=float, powerDegree=float, powerCutoffParam=float, powerDegreeParam=float, animCurveParam="string", script="string", direction=float, animCurve="string", image3="string"):
    """
    propModCtx is undoable, queryable, and editable.
    

    
Controls the proportional move context.

    """
    pass
    


def propMove(objects, rotate=int, percentZ=float, pivot=float, scale=float, percentY=float, translate="string", percentX=float, percent=float):
    """
    propMove is undoable, NOT queryable, and NOT editable.
    

    
Performs a proportional translate, scale or rotate operation on any number of objects. The percentages to rotate, scale or translate by can be specified using either the -p flags or -px, -py, -pz flags. Each selected object must have a corresponding -p or -px, -py, -pz flag. The rotate, scale or translate performed is relative.

    """
    pass
    


def psdChannelOutliner(docTag="string", height=int, allItems=bool, defineTemplate="string", parent="string", numberOfItems=bool, numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", preventOverride=bool, addChild="string", enableBackground=bool, exists=bool, enable=bool, doubleClickCommand="string", selectItem=bool, visibleChangeCommand="string", visible=bool, psdParent="string", fullPathName=bool, removeChild="string", dropCallback="string", dragCallback="string", selectCommand="string", noBackground=bool, removeAll=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    psdChannelOutliner is undoable, queryable, and editable.
    

    
Create a psdChannelOutliner control which is capable of displaying a tree structure upto one level.

    """
    pass
    


def psdEditTextureFile(addChannelImage="string", deleteChannel="string", psdFileName="string", uvSnapPostionTop=bool, addChannel="string", addChannelColor="string", snapShotImage="string"):
    """
    psdEditTextureFile is undoable, NOT queryable, and NOT editable.
    

    
Edits the existing PSD file. Addition and deletion of the channels (layer sets) are supported.

    """
    pass
    


def psdExport(preMultiplyAlpha=bool, layerSetName="string", bytesPerChannel=int, emptyLayerSet=bool, outFileName="string", layerName="string", psdFileName="string", format="string", alphaChannelIdx=int):
    """
    psdExport is NOT undoable, queryable, and NOT editable.
    

    
Writes the Photoshop file layer set into different formats. The output file depth (bit per channel ) can be different from that of the input. If the input is 16 bpc and output is 8 bpc, there will be data loss.

    """
    pass
    


def psdTextureFile(yResolution=int, channels="string", imageFileName="string", snapShotImageName="string", channelRGB="string", xResolution=int, psdFileName="string", uvSnapPostionTop=bool):
    """
    psdTextureFile is undoable, NOT queryable, and NOT editable.
    

    
Creates a Photoshop file with UVSnap shot image and the layer set names as the input.

    """
    pass
    


def querySubdiv(action=int, relative=bool, level=int):
    """
    querySubdiv is undoable, NOT queryable, and NOT editable.
    

    
Queries a subdivision surface based on a set of query parameters and updates the selection list with the results.

    """
    pass
    


def quit(force=bool, abort=bool, exitCode=int):
    """
    quit is undoable, NOT queryable, and NOT editable.
    

    
This command is used to exit the application.

    """
    pass
    


def radial(magnitude=float, position="string", perVertex=bool, type=float, attenuation=float, maxDistance="string", name="string"):
    """
    radial is undoable, queryable, and editable.
    

    
A radial field pushes objects directly towards or directly away from it, like a magnet.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def radioButton(string, docTag="string", height=int, onCommand="string", defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", select=bool, highlightColor=float, annotation="string", enable=bool, offCommand="string", preventOverride=bool, popupMenuArray=bool, enableBackground=bool, data=int, exists=bool, changeCommand="string", collection="string", recomputeSize=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, align="string", manage=bool, editable=bool, isObscured=bool):
    """
    radioButton is undoable, queryable, and editable.
    

    
This command creates a radio button that is added to the most recently created radio collection if the -cl/collection flag is not used.

    """
    pass
    


def radioButtonGrp(groupName, docTag="string", height=int, onCommand="string", labelAnnotation="string", useTemplate="string", data4=int, popupMenuArray=bool, rowAttach=int, annotation2="string", changeCommand3="string", numberOfRadioButtons=int, changeCommand4="string", visibleChangeCommand="string", columnAttach3="string", columnWidth1=int, select=int, dropCallback="string", noBackground=bool, offCommand1="string", vertical=bool, defineTemplate="string", parent="string", label="string", highlightColor=float, shareCollection="string", columnAlign4="string", onCommand2="string", columnAttach4="string", changeCommand2="string", columnOffset5=int, visible=bool, columnWidth2=int, columnAlign3="string", adjustableColumn3=int, backgroundColor=float, columnWidth5=int, label3="string", data1=int, enable1=bool, onCommand3="string", columnOffset6=int, offCommand4="string", dragCallback="string", columnAlign5="string", offCommand="string", columnWidth4=int, data3=int, adjustableColumn5=int, columnWidth6=int, columnOffset3=int, annotation1="string", label4="string", changeCommand1="string", adjustableColumn2=int, enable=bool, adjustableColumn6=int, columnWidth3=int, preventOverride=bool, annotation3="string", offCommand2="string", enable4=bool, onCommand4="string", annotation4="string", isObscured=bool, enable3=bool, numberOfPopupMenus=bool, width=int, labelArray3="string", offCommand3="string", columnOffset2=int, annotation="string", changeCommand="string", adjustableColumn4=int, exists=bool, onCommand1="string", columnAlign=int, enableBackground=bool, label1="string", adjustableColumn=int, columnAlign2="string", columnAlign6="string", labelArray4="string", fullPathName=bool, enable2=bool, labelArray2="string", columnAttach=int, columnAttach5="string", data2=int, columnWidth=int, manage=bool, editable=bool, columnOffset4=int, label2="string", columnAttach2="string", columnAttach6="string"):
    """
    radioButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates from one to four radio buttons in a single row. By default the radio buttons will share a single collection, but they can also share the collection of another radio button group. The buttons can also have an optional text label.

    """
    pass
    


def radioCollection(string, numberOfCollectionItems=bool, defineTemplate="string", parent="string", gl=bool, select="string", collectionItemArray=bool, exists=bool, useTemplate="string"):
    """
    radioCollection is undoable, queryable, and editable.
    

    
This command creates a radio button collection. Collections are parented to the current default layout if no parent is specified with the -p/parent flag. As children of the layout they will be deleted when the layout is deleted. Collections may also span more than one window if the -gl/global flag is used. In this case the collection has no parent and must be explicitly deleted with the deleteUI command when it is no longer wanted.

    """
    pass
    


def radioMenuItemCollection(string, defineTemplate="string", parent="string", useTemplate="string", gl=bool, exists=bool):
    """
    radioMenuItemCollection is undoable, queryable, and editable.
    

    
This command creates a radioMenuItemCollection. Attach radio menu items to radio menu item collection objects to get radio button behaviour. Radio menu item collections will be parented to the current menu if no parent is specified with the -p/parent flag. As children of the menu they will be deleted when the menu is deleted. Collections may also span more than one menu if the -g/global flag is used. In this case the collection has no parent menu and must be explicitly deleted with the deleteUI command when it is no longer wanted.

    """
    pass
    


def rampColorPort(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, fullPathName=bool, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", selectedColorControl="string", exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, selectedInterpControl="string", selectedPositionControl="string", node="string", preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, verticalLayout=bool, isObscured=bool):
    """
    rampColorPort is undoable, queryable, and editable.
    

    
This command creates a control that displays an image representing the ramp node specified, and supports editing of that node.

    """
    pass
    


def rangeControl(docTag="string", changedCommand="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", widthHeight=int, minRange=(), exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, maxRange=(), fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    rangeControl is undoable, queryable, and editable.
    

    
This command creates a control used for displaying and modifying the current playback range. Note: only one master rangeControl may exist. Any addition rangeControls that a user creates are slaved to the master range control widget.

    """
    pass
    


def readTake(frequency=float, noTime=bool, take="string", device="string", angle="string", linear="string"):
    """
    readTake is undoable, NOT queryable, and NOT editable.
    

    
This action reads a take (.mov) file to a defined device.
See also: writeTake, applyTake

    """
    pass
    


def rebuildCurve(curvecurve, smartSurfaceCurveRebuild=bool, degree=int, keepRange=int, rebuildType=int, keepControlPoints=bool, endKnots=int, spans=int, fitRebuild=bool, object=bool, keepTangents=bool, nodeState=int, range=bool, replaceOriginal=bool, name="string", keepEndPoints=bool, caching=bool, tolerance="string", constructionHistory=bool):
    """
    rebuildCurve is undoable, queryable, and editable.
    

    
This command rebuilds a curve by modifying its parameterization. In some cases the shape may also change. The rebuildType (-rt) determines how the curve is to be rebuilt.
The optional second curve can be used to specify a reference parameterization.

    """
    pass
    


def rebuildSurface(surfacesurface, keepRange=int, spansU=int, rebuildType=int, keepControlPoints=bool, endKnots=int, nodeState=int, object=bool, fitRebuild=int, spansV=int, direction=int, replaceOriginal=bool, name="string", degreeU=int, degreeV=int, keepCorners=bool, caching=bool, tolerance="string", constructionHistory=bool, polygon=int):
    """
    rebuildSurface is undoable, queryable, and editable.
    

    
This command rebuilds a surface by modifying its parameterization. In some cases the shape of the surface may also change. The rebuildType (-rt) attribute determines how the surface is rebuilt.
The optional second surface can be used to specify a reference parameterization.

    """
    pass
    


def recordAttr(delete=bool, attribute="string"):
    """
    recordAttr is undoable, queryable, and NOT editable.
    

    
This command sets up an attribute to be recorded. When the record command is executed, any changes to this attribute are recorded. When recording stops these changes are turned into keyframes.
If no attributes are specified all attributes of the node are recorded.
When the query flag is used, a list of the attributes being recorded will be returned.

    """
    pass
    


def recordDevice(cleanup=bool, playback=bool, wait=bool, data=bool, state=bool, duration=int, device="string"):
    """
    recordDevice is undoable, queryable, and NOT editable.
    

    
Starts and stops server side device recording. The data is recorded at the device rate. Once recorded, the data may be brought into Maya with the applyTake command.
See also: enableDevice, applyTake, readTake, writeTake

    """
    pass
    


def redo():
    """
    redo is undoable, NOT queryable, and NOT editable.
    

    
Takes the most recently undone command from the undo list and redoes it.

    """
    pass
    


def referenceEdit(removeEdits=bool, editCommand="string", successfulEdits=bool, changeEditTarget="string", applyFailedEdits=bool, failedEdits=bool, onReferenceNode="string"):
    """
    referenceEdit is NOT undoable, NOT queryable, and NOT editable.
    

    
Use this command to remove and change the modifications which have been applied to references. A valid commandTarget is either a reference node, a reference file, a node in a reference, or a plug from a reference. Only modifications that have been made from the currently open scene can be changed or removed. The 'referenceQuery -topReference' command can be used to determine what modifications have been made to a given commandTarget. Additionally only unapplied edits will be affected. Edits are unapplied when the node(s) which they affect are unloaded, or when they could not be successfully applied. By default this command only works on failed edits (this can be adjusted using the "-failedEdits" and "-successfulEdits" flags). Specifying a reference node as the command target is equivalent to specifying every node in the target reference file as a target. In this situation the results may differ depending on whether the target reference is loaded or unloaded. When it is unloaded, edits that affect both a node in the target reference and a node in one of its descendant references may be missed (e.g. those edits may not be removed). This is because when a reference is unloaded Maya no longer retains detailed information about which nodes belong to it. However, edits that only affect nodes in the target reference or in one of its ancestral references should be removed as expected. When the flags -removeEdits and -editCommand are used together, by default all connectAttr edits are removed from the specified source object. To remove only edits that connect to a specific target object, the target object can be passed as an additional argument to the command. This narrows the match criteria, so that only edits that connect the source object to the provided target in this additional argument are removed. See the example below. NOTE: When specifying a plug it is important to use the appropriate long attribute name.

    """
    pass
    


def referenceQuery(editCommand="string", editNodes=bool, isExportEdits=bool, referenceNode=bool, failedEdits=bool, dagPath=bool, namespace=bool, shortName=bool, isPreviewOnly=bool, successfulEdits=bool, child=bool, editAttrs=bool, onReferenceNode="string", unresolvedName=bool, isLoaded=bool, showDagPath=bool, editStrings=bool, parentNamespace=bool, withoutCopyNumber=bool, nodes=bool, topReference=bool, filename=bool, isNodeReferenced=bool, liveEdits=bool, parent=bool, showNamespace=bool):
    """
    referenceQuery is NOT undoable, NOT queryable, and NOT editable.
    

    
Use this command to find out information about references and referenced nodes. A valid target is either a reference node, a reference file, or a referenced node. Some flags don't require a target, see flag descriptions for more information on what effect this has. When a scene contains multiple levels of file references, those edits which affect a nested reference may be stored on several different reference nodes. For example: A.ma has a reference to B.ma which has a reference to C.ma which contains a poly sphere (pSphere1). If you were to open B.ma and translate the sphere, an edit would be stored on CRN which refers to a node named "C:pSphere1". If you were then to open A.ma and parent the sphere, an edit would be stored on BRN which refers to a node named "B:C:pSphere1". It is important to note that when querying edits which affect a nested reference, the edits will be returned in the same format that they were applied. In the above example, opening A.ma and querying all edits which affect C.ma, would return two edits a parent edit affecting "B:C:pSphere1", and a setAttr edit affecting "C:pSphere1". Since there is currently no node named C:pSphere1 (only B:C:pSphere1) care will have to be taken when interpreting the returned information. The same care should be taken when referenced DAG nodes have been parented or instanced. Continuing with the previous example, let's say that you were to open A.ma and, instead of simply parenting pSphere1, you were to instance it. While A.ma is open, "B:C:pSphere1" may now be an amibiguous name, replaced by "|B:C:pSphere1" and "group1|B:C:pSphere1". However querying the edits which affect C.ma would still return a setAttr edit affecting "C:pSphere1" since it was applied prior to B:C:pSphere1 being instanced. Some tips: 1. Use the '-topReference' flag to query only those edits which were applied from the currently open file. 2. Use the '-onReferenceNode' flag to limit the results to those edits where are stored on a given reference node. You can then use various string manipulation techniques to extrapolate the current name of any affected nodes.

    """
    pass
    


def refineSubdivSelectionList():
    """
    refineSubdivSelectionList is undoable, NOT queryable, and NOT editable.
    

    
Refines a subdivision surface set of components based on the selection list. The selected components are subdivided. The selection list after the command is the newly created components at the finer subdivision level.

    """
    pass
    


def refresh(force=bool, currentView=bool, suspend=bool):
    """
    refresh is undoable, NOT queryable, and NOT editable.
    

    
This command is used to force a redraw during script execution. Normally, redraw is suspended while scripts are executing but sometimes it is useful to show intermediate results for purposes such as capturing images from the screen.
If the -cv flag is specified, then only the current active view is redrawn.

    """
    pass
    


def refreshEditorTemplates():
    """
    refreshEditorTemplates is undoable, NOT queryable, and NOT editable.
    

    
This command refreshes all cached attribute editor templates, including those copied from the standard AE. These are the templates constructed internally on a per node type basis. This is useful if attribute elements have changed and the templates need to be re-evaluated accordingly.

    """
    pass
    


def regionSelectKeyCtx(image1="string", leftManip=float, topManip=float, bottomManip=float, history=bool, rightManip=float, exists=bool, image2="string", name="string", image3="string"):
    """
    regionSelectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the graph editor using the region select tool.

    """
    pass
    


def relationship(b=bool, relationshipData="string"):
    """
    relationship is undoable, queryable, and editable.
    

    
This is primarily for use with file IO. Rather than write out the specific attributes/connections required to maintain a relationship, a description of the related nodes/plugs is written instead. The relationship must have an owner node, and have a specific type. During file read, maya will make the connections and/or set the data necessary to represent the realtionship in the dependency graph.

    """
    pass
    


def reloadImage():
    """
    reloadImage is undoable, NOT queryable, and NOT editable.
    

    
This command reloads an xpm image from disk. This can be used when the file has changed on disk and needs to be reloaded.
The first string argument is the file name of the .xpm file. The second string argument is the name of a control using the specified pixmap.

    """
    pass
    


def removeJoint(object):
    """
    removeJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will remove the selected joint or the joint given at the command line from the skeleton.
The given (or selected) joint should not be the root joint of the skeleton, and not have skin attached. The command works on the given (or selected) joint. No options or flags are necessary.

    """
    pass
    


def removeMultiInstance(b=bool):
    """
    removeMultiInstance is undoable, NOT queryable, and NOT editable.
    

    
Removes a particular instance of a multiElement. This is only useful for input attributes since outputs will get regenerated the next time the node gets executed. This command will remove the instance and optionally break all incoming and outgoing connections to that instance. If the connections are not broken (with the -b true) flag, then the command will fail if connections exist.

    """
    pass
    


def rename(objectstring, uuid=bool, ignoreShape=bool):
    """
    rename is undoable, NOT queryable, and NOT editable.
    

    
Renames the given object to have the new name. If only one argument is supplied the command will rename the (first) selected object. If the new name conflicts with an existing name, the object will be given a unique name based on the supplied name. It is not legal to rename an object to the empty string.
When a transform is renamed then any shape nodes beneath the transform that have the same prefix as the old transform name are renamed. For example, "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to "ball|ballShape".
If the new name ends in a single '#' then the rename command will replace the trailing '#' with a number that ensures the new name is unique.
Notes
If the name has an absolute namespace part, it will be considered. Namespaces that do not exist will be created automatically as needed. If the name has a relative namespace part, it will be ignored. In that case, the object will be put under the current namespace. (see example below).

    """
    pass
    


def renameAttr():
    """
    renameAttr is undoable, NOT queryable, and NOT editable.
    

    
Renames the given user-defined attribute to the name given in the string argument. If the new name conflicts with an existing name then this command will fail. Note that it is not legal to rename an attribute to the empty string.

    """
    pass
    


def renameUI():
    """
    renameUI is undoable, NOT queryable, and NOT editable.
    

    
This command renames the UI object passed as first arument to the new name specified as second argument. If the new name is a duplicate, or not valid, then re-naming fails and the old name is returned.
Notes
This command does not update other objects or commands that reference this object by name, so use this command at your own risk.

    """
    pass
    


def render(camera, batch=bool, replace=bool, nshadows=bool, yresolution=int, nglowpass=bool, layer="string", abortMissingTexture=bool, xresolution=int, keepPreImage=bool):
    """
    render is NOT undoable, NOT queryable, and NOT editable.
    

    
The render command is used to start off a MayaSoftware rendering session of the currently active camera. If a rendering is already in progress, then this command stops the rendering. This command is not undoable.

    """
    pass
    


def renderer(string, changeIprRegionProcedure="string", showBatchRenderLogProcedure="string", iprOptionsProcedure="string", globalsTabCreateProcNames=bool, unregisterRenderer=bool, polyPrelightProcedure="string", batchRenderProcedure="string", renderDiagnosticsProcedure="string", globalsTabLabels=bool, renderProcedure="string", renderSequenceProcedure="string", rendererUIName="string", globalsTabUpdateProcNames=bool, globalsNodes=bool, showBatchRenderProcedure="string", pauseIprRenderProcedure="string", addGlobalsTab="string", logoImageName="string", batchRenderOptionsProcedure="string", materialViewRendererSuspend=bool, addGlobalsNode="string", cancelBatchRenderProcedure="string", exists=bool, stopIprRenderProcedure="string", startIprRenderProcedure="string", iprOptionsSubMenuProcedure="string", textureBakingProcedure="string", isRunningIprProcedure="string", commandRenderProcedure="string", iprOptionsMenuLabel="string", refreshIprRenderProcedure="string", batchRenderOptionsStringProcedure="string", renderingEditorsSubMenuProcedure="string", renderGlobalsProcedure="string", showRenderLogProcedure="string", namesOfAvailableRenderers=bool, renderOptionsProcedure="string", iprRenderProcedure="string", logoCallbackProcedure="string", materialViewRendererList=bool, renderMenuProcedure="string", materialViewRendererPause=bool, renderRegionProcedure="string", iprRenderSubMenuProcedure="string"):
    """
    renderer is NOT undoable, queryable, and editable.
    

    
Command to register renders. This command allows you to specify the UI name and procedure names for renderers. The command also allow you to query the UI name and the procedure names for the registered renders.

    """
    pass
    


def renderGlobalsNode(renderResolution="string", renderQuality="string"):
    """
    renderGlobalsNode is undoable, NOT queryable, and NOT editable.
    

    
The renderGlobalsNode creates a render globals node and registers it with the model. The createNode command will not register nodes of this type correctly.

    """
    pass
    


def renderInfo(chordHeight=float, useMinScreen=bool, vtype=int, doubleSided=bool, utype=int, castShadows=bool, edgeSwap=bool, chordHeightRatio=float, useDefaultLights=bool, vnum=int, unum=int, useChordHeight=bool, minScreen=float, smoothShading=bool, opposite=bool, useChordHeightRatio=bool):
    """
    renderInfo is undoable, queryable, and editable.
    

    
The renderInfo commands sets geometric properties of surfaces of the selected object.

    """
    pass
    


def renderLayerPostProcess(keepImages=bool, sceneName="string"):
    """
    renderLayerPostProcess is NOT undoable, queryable, and NOT editable.
    

    
Post process the results when rendering is done with. Presently this generates a layered PSD file using individual iff files.

    """
    pass
    


def renderManip(state=bool, spotLight=bool, camera=bool, light=bool):
    """
    renderManip is undoable, queryable, and editable.
    

    
This command creates manipulators for cameras or lights.

    """
    pass
    


def renderPartition():
    """
    renderPartition is undoable, queryable, and NOT editable.
    

    
Set or query the model's current partition. When flag q is not used, a partion name must be passed as an argument. In this case the current partition is set to that name.

    """
    pass
    


def renderPassRegistry(supportedRenderPassNames=bool, supportedPassSemantics=bool, renderer="string", passID="string", isPassSupported=bool, supportedRenderPasses=bool, supportedDataTypes=bool, passName=bool, channels=int, supportedChannelCounts=bool):
    """
    renderPassRegistry is NOT undoable, NOT queryable, and NOT editable.
    

    
query information related with render passes.

    """
    pass
    


def renderQualityNode():
    """
    renderQualityNode is undoable, NOT queryable, and NOT editable.
    

    
The renderQualityNode creates a render quality node and registers it with the model. The createNode command will not register nodes of this type correctly.

    """
    pass
    


def renderSettings(camera="string", lastImageName=bool, customTokenString="string", leaveUnmatchedTokens=bool, imageGenericName=bool, layer="string", fullPathTemp=bool, fullPath=bool, firstImageName=bool, genericFrameImageName="string"):
    """
    renderSettings is NOT undoable, NOT queryable, and NOT editable.
    

    
Query interface to the common tab of the render settings

    """
    pass
    


def renderThumbnailUpdate(forceUpdate="string"):
    """
    renderThumbnailUpdate is undoable, queryable, and NOT editable.
    

    
Toggle the updating of object thumbnails. These are visible in tools like the Attribute Editor and Hypershade. All thumbnails everywhere will not update to reflect changes to the object until this command is used to toggle to true unless a specific thumbnail is forced to render using the -forceUpdate flag.

    """
    pass
    


def renderWindowEditor(docTag="string", refresh=bool, defineTemplate="string", parent="string", removeAllImages=bool, useTemplate="string", lockMainConnection=bool, blendMode=int, compDisplay=int, displayStyle="string", unParent=bool, editorName=bool, colorManage=bool, nbImages=bool, compImageFile="string", scaleRed=float, stereo=int, changeCommand="string", panel="string", scaleGreen=float, doubleBuffer=bool, toggle=bool, mainListConnection="string", highlightConnection="string", singleBuffer=bool, nextViewImage=bool, writeImage="string", loadImage="string", exposure=float, stateString=bool, exists=bool, updateMainConnection=bool, scaleBlue=float, showRegion=int, stereoImageOrientation="string", control=bool, unlockMainConnection=bool, gamma=float, removeImage=bool, pcaption="string", currentCameraRig="string", realSize=bool, selectionConnection="string", frameImage=bool, forceMainConnection="string", snapshot="string", autoResize=bool, caption="string", viewTransformName="string", viewImageCount=int, currentCamera="string", saveImage=bool, displayImageViewCount=int, drawAxis=bool, stereoMode="string", resetViewImage=bool, displayImage=int, clear=int, resetRegion=bool, frameRegion=bool, marquee=float, filter="string", cmEnabled=bool):
    """
    renderWindowEditor is undoable, queryable, and editable.
    

    
Create a editor window that can receive the result of the rendering process

    """
    pass
    


def renderWindowSelectContext(exists=bool, image1="string", image2="string", image3="string"):
    """
    renderWindowSelectContext is undoable, queryable, and editable.
    

    
Set the selection context for the render view panel.

    """
    pass
    


def reorder(objects, relative=int, back=bool, front=bool):
    """
    reorder is undoable, NOT queryable, and NOT editable.
    

    
This command reorders (moves) objects relative to their siblings.
For relative moves, both positive and negative numbers may be specified. Positive numbers move the object forward and negative numbers move the object backward amoung its siblings. When an object is at the end (beginning) of the list of siblings, a relative move of 1 (-1) will put the object at the beginning (end) of the list of siblings. That is, relative moves will wrap if necessary.
If a shape is specified and it is the only child then its parent will be reordered.

    """
    pass
    


def reorderContainer(relative=int, back=bool, front=bool):
    """
    reorderContainer is undoable, queryable, and editable.
    

    
This command reorders (moves) objects relative to their siblings in a container.
For relative moves, both positive and negative numbers may be specified. Positive numbers move the object forward and negative numbers move the object backward amoung its siblings. When an object is at the end (beginning) of the list of siblings, a relative move of 1 (-1) will put the object at the beginning (end) of the list of siblings. That is, relative moves will wrap if necessary.
Only nodes within one container can be moved at a time. Note: The container command's -nodeList flag will return a sorted list of contained nodes. To see the effects of reordering, use the -unsortedOrder flag in conjunction with the -nodeList flag.

    """
    pass
    


def reorderDeformers(name="string"):
    """
    reorderDeformers is undoable, NOT queryable, and NOT editable.
    

    
This command changes the order in which 2 deformation nodes affect the output geometry. The first string argument is the name of deformer1, the second is deformer2, followed by the list of objects they deform.
It inserts deformer2 before deformer1. Currently supported deformer nodes include: sculpt, cluster, jointCluster, lattice, wire, jointLattice, boneLattice, blendShape.

    """
    pass
    


def requires(dataType="string", nodeType="string"):
    """
    requires is undoable, NOT queryable, and NOT editable.
    

    
This command is used during file I/O to specify the requirements needed to load the given file. It defines what file format version was used to write the file, or what plug-ins are required to load the scene.
The first string names a product (either "maya", or a plug-in name)
The second string gives the version. This command is only useful during file I/O, so users should not have any need to use this command themselves.
The flags "-nodeType" and "-dataType" specify the node types and data types defined by the plug-in. When Maya open a scene file, it runs "requires" command in the file and load required plug-ins. But some plug-ins may be not loaded because they are missing. The flags "-nodeType" and "-dataType" are used by the missing plug-ins. If one plug-in is missing, nodes and data created by this plug-in are created as unknown nodes and unknown data. Maya records their original types for these unknown nodes and data. When these nodes and data are saved back to file, it will be possible to determine the associated missing plug-ins. And when export selected nodes, Maya can write out the exact required plug-ins. The flags "-nodeType" and "-dataType" is optional. In this command, if these flags are not given for one plug-in and the plug-in is missing, the "requires" command of this plug-in will always be saved back.

    """
    pass
    


def reroot(object):
    """
    reroot is undoable, NOT queryable, and NOT editable.
    

    
This command will reroot a skeleton. The selected joint or the given joint at the command line will be the new root of the skeleton. All ikHandles passing through the selected joint or above it will be deleted.
The given(or selected) joint should not have skin attached. The command works on the given or selected joint. No options or flags are necessary.

    """
    pass
    


def resampleFluid(resampleWidth=int, resampleDepth=int, resampleHeight=int):
    """
    resampleFluid is undoable, queryable, and editable.
    

    
A command to extend the fluid grid, keeping the voxels the same size, and keeping the existing contents of the fluid in the same place. Note that the fluid transform is also modified to make this possible.

    """
    pass
    


def resetTool(string):
    """
    resetTool is undoable, NOT queryable, and NOT editable.
    

    
This command resets a tool back to its "factory settings"

    """
    pass
    


def resolutionNode():
    """
    resolutionNode is undoable, NOT queryable, and NOT editable.
    

    
The resolutionNode creates a render resolution node and registers it with the model. The createNode command will not register nodes of this type correctly.

    """
    pass
    


def resourceManager(saveAs="string", nameFilter="string"):
    """
    resourceManager is NOT undoable, NOT queryable, and NOT editable.
    

    
List resources matching certain properties.

    """
    pass
    


def retimeKeyCtx(image1="string", snapOnFrame=bool, history=bool, moveByFrame=int, exists=bool, image2="string", name="string", image3="string"):
    """
    retimeKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the graph editor using the retime tool.

    """
    pass
    


def reverseCurve(curveOnSurface=bool, object=bool, nodeState=int, range=bool, replaceOriginal=bool, constructionHistory=bool, caching=bool, name="string"):
    """
    reverseCurve is undoable, queryable, and editable.
    

    
The reverseCurve command reverses the direction of a curve or curve-on-surface. A string is returned containing the pathname of the newly reversed curve and the name of the resulting dependency node. The reversed curve has the same parameter range as the original curve.

    """
    pass
    


def reverseSurface(direction=int, object=bool, nodeState=int, replaceOriginal=bool, constructionHistory=bool, caching=bool, name="string"):
    """
    reverseSurface is undoable, queryable, and editable.
    

    
The reverseSurface command reverses one or both directions of a surface or can be used to "swap" the U and V directions (this creates the effect of reversing the surface normal). The name of the newly reversed surface and the name of the resulting dependency node is returned. The resulting surface has the same parameter ranges as the original surface.
This command also handles selected surface isoparms. For a selected isoparm, imagine that the isoparm curve is reversed after the operation. E.g. reverseSurface surface.v[0.1] will reverse in the U direction.

    """
    pass
    


def revolve(radius="string", rebuild=bool, polygon=int, startSweep=int, endSweep=int, radiusAnchor=float, degree=int, axis="string", pivotY="string", object=bool, range=bool, pivotX="string", caching=bool, tolerance="string", name="string", bridge=bool, autoCorrectNormal=bool, axisChoice=int, useLocalPivot=bool, axisY="string", pivot="string", pivotZ="string", sections=int, computePivotAndAxis=int, useTolerance=bool, nodeState=int, axisX="string", axisZ="string", constructionHistory=bool):
    """
    revolve is undoable, queryable, and editable.
    

    
This command creates a revolved surface by revolving the given profile curve about an axis. The profile curve can be a curve, curve-on-surface, surface isoparm, or trim edge.

    """
    pass
    


def rigidBody(initialVelocity=float, applyForceAt="string", mass=float, active=bool, centerOfMass=float, bounciness=float, damping=float, velocity=bool, staticFriction=float, contactName=bool, layer=int, ignore=bool, spinImpulse=float, impulsePosition=float, impulse=float, contactPosition=bool, solver="string", initialAngularVelocity=float, tesselationFactor=int, dynamicFriction=float, deleteCache=bool, contactCount=bool, position=float, orientation=float, particleCollision=bool, angularVelocity=bool, cache=bool, force=bool, collisions=bool, standInObject="string", lockCenterOfMass=bool, passive=bool, name="string"):
    """
    rigidBody is undoable, queryable, and editable.
    

    
This command creates a rigid body from a polygonal or nurbs surface.

    """
    pass
    


def rigidSolver(showCollision=bool, interpenetrationCheck=bool, displayVelocity=bool, contactData=bool, showInterpenetration=bool, displayCenterOfMass=bool, solverMethod=int, bounciness=bool, friction=bool, velocityVectorScale=float, autoTolerances=bool, deleteCache=bool, cacheData=bool, statistics=bool, startTime=float, collisionTolerance=float, rigidBodyCount=bool, collide=bool, stepSize=float, state=bool, current=bool, create=bool, dynamics=bool, interpenetrate=bool, rigidBodies=bool, displayConstraint=bool):
    """
    rigidSolver is undoable, queryable, and editable.
    

    
This command sets the attributes for the rigid solver

    """
    pass
    


def roll(camera, degree=int, relative=bool, absolute=bool):
    """
    roll is undoable, NOT queryable, and NOT editable.
    

    
The roll command rotates a camera about its viewing direction, a positive angle produces clockwise camera rotation, while a negative angle produces counter-clockwise camera rotation.
The default mode is relative and the rotation is applied with respect to the current orientation of the camera. When mode is set to absolute, the rotation is applied with respect to the plane constructed from the following three vectors in the world space: the world up vector, the camera view vector, and the camera up vector.
The rotation angle is specified in degrees.
The roll command can be applied to either a perspective or an orthographic camera.
This command may be applied to more than one camera; objects that are not cameras are ignored. When no camera name supplied, this command is applied to all currently active cameras.

    """
    pass
    


def rollCtx(context, image1="string", rollScale=float, alternateContext=bool, history=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    rollCtx is undoable, queryable, and editable.
    

    
Create, edit, or query a roll context.

    """
    pass
    


def rotate(floatfloatfloatobjects, reflectionAboutZ=bool, xformConstraint="string", symNegative=bool, rotateXY=bool, reflectionAboutBBox=bool, relative=bool, translate=bool, reflectionTolerance=float, reflectionAboutX=bool, rotateXYZ=bool, deletePriorHistory=bool, centerPivot=bool, rotateZ=bool, worldSpace=bool, objectSpace=bool, preserveGeometryPosition=bool, rotateYZ=bool, constrainAlongNormal=bool, forceOrderXYZ=bool, absolute=bool, preserveUV=bool, pivot="string", rotateY=bool, euler=bool, reflection=bool, objectCenterPivot=bool, rotateX=bool, preserveChildPosition=bool, reflectionAboutOrigin=bool, rotateXZ=bool, reflectionAboutY=bool):
    """
    rotate is undoable, NOT queryable, and NOT editable.
    

    
The rotate command is used to change the rotation of geometric objects. The rotation values are specified as Euler angles (rx, ry, rz). The values are interpreted based on the current working unit for Angular measurements. Most often this is degrees.
The default behaviour, when no objects or flags are passed, is to do a absolute rotate on each currently selected object in the world space.

    """
    pass
    


def rotationInterpolation(convert="string"):
    """
    rotationInterpolation is undoable, queryable, and NOT editable.
    

    
The rotationInterpolation command converts the rotation curves to the desired rotation interpolation representation. For example, an Euler-angled representation can be converted to Quaternion.

    """
    pass
    


def roundConstantRadius(stringstringstringstring, sideb=int, side="string", object=bool, radiuss="string", append=bool, constructionHistory=bool, sidea=int, name="string"):
    """
    roundConstantRadius is undoable, queryable, and editable.
    

    
This command generates constant radius NURBS fillets and NURBS corner surfaces for matching edge pairs on NURBS surfaces. An edge pair is a matching pair of surface isoparms or trim edges. This command can handle more than one edge pair at a time. This command can also handle compound edges, which is where an edge pair is composed of more than two surfaces. Use the "-sa" and "-sb" flags in this case.
The results from this command are three surface var groups plus the name of the new roundConstantRadius dependency node, if history was on. The 1st var group contains trimmed copies of the original surfaces. The 2nd var group contains the new NURBS fillet surfaces. The 3rd var group contains the new NURBS corners (if any).
A simple example of an edge pair is an edge of a NURBS cube, where two faces of the cube meet. This command generates a NURBS fillet at the edge and trims back the faces.
Another example is a NURBS cylinder with a planar trim surface cap. This command will create a NURBS fillet where the cap meets the the cylinder and will trim back the cap and the cylinder.
Another example involves all 12 edges of a NURBS cube. NURBS fillets are created where any face meets another face. NURBS corners are created whenever 3 edges meet at a corner.

    """
    pass
    


def rowColumnLayout(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfRows=int, numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", rowSpacing=int, numberOfChildren=bool, highlightColor=float, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, rowAttach=int, columnOffset=int, childArray=bool, exists=bool, numberOfColumns=int, columnSpacing=int, columnAlign=int, enableBackground=bool, rowHeight=int, visibleChangeCommand="string", visible=bool, rowOffset=int, rowAlign=int, fullPathName=bool, dropCallback="string", columnAttach=int, noBackground=bool, backgroundColor=float, columnWidth=int, manage=bool, isObscured=bool):
    """
    rowColumnLayout is undoable, queryable, and editable.
    

    
This command creates a rowColumn layout. A rowColumn layout positions children in either a row or column format. A column layout, specified with the -nc/numberOfColumns flag, allows you set text alignment, attachments and offsets for each column in the layout. Every member of a column will have the same alignment, attachment and offsets. Likewise the row format, specified by the -nr/numberOfRows flag, allows setting of these attributes for each row in the layout. Every member of a row will have the same attributes. The layout must be either a row or column format. This layout does not support both, or the specification of attributes on an individual child basis.
Some flags only make sense for one of either the row format or the column format. For example the -rh/rowHeight flag can only be specified in row format. In column format the row height is determined by the tallest child in the row, plus offsets.

    """
    pass
    


def rowLayout(string, docTag="string", height=int, columnWidth4=int, parent="string", columnAlign1="string", numberOfPopupMenus=bool, adjustableColumn1=int, defineTemplate="string", width=int, popupMenuArray=bool, highlightColor=float, numberOfChildren=bool, dragCallback="string", columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn5=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", childArray=bool, exists=bool, columnAttach4="string", useTemplate="string", numberOfColumns=int, noBackground=bool, adjustableColumn2=int, visible=bool, adjustableColumn6=int, enableBackground=bool, visibleChangeCommand="string", adjustableColumn=int, columnOffset1=int, columnAlign2="string", columnWidth3=int, columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", enable=bool, fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, manage=bool, columnAttach1="string", columnOffset4=int, columnAttach2="string", columnAttach6="string", isObscured=bool, columnOffset6=int):
    """
    rowLayout is undoable, queryable, and editable.
    

    
This command creates a layout capable of positioning children into a single horizontal row.

    """
    pass
    


def runup(maxFrame=(), state=bool, fromStartFrame=bool, cache=bool, fromPreviousFrame=bool):
    """
    runup is undoable, NOT queryable, and NOT editable.
    

    
runup plays the scene through a frame of frames, forcing dynamic objects to evaluate as it does so. If no max frame is specified, runup runs up to the current time.

    """
    pass
    


def sampleImage(fastSample=bool, resolution=int):
    """
    sampleImage is undoable, NOT queryable, and NOT editable.
    

    
The sampleImage command is used to control parameters of sample images, such as swatches in the multilister. The fast option turns on or off some rendering cheats which speed up the render but may cause edges to look ragged. The resolution option specifies the width in pixels of the image which will be rendered for the specified node. Note that the width of the image is also the height of the image since sample images are square.

    """
    pass
    


def saveAllShelves():
    """
    saveAllShelves is undoable, NOT queryable, and NOT editable.
    

    
This command writes all shelves that are immediate children of the specified control layout to the prefs directory.

    """
    pass
    


def saveFluid(currentTime=int, startTime=int, endTime=int):
    """
    saveFluid is undoable, queryable, and editable.
    

    
A command to save the current state of the fluid to the initial state cache. The grids to be saved are determined by the cache attributes: cacheDensity, cacheVelocity, etc. These attributes are normally set from the options on Set Initial State. The cache must be set up before invoking this command.

    """
    pass
    


def saveImage(imageNameimageName, docTag="string", height=int, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", preventOverride=bool, exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", sceneFile="string", objectThumbnail="string", dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, currentView=bool, isObscured=bool):
    """
    saveImage is undoable, queryable, and editable.
    

    
This command creates a static image for non-xpm files. Any image file format supported by the file texture node is supported by this command.
This command creates a static image control for non-xpm files used to display a thumbnail image of the scene file.

    """
    pass
    


def saveInitialState(saveall=bool, attribute="string"):
    """
    saveInitialState is undoable, NOT queryable, and NOT editable.
    

    
saveInitialState saves the current state of dynamics objects as the initial state. A dynamic object is a particle shape, rigid body, rigid constraint or rigid solver. If no objects are specified, it saves the initial state for any selected objects. It returns the names of the objects for which initial state was saved.

    """
    pass
    


def saveMenu():
    """
    saveMenu is undoable, NOT queryable, and NOT editable.
    

    
This command is used for saving the contents of a menu, so that another instance of the menu may be recreated later. The command writes out a file which, when run as a script, will rebuild the menuItems contained in the original menu. Note that the fileName is relative to the user's marking menu preference directory.
Note that this command is used solely by the Marking Menu Editor and is not intended to be used for general purposes.
Note that this command doesn't work well with controls that have mixed mel and python command callbacks. Also, because it saves the menu state to a mel file, it does not work with callbacks that are python callable objects.
The first argument is the name of the manu to save, the second one is the name of the file.

    """
    pass
    


def savePrefObjects():
    """
    savePrefObjects is undoable, NOT queryable, and NOT editable.
    

    
This command saves preference dependency nodes to "userPrefObjects.ma" in the user preference directory.

    """
    pass
    


def savePrefs(uiLayout=bool, menuSets=bool, general=bool, colors=bool, plugins=bool, hotkeys=bool):
    """
    savePrefs is undoable, NOT queryable, and NOT editable.
    

    
This command saves preferences to disk. If no flags are specified then all pref types get saved out.

    """
    pass
    


def saveShelf():
    """
    saveShelf is undoable, NOT queryable, and NOT editable.
    

    
This command saves the specified shelf (first argument) to the specified file (second argument).
Note that this command doesn't work well with controls that have mixed mel and python command callbacks. Also, because it saves the state to a mel file, it does not work with callbacks that are python callable objects.

    """
    pass
    


def saveToolSettings():
    """
    saveToolSettings is undoable, NOT queryable, and NOT editable.
    

    
This command causes all the tools not on the shelf to save their settings as optionVars. This is called automatically by the system when Maya exits.

    """
    pass
    


def saveViewportSettings():
    """
    saveViewportSettings is undoable, NOT queryable, and NOT editable.
    

    
This command causes all the 3d views to save their settings as optionVar's. This is called automatically by the system when Maya exits.

    """
    pass
    


def scale(floatfloatfloatobjects, reflectionAboutZ=bool, xformConstraint="string", symNegative=bool, distanceOnly=bool, reflectionAboutBBox=bool, relative=bool, reflectionTolerance=float, reflectionAboutX=bool, scaleY=bool, scaleZ=bool, deletePriorHistory=bool, centerPivot=bool, worldSpace=bool, scaleYZ=bool, objectSpace=bool, preserveGeometryPosition=bool, constrainAlongNormal=bool, scaleX=bool, scaleXZ=bool, absolute=bool, preserveUV=bool, pivot="string", scaleXY=bool, scaleXYZ=bool, reflection=bool, localSpace=bool, objectCenterPivot=bool, preserveChildPosition=bool, orientAxes=int, reflectionAboutOrigin=bool, reflectionAboutY=bool):
    """
    scale is undoable, NOT queryable, and NOT editable.
    

    
The scale command is used to change the sizes of geometric objects.
The default behaviour, when no objects or flags are passed, is to do a relative scale on each currently selected object object using each object's existing scale pivot point.

    """
    pass
    


def scaleComponents(floatfloatfloatobjects, pivot="string", rotation=int):
    """
    scaleComponents is undoable, NOT queryable, and NOT editable.
    

    
This is a limited version of the scale command. First, it only works on selected components. You provide a pivot in world space, and you can provide a rotation. This rotation affects the scaling, so that rather than scaling in X, Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given rotation.
This allows selected components to be scaled in any arbitrary space, not just object or world space as the regular scale allows.
Scale values are always relative, not absolute.

    """
    pass
    


def scaleConstraint(targetobject, remove=bool, scaleCompensate=bool, skip="string", maintainOffset=bool, weightAliasList=bool, layer="string", offset=float, targetList=bool, weight=float, name="string"):
    """
    scaleConstraint is undoable, queryable, and editable.
    

    
Constrain an object's scale to the scale of the target object or to the average scale of a number of targets.
A scaleConstraint takes as input one or more "target" DAG transform nodes to which to scale the single "constraint object" DAG transform node. The scaleConstraint scales the constrained object at the weighted geometric mean of the world space target scale factors.

    """
    pass
    


def scaleKey(scaleSpecifiedKeys=bool, hierarchy="string", newStartTime=(), newStartFloat=float, float=(), includeUpperBound=bool, controlPoints=bool, newEndTime=(), time=(), floatPivot=float, floatScale=float, shape=bool, newEndFloat=float, valueScale=float, valuePivot=float, timeScale=float, attribute="string", timePivot=(), animation="string", index=int):
    """
    scaleKey is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command takes keyframes at (or within) the specified times (or time ranges) and scales them. If no times are specified, the scale is applied to active keyframes or (if no keys are active) all keys of active objects.

    """
    pass
    


def scaleKeyCtx(image1="string", scaleSpecifiedKeys=bool, type="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    scaleKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the graph editor

    """
    pass
    


def sceneEditor(docTag="string", selectReference="string", defineTemplate="string", parent="string", useTemplate="string", lockMainConnection=bool, unParent=bool, forceMainConnection="string", panel="string", shortName=bool, mainListConnection="string", highlightConnection="string", stateString=bool, exists=bool, updateMainConnection=bool, unresolvedName=bool, control=bool, onlyParents=bool, selectItem=int, selectionConnection="string", refreshReferences=bool, withoutCopyNumber=bool, selectCommand="string", unlockMainConnection=bool, filter="string"):
    """
    sceneEditor is undoable, queryable, and editable.
    

    
This creates an editor for managing the files in a scene.

    """
    pass
    


def sceneUIReplacement(getNextFilter="string", clear=bool, update="string", getNextPanel="string", deleteRemaining=bool, getNextScriptedPanel="string"):
    """
    sceneUIReplacement is undoable, NOT queryable, and NOT editable.
    

    
This command returns existing scene based UI that can be utilized by the scene that is being loaded. It can also delete any such UI that is not used by the loading scene.

    """
    pass
    


def scmh(floatfloat, ignore=int, quiet=bool, relative=bool, absolute=bool):
    """
    scmh is undoable, NOT queryable, and NOT editable.
    

    
Set the current manipulator handle value(s). In UI units (where applicable), though the syntax is set to handle the unit type of the current manipulator handle (if available).

    """
    pass
    


def scriptCtx(setSelectionHeadsUp="string", spring=bool, follicle=bool, plane=bool, surfaceParameterPoint=bool, curve=bool, subdivMeshFace=bool, curveOnSurface=bool, nurbsSurface=bool, toolFinish="string", expandSelectionList=bool, setSelectionCount=int, animOutTangent=bool, animCurve=bool, surfaceKnot=bool, joint=bool, sculpt=bool, collisionModel=bool, particle=bool, editPoint=bool, dimension=bool, ignoreInvalidItems=bool, orientationLocator=bool, curveParameterPoint=bool, lastAutoComplete=bool, history=bool, polymeshEdge=bool, image2="string", latticePoint=bool, finalCommandScript="string", hairSystem=bool, polymeshFreeEdge=bool, toolStart="string", showManipulators=bool, springComponent=bool, imagePlane=bool, locatorUV=bool, nurbsCurve=bool, name="string", scalePivot=bool, fluid=bool, rigidConstraint=bool, surfaceFace=bool, nParticle=bool, isoparm=bool, texture=bool, polymesh=bool, cumulativeLists=bool, handle=bool, setDoneSelectionPrompt="string", particleShape=bool, lattice=bool, baseClassName="string", selectHandle=bool, rigidBody=bool, rotatePivot=bool, curveKnot=bool, light=bool, stroke=bool, subdivMeshEdge=bool, allObjects=bool, nCloth=bool, localRotationAxis=bool, image3="string", exitUponCompletion=bool, polymeshVertex=bool, subdivMeshPoint=bool, setNoSelectionHeadsUp="string", polymeshUV=bool, hull=bool, edge=bool, implicitGeometry=bool, jointPivot=bool, emitter=bool, polymeshFace=bool, objectComponent=bool, setAutoToggleSelection=bool, surfaceUV=bool, animKeyframe=bool, toolCursorType="string", surfaceRange=bool, ikEndEffector=bool, allComponents=bool, subdivMeshUV=bool, vertex=bool, subdiv=bool, nRigid=bool, surfaceEdge=bool, setNoSelectionPrompt="string", setAutoComplete=bool, totalSelectionSets=int, setSelectionPrompt="string", enableRootSelection=bool, locatorXYZ=bool, image1="string", field=bool, forceAddSelect=bool, controlVertex=bool, camera=bool, animBreakdown=bool, facet=bool, exists=bool, cluster=bool, dynamicConstraint=bool, polymeshVtxFace=bool, nonlinear=bool, ikHandle=bool, setAllowExcessCount=bool, animInTangent=bool, locator=bool, title="string", nParticleShape=bool):
    """
    scriptCtx is undoable, queryable, and editable.
    

    
This command allows a user to create their own tools based on the selection tool. A number of selection lists can be collected, the behaviour of the selection and the selection masks are fully customizable, etc.
The command is processed prior to being executed. The keyword "$Selection#" where # is a number 1 or greater specifies a selection set. The context can specify several selection sets which are substituted in place of the $Selection# keyword in the form of a Mel string array. Items that are specific per set need to be specified in each set, if they are going to be specified for any of the sets. See examples below.
In addition, in order to specify the type of selection you need to be making, any of the selection type flags from "selectType" command can be used here.

    """
    pass
    


def scriptEditorInfo(input="string", writeHistory=bool, clearHistory=bool, clearHistoryFile=bool, suppressErrors=bool, historyFilename="string", suppressWarnings=bool, suppressInfo=bool, suppressStackWindow=bool, suppressResults=bool):
    """
    scriptEditorInfo is undoable, queryable, and editable.
    

    
Use this command to directly manipulate and query the contents of the Command Window window.
Note: Due to recent changes, certain flags will no longer work on the Script Editor Window. All flags will continue to work with the CommandWindow (old Script Editor).
Note: This command cannot be used to create a new script editor window.

    """
    pass
    


def scriptedPanel(panelName, tearOff=bool, docTag="string", parent="string", useTemplate="string", label="string", replacePanel="string", unParent=bool, tearOffCopy="string", isUnique=bool, defineTemplate="string", createString=bool, needsInit=bool, type="string", exists=bool, control=bool, menuBarVisible=bool, init=bool, tearOffRestore=bool, popupMenuProcedure="string", editString=bool, copy="string"):
    """
    scriptedPanel is undoable, queryable, and editable.
    

    
This command will create an instance of the specified scriptedPanelType. A panel is a collection of UI objects (buttons, fields, graphical views) that are grouped together. A panel can be moved around as a group within the application interface, and torn off to exist in its own window. The panel takes care of maintaining the state of its UI when it is relocated, or recreated. A scripted panel is a panel that is defined in MEL, with all of the required callbacks available as MEL proc's.

    """
    pass
    


def scriptedPanelType(string, label="string", obsolete=bool, saveStateCallback="string", defineTemplate="string", deleteCallback="string", useTemplate="string", addCallback="string", initCallback="string", copyStateCallback="string", removeCallback="string", retainOnFileOpen=bool, createCallback="string", exists=bool, customView=bool, unique=bool):
    """
    scriptedPanelType is undoable, queryable, and editable.
    

    
This command defines the callbacks for a type of scripted panel. The panel type created by this command is then used when creating a scripted panel. See also the 'scriptedPanel' command.

    """
    pass
    


def scriptJob(parent="string", uiDeleted="string", conditionTrue="string", event="string", permanent=bool, listEvents=bool, listJobs=bool, kill=int, nodeDeleted="string", attributeChange="string", runOnce=bool, attributeDeleted="string", connectionChange="string", timeChange="string", conditionFalse="string", listConditions=bool, allChildren=bool, disregardIndex=bool, nodeNameChanged="string", replacePrevious=bool, protected=bool, compressUndo=bool, exists=int, force=bool, idleEvent="string", killWithScene=bool, conditionChange="string", killAll=bool, attributeAdded="string"):
    """
    scriptJob is undoable, NOT queryable, and NOT editable.
    

    
This command creates a "script job", which is a MEL command or script. This job is attached to the named condition, event, or attribute. Each time the condition switches to the desired state (or the trigger is triggered, etc), the script is run.
Script jobs are tied to the event loop in the interactive application. They are run during idle events. This means that script jobs do not exist in the batch application. The scriptJob command does nothing in batch mode.
This triggering happens very frequently so for speed considerations no events are forwarded during playback. This means that you cannot use scriptJob -tc tcCallback; to alter animation behaviour. Use an expression instead, or the rendering callbacks "preRenderMel" and "postRenderMel".
When setting up jobs for conditions, it is invalid to setup jobs for the true state, false state, and state change at the same time. The behaviour is undefined. The user can only setup jobs for the true and/or false state, or only for the state change, but not three at the same time. i.e. if you do:
// Set up a job that runs for the life of the application.
// This job cannot be deleted with the "kill" command no matter what.
scriptJob -e "SelectionChanged" "print \"Annoying Message!\\n\"" -permanent;
// set up a job for the true state
scriptJob -ct "playingBack" playBackCallback;
// set up a job for the false state
scriptJob -cf "playingBack" playBackCallback;
then you should NOT do
scriptJob -cc "playingBack" playBackCallback;
otherwise it will lead to undefined behaviour.
This command can also be used to list available conditions and events, and to kill running jobs.

    """
    pass
    


def scriptNode(attributeList, ignoreReferenceEdits=bool, scriptType=int, executeBefore=bool, afterScript="string", beforeScript="string", sourceType="string", executeAfter=bool, name="string"):
    """
    scriptNode is undoable, queryable, and editable.
    

    
scriptNodes contain scripts that are executed when a file is loaded or when the script node is deleted. If a script modifies a referenced node, the changes will be tracked as reference edits unless the scriptNode was created with the ignoreReferenceEdits flag. The scriptNode command is used to create, edit, query, and test scriptNodes.

    """
    pass
    


def scriptTable(name, docTag="string", afterCellChangedCmd="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, rowsToBeRemovedCmd="string", width=int, highlightColor=float, getCellCmd="string", label=int, dragCallback="string", annotation="string", sortEnabled=bool, deleteRow=int, preventOverride=bool, underPointerRow=bool, selectionBehavior=int, popupMenuArray=bool, clearTable=bool, enableBackground=bool, cellIndex=int, excludingHeaders=bool, insertRow=int, rowsRemovedCmd="string", selectedRows=int, exists=bool, visibleChangeCommand="string", cellValue="string", visible=bool, enable=bool, cellBackgroundColorCommand="string", rowHeight=int, multiEditEnabled=bool, rows=int, columnFilter=int, selectedColumns=int, selectionChangedCmd="string", useTemplate="string", selectedRow=bool, underPointerColumn=bool, fullPathName=bool, dropCallback="string", clearRow=int, useDoubleClickEdit=bool, cellForegroundColorCommand="string", noBackground=bool, backgroundColor=float, columnWidth=int, selectionMode=int, manage=bool, editable=bool, columns=int, selectedCells=int, isObscured=bool, cellChangedCmd="string"):
    """
    scriptTable is undoable, queryable, and editable.
    

    
This command creates/edits/queries the script table control.

    """
    pass
    


def scrollField(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", manage=bool, fontPointSize=int, enterCommand="string", dragCallback="string", numberOfLines=int, annotation="string", enable=bool, preventOverride=bool, popupMenuArray=bool, highlightColor=float, width=int, selection=bool, font="string", exists=bool, changeCommand="string", visible=bool, enableBackground=bool, visibleChangeCommand="string", qtFont="string", keyPressCommand="string", fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, wordWrap=bool, clear=bool, insertText="string", editable=bool, insertionPosition=int, isObscured=bool, text="string"):
    """
    scrollField is undoable, queryable, and editable.
    

    
This command creates a scrolling field that handles multiple lines of text.

    """
    pass
    


def scrollLayout(string, docTag="string", borderVisible=bool, childResizable=bool, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", height=int, numberOfChildren=bool, highlightColor=float, annotation="string", horizontalScrollBarThickness=int, preventOverride=bool, popupMenuArray=bool, scrollPage="string", verticalScrollBarThickness=int, childArray=bool, scrollByPixel="string", scrollAreaHeight=bool, exists=bool, resizeCommand="string", enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", scrollAreaWidth=bool, panEnabled=bool, noBackground=bool, backgroundColor=float, minChildWidth=int, manage=bool, scrollAreaValue=bool, verticalScrollBarAlwaysVisible=bool, isObscured=bool):
    """
    scrollLayout is undoable, queryable, and editable.
    

    
This command creates a scroll layout. A scroll layout is useful for when you have a number of controls which cannot all be visible at a time. This layout will display a horizontal and/or vertical scroll bar when necessary to bring into view the hidden controls. Since the scroll layout provides no real positioning of children you should use another control layout as the immediate child.

    """
    pass
    


def sculpt(before=bool, exclusive="string", after=bool, dropoffType="string", frontOfChain=bool, includeHiddenSelections=bool, objectCentered=bool, prune=bool, geometryIndices=bool, sculptTool="string", split=bool, insideMode="string", geometry="string", name="string", maxDisplacement="string", groupWithLocator=bool, parallel=bool, dropoffDistance="string", ignoreSelected=bool, afterReference=bool, remove=bool, mode="string", deformerTools=bool):
    """
    sculpt is undoable, queryable, and editable.
    

    
This command creates/edits/queries a sculpt object deformer. By default for creation mode an implicit sphere will be used as the sculpting object if no sculpt tool is specified. The name of the created/edited object is returned.

    """
    pass
    


def sculptMeshCacheChangeCloneSource(target="string", blendShape="string"):
    """
    sculptMeshCacheChangeCloneSource is undoable, queryable, and editable.
    

    
This command changes the source blend shape and target for the clone target tool. Used internally for undo/redo, don't call it directly.

    """
    pass
    


def sculptMeshCacheCtx(useGlobalSize=bool, buildUpRate=float, useSteadyStroke=bool, frame=bool, grabTwist=bool, steadyStrokeDistance=float, falloffType=int, constrainToSurface=bool, stampOrientToStroke=bool, minStrength=float, stampRandomizeScale=float, stampPlacement=int, freezeSelection=bool, minSize=float, stampRandomizeRotation=float, wholeStroke=bool, grabFollowPath=bool, displayWireframe=bool, grabSilhouette=bool, useStampDistance=bool, stampRandomizeStrength=float, lastMode="string", orientToSurface=bool, brushSize=float, wireframeAlpha=float, sculptFalloffCurve="string", useScreenSpace=bool, displayFrozen=bool, lockShellBorder=bool, inverted=bool, stampRotation=float, cloneTargetSource="string", useStampImage=bool, mirror=int, cloneHideSource=bool, cloneMethod=int, displayMask=bool, adjustSize=bool, stampRandomization=bool, affectAllLayers=bool, stampRandomizePosY=float, stampRandomizeFlipY=bool, stampFlipX=bool, adjustStrength=bool, brushDirection=int, stampDistance=float, updatePlane=bool, flood=float, stampRandomizePosX=float, size=float, stampFlipY=bool, cloneShapeSource="string", floodFreeze=float, mode="string", brushStrength=float, direction=int, stampFile="string", strength=float, stampRandomizeFlipX=bool, wireframeColor=float):
    """
    sculptMeshCacheCtx is undoable, queryable, and editable.
    

    
This is a tool context command for mesh cache sculpting tool.

    """
    pass
    


def sculptTarget(before=bool, exclusive="string", inbetweenWeight=float, geometryIndices=bool, after=bool, ignoreSelected=bool, split=bool, includeHiddenSelections=bool, target=int, snapshot=int, deformerTools=bool, parallel=bool, frontOfChain=bool, regenerate=bool, geometry="string", remove=bool, prune=bool, afterReference=bool, name="string"):
    """
    sculptTarget is undoable, NOT queryable, and editable.
    

    
This command is used to specify the blend shape target to be modified by the sculpting tools and transform manipulators.

    """
    pass
    


def select(objects, noExpand=bool, symmetry=bool, visible=bool, allDependencyNodes=bool, toggle=bool, all=bool, symmetrySide=int, hierarchy=bool, allDagObjects=bool, deselect=bool, containerCentric=bool, add=bool, addFirst=bool, clear=bool, replace=bool):
    """
    select is undoable, NOT queryable, and NOT editable.
    

    
This command is used to put objects onto or off of the active list. If none of the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to replace the objects on the active list with the given list of objects.
When selecting a set as in "select set1", the behaviour is for all the members of the set to become selected instead of the set itself. If you want to select a set, the "-ne/noExpand" flag must be used.
With the advent of namespaces, selection by name may be confusing. To clarify, without a qualified namespace, name lookup is limited to objects in the root namespace ":". There are really two parts of a name: the namespace and the name itself which is unique within the namespace. If you want to select objects in a specific namespace, you need to include the namespace separator ":".
For example, 'select -r "foo*"' is trying to look for an object with the "foo" prefix in the root namespace. It is not trying to look for all objects in the namespace with the "foo" prefix. If you want to select all objects in a namespace (foo), use 'select "foo:*"'.
Note: When the application starts up, there are several dependency nodes created by the system which must exist. These objects are not deletable but are selectable. All objects (dag and dependency nodes) in the scene can be obtained using the "ls" command without any arguments. When using the "-all", "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only the deletable objects are selected. The non deletable object can still be selected by explicitly specifying their name as in "select time1;".

    """
    pass
    


def selectContext(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    selectContext is undoable, queryable, and editable.
    

    
Creates a context to perform selection.

    """
    pass
    


def selectionConnection(addTo="string", activeCharacterList=bool, activeCacheList=bool, defineTemplate="string", parent="string", findObject="string", useTemplate="string", select="string", g=bool, addScript="string", editor="string", exists=bool, removeScript="string", activeList=bool, setList=bool, deselect="string", keyframeList=bool, characterList=bool, connectionList=bool, switch=bool, identify=bool, clear=bool, highlightList=bool, lock=bool, object="string", modelList=bool, worldList=bool, filter="string", remove="string"):
    """
    selectionConnection is undoable, queryable, and editable.
    

    
This command creates a named selectionConnection object. This object is simply a shared selection list. It may be used by editors to share their highlight data. For example, an outliner may attach its selected list to one of these objects, and a graph editor may use the same object as a list source. Then, the graph editor would only display objects that are selected in the outliner.
Selection connections are UI objects which contain a list of model objects. Selection connections are useful for specifying which objects are to be displayed within a particular editor. Editor's have three plug sockets where a selection connection may be attached. They are:
mainListConnection
an input socket which contains a list of objects that are to be displayed within the editor
selectionConnection
an output socket which contains a list of objects that are selected within the editor
highlightConnection
an input socket which contains a list of objects that are to be highlighted within the editor
There are several different types of selection connections that may be created. They include:
activeList
a selection connection which contains a list of everything in the model which is active (which includes geometry objects and keys)
modelList
a selection connection which contains a list of all the geometry (i.e. excluding keys) objects that are currently active
keyframeList
a selection connection which contains a list of all the keys that are currently active
worldList
a selection connection which contains a list of all the objects in the world
objectList
a selection connection which contains one model object (which may be a set)
listList
a selection connection which contains a list of selection connections
editorList
a selection connection which contains a list of objects that are attached to the mainListConnection of the specified editor
setList
a selection connection which contains a list of all the sets in the world
characterList
a selection connection which contains a list of all the characters in the world
highlightList
a selection connection which contains a list of objects to be highlighted in some fashion
Below is an example selectionConnection network between two editors. Editor 1 is setup to display objects on the activeList. Editor 2 is setup to display objects which are selected within Editor 1, and objects that are selected in Editor 2 are highlighted within Editor 1:
-- Editor 1--       -- Editor 2--
inputList-->| main |      |  |->| main |      |
|      | sele |--|  |      | sele |--|
|->| high |      |     | high |      |  |
|   -------------       -------------   |
|------------- fromEditor2 -------------|
The following commands will establish this network:
selectionConnection -activeList inputList;
selectionConnection fromEditor1;
selectionConnection fromEditor2;
editor -edit -mainListConnection inputList Editor1;
editor -edit -selectionConnection fromEditor1 Editor1;
editor -edit -mainListConnection fromEditor1 Editor2;
editor -edit -selectionConnection fromEditor2 Editor2;
editor -edit -highlightConnection fromEditor2 Editor1;
Note: to delete a selection connection use the deleteUI command
Note: commands which expect objects may be given a selection connection instead, and the command will operate upon the objects wrapped by the selection connection
Note: the graph editor and the dope sheet are the only editors which can use the editor connection to the highlightConnection of another editor
WARNING: some flag combinations may not behave as you expect. The command is really intended for internal use for managing the outliner used by the various editors.

    """
    pass
    


def selectKey(targetList, time=(), hierarchy="string", remove=bool, replace=bool, float=(), includeUpperBound=bool, keyframe=bool, controlPoints=bool, clear=bool, index=int, shape=bool, unsnappedKeys=float, outTangent=bool, addTo=bool, attribute="string", inTangent=bool, animation="string", toggle=bool):
    """
    selectKey is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command places keyframes and/or keyframe tangents on the active list.

    """
    pass
    


def selectKeyCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    selectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to select keyframes within the graph editor

    """
    pass
    


def selectKeyframeRegionCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    selectKeyframeRegionCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def selectMode(component=bool, hierarchical=bool, object=bool, root=bool, template=bool, preset=bool, leaf=bool):
    """
    selectMode is undoable, queryable, and NOT editable.
    

    
The selectMode command is used to change the selection mode. Object, component, root, leaf and template modes are mutually exclusive.

    """
    pass
    


def selectPref(selectTypeChangeAffectsActive=bool, preSelectHiliteSize=float, xformNoSelect=bool, preSelectTweakDeadSpace=int, affectsActive=bool, autoSelectContainer=bool, trackSelectionOrder=bool, preSelectDeadSpace=int, clickBoxSize=int, manipClickBoxSize=int, preSelectClosest=bool, selectionChildHighlightMode=int, clickDrag=bool, preSelectBackfacing=bool, paintSelectWithDepth=bool, singleBoxSelection=bool, disableComponentPopups=bool, expandPopupList=bool, useDepth=bool, paintSelect=bool, autoUseDepth=bool, containerCentricSelection=bool, popupMenuSelection=bool, ignoreSelectionPriority=bool, preSelectHilite=bool, allowHiliteSelection=bool, straightLineDistance=bool):
    """
    selectPref is undoable, queryable, and NOT editable.
    

    
This command controls state variables used to selection UI behavior.

    """
    pass
    


def selectPriority(polymeshFreeEdge=int, surfaceKnot=int, follicle=int, scalePivot=int, emitter=int, curveOnSurface=int, nCloth=int, fluid=int, motionTrailPoint=int, plane=int, rotatePivot=int, joint=int, sculpt=int, hairSystem=int, subdiv=int, animCurve=int, nonlinear=int, selectHandle=int, isoparm=int, polymesh=int, implicitGeometry=int, rigidConstraint=int, vertex=int, polymeshFace=int, light=int, texture=int, edge=int, animInTangent=int, subdivMeshUV=int, particleShape=int, editPoint=int, dimension=int, animBreakdown=int, animOutTangent=int, surfaceEdge=int, byName="string", curveKnot=int, controlVertex=int, nurbsCurve=int, localRotationAxis=int, facet=int, locatorUV=int, dynamicConstraint=int, polymeshVtxFace=int, orientationLocator=int, surfaceParameterPoint=int, allObjects=int, motionTrailTangent=int, rigidBody=int, polymeshVertex=int, ikEndEffector=int, subdivMeshPoint=int, particle=int, cluster=int, animKeyframe=int, handle=int, subdivMeshEdge=int, stroke=int, nParticleShape=int, surfaceFace=int, hull=int, locator=int, springComponent=int, polymeshUV=int, nurbsSurface=int, allComponents=int, curveParameterPoint=int, locatorXYZ=int, curve=int, collisionModel=int, meshUVShell=int, imagePlane=int, jointPivot=int, nParticle=int, surfaceRange=int, lattice=int, spring=int, field=int, polymeshEdge=int, nRigid=int, camera=int, subdivMeshFace=int, ikHandle=int, latticePoint=int, queryByName="string"):
    """
    selectPriority is undoable, queryable, and NOT editable.
    

    
The selectPriority command is used to change the selection priority of particular types of objects that can be selected when using the select tool. It accepts no other arguments besides the flags. These flags are the same as used by the 'selectType' command.

    """
    pass
    


def selectType(spring=bool, follicle=bool, plane=bool, surfaceParameterPoint=bool, curve=bool, subdivMeshFace=bool, curveOnSurface=bool, nurbsSurface=bool, animOutTangent=bool, animCurve=bool, surfaceKnot=bool, joint=bool, sculpt=bool, collisionModel=bool, particle=bool, editPoint=bool, dimension=bool, orientationLocator=bool, curveParameterPoint=bool, polymeshEdge=bool, queryByName="string", latticePoint=bool, hairSystem=bool, polymeshFreeEdge=bool, springComponent=bool, imagePlane=bool, locatorUV=bool, nurbsCurve=bool, scalePivot=bool, fluid=bool, rigidConstraint=bool, surfaceFace=bool, nParticle=bool, isoparm=bool, texture=bool, polymesh=bool, handle=bool, particleShape=bool, lattice=bool, motionTrailPoint=bool, selectHandle=bool, rigidBody=bool, rotatePivot=bool, curveKnot=bool, light=bool, meshUVShell=bool, stroke=bool, subdivMeshEdge=bool, allObjects=bool, nCloth=bool, localRotationAxis=bool, polymeshVertex=bool, subdivMeshPoint=bool, edge=bool, polymeshUV=bool, hull=bool, byName="string", implicitGeometry=bool, jointPivot=bool, emitter=bool, polymeshFace=bool, objectComponent=bool, surfaceUV=bool, animKeyframe=bool, surfaceRange=bool, ikEndEffector=bool, allComponents=bool, subdivMeshUV=bool, vertex=bool, subdiv=bool, nRigid=bool, motionTrailTangent=bool, surfaceEdge=bool, locatorXYZ=bool, field=bool, controlVertex=bool, camera=bool, animBreakdown=bool, facet=bool, cluster=bool, dynamicConstraint=bool, polymeshVtxFace=bool, nonlinear=bool, ikHandle=bool, animInTangent=bool, locator=bool, nParticleShape=bool):
    """
    selectType is undoable, queryable, and NOT editable.
    

    
The selectType command is used to change the set of allowable types of objects that can be selected when using the select tool. It accepts no other arguments besides the flags.
There are basically two different types of items that are selectable when interactively selecting objects in the 3D views. They are classified as objects (entire objects) or components (parts of objects). The object and component command flags control which class of objects are selectable.
It is possible to select components while in the object selection mode. To set the components which are selectable in object selection mode you must use the -ocm flag when specifying the component flags.

    """
    pass
    


def selLoadSettings(shortName=bool, numSettings=int, proxyManager="string", referenceNode="string", fileName="string", unresolvedName=bool, activeProxy="string", proxySetTags="string", deferReference=bool, proxySetFiles="string", proxyTag="string"):
    """
    selLoadSettings is NOT undoable, queryable, and editable.
    

    
This command is used to edit and query information about the implicit load settings. Currently this is primarily intended for internal use within the Preload Reference Editor. selLoadSettings acts on load setting IDs. When implict load settings are built for a target scene, there will be one load setting for each reference in the target scene. Each load setting has a numerical ID which is its index in a pre-order traversal of the target reference hierarchy (with the root scenefile being assigned an ID of 0). Although the IDs are numerical they must be passed to the command as string array. Example: Given the scene:
        a
       / \
      b   c
         / \
        d   e
where: a references b and c c references d and e the IDs will be as follows: a = 0 b = 1 c = 2 d = 3 e = 4 selLoadSettings can be used to change the load state of a reference: whether it will be loaded or unloaded (deferred) when the target scene is opened. Note: selLoadSettings can accept multiple command parameters, but the order must be selected carefully such that no reference is set to the loaded state while its parent is in the unlaoded state. Given the scene:
a
|
b [-]
|
c [-]
where: a references b b references c a = 0 b = 1 c = 2 and b and c are currently in the unloaded state. The following command will succeed and change both b and c to the loaded state: selLoadSettings -e -deferReference 0 "1" "2"; whereas the following command will fail and leave both b and c in the unloaded state: selLoadSettings -e -deferReference 0 "2" "1"; Bear in mind that the following command will also change both b and c to the loaded state: selLoadSettings -e -deferReference 0 "1"; This is because setting a reference to the loaded state automatically sets all child references to the loaded state as well. And vice versa, setting a reference the the unloaded state automatically sets all child reference to the unloaded state.

    """
    pass
    


def separator(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, horizontal=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, style="string", isObscured=bool):
    """
    separator is undoable, queryable, and editable.
    

    
This command creates a separator widget in a variety of drawing styles.

    """
    pass
    


def sequenceManager(addSequencerAudio="string", modelPanel="string", currentShot="string", currentTime=(), attachSequencerAudio="string", writableSequencer="string", node="string", listSequencerAudio="string", listShots=bool):
    """
    sequenceManager is undoable, queryable, and editable.
    

    
The sequenceManager command manages sequences, shots, and their related scenes.

    """
    pass
    


def setAttr(attributeAnyAny, clamp=bool, size=int, alteredValue=bool, capacityHint=int, type="string", lock=bool, channelBox=bool, keyable=bool, caching=bool):
    """
    setAttr is undoable, queryable, and editable.
    

    
Sets the value of a dependency node attribute. No value for the the attribute is needed when the -l/-k/-s flags are used. The -type flag is only required when setting a non-numeric attribute.
The following chart outlines the syntax of setAttr for non-numeric data types:
{TYPE} below means any number of values of type TYPE, separated by a space
[TYPE] means that the value of type TYPE is optional
A|B means that either of A or B may appear
In order to run its examples, first execute these commands to create the sample attribute types:
sphere -n node;
addAttr -ln short2Attr -at short2;
addAttr -ln short2a -p short2Attr -at short;
addAttr -ln short2b -p short2Attr -at short;
addAttr -ln short3Attr -at short3;
addAttr -ln short3a -p short3Attr -at short;
addAttr -ln short3b -p short3Attr -at short;
addAttr -ln short3c -p short3Attr -at short;
addAttr -ln long2Attr -at long2;
addAttr -ln long2a -p long2Attr -at long;
addAttr -ln long2b -p long2Attr -at long;
addAttr -ln long3Attr -at long3;
addAttr -ln long3a -p long3Attr -at long;
addAttr -ln long3b -p long3Attr -at long;
addAttr -ln long3c -p long3Attr -at long;
addAttr -ln float2Attr -at float2;
addAttr -ln float2a -p float2Attr -at "float";
addAttr -ln float2b -p float2Attr -at "float";
addAttr -ln float3Attr -at float3;
addAttr -ln float3a -p float3Attr -at "float";
addAttr -ln float3b -p float3Attr -at "float";
addAttr -ln float3c -p float3Attr -at "float";
addAttr -ln double2Attr -at double2;
addAttr -ln double2a -p double2Attr -at double;
addAttr -ln double2b -p double2Attr -at double;
addAttr -ln double3Attr -at double3;
addAttr -ln double3a -p double3Attr -at double;
addAttr -ln double3b -p double3Attr -at double;
addAttr -ln double3c -p double3Attr -at double;
addAttr -ln int32ArrayAttr -dt Int32Array;
addAttr -ln doubleArrayAttr -dt doubleArray;
addAttr -ln pointArrayAttr -dt pointArray;
addAttr -ln vectorArrayAttr -dt vectorArray;
addAttr -ln stringArrayAttr -dt stringArray;
addAttr -ln stringAttr -dt "string";
addAttr -ln matrixAttr -dt "matrix";
addAttr -ln sphereAttr -dt sphere;
addAttr -ln coneAttr -dt cone;
addAttr -ln meshAttr -dt mesh;
addAttr -ln latticeAttr -dt lattice;
addAttr -ln spectrumRGBAttr -dt spectrumRGB;
addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
addAttr -ln componentListAttr -dt componentList;
addAttr -ln attrAliasAttr -dt attributeAlias;
addAttr -ln curveAttr -dt nurbsCurve;
addAttr -ln surfaceAttr -dt nurbsSurface;
addAttr -ln trimFaceAttr -dt nurbsTrimface;
addAttr -ln polyFaceAttr -dt polyFaces;
-type short2
Array of two short integers
Value Syntax short short
Value Meaning value1 value2
Mel Example setAttr node.short2Attr -type short2 1 2;
Python Example cmds.setAttr('node.short2Attr',1,2,type='short2')
-type short3
Array of three short integers
Value Syntax short short short
Value Meaning value1 value2 value3
Mel Example setAttr node.short3Attr -type short3 1 2 3;
Python Example cmds.setAttr('node.short3Attr',1,2,3,type='short3')
-type long2
Array of two long integers
Value Syntax long long
Value Meaning value1 value2
Mel Example setAttr node.long2Attr -type long2 1000000 2000000;
Python Example cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')
-type long3
Array of three long integers
Value Syntax long long long
Value Meaning value1 value2 value3
Mel Example setAttr node.long3Attr -type long3 1000000 2000000 3000000;
Python Example cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')
-type Int32Array
Variable length array of long integers
Value Syntax int {int}
Value Meaning numberOfArrayValues {arrayValue}
Mel Example setAttr node.int32ArrayAttr -type Int32Array 2 12 75;
Python Example cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')
-type float2
Array of two floats
Value Syntax float float
Value Meaning value1 value2
Mel Example setAttr node.float2Attr -type float2 1.1 2.2;
Python Example cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')
-type float3
Array of three floats
Value Syntax float float float
Value Meaning value1 value2 value3
Mel Example setAttr node.float3Attr -type float3 1.1 2.2 3.3;
Python Example cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')
-type double2
Array of two doubles
Value Syntax double double
Value Meaning value1 value2
Mel Example setAttr node.double2Attr -type double2 1.1 2.2;
Python Example cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')
-type double3
Array of three doubles
Value Syntax double double double
Value Meaning value1 value2 value3
Mel Example setAttr node.double3Attr -type double3 1.1 2.2 3.3;
Python Example cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')
-type doubleArray
Variable length array of doubles
Value Syntax int {double}
Value Meaning numberOfArrayValues {arrayValue}
Mel Example setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;
Python Example cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,), type="doubleArray")
-type matrix
4x4 matrix of doubles
Value Syntax double double double double
double double double double
double double double double
double double double double
Value Meaning row1col1 row1col2 row1col3 row1col4
row2col1 row2col2 row2col3 row2col4
row3col1 row3col2 row3col3 row3col4
row4col1 row4col2 row4col3 row4col4
Alternate Syntax string double double double
double double double
integer
double double double
double double double
double double double
double double double
double double double
double double double
double double double double
double double double double
double double double
boolean
Alternate Meaning "xform" scaleX scaleY scaleZ
rotateX rotateY rotateZ
rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)
translateX translateY translateZ
shearXY shearXZ shearYZ
scalePivotX scalePivotY scalePivotZ
scaleTranslationX scaleTranslationY scaleTranslationZ
rotatePivotX rotatePivotY rotatePivotZ
rotateTranslationX rotateTranslationY rotateTranslationZ
rotateOrientW rotateOrientX rotateOrientY rotateOrientZ
jointOrientW jointOrientX jointOrientY jointOrientZ
inverseParentScaleX inverseParentScaleY inverseParentScaleZ
compensateForParentScale
Mel Example setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;
setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;
Python Example cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')
cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),
(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")
-type pointArray
Variable length array of points
Value Syntax int {double double double double}
Value Meaning numberOfArrayValues {xValue yValue zValue wValue}
Mel Example setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;
Python Example cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')
-type vectorArray
Variable length array of vectors
Value Syntax int {double double double}
Value Meaning numberOfArrayValues {xValue yValue zValue}
Mel Example setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;
Python Example cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')
-type "string"
Character string
Value Syntax string
Value Meaning characterStringValue
Mel Example setAttr node.stringAttr -type "string" "blarg";
Python Example cmds.setAttr('node.stringAttr',"blarg",type="string")
-type stringArray
Variable length array of strings
Value Syntax int {string}
Value Meaning numberOfArrayValues {arrayValue}
Mel Example setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";
Python Example cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')
-type sphere
Sphere data
Value Syntax double
Value Meaning sphereRadius
Example setAttr node.sphereAttr -type sphere 5.0;
-type cone
Cone data
Value Syntax double double
Value Meaning coneAngle coneCap
Mel Example setAttr node.coneAttr -type cone 45.0 5.0;
Python Example cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')
-type reflectanceRGB
Reflectance data
Value Syntax double double double
Value Meaning redReflect greenReflect blueReflect
Mel Example setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;
Python Example cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')
-type spectrumRGB
Spectrum data
Value Syntax double double double
Value Meaning redSpectrum greenSpectrum blueSpectrum
Mel Example setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;
Python Example cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')
-type componentList
Variable length array of components
Value Syntax int {string}
Value Meaning numberOfComponents {componentName}
Mel Example setAttr node.componentListAttr -type componentList 3 cv[1] cv[12] cv[3];
Python Example cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')
-type attributeAlias
String alias data
Value Syntax string string
Value Meaning newAlias currentName
Mel Example setAttr node.attrAliasAttr -type attributeAlias
{"GoUp", "translateY", "GoLeft", "translateX"};
Python Example cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY",
"GoLeft", "translateX"),type='attributeAlias')
-type nurbsCurve
NURBS curve data
Value Syntax int int int bool int int {double}
int {double double double}
Value Meaning degree spans form isRational dimension knotCount {knotValue}
cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}
Mel Example // degree is the degree of the curve(range 1-7)
// spans is the number of spans
// form is open (0), closed (1), periodic (2)
// dimension is 2 or 3, depending on the dimension of the curve
// isRational is true if the curve CVs contain a rational component
// knotCount is the size of the knot list
// knotValue is a single entry in the knot list
// cvCount is the number of CVs in the curve
// xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.
// zCVValue is only present when dimension is 3.
// wCVValue is only present when isRational is true.
//
setAttr node.curveAttr -type nurbsCurve 3 1 0 no 3
6 0 0 0 1 1 1
4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;
-type nurbsSurface
NURBS surface data
Value Syntax int int int int bool
int {double}
int {double}
[string] int {double double double}
Value Meaning uDegree vDegree uForm vForm isRational
uKnotCount {uKnotValue}
vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue zCVValue [wCVValue]}
Example // uDegree is degree of the surface in U direction (range 1-7)
// vDegree is degree of the surface in V direction (range 1-7)
// uForm is open (0), closed (1), periodic (2) in U direction
// vForm is open (0), closed (1), periodic (2) in V direction
// isRational is true if the surface CVs contain a rational component
// uKnotCount is the size of the U knot list
// uKnotValue is a single entry in the U knot list
// vKnotCount is the size of the V knot list
// vKnotValue is a single entry in the V knot list
// If "TRIM" is specified then additional trim information is expected
// If "NOTRIM" is specified then the surface is not trimmed
// cvCount is the number of CVs in the surface
// xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.
// zCVValue is only present when dimension is 3.
// wCVValue is only present when isRational is true
//
setAttr node.surfaceAttr -type nurbsSurface 3 3 0 0 no
6 0 0 0 1 1 1
6 0 0 0 1 1 1
16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0
-1 3 0 -1 1 0 -1 -1 0 -1 -3 0
1 3 0 1 1 0 1 -1 0 1 -3 0
3 3 0 3 1 0 3 -1 0 3 -3 0;
-type nurbsTrimface
NURBS trim face data
Value Syntax bool int {int {int {int int int} int {int int}}}
Value Meaning flipNormal boundaryCount {boundaryType tedgeCountOnBoundary
{splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}
{splineCountOnPedge {isMonotone pedgeTolerance}}}
Example // flipNormal if true turns the surface inside out
// boundaryCount: number of boundaries
// boundaryType:
// tedgeCountOnBoundary : number of edges in a boundary
// splineCountOnEdge : number of splines in an edge in
// edgeTolerance : tolerance used to build the 3d edge
// isEdgeReversed : if true, the edge is backwards
// geometricContinuity : if true, the edge is tangent continuous
// splineCountOnPedge : number of splines in a 2d edge
// isMonotone : if true, curvature is monotone
// pedgeTolerance : tolerance for the 2d edge
//
-type polyFace
Polygon face data
Value Syntax {"f" int {int}}
{"h" int {int}}
{"mf" int {int}}
{"mh" int {int}}
{"mu" int int {int}}
{"fc" int {int}}
Value Meaning {"f" faceEdgeCount {edgeIdValue}}
{"h" holeEdgeCount {edgeIdValue}}
{"mf" faceUVCount {uvIdValue}}
{"mh" holeUVCount {uvIdValue}}
{"mu" uvSet faceUVCount {uvIdValue}}
{"fc" faceColorCount {colorIndexValue}}
Example // This data type (polyFace) is meant to be used in file I/O
// after setAttrs have been written out for vertex position
// arrays, edge connectivity arrays (with corresponding start
// and end vertex descriptions), texture coordinate arrays and
// color arrays. The reason is that this data type references
// all of its data through ids created by the former types.
//
// "f" specifies the ids of the edges making up a face -
// negative value if the edge is reversed in the face
// "h" specifies the ids of the edges making up a hole -
// negative value if the edge is reversed in the face
// "mf" specifies the ids of texture coordinates (uvs) for a face.
// This data type is obsolete as of version 3.0. It is replaced by "mu".
// "mh" specifies the ids of texture coordinates (uvs) for a hole
// This data type is obsolete as of version 3.0. It is replaced by "mu".
// "mu" The first argument refers to the uv set. This is a zero-based
// integer number. The second argument refers to the number of vertices (n)
// on the face which have valid uv values. The last n values are the uv
// ids of the texture coordinates (uvs) for the face. These indices
// are what used to be represented by the "mf" and "mh" specification.
// There may be more than one "mu" specification, one for each unique uv set.
// "fc" specifies the color index values for a face
//
setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "fc" 3 4 4 6;
-type mesh
Polygonal mesh
Value Syntax {string [int {double double double}]}
{string [int {double double double}]}
[{string [int {double double}]}]
{string [int {double double string}]}
Value Meaning "v" [vertexCount {vertexX vertexY vertexZ}]
"vn" [normalCount {normalX normalY normalZ}]
["vt" [uvCount {uValue vValue}]]
"e" [edgeCount {startVertex endVertex "smooth"|"hard"}]
Example // "v" specifies the vertices of the polygonal mesh
// "vn" specifies the normal of each vertex
// "vt" is optional and specifies a U,V texture coordinate for each vertex
// "e" specifies the edge connectivity information between vertices
//
setAttr node.meshAttr -type mesh "v" 3 0 0 0 0 1 0 0 0 1
"vn" 3 1 0 0 1 0 0 1 0 0
"vt" 3 0 0 0 1 1 0
"e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard";
-type lattice
Lattice data
Value Syntax int int int int {double double double}
Value Meaning sDivisionCount tDivisionCount uDivisionCount
pointCount {pointX pointY pointZ}
Example // sDivisionCount is the horizontal lattice division count
// tDivisionCount is the vertical lattice division count
// uDivisionCount is the depth lattice division count
// pointCount is the total number of lattice points
// pointX,pointY,pointZ is one lattice point. The list is
// specified varying first in S, then in T, last in U so the
// first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
//
setAttr node.latticeAttr -type lattice 2 5 2 20
-2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2
2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2
-2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2
2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;

    """
    pass
    


def setAttrMapping(axis="string", clutch="string", selection=bool, offset=float, absolute=bool, relative=bool, attribute="string", scale=float, device="string"):
    """
    setAttrMapping is undoable, queryable, and NOT editable.
    

    
This command applies an offset and scale to a specified device attachment. This command is different than the setInputDeviceMapping command, which applies a mapping to a device axis.
The value from the device is multiplied by the scale and the offset is added to this product. With an absolute mapping, the attached attribute gets the resulting value. If the mapping is relative, the resulting value is added to the previous calculated value. The calculated value will also take into account the setInputDeviceMapping, if it was defined.
As an example, if the space ball is setup with absolute attachment mappings, pressing in one direction will cause the attached attribute to get a constant value. If a relative mapping is used, and the spaceball is pressed in one direction, the attached attribute will get a constantly increasing (or constantly decreasing) value.
Note that the definition of relative is different than the definition used by the setInputDeviceMapping command. In general, both a relative attachment mapping (this command) and a relative device mapping (setInputDeviceMapping) should not be used together one the same axis.

    """
    pass
    


def setDefaultShadingGroup():
    """
    setDefaultShadingGroup is undoable, queryable, and NOT editable.
    

    
The setDefaultShadingGroup command is used to change which shading group is considered the current default shading group. Subsequently created objects will be assigned to the new default group.

    """
    pass
    


def setDrivenKeyframe(objects, hierarchy="string", inTangentType="string", insert=bool, driver=bool, controlPoints=bool, driven=bool, shape=bool, outTangentType="string", driverValue=float, insertBlend=bool, currentDriver="string", attribute="string", value=float):
    """
    setDrivenKeyframe is undoable, queryable, and editable.
    

    
This command sets a driven keyframe. A driven keyframe is similar to a regular keyframe. However, while a standard keyframe always has an x-axis of time in the graph editor, for a drivenkeyframe the user may choose any attribute as the x-axis of the graph editor.

For example, you can keyframe the emission of a faucet so that so that it emits whenever the faucet handle is rotated around y. The faucet emission in this example is called the driven attribute. The handle rotation is called the driver. Once you have used setDrivenKeyframe to set up the relationship between the emission and the rotation, you can go to the graph editor and modify the relationship between the attributes just as you would modify the animation curve on any keyframed object.

In the case of an attribute driven by a single driver, the dependency graph is connected like this:

driver attribute ---> animCurve ---> driven attribute

You can set driven keyframes with more than a single driver. The effects of the multiple drivers are combined together by a blend node.

    """
    pass
    


def setDynamic(setAll=bool, disableAllOnWhenRun=bool, setOff=bool, setOn=bool, allOnWhenRun=bool):
    """
    setDynamic is undoable, NOT queryable, and NOT editable.
    

    
setDynamic sets the isDynamic attribute of particle objects on or off. If no objects are specified, it sets the attribute for any selected objects. If -all is thrown, it sets the attribute for all particle objects in the scene. By default it sets the attribute true (on); if the -off flag is thrown, it sets the attribute false (off).
WARNING: setDynamic is obsolescent. This is the last version of Maya in which it will be supported.

    """
    pass
    


def setEditCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    setEditCtx is undoable, queryable, and editable.
    

    
This command creates a tool that can be used to modify set membership.

    """
    pass
    


def setFluidAttr(reset=bool, floatRandom=float, zIndex=int, clear=bool, addValue=bool, yvalue=bool, lowerFace=bool, vectorRandom=float, yIndex=int, xIndex=int, xvalue=bool, floatValue=float, vectorValue=float, attribute="string", zvalue=bool):
    """
    setFluidAttr is NOT undoable, NOT queryable, and NOT editable.
    

    
Sets values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in the grid.

    """
    pass
    


def setFocus():
    """
    setFocus is undoable, NOT queryable, and NOT editable.
    

    
Give keyboard focus to a specific control or panel, passed as an argument.

    """
    pass
    


def setInfinity(hierarchy="string", preInfinite="string", controlPoints=bool, shape=bool, postInfinite="string", attribute="string"):
    """
    setInfinity is undoable, queryable, and editable.
    

    
Set the infinity type before (after) a paramCurve's first (last) keyframe.

    """
    pass
    


def setInputDeviceMapping(axis="string", relative=bool, view=bool, world=bool, scale=float, absolute=bool, offset=float, device="string"):
    """
    setInputDeviceMapping is undoable, NOT queryable, and NOT editable.
    

    
The command sets a scale and offset for all attachments made to a specified device axis. Any attachment made to a mapped device axis will have the scale and offset applied to its values.
The value from the device is multiplied by the scale and the offset is added to this product. With an absolute mapping, the attached attribute gets the resulting value. If the mapping is relative, the final value is the offset added to the scaled difference between the current device value and the previous device value.
This mapping will be applied to the device data before any mappings defined by the setAttrMapping command. A typical use would be to scale a device's input so that it is within a usable range. For example, the device mapping can be used to calibrate a spaceball to work in a specific section of a scene.
As an example, if the space ball is setup with absolute device mappings, constantly pressing in one direction will cause the attached attribute to get a constant value. If a relative mapping is used, and the spaceball is pressed in one direction, the attached attribute will jump a constantly increasing (or constantly decreasing) value and will find a rest value equal to the offset.
There are important differences between how the relative flag is handled by this command and the setAttrMapping command. (See the setAttrMapping documentation for specifics on how it calculates relative values). In general, both a relative device mapping (this command) and a relative attachment mapping (setAttrMapping) should not be used together on the same axis.

    """
    pass
    


def setKeyCtx(image1="string", breakdown=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    setKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to set keys within the graph editor

    """
    pass
    


def setKeyframe(objects, useCurrentLockedWeights=bool, hierarchy="string", controlPoints=bool, identity=bool, insert=bool, animLayer="string", dirtyDG=bool, respectKeyable=bool, minimizeRotation=bool, insertBlend=bool, value=float, float=float, animated=bool, inTangentType="string", time=(), shape=bool, attribute="string", clip="string", noResolve=bool, outTangentType="string", breakdown=bool):
    """
    setKeyframe is undoable, queryable, and editable.
    

    
This command creates keyframes for the specified objects, or the active objects if none are specified on the command line.
The default time for the new keyframes is the current time. Override this behavior with the "-t" flag on the command line.
The default value for the keyframe is the current value of the attribute for which a keyframe is set. Override this behavior with the "-v" flag on the command line.
When setting keyframes on animation curves that do not have "time" as an input attribute (ie, they are unitless animation curves), use "-f/-float" to specify the unitless value at which to set a keyframe.
The -time and -float flags may be combined in one command.
This command sets up Dependency Graph relationships for proper evaluation of a given attribute at a given time.

    """
    pass
    


def setKeyframeBlendshapeTargetWts():
    """
    setKeyframeBlendshapeTargetWts is undoable, NOT queryable, and NOT editable.
    

    
This command can be used to keyframe per-point blendshape target weights. It operates on the currently selected objects as follows. When the base object is selected, then the target weights are keyed for all targets. When only target shapes are selected, then the weights for thoses targets are keyframed.

    """
    pass
    


def setKeyPath(object):
    """
    setKeyPath is undoable, NOT queryable, and NOT editable.
    

    
The setKeyPath command either creates or edits the path (a nurbs curve) based on the current position of the selected object at the current time.

    """
    pass
    


def setMenuMode(string):
    """
    setMenuMode is NOT undoable, NOT queryable, and NOT editable.
    

    
Optionally sets a new Menu Mode for the menu bar in the main Maya window. Returns the current Menu Mode, and if a new one is specified, then the previous Menu Mode is returned. Note that due to recent changes to the menu set architecture (8.0+), this function now takes a menu set as a parameter instead of a label.

    """
    pass
    


def setNodeTypeFlag(string, threadSafe=bool, display=bool):
    """
    setNodeTypeFlag is undoable, queryable, and NOT editable.
    

    
This command sets static data on the specified node type. This will affect the class of node type as a whole. The argument passed may be the name of the node type or the node type tag. Node type tags may be found using the objectType command.

    """
    pass
    


def setParent(string, defineTemplate="string", topLevel=bool, useTemplate="string", menu=bool, upLevel=bool):
    """
    setParent is undoable, queryable, and NOT editable.
    

    
This command changes the default parent to be the specified parent. Two special parents are "|" which indicates the top level layout of the window hierarchy, or ".." which indicates one level up in the hierarchy. Trying to move above the top level has no effect.
A control must be parented to a control layout. A control layout may be parented to another control layout or a window. A menu may be parented to a window or a menu bar layout. For all of these cases the setParent command (with no flags) will indicate the current default parent.
A menu item must be parented to a menu. To specify the default menu parent use the command setParent -m/menu. Note that all menu item objects created using the -sm/subMenu may also be treated as menu objects.
The default parent is ignored by any object that explicitly sets the -p/parent flag when it is created.

    """
    pass
    


def setParticleAttr(randomVector=float, object="string", relative=bool, floatValue=float, randomFloat=float, attribute="string", vectorValue=float):
    """
    setParticleAttr is undoable, NOT queryable, and NOT editable.
    

    
This action will set the value of the chosen attribute for every particle or selected component in the selected or passed particle object. Components should not be passed to the command line. For setting the values of components, the components must be selected and only the particle object's names should be passed to this action. If the attribute is a vector attribute and the -vv flag is passed, then the three floats passed will be used to set the values. If the attribute is a vector and the -fv flag is pass and the -vv flag is not passed, then the float will be repeated for each of the X, Y, and Z values of the attribute. Similarly, if the attribute is a float attribute and a vector value is passed, then the length of the vector passed will be used for the value. Note: The attribute passed must be a Per-Particle attribute.

    """
    pass
    


def setRenderPassType(defaultDataType=bool, type="string", numChannels=int):
    """
    setRenderPassType is undoable, NOT queryable, and NOT editable.
    

    
This command will set the passID of a renderPass node and create the custom attributes specified by the corresponding render pass definition. If the render pass node already has a passID assigned to it, attributes that are no longer required become hidden, and new attributes are unhidden and/or created as needed. This allows passIDs to be changed back and forth without losing attribute data. It also allows common attributes to be transported from one render pass type to another.

    """
    pass
    


def sets(split="string", edges=bool, subtract="string", flatten="string", intersection="string", isIntersecting="string", renderable=bool, include="string", text="string", isMember="string", noSurfaceShader=bool, noWarnings=bool, name="string", layer=bool, union="string", size=bool, addElement="string", vertices=bool, editPoints=bool, forceElement="string", clear="string", color=int, empty=bool, nodesOnly=bool, facets=bool, copy="string", afterFilters=bool, remove="string"):
    """
    sets is undoable, queryable, and editable.
    

    
This command is used to create a set, query some state of a set, or perform operations to update the membership of a set. A set is a logical grouping of an arbitrary collection of objects, attributes, or components of objects. Sets are dependency nodes. Connections from objects to a set define membership in the set.
Sets are used throughout Maya in a multitude of ways. They are used to define an association of material properties to objects, to define an association of lights to objects, to define a bookmark or named collection of objects, to define a character, and to define the components to be deformed by some deformation operation.
Sets can be connected to any number of partitions. A partition is a node which enforces mutual exclusivity amoung the sets in the partition. That is, if an object is in a set which is in a partition, that object cannot be a member of any other set that is in the partition.
Without any flags, the sets command will create a set with a default name of "set#" (where # is an integer). If no items are specified on the command line, the currently selected items are added to the set. The -em/empty flag can be used to create an empty set and not have the selected items added to the set.
Sets can be created to have certain restrictions on membership. There can be "renderable" sets which only allow renderable objects (such as nurbs geometry or polymesh faces) to be members of the set. There can also be vertex (or control point), edit point, edge, or face sets which only allow those types of components to be members of a set. Note that for these sets, if an object with a valid type of component is to be added to a set, the components of the object are added to the set instead.
Sets can have an associated color which is only of use when creating vertex sets. The color can be one of the eight user defined colors defined in the color preferences. This color can be used, for example to distinguish which vertices are being deformed by a particular deformation.
Objects, components, or attributes can be added to a set using one of three flags. The -add/addElement flag will add the objects to a set as long as this won't break any mutual exclusivity constraints. If there are any items which can't be added, the command will fail. The -in/include flag will only add those items which can be added and warn of those which can't. The -fe/forceElement flag will add all the items to the set but will also remove any of those items that are in any other set which is in the same partition as the set.
There are several operations on sets that can be performed with the sets command. Membership can be queried. Tests for whether an item is in a set or whether two sets share the same item can be performed. Also, the union, intersection and difference of sets can be performed which returns a list of members of the sets which are a result of the operation.

    """
    pass
    


def setStartupMessage():
    """
    setStartupMessage is undoable, NOT queryable, and NOT editable.
    

    
Update the startup window message. Also know as the 'Splash Screen', this is the window that appears while the application is starting up.

    """
    pass
    


def setToolTo(string):
    """
    setToolTo is undoable, NOT queryable, and NOT editable.
    

    
This command switches control to the named context.

    """
    pass
    


def setUITemplate(string, popTemplate=bool, pushTemplate=bool):
    """
    setUITemplate is undoable, queryable, and NOT editable.
    

    
This command sets the current(default) command template for the ELF commands. The special name NONE can be used to set no templates current. See "uiTemplate" command also.

    """
    pass
    


def setXformManip(worldSpace=bool, suppress=bool, useRotatePivot=bool, showUnits=bool):
    """
    setXformManip is undoable, queryable, and NOT editable.
    

    
This command changes some of the settings of the xform manip, to control its appearance.

    """
    pass
    


def shadingConnection(connectionState=bool):
    """
    shadingConnection is undoable, queryable, and editable.
    

    
Sets the connection state of a connection between nodes that are used in shading. Specify the destination attribute of the connection.

    """
    pass
    


def shadingGeometryRelCtx(offCommand="string", image1="string", onCommand="string", shadingCentric=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    shadingGeometryRelCtx is undoable, queryable, and editable.
    

    
This command creates a context that can be used for associating geometry to shading groups. You can put the context into shading-centric mode by using the -shadingCentric flag and specifying true. This means that the shading group is selected first then geometry associated with the shading group are highlighted. Subsequent selections result in assignments.
Specifying -shadingCentric false means that the geometry is to be selected first. The shading group associated with the geometry will then be selected and subsequent selections will result in assignments being made.

    """
    pass
    


def shadingLightRelCtx(offCommand="string", image1="string", onCommand="string", shadingCentric=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    shadingLightRelCtx is undoable, queryable, and editable.
    

    
This command creates a context that can be used for associating lights to shading groups. You can put the context into shading-centric mode by using the -shadingCentric flag and specifying true. This means that the shading group is selected first then lights associated with the shading group are highlighted. Subsequent selections result in assignments.
Specifying -shadingCentric false means that the light is to be selected first. The shading groups associated with the light will then be selected and subsequent selections will result in assignments being made.

    """
    pass
    


def shadingNetworkCompare(network2=bool, delete=bool, byName=bool, byValue=bool, upstreamOnly=bool, network1=bool, equivalent=bool):
    """
    shadingNetworkCompare is NOT undoable, queryable, and NOT editable.
    

    
This command allows you to compare two shading networks.

    """
    pass
    


def shadingNode(skipSelect=bool, asTexture=bool, asUtility=bool, asLight=bool, parent="string", asPostProcess=bool, name="string", asShader=bool, asRendering=bool, shared=bool, isColorManaged=bool):
    """
    shadingNode is undoable, NOT queryable, and NOT editable.
    

    
This command creates a new node in the dependency graph of the specified type.
The shadingNode command classifies any DG node as a shader, texture light, post process, or utility so that it can be properly organized in the multi-lister. Recall that any DG node can be used a part of a a shader, texture or light - regardless of how it is classified by this. command. These classifications are provided for convenience in the UI.

    """
    pass
    


def shapeCompare(objectobject):
    """
    shapeCompare is undoable, NOT queryable, and NOT editable.
    

    
Compares two shapes. If no shapes are specified in the command line, then the shapes from the active list are used.

    """
    pass
    


def shapeEditor(panel="string", docTag="string", verticalSliders=bool, control=bool, mainListConnection="string", defineTemplate="string", parent="string", unParent=bool, highlightConnection="string", unlockMainConnection=bool, useTemplate="string", filter="string", lockMainConnection=bool, selectionConnection="string", targetList=bool, stateString=bool, exists=bool, updateMainConnection=bool, forceMainConnection="string", targetControlList=bool):
    """
    shapeEditor is undoable, queryable, and editable.
    

    
This command creates an editor that derives from the base editor class that has controls for deformer, control nodes.

    """
    pass
    


def shapePanel(tearOff=bool, docTag="string", isUnique=bool, control=bool, tearOffRestore=bool, defineTemplate="string", parent="string", createString=bool, unParent=bool, needsInit=bool, useTemplate="string", init=bool, label="string", replacePanel="string", popupMenuProcedure="string", editString=bool, copy="string", shapeEditor=bool, exists=bool, menuBarVisible=bool, tearOffCopy="string"):
    """
    shapePanel is undoable, queryable, and editable.
    

    
This command creates a panel that derives from the base panel class that houses a shapeEditor.

    """
    pass
    


def shelfButton(string, docTag="string", highlightImage="string", height=int, useAlpha=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", highlightColor=float, image3="string", dragCallback="string", imageOverlayLabel="string", overlayLabelBackColor=float, disabledImage="string", noDefaultPopup=bool, annotation="string", enable=bool, scaleIcon=bool, image1="string", popupMenuArray=bool, menuItem="string", handleNodeDropCallback="string", labelOffset=int, flipX=bool, font="string", exists=bool, rotation=float, flipY=bool, marginHeight=int, ltVersion="string", doubleClickCommand="string", menuItemPython=int, commandRepeatable=bool, visibleChangeCommand="string", visible=bool, labelEditingCallback="string", marginWidth=int, sourceType="string", preventOverride=bool, fullPathName=bool, enableCommandRepeat=bool, dropCallback="string", noBackground=bool, selectionImage="string", backgroundColor=float, enableBackground=bool, align="string", manage=bool, command="string", flat=bool, style="string", version="string", image2="string", isObscured=bool, overlayLabelColor=float):
    """
    shelfButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextButton that is designed to be on the shelf. The button contains a command that can be drag'n'dropped.

    """
    pass
    


def shelfLayout(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", manage=bool, dragCallback="string", numberOfChildren=bool, highlightColor=float, annotation="string", cellWidthHeight=int, preventOverride=bool, popupMenuArray=bool, width=int, childArray=bool, cellHeight=int, version="string", exists=bool, enable=bool, ltVersion="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", alignment="string", noBackground=bool, backgroundColor=float, cellWidth=int, position="string", style="string", spacing=int, isObscured=bool):
    """
    shelfLayout is undoable, queryable, and editable.
    

    
This command creates a new empty shelf layout. The shelf layout can accept drops of commands scripts. Use addNewShelfTab MEL command to add a shelf in top level shelves.

    """
    pass
    


def shelfTabLayout(string, docTag="string", height=int, childResizable=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", selectTabIndex=int, width=int, dragCallback="string", numberOfChildren=bool, highlightColor=float, scrollable=bool, tabsVisible=bool, annotation="string", enable=bool, horizontalScrollBarThickness=int, preventOverride=bool, selectTab="string", popupMenuArray=bool, preSelectCommand="string", enableBackground=bool, verticalScrollBarThickness=int, childArray=bool, innerMarginHeight=int, exists=bool, changeCommand="string", imageVisible=bool, innerMarginWidth=int, doubleClickCommand="string", visibleChangeCommand="string", visible=bool, showNewTab=bool, tabLabel="string", moveTab=int, fullPathName=bool, dropCallback="string", selectCommand="string", noBackground=bool, backgroundColor=float, minChildWidth=int, manage=bool, scrollableTabs=bool, borderStyle="string", tabsClosable=bool, tabLabelIndex=int, isObscured=bool, newTabCommand="string"):
    """
    shelfTabLayout is undoable, queryable, and editable.
    

    
This command creates/edits/queries a shelf tab group which is essentially a normal tabLayout with some drop behaviour in the tab bar. A garbage can icon can appear in the top right corner to dispose of buttons dragged to it from shelves.

    """
    pass
    


def shot(clipZeroOffset=(), flag1=bool, pasteInstance=bool, shotName="string", favorite=bool, flag10=bool, scale=float, mute=bool, flag8=bool, linkAudio="string", copy=bool, sourceDuration=(), postHoldTime=(), unlinkAudio=bool, deleteCustomAnim=bool, hasStereoCamera=bool, flag6=bool, clipSyncState=bool, flag2=bool, track=int, audio="string", clipOpacity=float, flag7=bool, transitionOutLength=(), startTime=(), transitionOutType=int, paste=bool, customAnim=bool, sequenceDuration=(), createCustomAnim=bool, transitionInLength=(), hasCameraSet=bool, flag3=bool, clip="string", flag12=bool, flag11=bool, sequenceStartTime=(), determineTrack=bool, currentCamera="string", selfmute=bool, flag4=bool, flag9=bool, lock=bool, clipDuration=(), flag5=bool, preHoldTime=(), transitionInType=int, endTime=(), sequenceEndTime=()):
    """
    shot is undoable, queryable, and editable.
    

    
Use this command to create a shot node or manipulate that node.

    """
    pass
    


def shotRipple(endTime=(), startDelta=(), deleted=bool, startTime=(), endDelta=()):
    """
    shotRipple is undoable, queryable, and editable.
    

    
When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated are moved in sequence time to either make way or close up gaps corresponding to that node's editing. Given some parameters about the shot edit that just took place, this command will choose which other shots to move, and move them the appropriate amounts If no shot name is provided, the command will attempt to use the first selected shot.

    """
    pass
    


def shotTrack(solo=bool, selfmute=bool, insertTrack=int, track=int, lock=bool, removeTrack=int, mute=bool, title="string", numTracks=int, removeEmptyTracks=bool, swapTracks=int, unsolo=bool):
    """
    shotTrack is undoable, queryable, and editable.
    

    
This command is used for inserting and removing tracks related to the shots displayed in the Sequencer. It can also be used to modify the track state, for example, to lock or mute a track.

    """
    pass
    


def showHelp(string, version=bool, docs=bool, helpTable=bool, absolute=bool):
    """
    showHelp is NOT undoable, queryable, and NOT editable.
    

    
Invokes a web browser to open the on-line documentation and help files. It will open the help page for a given topic, or open a browser to a specific URL.

    """
    pass
    


def showHidden(objects, allObjects=bool, below=bool, lastHidden=bool, above=bool):
    """
    showHidden is undoable, NOT queryable, and NOT editable.
    

    
The showHidden command is used to make invisible objects visible. If no flags are specified, only the objects given to the command will be made visible. If a parent of an object is invisible, the object will still be invisible. Invisibility is inherited. To ensure the object becomes visible, use the -a/above flag. This forces all invisible ancestors of the object(s) to be visible. If the -b/below flag is used, any invisible objects below the object will be made visible. To make all objects visible, use the -all/allObjects flag.
See also: hide

    """
    pass
    


def showManipCtx(toolStart="string", image1="string", currentNodeName=bool, incSnapUI=bool, name="string", toggleIncSnap=bool, toolFinish="string", incSnapValue=int, lockSelection=bool, incSnap=int, image3="string", exists=bool, image2="string", incSnapRelative=int, history=bool):
    """
    showManipCtx is undoable, queryable, and editable.
    

    
This command can be used to create a show manip context. The show manip context will display manips for all selected objects that have valid manips defined for them.

    """
    pass
    


def showMetadata(off=bool, listVisibleStreams=bool, method="string", stream="string", interpolation=bool, listMembers=bool, auto=bool, listAllStreams=bool, rayScale=float, isActivated=bool, listValidMethods=bool, dataType="string", member="string", range=float):
    """
    showMetadata is undoable, queryable, and NOT editable.
    

    
This command is used to show metadata values which is in the specified channels "vertex", "edge", "face", and "vertexFace" in the viewport. You can view the data by three ways:
"color": draw color on the components.
"ray": draw a ray on the components.
"string": draw 2d strings on the components.
For example, if the metadata of "shape.vtx[1]" is (1, 0, 0), you can turn on the visualization with all three modes. On "color" mode, you can see a red vertex which is on the position of "shape.vtx[1]". On "ray" mode, you can see a ray with the direction (1, 0, 0). On "string" mode, you can see strings "1 0 0" below the vertex in the viewport.
To use "color" or "ray" mode, you should make the member of the data structure with three or less items, such as float[3]. The three items are mapped to "RGB" as a color, or "XYZ" as a vector. The structure with two items works similarly. The only difference is that the third value will always be zero. However, if the structure has only one item, the value is mapped to all three variables. That means if the structure is "int" and its value is 1, the color will be white(1, 1, 1) and the vector will be (1, 1, 1).
You can get the current status of the flags on the query mode (using "-query"). But you can query only the status of one flag in a single command and you cannot set values on the query mode.
You can use the command on some specified objects, or run it with no arguments to make changes on all objects in the scene. The object must be a mesh shape. Components are not allowed as the command arguments.

    """
    pass
    


def showSelectionInTitle(string):
    """
    showSelectionInTitle is undoable, NOT queryable, and NOT editable.
    

    
This command causes the title of the window specified as an argument to be linked to the current file and selection. When selection changes, the window title will change to show the current file name and the name of the last selected object.

    """
    pass
    


def showShadingGroupAttrEditor():
    """
    showShadingGroupAttrEditor is undoable, queryable, and NOT editable.
    

    
The showShadingGroupAttrEditor command opens up the attribute editor for the current object's shading-group information.

    """
    pass
    


def showWindow(string):
    """
    showWindow is undoable, NOT queryable, and NOT editable.
    

    
Make a window visible. If no window is specified then the current window (most recently created) is used. See also the window command's vis/visible flag.
If the specified window is iconified, it will be opened.

    """
    pass
    


def simplify(time=(), hierarchy="string", floatTolerance=float, float=(), includeUpperBound=bool, controlPoints=bool, shape=bool, timeTolerance=(), valueTolerance=float, attribute="string", animation="string", index=int):
    """
    simplify is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command will simplify (reduce the number of keyframes) an animation curve.

    """
    pass
    


def singleProfileBirailSurface(transformMode=int, polygon=int, object=bool, nodeState=int, constructionHistory=bool, tangentContinuityProfile1=bool, caching=bool, name="string"):
    """
    singleProfileBirailSurface is undoable, queryable, and editable.
    

    
This cmd creates a railed surface by sweeping the profile curve along the two rail curves. One of the requirements for surface creation is the profile curve must intersect the two rail curves. If the profile is a surface curve i.e. isoparm, curve on surface or trimmed edge then tangent continuity across the surface underlying the profile may be enabled using the flag -tp1 true.
The first argument represetns the profile curve, the second and third the rails.

    """
    pass
    


def skeletonEmbed(segmentationResolution=int, segmentationMethod=int, mergedMesh=bool):
    """
    skeletonEmbed is undoable, queryable, and NOT editable.
    

    
This command is used to embed a skeleton inside meshes.

    """
    pass
    


def skinBindCtx(symmetry=bool, image1="string", axis="string", currentInfluence="string", image2="string", about="string", displayNormalized=bool, history=bool, displayInactiveMode=int, exists=bool, tolerance=float, falloffCurve="string", colorRamp="string", name="string", image3="string"):
    """
    skinBindCtx is undoable, queryable, and editable.
    

    
This command creates a tool that can be used to edit volumes from an interactive bind.

    """
    pass
    


def skinCluster(dropoffRate=float, before=bool, exclusive="string", split=bool, after=bool, smoothWeights=float, ignoreSelected=bool, nurbsSamples=int, ignoreHierarchy=bool, ignoreBindPose=bool, includeHiddenSelections=bool, weightDistribution=int, smoothWeightsMaxIterations=int, frontOfChain=bool, prune=bool, weight=float, normalizeWeights=int, baseShape="string", volumeType=int, skinMethod=int, heatmapFalloff=float, obeyMaxInfluences=bool, unbind=bool, removeInfluence="string", volumeBind=float, geometry="string", useGeometry=bool, name="string", unbindKeepHistory=bool, weightedInfluence=bool, moveJointsMode=bool, removeUnusedInfluence=bool, influence="string", bindMethod=int, parallel=bool, forceNormalizeWeights=bool, addInfluence="string", geometryIndices=bool, polySmoothness=float, afterReference=bool, remove=bool, maximumInfluences=int, selectInfluenceVerts="string", addToSelection=bool, lockWeights=bool, deformerTools=bool, removeFromSelection=bool, recacheBindMatrices=bool, toSkeletonAndTransforms=bool, toSelectedBones=bool):
    """
    skinCluster is undoable, queryable, and editable.
    

    
The skinCluster command is used for smooth skinning in maya. It binds the selected geometry to the selected joints or skeleton by means of a skinCluster node. Each point of the bound geometry can be affected by any number of joints. The extent to which each joint affects the motion of each point is regulated by a corresponding weight factor. Weight factors can be modified using the skinPercent command. The command returns the name of the new skinCluster.
The skinCluster binds only a single geometry at a time. Thus, to bind multiple geometries, multiple skinCluster commands must be issued.
Upon creation of a new skinCluster, the command can be used to add and remove transforms (not necessarily joints) that influence the motion of the bound skin points.
The skinCluster command can also be used to adjust parameters such as the dropoff, nurbs samples, polygon smoothness on a particular influence object. Note: Any custom weights on a skin point that the influence object affects will be lost after adjusting these parameters.

    """
    pass
    


def skinPercent(objectselectionList, resetToDefault=bool, transform="string", transformMoveWeights="string", transformValue="string", zeroRemainingInfluences=bool, relative=bool, ignoreBelow=float, pruneWeights=float, normalize=bool, value=bool):
    """
    skinPercent is undoable, queryable, and NOT editable.
    

    
This command edits and queries the weight values on members of a skinCluster node, given as the first argument. If no object components are explicitly mentioned in the command line, the current selection list is used.
Note that setting multiple weights in a single invocation of this command is far more efficient than calling it once per weighted vertex.

    """
    pass
    


def smoothCurve(smoothness=float, replaceOriginal=bool, object=bool, nodeState=int, constructionHistory=bool, caching=bool, name="string"):
    """
    smoothCurve is undoable, queryable, and editable.
    

    
The smooth command smooths the curve at the given control points.

    """
    pass
    


def smoothTangentSurface(direction=int, object=bool, nodeState=int, replaceOriginal=bool, constructionHistory=bool, parameter=float, caching=bool, smoothness=int, name="string"):
    """
    smoothTangentSurface is undoable, queryable, and editable.
    

    
The smoothTangentSurface command smooths the surface along an isoparm at each parameter value. The name of the surface is returned and if history is on, the name of the resulting dependency node is also returned. This command only applies to parameter values with a multiple knot value. (If the given parameter value has no multiple knot associated with it, then the dependency node is created but the surface doesn't change.)

When would you use this? If you have a surface consisting of a number of Bezier patches or any isoparms with more than a single knot multiplicity, you could get into a situation where a tangent break occurs. So, it only makes sense to do this operation on the knot isoparms, and not anywhere in between, because the surface is already smooth everywhere in between.

If you have a cubic or higher degree surface, asking for the maximal smoothness will give you tangent, curvature, etc. up to the degree-1 continuity. Asking for tangent will just give you tangent continuity.

It should be mentioned that this is "C", not "G" continuity we're talking about, so technically, you can still see visual tangent breaks if the surface is degenerate.
Note: A single smoothTangentSurface command cannot smooth in both directions at once; you must use two separate commands to do this.

    """
    pass
    


def snapKey(time=(), hierarchy="string", float=(), includeUpperBound=bool, controlPoints=bool, valueMultiple=float, shape=bool, timeMultiple=float, attribute="string", animation="string", index=int):
    """
    snapKey is undoable, NOT queryable, and NOT editable.
    

    
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices can be given individually or as part of a list or range.
-time 10pal means the key at frame 10 (PAL format).
-time 1.0sec -time 15ntsc -time 20 means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
Omitting one end of a range means "go to infinity", as in the following examples:
-time "10:" means all keys from time 10 (in the current time unit) onwards.
-time ":10" means all keys up to (and including) time 10 (in the current time unit).
-time ":" is a short form to specify all keys.
-index 0 means the first key of each animation curve. (Indices are 0-based.)
-index 2 -index 5 -index 7 means the 3rd, 6th, and 8th keys.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
This command "snaps" all target key times and/or values so that they have times and/or values that are multiples of the specified flag arguments. If neither multiple is specified, default is time snapping with a multiple of 1.0. Note that this command will fail to move keys over other neighboring keys: a key's index will not change as a result of a snapKey operation.
TbaseKeySetCmd.h

    """
    pass
    


def snapMode(liveFaceCenter=bool, edgeMagnet=int, pixelCenter=bool, tolerance=int, point=bool, grid=bool, meshCenter=bool, useTolerance=bool, curve=bool, edgeMagnetTolerance=float, pixelSnap=bool, viewPlane=bool, distanceIncrement="string", livePoint=bool, uvTolerance=int):
    """
    snapMode is undoable, queryable, and NOT editable.
    

    
The snapMode command is used to control snapping. It toggles the snapping modes in effect and sets information used for snapping.

    """
    pass
    


def snapshot(objects, startTime=(), name="string", update="string", endTime=(), motionTrail=bool, increment=(), constructionHistory=bool):
    """
    snapshot is undoable, queryable, and editable.
    

    
This command can be used to create either a series of surfaces evaluated at the times specified by the command flags, or a motion trail displaying the trajectory of the object's pivot point at the times specified.
If the constructionHistory flag is true, the output shapes or motion trail will re-update when modifications are made to the animation or construction history of the original shape. When construction history is used, the forceUpdate flag can be set to false to control when the snapshot recomputes, which will typically improve performance.

    """
    pass
    


def snapshotBeadCtx(image1="string", history=bool, outTangent=bool, exists=bool, inTangent=bool, image2="string", name="string", image3="string"):
    """
    snapshotBeadCtx is undoable, queryable, and editable.
    

    
Creates a context for manipulating in and/or out tangent beads on the motion trail

    """
    pass
    


def snapshotModifyKeyCtx(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    snapshotModifyKeyCtx is undoable, queryable, and editable.
    

    
Creates a context for inserting/delete keys on an editable motion trail

    """
    pass
    


def snapTogetherCtx(contextName, image1="string", image3="string", clearSelection=bool, snapPolygonFace=bool, exists=bool, setOrientation=bool, image2="string", name="string", history=bool):
    """
    snapTogetherCtx is undoable, queryable, and editable.
    

    
The snapTogetherCtx command creates a tool for snapping surfaces together.

    """
    pass
    


def soft(goal=float, duplicateHistory=bool, duplicate=bool, convert=bool, hideOriginal=bool, name="string"):
    r"""
    soft is undoable, queryable, and NOT editable.

    
Makes a soft body from the object(s) passed on the command line or in the selection list. The geometry can be a NURBS, polygonal, lattice object. The resulting soft body is made up of a hierarchy with a particle shape and a geometry shape, thus:
                              T    
            / \  
           T   G 
          /      
        P        
                  Dynamics are applied to the particle shape and the resulting particle positions then drive the locations of the geometry's CVs, vertices, or lattice points.
With the convert option, the particle shape and its transform are simply inserted below the original shape's hierarchy. With the duplicate option, the original geometry's transform and shape are duplicated underneath its parent, and the particle shape is placed under the duplicate. Note that any animation on the hierarchy will affect the particle shape as well. If you do not want then, then reparent the structure outside the hierarchy.
When duplicating, the soft portion (the duplicate) is given the name "copyOf" + "original object name". The particle portion is always given the name "original object name" + "Particles."
None of the flags of the soft command can be queried. The soft -q command is used only to identify when an object is a soft body, or when two objects are part of the same soft body. See the examples.

    """
    pass
    


def softMod(objects, before=bool, exclusive="string", after=bool, falloffBasedOnZ=bool, includeHiddenSelections=bool, relative=bool, frontOfChain=bool, falloffCenter=float, falloffRadius=float, prune=bool, geometryIndices=bool, split=bool, falloffBasedOnX=bool, afterReference=bool, envelope=float, bindState=bool, geometry="string", falloffBasedOnY=bool, resetGeometry=bool, curveValue=float, curvePoint=float, ignoreSelected=bool, weightedNode="string", falloffAroundSelection=bool, curveInterpolation=int, remove=bool, deformerTools=bool, parallel=bool, falloffMasking=bool, name="string", falloffMode=int):
    """
    softMod is undoable, queryable, and editable.
    

    
The softMod command creates a softMod or edits the membership of an existing softMod. The command returns the name of the softMod node upon creation of a new softMod.

    """
    pass
    


def softModCtx(image1="string", reset=bool, falseColor=bool, image3="string", exists=bool, dragSlider="string", image2="string"):
    """
    softModCtx is undoable, queryable, and editable.
    

    
Controls the softMod context.

    """
    pass
    


def softSelect(softSelectCurve="string", softSelectFalloff=int, softSelectEnabled=int, enableFalseColor=int, softSelectDistance=float, compressUndo=int, softSelectColorCurve="string", softSelectReset=bool, softSelectUVDistance=float):
    """
    softSelect is undoable, queryable, and editable.
    

    
This command allows you to change the soft modelling options.
Soft modelling is an option that allows for reflection of basic manipulator actions such as move, rotate, and scale.

    """
    pass
    


def soloMaterial(last=bool, node="string", unsolo=bool, attr="string"):
    """
    soloMaterial is undoable, queryable, and NOT editable.
    

    
Shows a preview of a specified material node output attribute.

    """
    pass
    


def sortCaseInsensitive():
    """
    sortCaseInsensitive is NOT undoable, NOT queryable, and NOT editable.
    

    
This command sorts all the strings of an array in a case insensitive way.

    """
    pass
    


def sound(objects, sourceEnd=(), offset=(), length=bool, file="string", mute=bool, endTime=(), sourceStart=(), name="string"):
    """
    sound is undoable, queryable, and editable.
    

    
Creates an audio node which can be used with UI commands such as soundControl or timeControl which support sound scrubbing and sound during playback.

    """
    pass
    


def soundControl(docTag="string", height=int, defineTemplate="string", parent="string", pressCommand="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", repeatOnHold=bool, highlightColor=float, annotation="string", preventOverride=bool, popupMenuArray=bool, repeatChunkSize=float, resample=bool, sound="string", beginScrub=bool, exists=bool, endScrub=bool, maxTime=(), visible=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", minTime=(), releaseCommand="string", fullPathName=bool, waveform="string", dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, displaySound=bool, isObscured=bool):
    """
    soundControl is undoable, queryable, and editable.
    

    
This command creates a control used for changing current time and scratching/scrubbing through sound files.

    """
    pass
    


def spaceLocator(position="string", relative=bool, absolute=bool, name="string"):
    """
    spaceLocator is undoable, queryable, and editable.
    

    
The command creates a locator at the specified position in space. By default it is created at (0,0,0).

    """
    pass
    


def sphere(degree=int, axis="string", pivot="string", sections=int, radius="string", tolerance="string", object=bool, useTolerance=bool, polygon=int, spans=int, nodeState=int, name="string", heightRatio=float, startSweep=int, caching=bool, endSweep=int, constructionHistory=bool):
    """
    sphere is undoable, queryable, and editable.
    

    
The sphere command creates a new sphere. The number of spans in the in each direction of the sphere is determined by the useTolerance attribute. If -ut is true then the -tolerance attribute will be used. If -ut is false then the -sections attribute will be used.

    """
    pass
    


def spotLight(discRadius="string", decayRate=int, softShadow=bool, topBarnDoorAngle=int, leftBarnDoorAngle=int, exclusive=bool, useRayTraceShadows=bool, shadowColor=float, penumbra=int, intensity=float, shadowSamples=int, bottomBarnDoorAngle=int, barnDoors=bool, dropOff=float, rgb=float, shadowDither=float, position="string", rotation=int, rightBarnDoorAngle=int, name="string", coneAngle=int):
    """
    spotLight is undoable, queryable, and editable.
    

    
TlightCmd is the base class for other light commands. TnonAmbientLightCmd is a class that looks like a command but is not. It is a base class for the extended/nonExtended lights. TnonExtendedLightCmd is a base class and not a real command. It is inherited by several lights: TpointLight, TdirectionalLight, TspotLight etc. The spotLight command is used to edit the parameters of existing spotLights, or to create new ones. The default behaviour is to create a new spotlight.

    """
    pass
    


def spotLightPreviewPort(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, spotLight="string", popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", widthHeight=int, exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    spotLightPreviewPort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays an image representing the illumination provided by the spotLight. It is a picture of a plane being illuminated by a light.
The optional argument is the name of the 3dPort.

    """
    pass
    


def spreadSheetEditor(name, allAttr=bool, defineTemplate="string", docTag="string", keyableOnly=bool, useTemplate="string", lockMainConnection=bool, unParent=bool, niceNames=bool, panel="string", longNames=bool, mainListConnection="string", parent="string", highlightConnection="string", execute="string", stateString=bool, exists=bool, updateMainConnection=bool, control=bool, attrRegExp="string", selectionConnection="string", forceMainConnection="string", unlockMainConnection=bool, showShapes=bool, precision=int, selectedAttr=bool, fixedAttrList="string", filter="string"):
    """
    spreadSheetEditor is undoable, queryable, and editable.
    

    
This command creates a new spread sheet editor in the current layout.

    """
    pass
    


def spring(stiffness=float, endForceWeight=float, allPoints=bool, stiffnessPS=float, damping=float, useRestLengthPS=bool, dampingPS=float, exclusive=bool, noDuplicate=bool, name="string", wireframe=bool, length=float, startForceWeight=float, restLength=float, walkLength=int, minDistance=float, count=bool, addSprings=bool, maxDistance=float, restLengthPS=float, minMax=bool, useDampingPS=bool, useStiffnessPS=bool):
    """
    spring is undoable, queryable, and editable.
    

    
The spring command can do any of the following:
* create a new spring object (shape plus transform). The shape contains springs between the points (particles, cvs, etc.) of the objects selected or listed on the command line.
* create new springs and add them to an existing spring object
* edit or query certain attributes of an existing spring object
One "spring object" may have hundreds or even thousands of individual springs. Certain attributes of the spring object specify exactly where the springs are attached to which other objects.
Springs may be attached to the following: particles, vertices of soft bodies, CVs or edit points of curves or surfaces, vertices of polygonal objects, and points of lattices. In the case where one endpoint of a spring is non-dynamic (a CV, edit point, etc.), the spring does not affect its motion, but the motion of the point affects the spring. A spring will be created only if at least one of the endpoints is dynamic: for example, a spring will never be created between two CVs. A single spring object can hold springs which are incident to any number of other objects.
The spring has creation-only flags and editable flags. Creation-only flags (minDistance, maxDistance, add, exclusive, all, wireframe, walklength, checkExisting) can be used only when creating new springs (including adding springs to existing spring object). Editable flags modify attributes of an existing spring object.
If a spring object is created, this command returns the names of the shape and transform. If a spring object is queried, the command returns the results of the query.

    """
    pass
    


def squareSurface(stringstringstringstring, rebuildCurve3=bool, polygon=int, continuityType1=int, curveFitCheckpoints=int, continuityType4=int, name="string", nodeState=int, endPointTolerance="string", continuityType3=int, rebuildCurve4=bool, rebuildCurve1=bool, rebuildCurve2=bool, caching=bool, object=bool, constructionHistory=bool, continuityType2=int):
    """
    squareSurface is undoable, queryable, and editable.
    

    
This command produces a square surface given 3 or 4 curves. This resulting square surface is created within the intersecting region of the selected curves. The order of selection is important and the curves must intersect or their ends must meet.
You must specify one continuity type flag for each selected curve. If continuity type is 1 (fixed, no tangent continuity) then the curveFitCheckpoints flag (cfc) is not required.

    """
    pass
    


def srtContext(image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    srtContext is undoable, queryable, and editable.
    

    
This command can be used to create a combined transform (translate/scale/rotate) context.

    """
    pass
    


def stereoCameraView(docTag="string", height=int, hairSystems=bool, textureDisplay="string", joints=bool, setSelected=bool, useTemplate="string", fogStart=float, cullingOverride="string", occlusionCulling=bool, panel="string", cameraSetup=bool, shadows=bool, jointXray=bool, updateColorMode=bool, smoothWireframe=bool, fogEnd=float, fogColor=float, selectionHiliteDisplay=bool, textures=bool, isFiltered=bool, grid=bool, addObjects="string", resetCustomCamera=bool, swapEyes=bool, textureAnisotropic=bool, noUndo=bool, forceMainConnection="string", displayTextures=bool, fogSource="string", dynamics=bool, wireframeOnShaded=bool, textureSampling=int, defineTemplate="string", parent="string", bumpResolution=int, sceneRenderFilter="string", rendererOverrideListUI=bool, activeSupported=bool, rigRoot="string", nCloths=bool, fluids=bool, ikHandles=bool, xray=bool, transpInShadows=bool, useCustomBackground=bool, lowQualityLighting=bool, displayLights="string", stateString=bool, deformers=bool, textureMaxSize=int, maxConstantTransparency=float, fogMode="string", control=bool, hulls=bool, colorMap=bool, useBaseRenderer=bool, activeCustomOverrideGeometry="string", selectionConnection="string", useColorIndex=bool, objectFilter="string", userNode="string", manipulators=bool, objectFilterUI="string", sortTransparent=bool, twoSidedLighting=bool, interactive=bool, colorResolution=int, rendererOverrideName="string", viewObjects=bool, controlVertices=bool, displayMode="string", allObjects=bool, rightCamera="string", objectFilterShowInHUD=bool, lockMainConnection=bool, editorChanged="string", removeSelected=bool, pluginObjects="string", dynamicConstraints=bool, mainListConnection="string", activeCustomLighSet="string", objectFilterList="string", nRigids=bool, updateMainConnection=bool, transparencyAlgorithm="string", polymeshes=bool, textureMemoryUsed=bool, ignorePanZoom=bool, fogDensity=float, follicles=bool, addSelected=bool, activeCustomGeometry="string", leftCamera="string", lineWidth=float, locators=bool, unlockMainConnection=bool, centerCamera="string", pivots=bool, fogging=bool, objectFilterListUI="string", nurbsCurves=bool, lights=bool, cameras=bool, bufferMode="string", rendererListUI=bool, rendererDeviceName=bool, activeCustomEnvironment="string", viewColor=float, width=int, filteredObjectList=bool, unParent=bool, planes=bool, activeView=bool, camera="string", nurbsSurfaces=bool, headsUpDisplay=bool, highlightConnection="string", dimensions=bool, handles=bool, subdivSurfaces=bool, exists=bool, imagePlane=bool, rendererList=bool, viewSelected=bool, pluginShapes=bool, captureSequenceNumber=int, nParticles=bool, useDefaultMaterial=bool, strokes=bool, activeCustomRenderer="string", activeOnly=bool, backfaceCulling=bool, activeShadingGraph="string", wireframeBackingStore=bool, useInteractiveMode=bool, useRGBImagePlane=bool, queryPluginObjects="string", rendererOverrideList=bool, activeComponentsXray=bool, default=bool, capture="string", textureHilight=bool, cameraName="string", rendererName="string", filter="string", displayAppearance="string"):
    """
    stereoCameraView is undoable, queryable, and editable.
    

    
This is the main command for creating stereo editors. This commands only acts as an interface to the actual viewport. It is derived off of MPxModelEditorCommand. This command manages the set of stereo rig tools.

    """
    pass
    


def stereoRigManager(addRig="string", rigDefinition="string", creationProcedure="string", cameraSetFunc="string", listRigs=bool, delete="string", defaultRig="string", language="string"):
    """
    stereoRigManager is undoable, queryable, and NOT editable.
    

    
This command manages the set of stereo rig tools.

    """
    pass
    


def stitchSurface(surfaceIsoparmsurfaceIsoparm, weight1=float, keepG1Continuity=bool, positionalContinuity=bool, cvIthIndex=int, cascade=bool, object=bool, replaceOriginal=bool, caching=bool, tolerance="string", name="string", parameterU=float, keepG0Continuity=bool, cvJthIndex=int, weight0=float, parameterV=float, togglePointNormals=bool, tangentialContinuity=bool, fixBoundary=bool, numberOfSamples=int, nodeState=int, toggleTolerance=bool, togglePointPosition=bool, bias=float, stepCount=int, constructionHistory=bool):
    """
    stitchSurface is undoable, queryable, and editable.
    

    
The stitchSurface command aligns two surfaces together to be G(0) and/or G(1) continuous by ajusting only the Control Vertices of the surfaces. The two surfaces can be stitched by specifying the two isoparm boundary edges that are to stitched together. The edge to which the two surfaces are stitched together is obtained by doing a weighted average of the two edges. The weights for the two edges is specified using the flags -wt0, -wt1 respectively.

    """
    pass
    


def stitchSurfacePoints(keepG1Continuity=bool, positionalContinuity=bool, cvIthIndex=int, cascade=bool, object=bool, replaceOriginal=bool, caching=bool, tolerance="string", name="string", parameterU=float, keepG0Continuity=bool, cvJthIndex=int, parameterV=float, equalWeight=bool, togglePointNormals=bool, tangentialContinuity=bool, fixBoundary=bool, nodeState=int, toggleTolerance=bool, togglePointPosition=bool, bias=float, stepCount=int, constructionHistory=bool):
    """
    stitchSurfacePoints is undoable, queryable, and editable.
    

    
The stitchSurfacePoints command aligns two or more surface points along the boundaries together to a single point. In the process, a node to average the points is created. The points are averaged together in a weighted fashion. The points may be control vertices along the boundaries. If the points are CVs then they are stitched together only with positional continuity.
Note: No two points can lie on the same surface.

    """
    pass
    


def stringArrayIntersector(reset=bool, defineTemplate="string", intersect="string", useTemplate="string", allowDuplicates=bool, exists=bool):
    """
    stringArrayIntersector is undoable, queryable, and editable.
    

    
The stringArrayIntersector command creates and edits an object which is able to efficiently intersect large string arrays. The intersector object maintains a sense of "the intersection so far", and updates the intersection when new string arrays are provided using the -i/intersect flag.
Note that the string intersector object may be deleted using the deleteUI command.

    """
    pass
    


def stroke(string, seed=int, name="string", pressure=bool):
    """
    stroke is undoable, NOT queryable, and NOT editable.
    

    
The stroke command creates a new Paint Effects stroke node.

    """
    pass
    


def subdAutoProjection(percentageSpace=float, planes=int, layout=int, worldSpace=bool, optimize=int, nodeState=int, constructionHistory=bool, layoutMethod=int, scale=int, caching=bool, name="string", skipIntersect=bool):
    """
    subdAutoProjection is undoable, queryable, and editable.
    

    
Projects a texture map onto an object, using several orthogonal projections simultaneously.
The argument is a face selection list.

    """
    pass
    


def subdCleanTopology():
    """
    subdCleanTopology is undoable, NOT queryable, and NOT editable.
    

    
Command cleans topology of subdiv surfaces - at all levels. It cleans the geometry of vertices that satisfy the following conditions: - Zero edits - Default uvs (uvs obtained by subdividing parent face). - No creases.

    """
    pass
    


def subdCollapse(string, object=bool, level=int, nodeState=int, constructionHistory=bool, caching=bool, name="string"):
    """
    subdCollapse is undoable, queryable, and editable.
    

    
This command converts a takes a subdivision surface, passed as the argument, and produces a subdivision surface with a number of hierarchy levels "removed". Returns the name of the subdivision surface created and optionally the DG node that does the conversion.

    """
    pass
    


def subdDuplicateAndConnect():
    """
    subdDuplicateAndConnect is undoable, NOT queryable, and NOT editable.
    

    
This command duplicates the input subdivision surface object, connects up the outSubdiv attribute of the original subd shape to the create attribute of the newly created duplicate shape and copies over the shader assignments from the original shape to the new duplicated shape.
The command will fail if no objects are selected or sent as argument or if the object sent as argument is not a subdivision surface object.

    """
    pass
    


def subdEditUV(uvSetName="string", angle=float, pivotU=float, uValue=float, scaleU=float, vValue=float, pivotV=float, scaleV=float, relative=bool, rotation=bool, scale=bool):
    """
    subdEditUV is undoable, queryable, and NOT editable.
    

    
Command edits uvs on subdivision surfaces. When used with the query flag, it returns the uv values associated with the specified components.

    """
    pass
    


def subdiv(currentSubdLevel=bool, proxyMode=int, maxPossibleLevel=int, faceStats=bool, smallOffsets=bool, currentLevel=bool, displayLoad=bool, deepestLevel=int, edgeStats=bool):
    """
    subdiv is undoable, queryable, and NOT editable.
    

    
Provides useful information about the selected subdiv or components, such as the deepest subdivided level, the children or parents of the currently selected components, etc.

    """
    pass
    


def subdivCrease(sharpness=bool):
    """
    subdivCrease is undoable, NOT queryable, and NOT editable.
    

    
Set the creasing on subdivision mesh edges or mesh points that are on the selection list.

    """
    pass
    


def subdivDisplaySmoothness(all=bool, smoothness=int):
    """
    subdivDisplaySmoothness is undoable, queryable, and NOT editable.
    

    
Sets or querys the display smoothness of subdivision surfaces on the selection list or of all subdivision surfaces if the -all option is set. Smoothness options are; rough, medium, or fine. Rough is the default.

    """
    pass
    


def subdLayoutUV(rotateForBestFit=int, flipReversed=bool, percentageSpace=float, layout=int, worldSpace=bool, nodeState=int, constructionHistory=bool, separate=int, layoutMethod=int, scale=int, caching=bool, name="string"):
    """
    subdLayoutUV is undoable, queryable, and editable.
    

    
Move UVs in the texture plane to avoid overlaps.

    """
    pass
    


def subdListComponentConversion(objects, internal=bool, fromVertex=bool, uvShell=bool, uvShellBorder=bool, fromUV=bool, toUV=bool, fromEdge=bool, toVertex=bool, border=bool, fromFace=bool, toEdge=bool, toFace=bool):
    """
    subdListComponentConversion is undoable, NOT queryable, and NOT editable.
    

    
This command converts subdivision surface components from one or more types to another one or more types, and returns the list of the conversion. It doesn't change the currently selected objects.
Use the "-in/internal" flag to specify conversion to "connected" vs. "contained" components. For example, if the internal flag is specified when converting from subdivision surface vertices to faces, then only faces that are entirely contained by the vertices will be returned. If the internal flag is not specified, then all faces that are connected to the vertices will be returned.

    """
    pass
    


def subdMapCut(nodeState=int, caching=bool, name="string", constructionHistory=bool):
    """
    subdMapCut is undoable, queryable, and editable.
    

    
Cut along edges of the texture mapping. The cut edges become map borders.

    """
    pass
    


def subdMapSewMove(numberFaces=int, worldSpace=bool, nodeState=int, limitPieceSize=bool, constructionHistory=bool, caching=bool, name="string"):
    """
    subdMapSewMove is undoable, queryable, and editable.
    

    
This command can be used to Move and Sew together separate UV pieces along geometric edges. UV pieces that correspond to the same geometric edge, are merged together by moving the smaller piece to the larger one.

The argument is a UV selection list.

    """
    pass
    


def subdMatchTopology(frontOfChain=bool):
    """
    subdMatchTopology is undoable, NOT queryable, and NOT editable.
    

    
Command matches topology across multiple subdiv surfaces - at all levels.

    """
    pass
    


def subdMirror(string, xMirror=bool, zMirror=bool, object=bool, nodeState=int, name="string", caching=bool, constructionHistory=bool, yMirror=bool):
    """
    subdMirror is undoable, queryable, and editable.
    

    
This command takes a subdivision surface, passed as the argument, and produces a subdivision surface that is a mirror. Returns the name of the subdivision surface created and optionally the DG node that does the mirroring.

    """
    pass
    


def subdPlanarProjection(imageScaleU=float, imageCenter=float, projectionWidth="string", rotateX=int, insertBeforeDeformers=bool, keepImageRatio=bool, projectionCenterZ="string", projectionCenter="string", mapDirection="string", imageScaleV=float, worldSpace=bool, projectionCenterY="string", rotationAngle=int, caching=bool, name="string", imageCenterY=float, smartFit=bool, projectionScale="string", imageScale=float, projectionHeight="string", rotate=int, rotateY=int, createNewMap=bool, nodeState=int, constructionHistory=bool, rotateZ=int, projectionCenterX="string", imageCenterX=float):
    """
    subdPlanarProjection is undoable, queryable, and editable.
    

    
TsubProjCmdBase is a base class for the command to create a mapping on the selected subdivision faces. Projects a map onto an object, using an orthogonal projection. The piece of the map defined from isu, isv, icx, icy area, is placed at pcx, pcy, pcz location.

    """
    pass
    


def subdToBlind(absolutePosition=bool, includeZeroOffsets=bool, includeCreases=bool):
    """
    subdToBlind is undoable, NOT queryable, and NOT editable.
    

    
The subdivision surface hierarchical edits will get copied into blind data on the given polygon. The polygon face count and topology must match the subdivision surface base mesh face count and topology. If they don't, the blind data will still appear, but is not guaranteed to produce the same result when converted back to a subdivision surface.

The command takes a single subdivision surface and a single polygonal object. Additional subdivision surfaces or polygonal objects will be ignored.

    """
    pass
    


def subdToPoly(subd, outSubdCVId=int, extractPointPosition=bool, addUnderTransform=bool, preserveVertexOrdering=bool, applyMatrixToResult=bool, inSubdCVIdRight=int, object=bool, outv=int, inSubdCVId=int, outSubdCVIdLeft=int, inSubdCVIdLeft=int, format=int, caching=bool, name="string", shareUVs=bool, connectShaders=bool, outSubdCVIdRight=int, depth=int, copyUVTopology=bool, sampleCount=int, maxPolys=int, nodeState=int, subdNormals=bool, constructionHistory=bool):
    """
    subdToPoly is undoable, queryable, and editable.
    

    
This command tessellates a subdivision surface and produces polygon. The name of the new polygon is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def subdTransferUVsToCache():
    """
    subdTransferUVsToCache is undoable, NOT queryable, and NOT editable.
    

    
The subdivision surface finer level uvs will get copied to the polygonToSubd node sent in as argument.

The command takes a single subdivision surface and a single polygonToSubd node as input. Additional inputs will be ignored. Please note that this command is an internal command and is to be used with care, directly by the user

    """
    pass
    


def substituteGeometry(disableNonSkinDeformers=bool, retainOldGeometry=bool, reWeightDistTolerance=float, newGeometryToLayer=bool, oldGeometryToLayer=bool):
    """
    substituteGeometry is undoable, NOT queryable, and NOT editable.
    

    
This command can be used to replace the geometry which is already connected to deformers with a new geometry. The weights on the old geometry will be retargeted to the new geometry.

    """
    pass
    


def suitePrefs(isCompleteSuite=bool, applyToSuite="string", installedAsSuite=bool):
    """
    suitePrefs is undoable, NOT queryable, and NOT editable.
    

    
This command sets the mouse and keyboard interaction mode for Maya and other Suites applications (if Maya is part of a Suites install).

    """
    pass
    


def surface(degreeU=int, degreeV=int, formU="string", worldSpace=bool, knotU=float, objectSpace=bool, formV="string", point="string", knotV=float, pointWeight="string", name="string"):
    """
    surface is undoable, NOT queryable, and NOT editable.
    

    
The cmd creates a NURBS spline surface (rational or non rational). The surface is created by specifying control vertices (CV's) and knot sequences in the U and V direction. You cannot query the properties of the surface using this command. See examples below.

    """
    pass
    


def surfaceSampler(flipV=bool, superSampling=int, targetUVSpace="string", maxSearchDistance="string", useGeometryNormals=bool, ignoreTransforms=bool, camera="string", shadows=bool, mapWidth=int, searchMethod=int, ignoreMirroredFaces=bool, filterType=int, target="string", uvSet="string", filterSize=float, sourceUVSpace="string", mapMaterials=bool, mapSpace="string", mapHeight=int, fileFormat="string", overscan=int, source="string", flipU=bool, maximumValue="string", filename="string", searchCage="string", searchOffset="string", mapOutput="string"):
    """
    surfaceSampler is undoable, NOT queryable, and NOT editable.
    

    
Maps surface detail from a source surface to a new texture map on a target surface. Both objects must be selected when the command is invoked, with the source surface selected first, and the target last.

    """
    pass
    


def surfaceShaderList(remove="string", add="string"):
    """
    surfaceShaderList is undoable, queryable, and editable.
    

    
Add/Remove a relationship between an object and the current shading group.

    """
    pass
    


def swatchDisplayPort(string, docTag="string", height=int, defineTemplate="string", parent="string", pressCommand="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", enable=bool, preventOverride=bool, widthHeight=int, borderWidth=int, exists=bool, renderPriority=int, enableBackground=bool, visibleChangeCommand="string", visible=bool, noBackground=bool, fullPathName=bool, dropCallback="string", dragCallback="string", renderSize=int, borderColor=float, backgroundColor=float, manage=bool, shadingNode="string", isObscured=bool):
    """
    swatchDisplayPort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays a swatch representing the shading node.
The optional argument is the name of the 3dPort.

    """
    pass
    


def swatchRefresh():
    """
    swatchRefresh is NOT undoable, NOT queryable, and NOT editable.
    

    
The swatchRefresh command causes image source node swatches to be refreshed on screen. The purpose of this command is to provide a mechanism to trigger a swatch refresh in cases that are not subject to dirty propagation in the dependency graph. This command only works with imageSource-derived node types. Invoking this command with no arguments will cause all imageSource swatches to be refreshed.

    """
    pass
    


def switchTable(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", underPointerRow=bool, exists=bool, visibleChangeCommand="string", enableBackground=bool, label1="string", visible=bool, switchNode="string", selectedRow=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, label2="string", isObscured=bool):
    """
    switchTable is undoable, queryable, and editable.
    

    
This command creates/edits/queries the switch table control.
The optional argument is the name of the control.

    """
    pass
    


def symbolButton(string, docTag="string", height=int, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", width=int, popupMenuArray=bool, highlightColor=float, annotation="string", enable=bool, dropCallback="string", exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, command="string", isObscured=bool):
    """
    symbolButton is undoable, queryable, and editable.
    

    
This command creates a symbol button. A symbol button behaves like a regular button, the only difference is a symbol button displays an image rather that a text label. A command may be attached to the button which will be executed when the button is pressed.

    """
    pass
    


def symbolCheckBox(string, docTag="string", height=int, onCommand="string", defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, disableOnImage="string", disableOffImage="string", width=int, dragCallback="string", highlightColor=float, annotation="string", enable=bool, offCommand="string", offImage="string", popupMenuArray=bool, value=bool, exists=bool, changeCommand="string", enableBackground=bool, visibleChangeCommand="string", visible=bool, useTemplate="string", innerMargin=bool, preventOverride=bool, fullPathName=bool, dropCallback="string", onImage="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    symbolCheckBox is undoable, queryable, and editable.
    

    
This command creates a symbol check box. A symbol check box is a simple control containing a pixmap and a state of either on or off. Commands can be attached to any or all of the following events: when the symbol check box is turned on, turned off, or simply when it's state is changed.

    """
    pass
    


def symmetricModelling(reset=bool, symmetry=int, seamTolerance=float, preserveSeam=int, seamFalloffCurve="string", about="string", axis="string", allowPartial=bool, tolerance=float, topoSymmetry=bool):
    """
    symmetricModelling is undoable, queryable, and editable.
    

    
This command allows you to change the symmetric modelling options.
Symmetric modelling is an option that allows for reflection of basic manipulator actions such as move, rotate, and scale.

    """
    pass
    


def sysFile(delete=bool, makeDir=bool, rename="string", move="string", copy="string", removeEmptyDir=bool):
    """
    sysFile is undoable, NOT queryable, and NOT editable.
    

    
This command provides a system independent way to create a directory or to rename or delete a file.

    """
    pass
    


def tabLayout(string, docTag="string", height=int, childResizable=bool, defineTemplate="string", parent="string", image="string", numberOfPopupMenus=bool, useTemplate="string", selectTabIndex=int, width=int, dragCallback="string", numberOfChildren=bool, highlightColor=float, scrollable=bool, tabsVisible=bool, annotation="string", enable=bool, horizontalScrollBarThickness=int, preventOverride=bool, selectTab="string", popupMenuArray=bool, preSelectCommand="string", enableBackground=bool, verticalScrollBarThickness=int, childArray=bool, innerMarginHeight=int, exists=bool, changeCommand="string", imageVisible=bool, innerMarginWidth=int, doubleClickCommand="string", visibleChangeCommand="string", visible=bool, showNewTab=bool, tabLabel="string", moveTab=int, fullPathName=bool, dropCallback="string", selectCommand="string", noBackground=bool, backgroundColor=float, minChildWidth=int, manage=bool, scrollableTabs=bool, borderStyle="string", tabsClosable=bool, tabLabelIndex=int, isObscured=bool, newTabCommand="string"):
    """
    tabLayout is undoable, queryable, and editable.
    

    
This command creates a tab group. Tab groups are a specialized form of control layouts that contain only control layouts. Whenever a control layout is added to a tab group it will have a tab provided for it that allows selection of that group from amongst other tabbed control groups. Only one child of a tab layout is visible at a time.

    """
    pass
    


def tangentConstraint(targetobject, worldUpObject="string", worldUpVector=float, remove=bool, worldUpType="string", weightAliasList=bool, layer="string", targetList=bool, upVector=float, aimVector=float, weight=float, name="string"):
    """
    tangentConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation based on the tangent of the target curve[s] at the closest point[s] to the object.
A tangentConstraint takes as input one or more NURBS curves (the targets) and a DAG transform node (the object). The tangentConstraint orients the constrained object such that the aimVector (in the object's local coordinate system) aligns in world space to combined tangent vector. The upVector (again the the object's local coordinate system) is aligned in world space with the worldUpVector. The combined tangent vector is a weighted average of the tangent vector for each target curve at the point closest to the constrained object.

    """
    pass
    


def targetWeldCtx(exists=bool, image1="string", image2="string", mergeToCenter=bool, image3="string"):
    """
    targetWeldCtx is undoable, queryable, and editable.
    

    
Create a new context to weld vertices together on a poly object.

    """
    pass
    


def texCutContext(touchToSew=bool, moveRatio=float, image1="string", edgeSelectSensitive=float, steadyStroke=bool, size=float, mode="string", displayShellBorders=bool, steadyStrokeDistance=float, adjustSize=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    texCutContext is undoable, queryable, and editable.
    

    
This command creates a context for cut uv tool. This context only works in the UV editor.

    """
    pass
    


def texLatticeDeformContext(image1="string", useBoundingRect=bool, latticeRows=int, latticeColumns=int, envelope=float, snapPixelMode=bool, history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    texLatticeDeformContext is undoable, queryable, and editable.
    

    
This command creates a context which may be used to deform UV maps with lattice manipulator. This context only works in the texture UV editor.

    """
    pass
    


def texManipContext(exists=bool, image1="string", image2="string", image3="string"):
    """
    texManipContext is undoable, queryable, and editable.
    

    
Command used to register the texSelectCtx tool. Command used to register the texManipCtx tool.

    """
    pass
    


def texMoveContext(object, snapComponentsRelative=bool, image1="string", snapPixelMode=int, image3="string", exists=bool, image2="string", position=bool):
    """
    texMoveContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    """
    pass
    


def texMoveUVShellContext(object, mask=bool, image1="string", iterations=int, image3="string", shellBorder=float, exists=bool, image2="string", position=bool):
    """
    texMoveUVShellContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    """
    pass
    


def texRotateContext(snapValue=float, image1="string", snapRelative=bool, snap=bool, image3="string", exists=bool, image2="string", position=bool):
    """
    texRotateContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a rotate context for the UV Editor. Note that the above flag controls the global behaviour of all texture editor rotate contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flag, will change all existing texture editor rotate contexts.

    """
    pass
    


def texScaleContext(snapValue=float, image1="string", snapRelative=bool, snap=bool, image3="string", exists=bool, image2="string", position=bool):
    """
    texScaleContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a scale context for the UV Editor. Note that the above flag controls the global behaviour of all texture editor scale contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flag, will change all existing texture editor scale contexts.

    """
    pass
    


def texSculptCacheContext(inverted=bool, size=float, strength=float, mode="string", grabTwist=bool, showBrushRingDuringStroke=bool, falloffType=int, direction=int, adjustSize=bool, floodPin=float, adjustStrength=bool, sculptFalloffCurve="string"):
    """
    texSculptCacheContext is undoable, queryable, and editable.
    

    
This is a tool context command for uv cache sculpting tool.

    """
    pass
    


def texSelectContext(exists=bool, image1="string", image2="string", image3="string"):
    """
    texSelectContext is undoable, queryable, and editable.
    

    
Command used to register the texSelectCtx tool.

    """
    pass
    


def texSelectShortestPathCtx(exists=bool, image1="string", image2="string", image3="string"):
    """
    texSelectShortestPathCtx is undoable, queryable, and editable.
    

    
Creates a new context to select shortest edge path between two vertices or UVs in the texture editor window.

    """
    pass
    


def texSmudgeUVContext(effectType="string", image1="string", functionType="string", smudgeIsMiddle=bool, history=bool, pressure=float, exists=bool, radius=float, dragSlider="string", image2="string", name="string", image3="string"):
    """
    texSmudgeUVContext is undoable, queryable, and editable.
    

    
This command creates a context for smudge UV tool. This context only works in the texture UV editor.

    """
    pass
    


def text(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", highlightColor=float, annotation="string", enable=bool, hyperlink=bool, preventOverride=bool, popupMenuArray=bool, dropRectCallback="string", font="string", exists=bool, enableBackground=bool, recomputeSize=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, wordWrap=bool, align="string", manage=bool, isObscured=bool):
    """
    text is undoable, queryable, and editable.
    

    
Create a simple text label control.

    """
    pass
    


def textCurves(string, font="string", text="string", name="string", object=bool):
    """
    textCurves is undoable, queryable, and editable.
    

    
The textCurves command creates NURBS curves from a text string using the specified font.
A single letter can be made up of more than one NURBS curve. The number of curves per letter varies with the font.

    """
    pass
    


def textField(string, docTag="string", height=int, defineTemplate="string", parent="string", fileName="string", useTemplate="string", manage=bool, highlightColor=float, enterCommand="string", textChangedCommand="string", dragCallback="string", annotation="string", enable=bool, alwaysInvokeEnterCommandOnReturn=bool, preventOverride=bool, popupMenuArray=bool, text="string", width=int, placeholderText="string", disableButtons=bool, font="string", exists=bool, changeCommand="string", disableHistoryButton=bool, enableBackground=bool, numberOfPopupMenus=bool, visibleChangeCommand="string", visible=bool, noBackground=bool, fullPathName=bool, dropCallback="string", disableClearButton=bool, searchField=bool, isObscured=bool, backgroundColor=float, insertText="string", editable=bool, insertionPosition=int, drawInactiveFrame=bool, receiveFocusCommand="string"):
    """
    textField is undoable, queryable, and editable.
    

    
Create a text field control.

    """
    pass
    


def textFieldButtonGrp(groupName, docTag="string", buttonCommand="string", buttonLabel="string", parent="string", popupMenuArray=bool, fileName="string", forceChangeCommand=bool, defineTemplate="string", manage=bool, label="string", highlightColor=float, height=int, textChangedCommand="string", dragCallback="string", columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, adjustableColumn6=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnWidth4=int, columnAlign4="string", adjustableColumn5=int, placeholderText="string", exists=bool, columnAttach4="string", noBackground=bool, adjustableColumn2=int, visible=bool, enable=bool, columnAlign=int, enableBackground=bool, numberOfPopupMenus=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, insertText="string", editable=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", width=int, insertionPosition=int, enableButton=bool, columnAttach6="string", isObscured=bool, text="string", columnOffset6=int):
    """
    textFieldButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command adds a button to the textFieldGrp command.

    """
    pass
    


def textFieldGrp(groupName, docTag="string", height=int, columnWidth4=int, parent="string", popupMenuArray=bool, fileName="string", forceChangeCommand=bool, defineTemplate="string", manage=bool, label="string", highlightColor=float, textChangedCommand="string", dragCallback="string", columnOffset2=int, annotation="string", columnAlign5="string", columnOffset5=int, preventOverride=bool, columnAlign=int, columnWidth6=int, adjustableColumn4=int, rowAttach=int, columnOffset3=int, columnAlign4="string", adjustableColumn5=int, placeholderText="string", exists=bool, columnAttach4="string", noBackground=bool, adjustableColumn2=int, visible=bool, enable=bool, adjustableColumn6=int, enableBackground=bool, numberOfPopupMenus=bool, visibleChangeCommand="string", adjustableColumn=int, columnWidth3=int, columnAlign2="string", useTemplate="string", columnAlign6="string", columnWidth1=int, columnWidth2=int, columnAttach3="string", fullPathName=bool, dropCallback="string", columnAlign3="string", columnAttach=int, adjustableColumn3=int, columnAttach5="string", backgroundColor=float, columnWidth5=int, columnWidth=int, insertText="string", editable=bool, columnOffset4=int, changeCommand="string", columnAttach2="string", width=int, insertionPosition=int, columnAttach6="string", isObscured=bool, text="string", columnOffset6=int):
    """
    textFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text and editable text field. The label text is optional.

    """
    pass
    


def textManip(visible=bool):
    """
    textManip is undoable, queryable, and NOT editable.
    

    
Shows/hides the text manip.

    """
    pass
    


def textScrollList(string, allowMultiSelection=bool, height=int, allItems=bool, defineTemplate="string", docTag="string", numberOfItems=bool, numberOfPopupMenus=bool, useTemplate="string", append="string", highlightColor=float, deselectIndexedItem=int, deselectAll=bool, selectItem="string", doubleClickCommand="string", numberOfRows=int, dragCallback="string", deleteKeyCommand="string", parent="string", annotation="string", enable=bool, deselectItem="string", preventOverride=bool, lineFont=int, popupMenuArray=bool, uniqueTag="string", selectUniqueTagItem="string", appendPosition=int, font="string", exists=bool, removeItem="string", enableBackground=bool, showIndexedItem=int, visibleChangeCommand="string", visible=bool, selectIndexedItem=int, fullPathName=bool, dropCallback="string", numberOfSelectedItems=bool, selectCommand="string", noBackground=bool, removeAll=bool, backgroundColor=float, allowAutomaticSelection=bool, manage=bool, removeIndexedItem=int, width=int, isObscured=bool):
    """
    textScrollList is undoable, queryable, and editable.
    

    
This command creates/edits/queries a text scrolling list. The list can be in single select mode where only one item at at time is selected, or in multi-select mode where many items may be selected.
Note: The -dgc/dragCallback flag works only on Windows.

    """
    pass
    


def textureDeformer(before=bool, exclusive="string", after=bool, pointSpace="string", includeHiddenSelections=bool, frontOfChain=bool, prune=bool, vectorSpace="string", vectorStrength=float, geometryIndices=bool, split=bool, envelope=float, offset=float, geometry="string", name="string", parallel=bool, vectorOffset=float, ignoreSelected=bool, afterReference=bool, remove=bool, direction="string", deformerTools=bool, strength=float):
    """
    textureDeformer is undoable, queryable, and editable.
    

    
This command creates a texture deformer for the object. The selected objects are the input geometry objects. The deformer node name will be returned.

    """
    pass
    


def texturePlacementContext(labelMapping=bool, image1="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    texturePlacementContext is undoable, queryable, and editable.
    

    
Create a command for creating new texture placement contexts. By default label mapping is on when the context is created.

    """
    pass
    


def textureWindow(docTag="string", displayPreselection=bool, useTemplate="string", toggleGamma=bool, displayStyle="string", singleBuffer=bool, panel="string", setUvSet=int, loadImage="string", imagePixelSnap=bool, imageBaseColor=float, forceMainConnection="string", scaleBlue=float, reset=bool, displayAxes=bool, drawAxis=bool, checkerDensity=int, scaleGreen=float, defineTemplate="string", parent="string", tileLabels=bool, useFaceGroup=bool, doubleBuffer=bool, displaySolidMap=bool, internalFaces=bool, divisions=int, writeImage="string", displayCheckered=bool, exposure=float, stateString=bool, control=bool, toggleExposure=bool, imageNumber=int, imageDisplay=bool, selectionConnection="string", removeImage=bool, numberOfImages=int, viewTransformName="string", uvSets=bool, viewPortImage=bool, selectRelatedFaces=bool, lockMainConnection=bool, nbImages=bool, spacing=float, toggle=bool, mainListConnection="string", displayDivisionLines=bool, imageSize=bool, updateMainConnection=bool, style=int, frontFacingColor=float, capture="string", backFacingColor=float, unlockMainConnection=bool, displayLabels=bool, displayImage=int, relatedFaces=bool, removeAllImages=bool, numUvSets=bool, imageTileRange=float, selectInternalFaces=bool, maxResolution=int, refresh=bool, unParent=bool, changeCommand="string", imageRatio=bool, forceRebake=bool, distortionPerObject=bool, drawSubregions=bool, highlightConnection="string", displayGridLines=bool, exists=bool, frameAll=bool, displayDistortion=bool, captureSequenceNumber=int, labelPosition="string", gamma=float, frameSelected=bool, realSize=bool, rendererString="string", size=float, saveImage=bool, imageUnfiltered=bool, clearImage=bool, imageNames=bool, scaleRed=float, filter="string", cmEnabled=bool):
    """
    textureWindow is undoable, queryable, and editable.
    

    
This command is used to create a UV Editor and to query or edit the texture editor settings.
The UV Editor displays texture mapped polygon objects in 2D texture space. Only active objects are visible in this window.
The UV Editor has the ability to display two types of images. The Texture Image is a visualisation of the current texture and associated placement parameters. The Editor Image is a user specified image loaded from disk.
A UV Editor can be invoked by selecting the "Window -> UV Texture Editor..." menu item from the main maya menu listing that appears at the top of the maya window. It can also be invoked by selecting the "Panel -> UV Editor" item under the "Panels" menu item that appears at the top right hand corner of the view.
As a UV Editor typically exists at start-up time, and as only one of these can exist at any given time, this command is normally used to query and edit the editor settings.

    """
    pass
    


def texTweakUVContext(object, image1="string", image3="string", exists=bool, tolerance=float, image2="string", position=bool):
    """
    texTweakUVContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    """
    pass
    


def texWinToolCtx(image1="string", dolly=bool, track=bool, boxzoom=bool, alternateContext=bool, history=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    texWinToolCtx is undoable, queryable, and editable.
    

    
This class creates a context for the View Tools "track", "dolly", and "box zoom" in the texture window.

    """
    pass
    


def threadCount(numberOfThreads=int):
    """
    threadCount is undoable, queryable, and NOT editable.
    

    
This command sets the number of threads to be used by Maya in regions of code that are multithreaded. By default the number of threads is equal to the number of logical CPUs, not the number of physical CPUs. Logical CPUs are different from physical CPUs in the following ways:
A physical CPU with hyperthreading counts as two logical CPUs
A dual-core CPU counts as two logical CPUs
With some workloads, using one thread per logical CPU may not perform well. This is sometimes the case with hyperthreading. It is worth experimenting with different numbers of threads to see which gives the best performance. Note that having more threads can mean Maya uses more memory.
Setting a value of zero means the number of threads used will equal the number of logical processors in the system.

    """
    pass
    


def threePointArcCtx(degree=int, image1="string", spans=int, image3="string", exists=bool, image2="string", name="string", history=bool):
    """
    threePointArcCtx is undoable, queryable, and editable.
    

    
The threePointArcCtx command creates a new context for creating 3 point arcs

    """
    pass
    


def thumbnailCaptureComponent(string, delete=bool, previewPath=bool, closeCurrentSession=bool, isSessionOpened=bool, launchedFromOptionsBox=bool, capturedFrameCount=bool, save="string", startFrame=int, fileDialogCallback="string", capture=bool, endFrame=int, removeProjectThumbnail="string"):
    """
    thumbnailCaptureComponent is undoable, queryable, and NOT editable.
    

    
This command is used to generate a thumbnail/playblast sequence from the scene.

    """
    pass
    


def timeCode(productionStartSecond=float, productionStartHour=float, productionStartFrame=float, mayaStartFrame=float, productionStartMinute=float):
    """
    timeCode is undoable, queryable, and editable.
    

    
Use this command to query and set the time code information in the file

    """
    pass
    


def timeControl(showKeys="string", docTag="string", height=int, defineTemplate="string", parent="string", pressCommand="string", tickSpan=int, numberOfPopupMenus=bool, useTemplate="string", width=int, popupMenuArray=bool, highlightColor=float, repeatOnHold=bool, rangeArray=bool, dragCallback="string", forceRedraw=bool, beginScrub=bool, enable=bool, showGreaseFrames="string", preventOverride=bool, mainListConnection="string", repeatChunkSize=float, resample=bool, sound="string", range=bool, globalTime=bool, annotation="string", exists=bool, endScrub=bool, visibleChangeCommand="string", rangeVisible=bool, foregroundColor=float, animCurveNames=bool, enableBackground=bool, snap=bool, showKeysCombined=bool, visible=bool, currentFrameColor=float, animLayerShowWeight=bool, releaseCommand="string", tickSize=int, fullPathName=bool, waveform="string", dropCallback="string", animLayerFilterOptions="string", noBackground=bool, backgroundColor=float, manage=bool, displaySound=bool, greasePencilSequenceNames=bool, forceRefresh=bool, isObscured=bool):
    """
    timeControl is undoable, queryable, and editable.
    

    
This command creates a control that can be used for changing current time, displaying/editing keys, and displaying/scrubbing sound.
Note: only one timeControl may be created. The one Maya creates on startup can be accessed from the global string variable $gPlayBackSlider. Also, it is not a good idea to delete it.

    """
    pass
    


def timeEditor(clipId=int, composition="string", topLevelClips="string", drivingClipsForObj="string", selectedClips="string", drivingClipsForAttr="string", allClips="string", mute=bool, commonParentTrack=bool, includeParent=bool):
    """
    timeEditor is undoable, queryable, and NOT editable.
    

    
General Time Editor commands

    """
    pass
    


def timeEditorAnimSource(addSelectedObjects=bool, exclusive=bool, targetIndex="string", export="string", importMayaFile="string", importedContainerNames="string", addRelatedKG=bool, importPopulateOption="string", removeSceneAnimation=bool, takesToImport="string", isUnique=bool, type="string", recursively=bool, includeRoot=bool, drivenClips=bool, populateImportedAnimSources="string", importFbx="string", addObjects="string", poseClip=bool, removeSource="string", attribute="string", bakeToAnimSource="string", showAnimSourceRemapping=bool, addSource="string", importFbxTakes="string", calculateTiming=bool, apply=bool, importOption="string", takeList="string", copyAnimation=bool, importAllFbxTakes=bool, targets=bool):
    """
    timeEditorAnimSource is undoable, queryable, and editable.
    

    
Commands for managing animation sources.

    """
    pass
    


def timeEditorBakeClips(combineLayers=bool, targetTracksNode="string", clipId=int, bakeToClip="string", keepOriginalClip=bool, forceSampling=bool, targetTrackIndex=int, path="string", sampleBy=()):
    """
    timeEditorBakeClips is undoable, queryable, and editable.
    

    
This command is used to bake Time Editor clips and to blend them into a single clip.

    """
    pass
    


def timeEditorClip(clipIdFromPath=bool, exclusive=bool, removeAttribute="string", speedRamping=int, importMayaFile="string", remap="string", ghostRootRemove="string", exportAllClips=bool, takeList="string", takesToImport="string", removeCrossfade=bool, parent=int, holdStart=(), timeWarp=bool, setKeyframe="string", parentClipId=int, clipPath=bool, populateImportedAnimSources="string", clipId=int, loopStart=(), addObjects="string", crossfadeMode=int, ripple=bool, absolute=bool, removeSceneAnimation=bool, exists=bool, importFbxTakes="string", clipDataType=bool, name="string", zeroKeying=bool, removeWeightCurve=bool, endTime=(), importTakeDestination=int, scaleStart=(), addSelectedObjects=bool, group=bool, loopEnd=(), animSource="string", addRelatedKG=bool, importPopulateOption="string", rootPath="string", includeRoot=bool, duplicateClip=bool, extendParents=bool, importFbx="string", clipAfter=bool, transition=bool, allowShrinking=bool, drivenClipsBySource="string", explode=int, path="string", clipBefore=bool, holdEnd=(), timeWarpCurve=bool, curveTime=(), importOption="string", remappedSourceAttrs=bool, importAllFbxTakes=bool, isContainer=bool, parentGroupId=bool, trimEnd=(), duration=(), scaleEnd=(), remapSource="string", mute=bool, clipNode=bool, preserveAnimationTiming=bool, remappedTargetAttrs=bool, emptySource=bool, recursively=bool, audio="string", resetTiming=bool, drivenObjects=bool, ghostRootAdd="string", resetTransition=bool, uniqueAnimSource=bool, pasteClip=(), poseClip=bool, children=int, defaultGhostRoot=bool, existingOnly=bool, track="string", startTime=(), listUserGhostRoot=bool, modifyAnimSource=bool, moveClip=(), trimStart=(), extend=bool, copyClip=bool, extendParent=bool, razorClip=(), drivenAttributes=bool, importedContainerNames="string", rootClipId=int, drivingSources="string", type="string", clipIdFromNodeName=int, truncated=bool, addAttribute="string", tracksNode=bool, userGhostRoot=bool, exportFbx="string", crossfadePlug=bool, attribute="string", minClipDuration=bool, timeWarpType=int, scalePivot=(), ghost=bool, weightCurve=bool, removeClip=bool, showAnimSourceRemapping=bool):
    """
    timeEditorClip is undoable, queryable, and editable.
    

    
This command edits/queries Time Editor clips.

    """
    pass
    


def timeEditorClipLayer(removeLayer=bool, removeAttribute="string", layerName="string", mute=bool, resetSolo=bool, keySiblings=bool, allLayers=bool, attribute="string", mode=int, setKeyframe=bool, addLayer="string", addObject="string", clipId=int, addAttribute="string", solo=bool, name=bool, layerId=int, path="string", index=int, attributeKeyable="string", zeroKeying=bool, removeObject="string"):
    """
    timeEditorClipLayer is undoable, queryable, and editable.
    

    
Time Editor clip layers commands

    """
    pass
    


def timeEditorClipOffset(upVectorZ=float, clipId=int, upVectorY=float, matchObj="string", matchPath="string", upVectorX=float, matchSrcTime=(), matchOffsetRot=bool, resetMatch=int, matchClipId=int, matchRotOp=int, path="string", applyToAllRoots=bool, rootObj="string", resetMatchPath="string", matchOffsetTrans=bool, matchDstTime=(), offsetTransform=bool, matchTransOp=int):
    """
    timeEditorClipOffset is undoable, queryable, and NOT editable.
    

    
This command is used to compute an offset to apply on a source clip in order to automatically align it to a destination clip at a specified match element. For this command to work, offset objects must be specified for the character.

    """
    pass
    


def timeEditorComposition(delete=bool, allCompositions=bool, tracksNode=bool, createTrack=bool, rename="string", active=bool, duplicateFrom="string"):
    """
    timeEditorComposition is undoable, queryable, and editable.
    

    
Commands related to composition management inside Time Editor.

    """
    pass
    


def timeEditorPanel(docTag="string", activeTabTime=bool, defineTemplate="string", parent="string", displayTangents="string", useTemplate="string", lockMainConnection=bool, unParent=bool, panel="string", displayActiveKeyTangents="string", mainListConnection="string", displayValues="string", snapValue="string", highlightConnection="string", activeTabRootClipId=bool, keyingTarget=int, lookAt="string", snapTolerance=int, stateString=bool, exists=bool, displayInfinities="string", displayActiveKeys="string", control=bool, menu="string", snapTime="string", snapToClip=bool, autoFit="string", tabView=int, layerId=int, selectionConnection="string", forceMainConnection="string", timeCursor=bool, unlockMainConnection=bool, groupIdForTabView=int, updateMainConnection=bool, activeTabView=int, activeClipEditMode=int, setToPrevClipEditMode=bool, snapToFrame=bool, displayKeys="string", filter="string"):
    """
    timeEditorPanel is undoable, queryable, and editable.
    

    
Time Editor - non-linear animation editor

    """
    pass
    


def timeEditorTracks(resetSolo=bool, trackName="string", resetMute=bool, trackSolo=bool, trackGhost=bool, trackMuted=bool, allClips=bool, removeTrackByPath="string", allTracks=bool, plugIndex=int, addTrack=int, selectedTracks=bool, trackType=int, removeTrack=int, trackIndex=int, composition=bool, activeClipWeightId=(), path="string", activeClipWeight=(), reorderTrack=int, allTracksRecursive=bool):
    """
    timeEditorTracks is undoable, queryable, and editable.
    

    
Time Editor tracks commands

    """
    pass
    


def timePort(docTag="string", height=int, defineTemplate="string", parent="string", snap=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", dropCallback="string", globalTime=bool, exists=bool, enable=bool, enableBackground=bool, numberOfPopupMenus=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    timePort is undoable, queryable, and editable.
    

    
This command creates a simple time control widget. See also the "timeControl" command.

    """
    pass
    


def timer(lapTime=bool, endTimer=bool, name="string", startTimer=bool):
    """
    timer is NOT undoable, NOT queryable, and NOT editable.
    

    
Allow simple timing of scripts and commands. The resolution of this timer is at the level of your OS's gettimeofday() function.
Note:This command does not handle stacked calls. For example, this code below will give an incorrect answer on the second timer -e call.
timer -s;
timer -s;
timer -e;
timer -e;
To do this use named timers:
timer -s;
timer -s -name "innerTimer";
timer -e -name "innerTimer";
timer -e;
I the -e flag or -lap flag return the time elapsed since the last 'timer -s' call.
I the -s flag has no return value.

    """
    pass
    


def timerX(startTime=float):
    """
    timerX is undoable, NOT queryable, and NOT editable.
    

    
Used to calculate elapsed time. This command returns sub-second accurate time values. It is useful from scripts for timing the length of operations. Call this command before and after the operation you wish to time. On the first call, do not use any flags. It will return the start time. Save this value. After the operation, call this command a second time, and pass the saved start time using the -st flag. The elapsed time will be returned.

    """
    pass
    


def timeWarp(interpType=int, moveFrame=int, frame=float, g=bool, deleteFrame=int):
    """
    timeWarp is undoable, queryable, and editable.
    

    
This command is used to create a time warp input to a set of animation curves.

    """
    pass
    


def toggle(objects, latticePoint=bool, above=bool, newPolymesh=bool, pointFacet=bool, gl=bool, boundary=bool, newCurve=bool, geometry=bool, point=bool, normal=bool, state=bool, hull=bool, below=bool, controlVertex=bool, pointDisplay=bool, origin=bool, scalePivot=bool, doNotWrite=bool, surfaceFace=bool, extent=bool, newSurface=bool, template=bool, editPoint=bool, localAxis=bool, vertex=bool, boundingBox=bool, highPrecisionNurbs=bool, uvCoords=bool, selectHandle=bool, facet=bool, rotatePivot=bool, latticeShape=bool):
    """
    toggle is undoable, queryable, and NOT editable.
    

    
The toggle command is used to toggle the display of various object features for objects which have these components. For example, CV and edit point display may be toggled for those listed NURB curves or surfaces.
Note: This command is not undoable.

    """
    pass
    


def toggleAxis(origin=bool, view=bool):
    """
    toggleAxis is undoable, queryable, and NOT editable.
    

    
Toggles the state of the display axis.
Note: the display of the axis in the bottom left corner has been rendered obsolete by the headsUpDisplay command.

    """
    pass
    


def toggleWindowVisibility(string):
    """
    toggleWindowVisibility is undoable, NOT queryable, and NOT editable.
    

    
Toggle the visibility of a window. If no window is specified then the current window (most recently created) is used. See also the window command's vis/visible flag.

    """
    pass
    


def tolerance(angular=int, linear="string"):
    """
    tolerance is undoable, queryable, and NOT editable.
    

    
This command sets tolerances used by modelling operations that require a tolerance, such as surface fillet. Linear tolerance is also known as "positional" tolerance. Angular tolerance is also known as "tangential" tolerance.

    """
    pass
    


def toolBar(name, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, label="string", dragCallback="string", highlightColor=float, annotation="string", preventOverride=bool, popupMenuArray=bool, exists=bool, enable=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, manage=bool, allowedArea="string", isObscured=bool, area="string", content="string"):
    """
    toolBar is undoable, queryable, and editable.
    

    
Create a toolbar. Tool bars are movable panel that contains a set of controls. They are placed in the tool bar area around the central control in a main window. Tool bars can be moved inside their current area, moved into new areas and floated.

    """
    pass
    


def toolButton(string, docTag="string", height=int, onCommand="string", defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, dragCallback="string", select=bool, image3="string", highlightColor=float, imageOverlayLabel="string", allowMultipleTools=bool, toolCount=bool, annotation="string", enable=bool, offCommand="string", image1="string", popupMenuArray=bool, tool="string", toolImage1="string", doubleClickCommand="string", exists=bool, changeCommand="string", ltVersion="string", collection="string", visibleChangeCommand="string", visible=bool, preventOverride=bool, fullPathName=bool, toolArray=bool, dropCallback="string", toolImage3="string", popupIndicatorVisible=bool, noBackground=bool, toolImage2="string", backgroundColor=float, enableBackground=bool, manage=bool, style="string", version="string", image2="string", isObscured=bool):
    """
    toolButton is undoable, queryable, and editable.
    

    
This command creates a toolButton that is added to the most recently created tool button collection unless the cl/collection flag is used. It also attaches the named tool, activating it when this control is selected.
By default, this control only handles one tool at a time. Using the t/tool flag to associate a new tool will simply override the previous attached tool. If you use the amt/allowMultipleTools flag then you will be able to attach more than one tool with this control. Only one tool will be current within the control. To access the other tools press the right mouse button to display a popup menu containing all the tools associated with this control. If you set the piv/popupIndicatorVisible flag then a small arrow will be drawn on the control to indicate that additional tools are attached to this control.

    """
    pass
    


def toolCollection(string, numberOfCollectionItems=bool, defineTemplate="string", parent="string", gl=bool, select="string", collectionItemArray=bool, exists=bool, useTemplate="string"):
    """
    toolCollection is undoable, queryable, and editable.
    

    
This command creates a tool button collection. Collections are parented to the current default layout if no parent is specified with the -p/parent flag. As children of the layout they will be deleted when the layout is deleted. Collections may also span more than one window if the -gl/global flag is used. In this case the collection has no parent and must be explicitly deleted with the 'deleteUI' command when it is no longer wanted.

    """
    pass
    


def toolDropped(string):
    """
    toolDropped is undoable, NOT queryable, and NOT editable.
    

    
This command builds and executes the commands necessary to recreate the specified tool button. It is invoked when a tool is dropped on the shelf.

    """
    pass
    


def toolHasOptions():
    """
    toolHasOptions is undoable, NOT queryable, and NOT editable.
    

    
This command queries a tool to see if it has options. If it does, it returns true. Otherwise it returns false.

    """
    pass
    


def toolPropertyWindow(showCommand="string", icon="string", location="string", helpButton="string", field="string", resetButton="string", inMainWindow=bool, noviceMode=bool, selectCommand="string"):
    """
    toolPropertyWindow is undoable, queryable, and editable.
    

    
End users should only call this command as 1. a query (in the custom tool property sheet code) or 2. with no arguments to create the default tool property sheet. The more complex uses of it are internal.

    """
    pass
    


def torus(degree=int, minorSweep=int, axis="string", pivot="string", sections=int, radius="string", tolerance="string", object=bool, useTolerance=bool, polygon=int, spans=int, nodeState=int, name="string", heightRatio=float, startSweep=int, caching=bool, endSweep=int, constructionHistory=bool):
    """
    torus is undoable, queryable, and editable.
    

    
The torus command creates a new torus and/or a dependency node that creates one, and returns their names.

    """
    pass
    


def track(camera, upDistance01="string", left="string", down="string", right="string", upDistance02="string"):
    """
    track is undoable, NOT queryable, and NOT editable.
    

    
The track command translates a camera horizontally or vertically in the world space. The viewing-direction and up-direction of the camera are not altered. There is no translation in the viewing direction.
The track command can be applied to either a perspective or an orthographic camera.
When no camera name is supplied, this command is applied to the camera in the active view.

    """
    pass
    


def trackCtx(image1="string", trackScale=float, trackGeometry=bool, alternateContext=bool, history=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    trackCtx is undoable, queryable, and editable.
    

    
This command can be used to create a track context.

    """
    pass
    


def transferAttributes(before=bool, exclusive="string", split=bool, after=bool, flipUVs=int, searchScaleY=float, includeHiddenSelections=bool, transferColors=int, sourceUvSet="string", frontOfChain=bool, targetUvSet="string", prune=bool, sourceUvSpace="string", targetColorSet="string", geometryIndices=bool, colorBorders=int, sampleSpace=int, searchMethod=int, geometry="string", matchChoice=int, name="string", transferPositions=int, targetUvSpace="string", parallel=bool, sourceColorSet="string", transferNormals=int, ignoreSelected=bool, afterReference=bool, remove=bool, searchScaleX=float, searchScaleZ=float, deformerTools=bool, transferUVs=int):
    """
    transferAttributes is undoable, queryable, and editable.
    

    
Samples the attributes of a source surface (first argument) and transfers them onto a target surface (second argument).

    """
    pass
    


def transferShadingSets(sampleSpace=int, searchMethod=int):
    """
    transferShadingSets is undoable, queryable, and editable.
    

    
Command to transfer shading set assignments between meshes. The last mesh in the list receives the shading assignments from the other meshes.

    """
    pass
    


def transformCompare(dagObjectdagObject, root=bool):
    """
    transformCompare is undoable, NOT queryable, and NOT editable.
    

    
Compares two transforms passed as arguments. If they are the same, returns 0. If they are different, returns 1. If no transforms are specified in the command line, then the transforms from the active list are used.

    """
    pass
    


def transformLimits(object, remove=bool, enableTranslationZ=bool, scaleX=float, rotationY=int, translationZ="string", rotationX=int, enableScaleX=bool, translationX="string", enableRotationY=bool, translationY="string", enableScaleZ=bool, enableRotationZ=bool, scaleY=float, enableScaleY=bool, enableTranslationY=bool, enableTranslationX=bool, rotationZ=int, enableRotationX=bool, scaleZ=float):
    """
    transformLimits is undoable, queryable, and editable.
    

    
The transformLimits command allows us to set, edit, or query the limits of the transformation that can be applied to objects.
We can also turn any limits off which may have been previously set. When an object is first created, all the transformation limits are off by default.
Transformation limits allow us to control how much an object can be transformed. This is most useful for joints, although it can be used any place we would like to limit the movement of an object.
Default values are:
( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    """
    pass
    


def translator(string, list=bool, defaultOptions="string", filter=bool, optionsScript=bool, extension=bool, fileCompression="string", objectType=bool, readSupport=bool, loaded=bool, defaultFileRule=bool, writeSupport=bool):
    """
    translator is undoable, queryable, and NOT editable.
    

    
Set or query parameters associated with the file translators specified in as the argument.

    """
    pass
    


def treeLister(string, vnnString=bool, docTag="string", height=int, defineTemplate="string", parent="string", clearContents=bool, addVnnItem="string", numberOfPopupMenus=bool, useTemplate="string", favoritesList=bool, width=int, highlightColor=float, dragCallback="string", favoritesCallback="string", collapsePath="string", annotation="string", preventOverride=bool, popupMenuArray=bool, refreshCommand="string", addFavorite="string", exists=bool, resultsPathUnderCursor=bool, executeItem="string", enable=bool, enableBackground=bool, selectPath="string", visibleChangeCommand="string", visible=bool, expandPath="string", itemScript="string", removeItem="string", fullPathName=bool, dropCallback="string", noBackground=bool, backgroundColor=float, removeFavorite="string", addItem="string", manage=bool, expandToDepth=int, isObscured=bool):
    """
    treeLister is undoable, queryable, and editable.
    

    
This command creates/edits/queries the tree lister control. The optional argument is the name of the control.

    """
    pass
    


def treeView(string, docTag="string", attachButtonRight=int, height=int, displayLabel="string", useTemplate="string", itemDblClickCommand="string", itemVisible="string", popupMenuArray=bool, pressCommand=int, dropCallback="string", contextMenuCommand="string", clearSelection=bool, visibleChangeCommand="string", allowReparenting=bool, highlite="string", numberOfButtons=int, itemSelected="string", selectCommand="string", item="string", noBackground=bool, itemDblClickCommand2="string", buttonErase=bool, editLabelCommand="string", selectionChangedCommand="string", labelBackgroundColor="string", buttonTransparencyColor="string", selectionColor="string", itemIndex="string", isItemExpanded="string", itemRenamedCommand="string", defineTemplate="string", parent="string", highliteColor="string", enableLabel="string", selectItem="string", buttonStyle="string", displayLabelSuffix="string", highlightColor=float, children="string", ornamentColor="string", showItem="string", buttonVisible="string", buttonState="string", borderHighliteColor="string", visible=bool, expandItem="string", fontFace="string", backgroundColor=float, buttonTransparencyOverride="string", itemParent="string", buttonTooltip="string", image="string", dragAndDropCommand="string", dragCallback="string", buttonTextIcon="string", font="string", itemExists="string", allowHiddenParents=bool, removeItem="string", enable=bool, enableButton="string", borderHighlite="string", preventOverride=bool, removeAll=bool, rightPressCommand=int, addItem="string", isObscured=bool, allowMultiSelection=bool, numberOfPopupMenus=bool, manage=bool, itemAnnotation="string", reverseTreeOrder=bool, annotation="string", allowDragAndDrop=bool, hideButtons=bool, ignoreButtonClick="string", enableKeys=bool, textColor="string", exists=bool, enableBackground=bool, isLeaf="string", fullPathName=bool, expandCollapseCommand="string", ornament="string", width=int):
    """
    treeView is undoable, queryable, and editable.
    

    
This command creates a custom control.

    """
    pass
    


def trim(locatorV=float, selected=int, object=bool, shrink=bool, nodeState=int, constructionHistory=bool, locatorU=float, caching=bool, tolerance="string", name="string"):
    """
    trim is undoable, queryable, and editable.
    

    
This command trims a surface to its curves on surface by first splitting the surface and then selecting which regions to keep or discard.

    """
    pass
    


def truncateFluidCache():
    """
    truncateFluidCache is undoable, queryable, and editable.
    

    
This command sets the end time of a fluid cache to the current time. If the current time is less than the end time of the cache, the cache is truncated so that only the portion of the cache up to and including the current time is preserved.

    """
    pass
    


def truncateHairCache():
    """
    truncateHairCache is undoable, queryable, and editable.
    

    
This command sets the end time of a hair cache to the current time. If the current time is less than the end time of the cache, the cache is truncated so that only the portion of the cache up to and including the current time is preserved.

    """
    pass
    


def tumble(camera, pivotPoint="string", localTumble=int, azimuthAngle=int, rotationAngles=int, elevationAngle=int):
    """
    tumble is undoable, NOT queryable, and NOT editable.
    

    
The tumble command revolves the camera(s) by varying the azimuth and elevation angles in the perspective window. When both the azimuth and the elevation angles are supplied on the command line, the camera is firstly tumbled for the azimuth angle, then tumbled for the elevation angle.
When no camera name is supplied, this command is applied to the camera in the active view.
The camera's rotate pivot will override a specified pivot point if the rotate pivot is not at the camera's eye point.

    """
    pass
    


def tumbleCtx(image1="string", orthoStep=int, tumbleScale=float, localTumble=int, orthoLock=bool, objectTumble=bool, alternateContext=bool, image3="string", history=bool, autoOrthoConstrain=bool, toolName="string", exists=bool, image2="string", name="string", autoSetPivot=bool):
    """
    tumbleCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a tumble context.

    """
    pass
    


def turbulence(noiseRatio=float, magnitude=float, noiseLevel=int, phase=float, phaseX=float, phaseZ=float, perVertex=bool, maxDistance="string", attenuation=float, frequency=float, position="string", phaseY=float, name="string"):
    """
    turbulence is undoable, queryable, and editable.
    

    
A turbulence field causes irregularities (also called 'noise' or 'jitter') in the motion of affected objects.
Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def twoPointArcCtx(degree=int, image1="string", spans=int, image3="string", exists=bool, image2="string", name="string", history=bool):
    """
    twoPointArcCtx is undoable, queryable, and editable.
    

    
The twoPointArcCtx command creates a new context for creating two point circular arcs

    """
    pass
    


def ubercam(string):
    """
    ubercam is undoable, NOT queryable, and NOT editable.
    

    
Use this command to create a "ubercam" with equivalent behavior to all cameras used by shots in the sequencer.

    """
    pass
    


def uiTemplate(string, exists=bool):
    """
    uiTemplate is undoable, queryable, and editable.
    

    
This command creates a new command template object. Template objects can hold default flag arguments for multiple UI commands. The command arguments are specified with the individual commands using the -defineTemplate flag and the desired flags and arguments. See also setUITemplate.

    """
    pass
    


def unassignInputDevice(clutch="string", device="string"):
    """
    unassignInputDevice is undoable, queryable, and NOT editable.
    

    
This command deletes all command strings associated with this device.

    """
    pass
    


def undo():
    """
    undo is undoable, NOT queryable, and NOT editable.
    

    
Takes the most recent command from the undo list and undoes it.

    """
    pass
    


def undoInfo(undoName="string", openChunk=bool, printQueue=bool, length=int, stateWithoutFlush=bool, state=bool, closeChunk=bool, undoQueueEmpty=bool, redoQueueEmpty=bool, infinity=bool, redoName="string", chunkName="string"):
    """
    undoInfo is undoable, queryable, and NOT editable.
    

    
This command controls the undo/redo parameters.
In query mode, if invoked without flags (other than the query flag), this command will return the number of items currently on the undo queue.

    """
    pass
    


def unfold(optimizeAxis=int, iterations=int, pinSelected=bool, scale=float, useScale=bool, globalMethodBlend=float, globalBlend=float, pinUvBorder=bool, applyToShell=bool, areaWeight=float, stoppingThreshold=float):
    """
    unfold is undoable, NOT queryable, and NOT editable.
    

    
None

    """
    pass
    


def ungroup(objects, world=bool, relative=bool, absolute=bool, parent="string"):
    """
    ungroup is undoable, NOT queryable, and NOT editable.
    

    
This command ungroups the specified objects.
The objects will be placed at the same level in the hierarchy the group node occupied unless the -w flag is specified, in which case they will be placed under the world.
If an object is ungrouped and there is an object in the new group with the same name then this command will rename the ungrouped object.
See also: group, parent, instance, duplicate

    """
    pass
    


def uniform(directionX=float, magnitude=float, directionY=float, perVertex=bool, directionZ=float, attenuation=float, maxDistance="string", position="string", name="string"):
    """
    uniform is undoable, queryable, and editable.
    

    
A uniform field pushes objects in a fixed direction. The field strength, but not the field direction, depends on the distance from the object to the field location.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def unknownNode(plugin=bool, realClassName=bool, realClassTag=bool):
    """
    unknownNode is undoable, queryable, and NOT editable.
    

    
Allows querying of the data stored for unknown nodes (nodes that are defined by a plug-in that Maya could not load when loading a scene file).

    """
    pass
    


def unknownPlugin(list=bool, version=bool, dataTypes=bool, remove=bool, nodeTypes=bool):
    """
    unknownPlugin is undoable, queryable, and NOT editable.
    

    
Allows querying of the unknown plug-ins used by the scene, and provides a means to remove them.

    """
    pass
    


def unloadPlugin(stringstring, addCallback="string", removeCallback="string", force=bool):
    """
    unloadPlugin is undoable, NOT queryable, and NOT editable.
    

    
Unload plug-ins from Maya. After the successful execution of this command, plug-in services will no longer be available.

    """
    pass
    


def untangleUV(pinBorder=bool, pinUnselected=bool, pinSelected=bool, shapeDetail=float, mapBorder="string", relax="string", relaxTolerance=float, maxRelaxIterations=int):
    """
    untangleUV is undoable, NOT queryable, and NOT editable.
    

    
This command will aid in the creation of non-overlapping regions (i.e. polygons) in texture space by untangling texture UVs. This is done in two stages:
1) Use this command to map the UV border determined by the current selection or passed component into a shape that is more suitable for subsequent relaxation.
2) Relax all the internal texture UVs by performing a length minimization algorithm on all edges in texture space.

    """
    pass
    


def untrim(noChanges=bool, curveOnSurface=bool, object=bool, nodeState=int, replaceOriginal=bool, constructionHistory=bool, caching=bool, untrimAll=bool, name="string"):
    """
    untrim is undoable, queryable, and editable.
    

    
Untrim the surface.

    """
    pass
    


def upAxis(rotateView=bool, axis="string"):
    """
    upAxis is undoable, queryable, and NOT editable.
    

    
The upAxis command changes the world up direction. Current implementation provides only two choices of axis (the Y-axis or the Z-axis) as the world up direction.
By default, the ground plane in Maya is on the XY plane. Hence, the default up-direction is the direction of the positive Z-axis.
The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag is specified, the camera of currently active view is revolved about the X-axis such that the position of the groundplane in the view will remain the same as before the the up direction is changed.
The screen update is applied to all cameras of all views.

    """
    pass
    


def uvLink(objects, isValid=bool, make=bool, texture="string", b=bool, queryObject="string", uvSet="string"):
    """
    uvLink is undoable, queryable, and NOT editable.
    

    
This command is used to make, break and query UV linking relationships between UV sets on objects and textures that use those UV sets.
If no make, break or query flag is specified and both uvSet and texture flags are present, the make flag is assumed to be specified.
If no make, break or query flag is specified and only one of the uvSet and texture flags is present, the query flag is assumed to be specified.
The term "texture" in the context of UV linking is a bit of an oversimplification. In fact, UV sets can be linked to any node which takes UV coordinates as input. However in most cases it will be a texture to which you wish to link a UV set.

    """
    pass
    


def uvSnapshot(antiAliased=bool, uMin=float, uMax=float, blueColor=int, redColor=int, entireUVRange=bool, uvSetName="string", vMax=float, yResolution=int, fileFormat="string", overwrite=bool, vMin=float, greenColor=int, name="string", xResolution=int):
    """
    uvSnapshot is NOT undoable, NOT queryable, and NOT editable.
    

    
Builds an image containg the UVs of the selected objects.

    """
    pass
    


def vectorize(frameRate=int, height=int, browserView=bool, renderView=bool, endFrame=float, reflectionDepth=int, flashVersion=int, detailLevel=int, startFrame=float, outputFileName="string", camera="string", hiddenEdges=bool, highlightLevel=int, pixelAspectRatio=float, renderLayers=bool, currentFrame=bool, width=int, imageFormat="string", reflections=bool, fillStyle="string", highlights=bool, combineFillsEdges=bool, showBackFaces=bool, secondaryCurveFitting=bool, filenameFormat="string", byFrame=float, outlinesAtIntersections=bool, layer="string", shadows=bool, edgeWeight=float, svgAnimation="string", edgeDetail=bool, curveTolerance=float, customExtension="string", edgeColor=int, renderOptimization="string", minEdgeAngle=float, edgeStyle="string", svgCompression=bool):
    """
    vectorize is NOT undoable, NOT queryable, and NOT editable.
    

    
This command renders Maya scenes to various vector and raster formats using the Maya Vector renderer.

    """
    pass
    


def view2dToolCtx(image1="string", dolly=bool, track=bool, boxzoom=bool, alternateContext=bool, history=bool, toolName="string", exists=bool, image2="string", name="string", image3="string"):
    """
    view2dToolCtx is undoable, queryable, and editable.
    

    
This class creates a context for the View Tools "track", "dolly", and "box zoom" in the Hypergraph.

    """
    pass
    


def viewCamera(camera, move="string", sideView=bool, topView=bool):
    """
    viewCamera is undoable, NOT queryable, and NOT editable.
    

    
The viewCamera command is used to position a camera to look directly at the side or top of another camera. This is primarily useful for the user when he or she is setting depth-of-field and clipping planes, if they are being used.
The default behaviour: If no other flags are specified, the camera in the active panel is moved and the -t is presumed. If there is a camera selected, it is used as the target camera.

    """
    pass
    


def viewClipPlane(camera, nearClipPlane="string", farClipPlane="string", surfacesOnly=bool, autoClipPlane=bool):
    """
    viewClipPlane is undoable, queryable, and NOT editable.
    

    
The viewClipPlane command can be used to query or set a camera's clip planes. If a camera is not specified, the camera in the active view will be used. The near and far clip plane flags may be used in conjunction with the auto clip plane flag.

    """
    pass
    


def viewFit(camera, allObjects=bool, namespace="string", fitFactor=float, center=bool, animate=bool):
    """
    viewFit is undoable, NOT queryable, and NOT editable.
    

    
The viewFit command positions the specified camera so its point-of-view contains all selected objects other than itself. If no objects are selected, everything is fit to the view (excepting cameras, lights, and sketching plannes). The fit-factor, if specified, determines how much of the view should be filled. If a camera is not specified, the camera in the active view will be used. After the camera is moved, its center of interest is set to the center of the bounding box of the objects.

    """
    pass
    


def viewHeadOn(camera):
    """
    viewHeadOn is undoable, NOT queryable, and NOT editable.
    

    
The viewHeadOn command positions the specified camera so it is looking "down" the normal of the live object, and fitted to the live object. If the live object is a surface, an arbitrary normal is chosen.

    """
    pass
    


def viewLookAt(camera, position="string"):
    """
    viewLookAt is undoable, NOT queryable, and NOT editable.
    

    
The viewLookAt command positions the specified camera so it is looking at the centroid of all selected objects. If no objects are specified the camera will look at the ground plane.

    """
    pass
    


def viewManip(bottomLeft=bool, drawCompass=bool, size="string", bottomRight=bool, zoomToFitScene=bool, compassAngle=float, visible=bool, topRight=bool, restoreCenter=bool, dragSnap=bool, levelCamera=bool, minOpacity=float, topLeft=bool, fitToView=bool):
    """
    viewManip is undoable, queryable, and NOT editable.
    

    
Mel access to the view cube manipulator.

    """
    pass
    


def viewPlace(camera, fieldOfView=int, eyePoint="string", lookAt="string", ortho=bool, perspective=bool, viewDirection="string", upDirection="string", animate=bool):
    """
    viewPlace is undoable, NOT queryable, and NOT editable.
    

    
This command positions the camera as specified. The lookAt and viewDirection flags are mutually exclusive, as are the ortho and perspective flags. If this command switches a camera from ortho to perspective or the other way around without specifying a new field of view, then one is calculated based on a heuristic involving the selected objects.
If the camera is not specified on the command line, the command will check to see if there is a camera on the active list.
The user should be aware that some positions will be unattainable. For example, using a new camera located at the origin and specifying a lookAt of [0 0 -5] and an up of [1 1 1]. In these cases, the camera will always aim at the lookAt, and the new up direction will be determined by transforming the specified up into camera space and then projecting this vector onto a plane defined by the camera's up and right vectors. Using the example above, the new up vector will be [1 1 0].

    """
    pass
    


def viewSet(camera, viewNegativeZ=bool, bottom=bool, viewX=bool, viewNegativeY=bool, previousView=bool, viewNegativeX=bool, fit=bool, leftSide=bool, animate=bool, persp=bool, nextView=bool, top=bool, viewY=bool, back=bool, rightSide=bool, viewZ=bool, side=bool, namespace="string", fitFactor=float, keepRenderSettings=bool, home=bool, front=bool):
    """
    viewSet is undoable, queryable, and NOT editable.
    

    
This command positions the camera to one of the pre-defined positions. If the fit flag is set in conjunction with persp, top, side, or front, the view is "fit" based on the list of selected objects (if there are any) or on all the objects if nothing is selected. Notice that the fit flag cannot be set in conjunction with view along axis commands like viewX. If a camera is not specified, the camera in the active view will be used. If no flag is specified, the camera is set to the home position.

    """
    pass
    


def visor(popupMenuScript="string", selectedGadgets="string", parent="string", addFolder=bool, rebuild=bool, showFolders=bool, refreshSwatch="string", allowZooming=bool, refreshAllSwatches=bool, showNodes=bool, transform="string", type="string", showDividers=bool, restrictPanAndZoom=bool, allowPanningInX=bool, stateString=bool, deleteFolder="string", editFolder="string", name="string", saveSwatches=bool, scrollPercent=float, addNodes="string", menu="string", showFiles=bool, refreshSelectedSwatches=bool, path="string", openFolder=bool, reset=bool, allowPanningInY=bool, folderList="string", nodeType="string", command="string", style="string", scrollBar="string", openDirectories=bool):
    """
    visor is undoable, queryable, and NOT editable.
    

    
Command for the creation and manipulation of a Visor UI element. The Visor is used to display the contents of a scene (rendering related nodes in particular), as well as files on disk which the user may wish to bring into the scene (shader and texture libraries for example).

    """
    pass
    


def vnn(libraries="string", nodes="string", runTimes=bool, listPortTypes="string", flushProxies="string"):
    """
    vnn is NOT undoable, queryable, and NOT editable.
    

    
This command is used for operations that apply to a whole VNN runtime, for example Bifrost. The Create Node window uses it to build its list of nodes.

    """
    pass
    


def vnnCompound(renameNode="string", addNode="string", queryPortDataType="string", specializedTypeName=bool, queryMetaData="string", saveAs="string", resetToFactory="string", connectedToOutput=bool, queryIsReferenced=bool, listPortChildren="string", queryPortMetaDataValue="string", listNodes=bool, explode="string", movePort="string", inputPort=bool, createOutputPort="string", setIsReferenced=bool, publish="string", outputPort=bool, removeNode="string", create="string", connectedTo="string", setPortMetaDataValue="string", createInputPort="string", moveNodeIn="string", connectedToInput=bool, canResetToFactory="string", addStatePortUI=bool, nodeType="string", deletePort="string", setPortDataType="string", portDefaultValue="string", renamePort="string", connected=bool, setMetaData="string", listPorts=bool, queryIsImported=bool, queryPortDefaultValue="string"):
    """
    vnnCompound is undoable, NOT queryable, and NOT editable.
    

    
The vnnCompound command is used to operate compound and its VNN graph. The first parameter is the full name of the DG node that contains the VNN graph. The second parameter is the name of the compound.

    """
    pass
    


def vnnConnect(disconnect=bool):
    """
    vnnConnect is undoable, NOT queryable, and NOT editable.
    

    
Makes a connection between two VNN node ports. The first parameter is the full name of the DG node that contains the VNN graph. The next two parameters are the full path of the ports from the root of the VNN container. This command can be used for compound or node connections, and the parameters can be out-of-order.

    """
    pass
    


def vnnCopy(sourceNode="string"):
    """
    vnnCopy is NOT undoable, NOT queryable, and NOT editable.
    

    
Copy a set of VNN nodes to clipper board. The first parameter is the full name of the DG node that contains the VNN graph. The second parameter is the full path of the parent VNN compound. The source VNN nodes must be set by the flag "-sourceNode".

    """
    pass
    


def vnnNode(queryIsUnresolved=bool, queryTypeName=bool, queryPortDataType="string", listConnectedNodes=bool, setPortDataType="string", portDefaultValue="string", connectedTo="string", connected=bool, queryAcceptablePortDataTypes="string", queryPortDefaultValue="string", listPortChildren="string", listPorts=bool):
    """
    vnnNode is undoable, NOT queryable, and NOT editable.
    

    
The vnnNode command is used to operate vnnNode and query its port and connections. The first argument is the full name of the DG node that the VNN node is in. The second argument is the name of the full path of the VNN node.

    """
    pass
    


def vnnPaste():
    """
    vnnPaste is undoable, NOT queryable, and NOT editable.
    

    
Paste the copied VNN nodes to target VNN compound. The first parameter is the full name of the DG node that contains the VNN graph. The second parameter is the full path of the target VNN compound. A "vnnCopy" must be called before this command is called.

    """
    pass
    


def volumeAxis(turbulenceOffsetY=float, perVertex=bool, maxDistance="string", turbulenceFrequencyZ=float, directionX=float, alongAxis=float, turbulenceFrequencyX=float, directionalSpeed=float, turbulenceFrequencyY=float, turbulenceSpeed=float, aroundAxis=float, awayFromAxis=float, awayFromCenter=float, name="string", detailTurbulence=float, magnitude=float, directionZ=float, attenuation=float, turbulence=float, turbulenceOffsetX=float, turbulenceOffsetZ=float, invertAttenuation=bool, directionY=float, position="string"):
    """
    volumeAxis is undoable, queryable, and editable.
    

    
A volume axis field can push particles in four directions, defined with respect to a volume: along the axis, away from the axis or center, around the axis, and in a user-specified direction. These are analogous to the emission speed controls of volume emitters. The volume axis field also contains a wind turbulence model (different from the turbulence field) that simulates an evolving flow of liquid or gas. The turbulence has a build in animation that is driven by a connection to a time node.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def volumeBind(influence="string", name="string"):
    """
    volumeBind is undoable, queryable, and editable.
    

    
Command for creating and editing volume binding nodes. The node is use for storing volume data to define skin weighting data.

    """
    pass
    


def vortex(axisY=float, magnitude=float, axisX=float, position="string", perVertex=bool, maxDistance="string", attenuation=float, axisZ=float, name="string"):
    """
    vortex is undoable, queryable, and editable.
    

    
A vortex field pulls objects in a circular direction, like a whirlpool or tornado. Objects affected by the vortex field tend to rotate around the axis specified by -ax, -ay, and -az.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def waitCursor(state=bool):
    """
    waitCursor is undoable, queryable, and NOT editable.
    

    
This command sets/resets a wait cursor for the entire Maya application. This works as a stack, such that for each waitCursor -state on command executed there should be a matching waitCursor -state off command pending.
Warning: If a script fails that has turned the wait cursor on, the wait cursor may be left on. You need to turn it off manually from the command line by entering and executing the command 'waitCursor -state off'.

    """
    pass
    


def walkCtx(image1="string", walkSensitivity=float, alternateContext=bool, walkSpeed=float, walkHeight=float, history=bool, crouchCount=float, toolName="string", walkToolHud=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    walkCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a walk context.

    """
    pass
    


def warning(showLineNumber=bool, noContext=bool):
    """
    warning is NOT undoable, NOT queryable, and NOT editable.
    

    
The warning command is provided so that the user can issue warning messages from his/her scripts. The string argument is displayed in the command window (or stdout if running in batch mode) after being prefixed with a warning message heading and surrounded by the appropriate language separators (# for Python, // for Mel).

    """
    pass
    


def webBrowser(string, docTag="string", height=int, defineTemplate="string", parent="string", numberOfPopupMenus=bool, useTemplate="string", width=int, highlightColor=float, popupMenuArray=bool, annotation="string", enable=bool, dropCallback="string", exists=bool, enableBackground=bool, visibleChangeCommand="string", visible=bool, fullPathName=bool, preventOverride=bool, dragCallback="string", noBackground=bool, backgroundColor=float, manage=bool, isObscured=bool):
    """
    webBrowser is undoable, queryable, and editable.
    

    
This command is obsolete and will be removed in next version of Maya. The internal web browser of Maya has been replaced by a plug-in which allows your own browser to connect with Maya. Please refer help for information on how to setup communication of Maya with external web browser application.

    """
    pass
    


def webView(urlAddress="string", windowHeight=int, windowWidth=int):
    """
    webView is undoable, NOT queryable, and NOT editable.
    

    
This command allows the user to bring up a web page view

    """
    pass
    


def whatsNewHighlight(highlightColor=float, highlightOn=bool, showStartupDialog=bool):
    """
    whatsNewHighlight is undoable, queryable, and NOT editable.
    

    
This command is used to toggle the What's New highlighting feature, and the display of the settings dialog for the feature that appears on startup.

    """
    pass
    


def window(string, docTag="string", height=int, defineTemplate="string", parent="string", leftEdge=int, useTemplate="string", menuBarResize=bool, restoreCommand="string", topEdge=int, dockCorner="string", minimizeButton=bool, resizeToFitChildren=bool, titleBar=bool, menuBarCornerWidget="string", widthHeight=int, mainWindow=bool, exists=bool, numberOfMenus=bool, dockStation=bool, visible=bool, maximizeButton=bool, menuArray=bool, topLeftCorner=int, closeCommand="string", state="string", dockingLayout="string", sizeable=bool, nestedDockingEnabled=bool, iconName="string", menuBarVisible=bool, iconify=bool, titleBarMenu=bool, retain=bool, backgroundColor=float, width=int, interactivePlacement=bool, menuBar=bool, frontWindow=bool, menuIndex="string", title="string", minimizeCommand="string", toolbox=bool):
    """
    window is undoable, queryable, and editable.
    

    
This command creates a new window but leaves it invisible. It is most efficient to add the window's elements and then make it visible with the showWindow command. The window can have an optional menu bar. Also, the title bar and minimize/maximize buttons can be turned on or off. If the title bar is off, then you cannot have minimize or maximize buttons.
Note: The window will require a control layout of some kind to arrange the controls (buttons, sliders, fields, etc.). Examples of control layouts are columnLayout, formLayout, rowLayout, etc.
Note: This command will clear the uiTemplate stack. Templates for a window need to be set after the window cmd.

    """
    pass
    


def windowPref(topLeftCorner=int, remove=bool, height=int, removeAll=bool, maximized=bool, saveAll=bool, loadAll=bool, leftEdge=int, width=int, enableAll=bool, widthHeight=int, restoreMainWindowState="string", saveMainWindowState="string", exists=bool, topEdge=int, parentMain=bool):
    """
    windowPref is undoable, queryable, and editable.
    

    
Create or modify preferred window attributes. The size and position of a window is retained during and between application sessions. A default window preference is created when a window is closed. Window preferences must be named and, consequently, only affect the window with a matching name.
Note that window preferences are not applied to the main Maya window nor the Command window.

    """
    pass
    


def wire(objects, before=bool, exclusive="string", dropoffDistance=int, after=bool, ignoreSelected=bool, includeHiddenSelections=bool, localInfluence=float, frontOfChain=bool, holder=int, prune=bool, geometryIndices=bool, split=bool, envelope=float, geometry="string", name="string", wireCount=int, crossingEffect=float, groupWithBase=bool, afterReference=bool, remove=bool, wire="string", deformerTools=bool, parallel=bool):
    """
    wire is undoable, queryable, and editable.
    

    
This command creates a wire deformer.
In the create mode the selection list is treated as the object(s) to be deformed, Wires are specified with the -w flag. Each wire can optionally have a holder which helps define the the regon of the object that is affected by the deformer.

    """
    pass
    


def wireContext(image1="string", envelope="string", exclusive=bool, localInfluence="string", name="string", deformationOrder="string", image3="string", exclusivePartition="string", groupWithBase=bool, holder=bool, dropoffDistance="string", exists=bool, image2="string", crossingEffect="string", history=bool):
    """
    wireContext is undoable, queryable, and editable.
    

    
This command creates a tool that can be used to create a wire deformer.

    """
    pass
    


def workspace(string, projectPath="string", updateAll=bool, fileRuleList=bool, fileRuleEntry="string", renderTypeEntry="string", renderType="string", active=bool, expandName="string", objectType="string", saveWorkspace=bool, shortName=bool, objectTypeList=bool, fileRule="string", filter=bool, newWorkspace=bool, listFullWorkspaces=bool, listWorkspaces=bool, fullName=bool, objectTypeEntry="string", variableEntry="string", rootDirectory=bool, update=bool, list=bool, renderTypeList=bool, variableList=bool, removeVariableEntry="string", create="string", baseWorkspace="string", directory="string", variable="string", removeFileRuleEntry="string", openWorkspace=bool):
    """
    workspace is undoable, queryable, and NOT editable.
    

    
Create, open, or edit a workspace associated with a given workspace file.
The string argument represents the workspace. If no workspace is specified then the current workspace is assumed.
A workspace provides the underlying definition of a Maya Project. Each project has an associated workspace file, named workspace.mel, which is stored in the project root directory. The workspace file defines a set of rules that map file types to their storage, either relative to the project root or as an absolute location. These rules are used when resolving file paths at runtime.
The workspace command operates directly on the low-level definition of the workspace to read, change and store the definition to the underlying file. Use of this command is not generally required, for most purposes it is recommended that project definition changes be done via the Project Window in the User Interface. Multiple actions go under the assumption that given paths exist.

    """
    pass
    


def workspaceControl(name, dockToPanel="string", defineTemplate="string", requiredControl="string", useTemplate="string", label="string", heightProperty="string", tabToControl="string", widthProperty="string", width=bool, collapse=bool, checksPlugins=bool, height=bool, loadImmediately=bool, requiredPlugin="string", exists=bool, restore=bool, initialWidth=int, visibleChangeCommand="string", visible=bool, closeCommand="string", dockToMainWindow="string", minimumWidth=bool, dockToControl="string", r=bool, uiScript="string", retain=bool, initialHeight=int, close=bool, floating=bool):
    """
    workspaceControl is undoable, queryable, and editable.
    

    
Creates and manages the widget used to host windows in a layout that enables docking and stacking windows together.

    """
    pass
    


def workspaceControlState(topLeftCorner=int, remove=bool, height=int, defaultWidthHeight=int, leftEdge=int, width=int, defaultTopLeftCorner=int, maximized=bool, widthHeight=int, exists=bool, topEdge=int):
    """
    workspaceControlState is undoable, queryable, and editable.
    

    
Create or modify preferred window attributes for workspace controls. The size and position of a workspace control is retained during application sessions (although position only applies to workspace controls that are alone in a floating workspace docking panel). A default workspace control state is created when a workspace control is closed. Workspace control states must be named and, consequently, only affect the workspace control with a matching name.

    """
    pass
    


def workspaceLayoutManager(name, delete="string", listLayouts=bool, parentWorkspaceControl="string", type="string", modified="string", listUserLayouts=bool, i="string", saveAs="string", current=bool, restoreMainWindowControls=bool, save=bool, reset=bool, setCurrentCallback="string", setCurrent="string", collapseMainWindowControls="string"):
    """
    workspaceLayoutManager is undoable, queryable, and editable.
    

    
The Workspace Layout Manager loads and saves the layout of the various toolbars and windows in the user interface. This command allows listing and managing their properties.

    """
    pass
    


def workspacePanel(exists=bool, useTemplate="string", defineTemplate="string", mainWindow=bool):
    """
    workspacePanel is undoable, queryable, and editable.
    

    
This is not a real description - just to get docs to build.

    """
    pass
    


def wrinkle(randomness="string", axis="string", envelope="string", uvSpace="string", wrinkleCount=int, branchDepth=int, thickness="string", branchCount=int, style="string", crease="string", wrinkleIntensity="string", dropoffDistance="string", center="string"):
    """
    wrinkle is undoable, NOT queryable, and NOT editable.
    

    
The wrinkle command is used to create a network of wrinkles on a surface. It automatically creates a network of wrinkle curves that control a wire deformer. The wrinkle curves are attached to a cluster deformer.

    """
    pass
    


def wrinkleContext(image1="string", wrinkleIntensity="string", style="string", wrinkleCount=int, branchDepth=int, thickness="string", branchCount=int, randomness="string", history=bool, exists=bool, image2="string", name="string", image3="string"):
    """
    wrinkleContext is undoable, queryable, and editable.
    

    
This command creates a context that creates wrinkles.

    """
    pass
    


def writeTake(noTime=bool, take="string", virtualDevice="string", device="string", precision=int, angle="string", linear="string"):
    """
    writeTake is undoable, NOT queryable, and NOT editable.
    

    
This action writes a take from a device with recorded data to a take (.mov) file. The writeTake action can also write the virtual definition of a device.
See also: recordDevice, readTake, defineVirtualDevice

    """
    pass
    


def xform(objects, reflectionAboutZ=bool, rotateAxis=int, shear=float, translation="string", reflectionAboutBBox=bool, relative=bool, matrix=float, reflectionTolerance=float, reflectionAboutX=bool, zeroTransformPivots=bool, rotateOrder="string", worldSpace=bool, objectSpace=bool, centerPivots=bool, boundingBox=bool, scale=float, preserve=bool, scaleTranslation="string", centerPivotsOnComponents=bool, absolute=bool, scalePivot="string", rotation=int, preserveUV=bool, worldSpaceDistance=bool, rotatePivot="string", euler=bool, reflection=bool, deletePriorHistory=bool, pivots="string", boundingBoxInvisible=bool, reflectionAboutOrigin=bool, rotateTranslation="string", reflectionAboutY=bool):
    """
    xform is undoable, queryable, and NOT editable.
    

    
This command can be used query/set any element in a transformation node. It can also be used to query some values that cannot be set directly such as the transformation matrix or the bounding box. It can also set both pivot points to convenient values.
All values are specified in transformation coordinates. (attribute-space)
In addition, the attributes are applied/returned in the order in which they appear in the flags section. (which corresponds to the order they appear in the transformation matrix as given below)
See also: move, rotate, scale
Notes
The transformation matrix for a node is built by post-multiplying the following matrices in the given order (Note: rotations are applied according to the rotation order parameter and the 6 different rotation possibilities are not shown below)
-1                       -1
[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
where:
[sp] = |  1      0        0       0 | = scale pivot matrix
|  0      1        0       0 |
|  0      0        1       0 |
| -spx   -spy     -spz     1 |
[s]  = |  sx     0        0       0 | = scale matrix
|  0      sy       0       0 |
|  0      0        sz      0 |
|  0      0        0       1 |
[sh] = |  1      0        0       0 | = shear matrix
|  xy     1        0       0 |
|  xz     yz       1       0 |
|  0      0        0       1 |
-1
[sp] = |  1       0       0       0 | = scale pivot inverse matrix
|  0       1       0       0 |
|  0       0       1       0 |
|  spx     spy     spz     1 |
[st] = |  1       0       0       0 | = scale translate matrix
|  0       1       0       0 |
|  0       0       1       0 |
|  stx     sty     stz     1 |
[rp] = |  1       0       0       0 | = rotate pivot matrix
|  0       1       0       0 |
|  0       0       1       0 |
| -rpx    -rpy    -rpz     1 |
[ar] = |  *       *       *       0 | = axis rotation matrix
|  *       *       *       0 |   (composite rotation,
|  *       *       *       0 |    see [rx], [ry], [rz]
|  0       0       0       1 |    below for details)
[rx] = |  1       0       0       0 | = rotate X matrix
|  0       cos(x)  sin(x)  0 |
|  0      -sin(x)  cos(x)  0 |
|  0       0       0       1 |
[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
|  0       1       0       0 |
|  sin(y)  0       cos(y)  0 |
|  0       0       0       1 |
[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
| -sin(z)  cos(z)  0       0 |
|  0       0       1       0 |
|  0       0       0       1 |
-1
[rp] = |  1       0       0       0 | = rotate pivot matrix
|  0       1       0       0 |
|  0       0       1       0 |
|  rpx     rpy     rpz     1 |
[rt] = |  1       0       0       0 | = rotate translate matrix
|  0       1       0       0 |
|  0       0       1       0 |
|  rtx     rty     rtz     1 |
[t]  = |  1       0       0       0 | = translation matrix
|  0       1       0       0 |
|  0       0       1       0 |
|  tx      ty      tz      1 |

    """
    pass
    


def xformConstraint(alongNormal=int, live=bool, type="string"):
    """
    xformConstraint is undoable, queryable, and editable.
    

    
This command allows you to change the transform constraint used by the transform tools during component transforms.

    """
    pass
    


def xpmPicker(fileName="string", parent="string"):
    """
    xpmPicker is undoable, NOT queryable, and NOT editable.
    

    
Open a dialog and ask you to choose a xpm file

    """
    pass
    

