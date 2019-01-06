
def aaf2fcp(deleteFile=boolean, dstPath=string, getFileName=int, progress=int, srcFile=string, terminate=int, waitCompletion=int):
    """
    aaf2fcp is NOT undoable, NOT queryable, and NOT editable.
    

    
This command is used to convert an aff file to a Final Cut Pro (fcp) xml file The conversion process can take several seconds to complete and the command is meant to be run asynchronously

    """
    pass
    


def about(apiVersion=boolean, application=boolean, batch=boolean, buildDirectory=boolean, buildVariant=boolean, codeset=boolean, compositingManager=boolean, connected=boolean, ctime=boolean, currentDate=boolean, currentTime=boolean, cutIdentifier=boolean, date=boolean, environmentFile=boolean, evalVersion=boolean, file=boolean, fontInfo=boolean, helpDataDirectory=boolean, installedVersion=boolean, irix=boolean, is64=boolean, languageResources=boolean, linux=boolean, linux64=boolean, liveUpdate=boolean, localizedResourceLocation=boolean, ltVersion=boolean, macOS=boolean, macOSppc=boolean, macOSx86=boolean, ntOS=boolean, operatingSystem=boolean, operatingSystemVersion=boolean, preferences=boolean, product=boolean, qtVersion=boolean, tablet=boolean, tabletMode=boolean, uiLanguage=boolean, uiLanguageForStartup=boolean, uiLanguageIsLocalized=boolean, uiLocaleLanguage=boolean, version=boolean, win64=boolean, windowManager=boolean, windows=boolean):
    """
    about is undoable, NOT queryable, and NOT editable.
    

    
This command displays version information about the application if it is executed without flags. If one of the above flags is specified then the specified version information is returned.

    """
    pass
    


def addAttr(attributeType=string, binaryTag=string, cachedInternally=boolean, category=string, dataType=string, defaultValue=float, disconnectBehaviour=uint, enumName=string, exists=boolean, fromPlugin=boolean, hasMaxValue=boolean, hasMinValue=boolean, hasSoftMaxValue=boolean, hasSoftMinValue=boolean, hidden=boolean, indexMatters=boolean, internalSet=boolean, keyable=boolean, longName=string, maxValue=float, minValue=float, multi=boolean, niceName=string, numberOfChildren=uint, parent=string, proxy=string, readable=boolean, shortName=string, softMaxValue=float, softMinValue=float, storable=boolean, usedAsColor=boolean, usedAsFilename=boolean, usedAsProxy=boolean, writable=boolean):
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
    


def addDynamic(*args, **kwargs):
    """
    addDynamic is undoable, NOT queryable, and NOT editable.
    

    
Makes the "object" specified as second argument the source of an existing field or emitter specified as the first argument. In practical terms, what this means is that a field will emanate its force from its owner object, and an emitter will emit from its owner object.
addDynamic makes the specified field or emitter a child of the owner's transform (adding it to the model if it was not already there), and makes the necessary attribute connections.
If either of the arguments is omitted, addDynamic searches the selection list for objects to use instead. If more than one possible owner or field/emitter is selected, addDynamic will do nothing.
If the specified field/emitter already has a source, addDynamic will remove the current source and replace it with the newly specified source.
If a subset of the owner object's cvs/particles/vertices is selected, addDynamic will add the field/emitter to that subset only.

    """
    pass
    


def addExtension(attributeType=string, binaryTag=string, cachedInternally=boolean, category=string, dataType=string, defaultValue=float, disconnectBehaviour=uint, enumName=string, exists=boolean, fromPlugin=boolean, hasMaxValue=boolean, hasMinValue=boolean, hasSoftMaxValue=boolean, hasSoftMinValue=boolean, hidden=boolean, indexMatters=boolean, internalSet=boolean, keyable=boolean, longName=string, maxValue=float, minValue=float, multi=boolean, niceName=string, nodeType=string, numberOfChildren=uint, parent=string, proxy=string, readable=boolean, shortName=string, softMaxValue=float, softMinValue=float, storable=boolean, usedAsColor=boolean, usedAsFilename=boolean, usedAsProxy=boolean, writable=boolean):
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
    


def addMetadata(channelName=string, channelType=string, indexType=string, scene=boolean, streamName=string, structure=string):
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
    


def addPP( objects , attribute=string):
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
    


def affectedNet( node... , type=string):
    """
    affectedNet is undoable, queryable, and editable.
    

    
This command gets the list of attributes on a node or node type and creates nodes of type TdnAffect, one for each attribute, that are connected iff the source node's attribute affects the destination node's attribute.

    """
    pass
    


def affects(string, by=boolean, type=string):
    """
    affects is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns the list of attributes on a node or node type which affect the named attribute.

    """
    pass
    


def aimConstraint( target... object , aimVector=float, float, float, layer=string, maintainOffset=boolean, name=string, offset=float, float, float, remove=boolean, skip=string, targetList=boolean, upVector=float, float, float, weight=float, weightAliasList=boolean, worldUpObject=name, worldUpType=string, worldUpVector=float, float, float):
    """
    aimConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation to point at a target object or at the average position of a number of targets.
An aimConstraint takes as input one or more "target" DAG transform nodes at which to aim the single "constraint object" DAG transform node. The aimConstraint orients the constrained object such that the aimVector (in the object's local coordinate system) points to the in weighted average of the world space position target objects. The upVector (again the the object's local coordinate system) is aligned in world space with the worldUpVector.

    """
    pass
    


def air( objects , attenuation=float, directionX=float, directionY=float, directionZ=float, enableSpread=boolean, fanSetup=boolean, inheritRotation=boolean, inheritVelocity=float, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear, speed=float, spread=float, velocityComponentOnly=boolean, wakeSetup=boolean, windSetup=boolean):
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
    


def aliasAttr(remove=boolean):
    """
    aliasAttr is undoable, queryable, and editable.
    

    
Allows aliases (alternate names) to be defined for any attribute of a specified node. When an attribute is aliased, the alias will be used by the system to display information about the attribute. The user may, however, freely use either the alias or the original name of the attribute. Only a single alias can be specified for an attribute so setting an alias on an already-aliased attribute destroys the old alias.

    """
    pass
    


def align(alignToLead=boolean, coordinateSystem=name, xAxis=string, yAxis=string, zAxis=string):
    """
    align is undoable, NOT queryable, and NOT editable.
    

    
Align or spread objects along X Y and Z axis.

    """
    pass
    


def alignCtx( contextName , align=boolean, anchorFirstObject=boolean, distribute=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, showAlignTouch=boolean):
    """
    alignCtx is undoable, queryable, and editable.
    

    
The alignCtx command creates a tool for aligning and distributing objects.

    """
    pass
    


def alignCurve( curve curve , caching=boolean, constructionHistory=boolean, curvatureContinuity=boolean, curvatureScale1=float, curvatureScale2=float, joinParameter=float, name=string, nodeState=int, object=boolean, positionalContinuity=boolean, positionalContinuityType=int, replaceOriginal=boolean, reverse1=boolean, reverse2=boolean, tangentContinuity=boolean, tangentContinuityType=int, tangentScale1=float, tangentScale2=float):
    """
    alignCurve is undoable, queryable, and editable.
    

    
The curve align command is used to align curves in maya. The main alignment options are positional, tangent and curvature continuity. Curvature continuity implies tangent continuity.
Positional continuity means the curves (move) or the ends of the curves (modify) are changed.
Tangent continuity means one of the curves is modified to be tangent at the points where they meet.
Curvature continuity means one of the curves is modified to be curvature continuous as well as tangent.
The default behaviour, when no curves or flags are passed, is to only do positional and tangent continuity on the active list with the end of the first curve and the start of the other curve used for alignment.

    """
    pass
    


def alignSurface( surface surface , caching=boolean, constructionHistory=boolean, curvatureContinuity=boolean, curvatureScale1=float, curvatureScale2=float, directionU=boolean, joinParameter=float, name=string, nodeState=int, object=boolean, positionalContinuity=boolean, positionalContinuityType=int, replaceOriginal=boolean, reverse1=boolean, reverse2=boolean, swap1=boolean, swap2=boolean, tangentContinuity=boolean, tangentContinuityType=int, tangentScale1=float, tangentScale2=float, twist=boolean):
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
    


def allNodeTypes(includeAbstract=boolean):
    """
    allNodeTypes is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns a list containing the type names of every kind of creatable node registered with the system. Note that some node types are abstract and cannot be created. These will not show up on this list. (e.g. transform and polyShape both inherit from dagObject, but dagObject cannot be created directly so it will not appear on this list.)

    """
    pass
    


def ambientLight(ambientShade=float, discRadius=linear, intensity=float, name=string, rgb=float, float, float, shadowColor=float, float, float, shadowDither=float, shadowSamples=int, softShadow=boolean, useRayTraceShadows=boolean):
    """
    ambientLight is undoable, queryable, and editable.
    

    
The ambientLight command is used to edit the parameters of existing ambientLights, or to create new ones. The default behaviour is to create a new ambientlight.

    """
    pass
    


def angleBetween(constructionHistory=boolean, euler=boolean, vector1=linear, linear, linear, vector2=linear, linear, linear):
    """
    angleBetween is undoable, NOT queryable, and NOT editable.
    

    
Returns the axis and angle required to rotate one vector onto another. If the construction history (ch) flag is ON, then the name of the new dependency node is returned.

    """
    pass
    


def animCurveEditor( editorName , areCurvesSelected=boolean, autoFit=string, classicMode=boolean, clipTime=string, constrainDrag=uint, control=boolean, curvesShown=boolean, curvesShownForceUpdate=boolean, defineTemplate=string, denormalizeCurvesCommand=string, displayActiveKeyTangents=string, displayActiveKeys=string, displayInfinities=string, displayKeys=string, displayNormalized=boolean, displayTangents=string, displayValues=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, lookAt=string, mainListConnection=string, menu=script, normalizeCurvesCommand=string, outliner=string, panel=string, parent=string, preSelectionHighlight=boolean, renormalizeCurves=boolean, resultSamples=time, resultScreenSamples=int, resultUpdate=string, selectionConnection=string, showActiveCurveNames=boolean, showBufferCurves=string, showCurveNames=boolean, showResults=string, showUpstreamCurves=boolean, smoothness=string, snapTime=string, snapValue=string, stackedCurves=boolean, stackedCurvesMax=float, stackedCurvesMin=float, stackedCurvesSpace=float, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    animCurveEditor is undoable, queryable, and editable.
    

    
Edit a characteristic of a graph editor

    """
    pass
    


def animDisplay(modelUpdate=string, refAnimCurvesEditable=boolean, timeCode=boolean, timeCodeOffset=string):
    """
    animDisplay is undoable, queryable, and editable.
    

    
This command changes certain display options used by animation windows.

    """
    pass
    


def animLayer(addRelatedKG=boolean, addSelectedObjects=boolean, affectedLayers=boolean, animCurves=boolean, attribute=string, baseAnimCurves=boolean, bestAnimLayer=boolean, bestLayer=boolean, blendNodes=boolean, children=string, collapse=boolean, copy=string, copyAnimation=string, copyNoAnimation=string, excludeBoolean=boolean, excludeDynamic=boolean, excludeEnum=boolean, excludeRotate=boolean, excludeScale=boolean, excludeTranslate=boolean, excludeVisibility=boolean, exists=boolean, extractAnimation=string, findCurveForPlug=string, forceUIRebuild=boolean, forceUIRefresh=boolean, layeredPlug=string, lock=boolean, maxLayers=boolean, moveLayerAfter=string, moveLayerBefore=string, mute=boolean, override=boolean, parent=string, passthrough=boolean, preferred=boolean, removeAllAttributes=boolean, removeAttribute=string, root=string, selected=boolean, solo=boolean, weight=float, writeBlendnodeDestinations=boolean):
    """
    animLayer is undoable, queryable, and editable.
    

    
This command creates and edits animation layers.

    """
    pass
    


def animView( string , endTime=time, maxValue=float, minValue=float, nextView=boolean, previousView=boolean, startTime=time):
    """
    animView is undoable, queryable, and editable.
    

    
This command allows you to specify the current view range within an animation editor.

    """
    pass
    


def annotate( objects , point=linear, linear, linear, text=string):
    """
    annotate is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create an annotation to be attached to the specified objects at the specified point.

    """
    pass
    


def applyAttrPattern(nodeType=string, patternName=string):
    """
    applyAttrPattern is undoable, NOT queryable, and NOT editable.
    

    
Take the attribute structure described by a pre-defined pattern and apply it either to a node (as dynamic attributes) or a node type (as extension attributes). The same pattern can be applied more than once to different nodes or node types as the operation duplicates the attribute structure described by the pattern. See the 'createAttrPatterns' command for a description of how to create a pattern.

    """
    pass
    


def applyMetadata(format=string, scene=boolean, value=string):
    """
    applyMetadata is undoable, NOT queryable, and NOT editable.
    

    
Define the values of a particular set of metadata on selected objects. This command is used in preservation of metadata through Maya file formats (.ma/.mb). If any metadata already exists it will be kept and merged with the new metadata, overwriting duplicate entries. (i.e. if this command specifies data at index N and you already have a value at index N then the one this command specifies will be the new value and the old one will cease to exist.)
Unlike the editMetadata command it is not necessary to first use the addMetadata command or API equivalent to attach a metadata stream to the object, this command will do both assignment of structure and of metadata values. You do have to use the dataStructure command or API equivalent to create the structure being assigned first though.
The formatted input will be in a form expected by the data associations serializer (see adsk::Data::AssociationsSerializer for more information). The specific serialization type will be the default 'raw' if the format flag is not used.
For example the "raw" format input string "channel face\n[STREAMDATA]\nendChannels\nendAssociations" with no flags is equivalent to the input "[STREAMDATA]\nendChannels" with the channel flag set to 'face'

    """
    pass
    


def applyTake(channel=string, device=string, filter=string, preview=boolean, recurseChannel=boolean, reset=boolean, specifyChannel=boolean, startTime=time):
    """
    applyTake is undoable, NOT queryable, and NOT editable.
    

    
This command takes data in a device (refered to as a take) and converts it into a form that may be played back and reviewed. The take can either be imported through the readTake action, or recorded by the recordDevice action. The take is either converted into animation curves or if the -preview flag is used, into blendDevice nodes.
The command looks for animation curves attached to the target attributes of a device attachment. If animation curves exist, the take is pasted over the existing curves. If the curves do not exist, new animation curves are created.
If devices are not specified, all of the devices with take data and that are enabled for applyTake, will have their data applied.
See also: recordDevice, enableDevice, readTake, writeTake

    """
    pass
    


def arclen( curve , constructionHistory=boolean):
    """
    arclen is undoable, queryable, and editable.
    

    
This command returns the arclength of a curve if the history flag is not set (the default). If the history flag is set, a node is created that can produce the arclength, and is connected and its name returned. Having the construction history option on makes this command useful for expressions.

    """
    pass
    


def arcLenDimContext(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    arcLenDimContext is undoable, queryable, and editable.
    

    
Command used to register the arcLenDimCtx tool.

    """
    pass
    


def arcLengthDimension( curve|surface ):
    """
    arcLengthDimension is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create an arcLength dimension to display the arcLength of a curve/surface at a specified point on the curve/surface.

    """
    pass
    


def arrayMapper(destAttr=string, inputU=string, inputV=string, mapTo=string, target=string, type=string):
    """
    arrayMapper is undoable, NOT queryable, and NOT editable.
    

    
Create an arrayMapper node and connect it to a target object. If the -type flag is used, then this command also creates an external node used for computing the output values. If the input attribute does not already exist, it will be created. The output attribute must exists. If a flag is omitted, the selection list will be used to supply the needed objects. If none are found, that action is omitted.

    """
    pass
    


def art3dPaintCtx(accopacity=boolean, alphablendmode=string, assigntxt=boolean, brushalignment=boolean, brushfeedback=boolean, clear=boolean, commonattr=string, dragSlider=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, extendFillColor=boolean, filetxtaspectratio=float, filetxtsizex=int, filetxtsizey=int, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, keepaspectratio=boolean, lowerradius=float, mappressure=string, name=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintmode=string, paintoperationtype=string, painttxtattr=string, painttxtattrname=string, pfxScale=float, pfxWidth=float, profileShapeFile=string, projective=boolean, radius=float, reflection=boolean, reflectionaxis=string, reloadtexfile=boolean, resizeratio=float, resizetxt=boolean, saveTextureOnStroke=boolean, saveonstroke=boolean, savetexture=boolean, shadernames=string, shapeattr=boolean, shapenames=string, showactive=boolean, soloAsDiffuse=boolean, stampProfile=string, stampSpacing=float, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, textureFilenames=boolean, usepressure=boolean):
    """
    art3dPaintCtx is undoable, queryable, and editable.
    

    
This is a tool context command for 3d Paint tool.

    """
    pass
    


def artAttrCtx(accopacity=boolean, activeListChangedProc=string, afterStrokeCmd=string, alphaclamp=string, alphaclamplower=float, alphaclampupper=float, attrSelected=string, beforeStrokeCmd=string, brushalignment=boolean, brushfeedback=boolean, clamp=string, clamplower=float, clampupper=float, clear=boolean, colorRamp=string, colorfeedback=boolean, colorrangelower=float, colorrangeupper=float, dataTypeIndex=int, disablelighting=boolean, dragSlider=string, duringStrokeCmd=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, filterNodes=boolean, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, interactiveUpdate=boolean, lowerradius=float, mappressure=string, maxvalue=float, minvalue=float, name=string, objattrArray=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintNodeArray=string, paintattrselected=string, paintmode=string, profileShapeFile=string, projective=boolean, radius=float, rampMaxColor=float, float, float, rampMinColor=float, float, float, reflection=boolean, reflectionaxis=string, selectedattroper=string, showactive=boolean, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, toolOffProc=string, toolOnProc=string, useColorRamp=boolean, useMaxMinColor=boolean, usepressure=boolean, value=float, whichTool=string):
    """
    artAttrCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This is a context command to set the flags on the Attribute Paint Tool context.

    """
    pass
    


def artAttrPaintVertexCtx( context , accopacity=boolean, activeListChangedProc=string, afterStrokeCmd=string, alphaclamp=string, alphaclamplower=float, alphaclampupper=float, attrSelected=string, beforeStrokeCmd=string, brushalignment=boolean, brushfeedback=boolean, clamp=string, clamplower=float, clampupper=float, clear=boolean, colorRamp=string, colorfeedback=boolean, colorrangelower=float, colorrangeupper=float, dataTypeIndex=int, disablelighting=boolean, dragSlider=string, duringStrokeCmd=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, filterNodes=boolean, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, interactiveUpdate=boolean, lowerradius=float, mappressure=string, maxvalue=float, minvalue=float, name=string, objattrArray=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintComponent=int, paintNodeArray=string, paintRGBA=boolean, paintVertexFace=boolean, paintattrselected=string, paintmode=string, profileShapeFile=string, projective=boolean, radius=float, rampMaxColor=float, float, float, rampMinColor=float, float, float, reflection=boolean, reflectionaxis=string, selectedattroper=string, showactive=boolean, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, toolOffProc=string, toolOnProc=string, useColorRamp=boolean, useMaxMinColor=boolean, usepressure=boolean, value=float, vertexColorRange=boolean, vertexColorRangeLower=float, vertexColorRangeUpper=float, whichTool=string):
    """
    artAttrPaintVertexCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This is a context command to set the flags on the Paint color on vertex Tool context.

    """
    pass
    


def artAttrSkinPaintCtx( context , accopacity=boolean, activeListChangedProc=string, afterStrokeCmd=string, alphaclamp=string, alphaclamplower=float, alphaclampupper=float, attrSelected=string, beforeStrokeCmd=string, brushalignment=boolean, brushfeedback=boolean, clamp=string, clamplower=float, clampupper=float, clear=boolean, colorRamp=string, colorfeedback=boolean, colorrangelower=float, colorrangeupper=float, dataTypeIndex=int, disablelighting=boolean, dragSlider=string, duringStrokeCmd=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, filterNodes=boolean, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, influence=string, interactiveUpdate=boolean, lowerradius=float, mappressure=string, maxvalue=float, minvalue=float, name=string, objattrArray=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintNodeArray=string, paintSelectMode=int, paintattrselected=string, paintmode=string, profileShapeFile=string, projective=boolean, radius=float, rampMaxColor=float, float, float, rampMinColor=float, float, float, reflection=boolean, reflectionaxis=string, selectedattroper=string, showactive=boolean, skinPaintMode=int, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, toolOffProc=string, toolOnProc=string, useColorRamp=boolean, useMaxMinColor=boolean, usepressure=boolean, value=float, whichTool=string, xrayJoints=boolean):
    """
    artAttrSkinPaintCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This is a context command to set the flags on the Paint skin weights tool context.

    """
    pass
    


def artAttrTool(add=string, exists=string, remove=string):
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
    


def artFluidAttrCtx(accopacity=boolean, autoSave=string, brushalignment=boolean, brushfeedback=boolean, clear=boolean, currentPaintableFluid=string, delaySelectionChanged=boolean, displayAsRender=boolean, displayVelocity=boolean, doAutoSave=boolean, dragSlider=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, lowerradius=float, mappressure=string, name=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintmode=string, profileShapeFile=string, projective=boolean, property=string, radius=float, reflection=boolean, reflectionaxis=string, rgbValue=float, float, float, showactive=boolean, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, useStrokeDirection=boolean, usepressure=boolean, velocity=float, float, float):
    """
    artFluidAttrCtx is undoable, queryable, and editable.
    

    
This command is used to paint properties (such as density) of selected fluid volumes.

    """
    pass
    


def artPuttyCtx(accopacity=boolean, activeListChangedProc=string, afterStrokeCmd=string, alphaclamp=string, alphaclamplower=float, alphaclampupper=float, attrSelected=string, autosmooth=boolean, beforeStrokeCmd=string, brushStrength=float, brushalignment=boolean, brushfeedback=boolean, clamp=string, clamplower=float, clampupper=float, clear=boolean, collapsecvtol=float, colorRamp=string, colorfeedback=boolean, colorrangelower=float, colorrangeupper=float, dataTypeIndex=int, disablelighting=boolean, dispdecr=boolean, dispincr=boolean, dragSlider=string, duringStrokeCmd=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, filterNodes=boolean, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, interactiveUpdate=boolean, invertrefvector=boolean, lowerradius=float, mappressure=string, maxdisp=float, maxvalue=float, minvalue=float, mouldtypemouse=string, name=string, objattrArray=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintNodeArray=string, paintattrselected=string, paintmode=string, polecv=boolean, profileShapeFile=string, projective=boolean, radius=float, rampMaxColor=float, float, float, rampMinColor=float, float, float, reflection=boolean, reflectionaxis=string, refsurface=boolean, refvector=string, refvectoru=float, refvectorv=float, selectedattroper=string, showactive=boolean, smoothiters=int, stampProfile=string, stitchcorner=boolean, stitchedgeflood=boolean, stitchtype=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, toolOffProc=string, toolOnProc=string, updateerasesrf=boolean, updaterefsrf=boolean, useColorRamp=boolean, useMaxMinColor=boolean, usepressure=boolean, value=float, whichTool=string):
    """
    artPuttyCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This command is used to modify NURBS surfaces using a brush based interface (Maya Artisan). This is accomplished by moving the control vertices (CVs) under the brush in the specified direction.

    """
    pass
    


def artSelectCtx(accopacity=boolean, addselection=boolean, afterStrokeCmd=string, beforeStrokeCmd=string, brushalignment=boolean, brushfeedback=boolean, clear=boolean, dragSlider=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, importthreshold=float, lowerradius=float, mappressure=string, name=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintmode=string, profileShapeFile=string, projective=boolean, radius=float, reflection=boolean, reflectionaxis=string, selectall=boolean, selectop=string, showactive=boolean, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, toggleall=boolean, unselectall=boolean, usepressure=boolean):
    """
    artSelectCtx is undoable, queryable, and editable.
    

    
This command is used to select/deselect/toggle components on selected surfaces using a brush interface (Maya Artisan). Since, it selects components of the surface, it only works in the component mode.

    """
    pass
    


def artSetPaintCtx(accopacity=boolean, brushalignment=boolean, brushfeedback=boolean, clear=boolean, dragSlider=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, lowerradius=float, mappressure=string, name=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintmode=string, profileShapeFile=string, projective=boolean, radius=float, reflection=boolean, reflectionaxis=string, setcolorfeedback=boolean, setdisplaycvs=boolean, setopertype=string, settomodify=string, showactive=boolean, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, usepressure=boolean):
    """
    artSetPaintCtx is undoable, queryable, and editable.
    

    
This tool allows the user to modify the set membership (add, transfer, remove cvs) on nurbs surfaces using Maya Artisan's interface.

    """
    pass
    


def artUserPaintCtx(accopacity=boolean, activeListChangedProc=string, afterStrokeCmd=string, alphaclamp=string, alphaclamplower=float, alphaclampupper=float, attrSelected=string, beforeStrokeCmd=string, brushalignment=boolean, brushfeedback=boolean, clamp=string, clamplower=float, clampupper=float, clear=boolean, colorRamp=string, colorfeedback=boolean, colorrangelower=float, colorrangeupper=float, dataTypeIndex=int, disablelighting=boolean, dragSlider=string, duringStrokeCmd=string, exists=boolean, expandfilename=boolean, exportfilemode=string, exportfilesave=string, exportfilesizex=int, exportfilesizey=int, exportfiletype=string, filterNodes=boolean, finalizeCmd=string, fullpaths=boolean, getArrayAttrCommand=string, getSurfaceCommand=string, getValueCommand=string, history=boolean, image1=string, image2=string, image3=string, importfileload=string, importfilemode=string, importreassign=boolean, initializeCmd=string, interactiveUpdate=boolean, lowerradius=float, mappressure=string, maxvalue=float, minvalue=float, name=string, objattrArray=string, opacity=float, outline=boolean, outwhilepaint=boolean, paintNodeArray=string, paintattrselected=string, paintmode=string, profileShapeFile=string, projective=boolean, radius=float, rampMaxColor=float, float, float, rampMinColor=float, float, float, reflection=boolean, reflectionaxis=string, selectedattroper=string, setArrayValueCommand=string, setValueCommand=string, showactive=boolean, stampProfile=string, surfaceConformedBrushVertices=boolean, tablet=boolean, tangentOutline=boolean, toolCleanupCmd=string, toolOffProc=string, toolOnProc=string, toolSetupCmd=string, useColorRamp=boolean, useMaxMinColor=boolean, usepressure=boolean, value=float, whichTool=string):
    """
    artUserPaintCtx is undoable, queryable, and editable.
    

    
This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.
This command executes a scriptable paint (Maya Artisan). It allows the user to apply mel commands/scripts to modify cvs' attributes for all cvs under the paint brush.

    """
    pass
    


def assembly(active=string, activeLabel=string, canCreate=string, createOptionBoxProc=script, createRepresentation=string, defaultType=string, deleteRepresentation=string, deregister=string, input=string, isAType=string, isTrackingMemberEdits=string, label=string, listRepTypes=boolean, listRepTypesProc=script, listRepresentations=boolean, listTypes=boolean, name=string, newRepLabel=string, postCreateUIProc=script, proc=script, renameRepresentation=string, repLabel=string, repName=string, repNamespace=string, repPostCreateUIProc=string, repPreCreateUIProc=string, repType=string, repTypeLabel=string, repTypeLabelProc=script, type=string):
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
    


def assignCommand( int , addDivider=string, altModifier=boolean, annotation=string, command=script, commandModifier=boolean, ctrlModifier=boolean, data1=string, data2=string, data3=string, delete=int, dividerString=string, factorySettings=boolean, index=int, keyString=string, keyUp=boolean, name=boolean, numDividersPreceding=int, numElements=boolean, optionModifier=boolean, sortByKey=boolean, sourceUserCommands=boolean):
    """
    assignCommand is undoable, queryable, and editable.
    

    
This command allows the user to assign hotkeys and manipulate the internal array of named command objects. Each object in the array has an 1-based index which is used for referencing. Under expected usage you should not need to use this command directly as the Hotkey Editor may be used to assign hotkeys.
This command is obsolete for setting new hotkeys, instead please use the "hotkey" command.

    """
    pass
    


def assignInputDevice(clutch=string, continuous=boolean, device=string, immediate=boolean, multiple=boolean):
    """
    assignInputDevice is undoable, queryable, and NOT editable.
    

    
This command associates a command string (i.e. a mel script) with the input device. When the device moves or a button on the device is pressed, the command string is executed as if you typed it into the window. If the command string contains the names of buttons or axes of the device, the current value of these buttons/axes are substituted in. Buttons are reported as booleans and axes as doubles.
This command is most useful for associating buttons on a device with commands. For using a device to capture continous movements it is much more efficient to attach the device directly into the dependency graph.

    """
    pass
    


def assignViewportFactories(string, materialFactory=string, nodeType=string, textureFactory=string):
    """
    assignViewportFactories is NOT undoable, queryable, and editable.
    

    
Sets viewport factories for displays as materials or textures.

    """
    pass
    


def attachCurve( curve curve curve... , blendBias=float, blendKnotInsertion=boolean, caching=boolean, constructionHistory=boolean, keepMultipleKnots=boolean, method=int, name=string, nodeState=int, object=boolean, parameter=float, replaceOriginal=boolean, reverse1=boolean, reverse2=boolean):
    """
    attachCurve is undoable, queryable, and editable.
    

    
This attach command is used to attach curves. Once the curves are attached, there will be multiple knots at the joined point(s). These can be kept or removed if the user wishes.
If there are two curves, the end of the first curve is attached to the start of the second curve. If there are more than two curves, closest endpoints are joined.
Note: if the command is done with Keep Original off, the first curve is replaced by the attached curve. All other curves will remain, the command does not delete them.

    """
    pass
    


def attachDeviceAttr(attribute=string, axis=string, camera=boolean, cameraRotate=boolean, cameraTranslate=boolean, clutch=string, device=string, selection=boolean):
    """
    attachDeviceAttr is undoable, queryable, and NOT editable.
    

    
This command associates a device/axis pair with a node/attribute pair. When the device axis moves, the value of the attribute is set to the value of the axis. This value can be scaled and offset using the setAttrScale command.

    """
    pass
    


def attachSurface( surface surface , blendBias=float, blendKnotInsertion=boolean, caching=boolean, constructionHistory=boolean, directionU=boolean, keepMultipleKnots=boolean, method=int, name=string, nodeState=int, object=boolean, parameter=float, replaceOriginal=boolean, reverse1=boolean, reverse2=boolean, swap1=boolean, swap2=boolean, twist=boolean):
    """
    attachSurface is undoable, queryable, and editable.
    

    
This attach command is used to attach surfaces. Once the surfaces are attached, there will be multiple knots at the joined point(s). These can be kept or removed if the user wishes.
The end of the first surface is attached to the start of the second surface in the specified direction.
Note: if the command is done with Keep Original off there will be an extra surface in the model (the second surface). The command does not delete it. The first surface is replaced by the attached surface.

    """
    pass
    


def attrColorSliderGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, attrNavDecision=name, string, attribute=string, backgroundColor=float, float, float, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, hsvValue=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rgbValue=float, float, float, rowAttach=int, string, int, showButton=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    attrColorSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
Create a color slider group consisting of a label, a color canvas, a slider and a button. Clicking on the canvas will bring up the color editor. If the button is visible, it will allow you to map a texture to the attribute.

    """
    pass
    


def attrCompatibility( string string , addAttr=boolean, clear=boolean, dumpTable=boolean, enable=boolean, nodeRename=string, pluginNode=string, removeAttr=boolean, renameAttr=string, type=string, version=string):
    """
    attrCompatibility is undoable, NOT queryable, and NOT editable.
    

    
This command is used by Maya to handle compatibility issues between file format versions by providing a mechanism to describe differences between two versions. Plug-in writers can make use of this command to handle attribute compatibility changes to files.
The first optional command argument argument is a node type name and the second optional command argument is the short name of an attribute.
Warning: Only use this command to describe changes in names or attributes of nodes that you have written as plugins. Do not use this command to change information about builtin dependency graph nodes. Removing attributes on a plug-in node is a special case. Use a separate attrCompatibility call with pluginNode flag and name so that these attributes can be tracked even though the plug-in may not be loaded.
Only one flag may be used per invocation of the command. If multiple flags are provided one will arbitrarily be chosen as the action to perform and the others will be silently ignored.

    """
    pass
    


def attrControlGrp(annotation=string, attribute=name, changeCommand=script, enable=boolean, handlesAttribute=name, hideMapButton=boolean, label=string, preventOverride=boolean):
    """
    attrControlGrp is NOT undoable, queryable, and editable.
    

    
This command creates a control of the type most appropriate for the specified attribute, and associates the control with the attribute. Any change to the control will cause a change in the attribute value, and any change to the attribute value will be reflected in the control. Not all attribute types are supported.

    """
    pass
    


def attrEnumOptionMenu( string , annotation=string, attribute=name, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, enumeratedItem=int, string, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    attrEnumOptionMenu is undoable, queryable, and editable.
    

    
This command creates an enumerated attribute control. It is usually an option menu.

    """
    pass
    


def attrEnumOptionMenuGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, attribute=name, backgroundColor=float, float, float, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, enumeratedItem=int, string, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    attrEnumOptionMenuGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label and option menu button associated with an attribute of a node. The attribute should be an integer, and this control allows a UI association of strings to the integers of the attribute. When a new menu item is choosen the corresponding integer will be assigned to the attribute.
This control will automatically read the enumeration values from the attribute if none are provided.

    """
    pass
    


def attrFieldGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, attribute=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, fullPathName=boolean, height=int, hideMapButton=boolean, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfFields=int, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowAttach=int, string, int, step=float, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    attrFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text, plus two to four float fields. These fields will be attached to the specified vector attribute, so that changes in either will be reflected in the other.
The fields created here are expression fields -- while normally operating as a float field, the user can type in any expression starting with the character "-".
The field also has an automatic menu brought up by the right mouse button. The contents of this menu change depending on the state of the attribute being watched by the field.

    """
    pass
    


def attrFieldSliderGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, attribute=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fieldMaxValue=float, fieldMinValue=float, fieldStep=float, fullPathName=boolean, height=int, hideMapButton=boolean, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowAttach=int, string, int, sliderMaxValue=float, sliderMinValue=float, sliderStep=float, step=float, useTemplate=string, vertical=boolean, visible=boolean, visibleChangeCommand=script, width=int):
    """
    attrFieldSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text, float field and float slider (for values with a min or max specified) The group also supports the notion of a larger secondary range of possible field values.
If an attribute is specified for this object, then it will use any min and max values defined in the attribute. The user-specified values can reduce the min and max, but cannot expand them.
The field created here is an expression field -- while normally operating as a float field, the user can type in any expression starting with the character "=". This will expand the field to occupy the space previously taken by the slider.
The field also has an automatic menu brought up by the right mouse button. The contents of this menu change depending on the state of the attribute being watched by the field.

    """
    pass
    


def attributeInfo(allAttributes=boolean, bool=boolean, enumerated=boolean, hidden=boolean, inherited=boolean, internal=boolean, leaf=boolean, logicalAnd=boolean, multi=boolean, short=boolean, type=string, userInterface=boolean, writable=boolean):
    """
    attributeInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
This command lists all of the attributes that are marked with certain flags. Combinations of flags may be specified and all will be considered. (The method of combination depends on the state of the "logicalAnd/and" flag.) When the "allAttributes/all" flag is specified, attributes of all types will be listed.

    """
    pass
    


def attributeMenu(beginMenu=boolean, editor=string, finishMenu=boolean, inputs=boolean, plug=name, regPulldownMenuCommand=string, unregPulldownMenuCommand=int):
    """
    attributeMenu is NOT undoable, NOT queryable, and NOT editable.
    

    
Action to generate popup connection menus for Hypershade. This command is used internally by the Hypershade panel.

    """
    pass
    


def attributeName(leaf=boolean, long=boolean, nice=boolean, short=boolean):
    """
    attributeName is NOT undoable, NOT queryable, and NOT editable.
    

    
This command takes one "node.attribute"-style specifier on the command line and returns either the attribute's long, short, or nice name. (The "nice" name, or UI name, is the name used to display the attribute in Maya's interface, and may be localized when running Maya in a language other than English.) If more than one "node.attribute" specifier is given on the command line, only the first valid specifier is processed.

    """
    pass
    


def attributeQuery(affectsAppearance=boolean, affectsWorldspace=boolean, attributeType=boolean, cachedInternally=boolean, categories=boolean, channelBox=boolean, connectable=boolean, enum=boolean, exists=boolean, hidden=boolean, indeterminant=boolean, indexMatters=boolean, internal=boolean, internalGet=boolean, internalSet=boolean, keyable=boolean, listChildren=boolean, listDefault=boolean, listEnum=boolean, listParent=boolean, listSiblings=boolean, longName=boolean, maxExists=boolean, maximum=boolean, message=boolean, minExists=boolean, minimum=boolean, multi=boolean, niceName=boolean, node=name, numberOfChildren=boolean, range=boolean, rangeExists=boolean, readable=boolean, renderSource=boolean, shortName=boolean, softMax=boolean, softMaxExists=boolean, softMin=boolean, softMinExists=boolean, softRange=boolean, softRangeExists=boolean, storable=boolean, type=string, typeExact=string, usedAsColor=boolean, usedAsFilename=boolean, usesMultiBuilder=boolean, worldspace=boolean, writable=boolean):
    """
    attributeQuery is NOT undoable, NOT queryable, and NOT editable.
    

    
attributeQuery returns information about the configuration of an attribute. It handles both boolean flags, returning true or false, as well as other return values. Specifying more than one boolean flag will return the logical "and" of all the specified boolean flags. You may not specify any two flags when both do not provide a boolean return type. (eg. "-internal -hidden" is okay but "-range -hidden" or "-range -softRange" is not.)

    """
    pass
    


def attrNavigationControlGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, attrNavDecision=name, string, attribute=name, backgroundColor=float, float, float, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, connectAttrToDropped=script, connectNodeToDropped=script, connectToExisting=script, createNew=script, defaultTraversal=script, defineTemplate=string, delete=script, disconnect=script, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, ignore=script, ignoreNotSupported=boolean, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, relatedNodes=script, rowAttach=int, string, int, unignore=script, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    attrNavigationControlGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged label navigation button.
The group is used to help the user manage connections to a particular attribute.
When creating the control you have the opportunity to attach scripts to the control that are executed on various UI events. You can define what happens when the navigation button is pressed, and when a node is dragged and dropped onto this attribute.
The navigation button can traverse to the connected node or can bring up UI to create new connections to the attribute. The button also can show you state information: if there already exists a connection/if the connection is ignored.

    """
    pass
    


def audioTrack(insertTrack=uint, lock=boolean, mute=boolean, numTracks=uint, removeEmptyTracks=boolean, removeTrack=uint, solo=boolean, swapTracks=uint, uint, title=string, track=uint):
    """
    audioTrack is undoable, queryable, and editable.
    

    
This command is used for inserting and removing tracks related to the audio clips displayed in the sequencer. It can also be used to modify the track state, for example, to lock or mute a track.

    """
    pass
    


def autoKeyframe(characterOption=string, noReset=boolean, state=boolean):
    """
    autoKeyframe is undoable, queryable, and editable.
    

    
With no flags, this command will set keyframes on all attributes that have been modified since an "autoKeyframe -state on" command was issued. To stop keeping track of modified attributes, use "autoKeyframe -state off"
autoKeyframe does not create new animation curves. An attribute must have already been keyframed (with the setKeyframe command) for autoKeyframe to add new keyframes for modified attributes.
You can also query the current state of autoKeyframing with "autoKeyframe -query -state".

    """
    pass
    


def autoPlace(useMouse=boolean):
    """
    autoPlace is undoable, NOT queryable, and NOT editable.
    

    
This command takes a point in the centre of the current modeling pane and projects it onto the live surface. This produces a point in 3 space which is returned. If the um/useMouse flag is set the current mouse position is used rather than the centre of the modeling pane.

    """
    pass
    


def autoSave(destination=int, destinationFolder=boolean, enable=boolean, folder=string, interval=float, limitBackups=boolean, maxBackups=int, perform=boolean, prompt=boolean):
    """
    autoSave is undoable, queryable, and NOT editable.
    

    
Provides an interface to the auto-save mechanism.

    """
    pass
    


def bakeClip(blend=uint, uint, clipIndex=uint, keepOriginals=boolean, name=string):
    """
    bakeClip is undoable, NOT queryable, and NOT editable.
    

    
This command is used to bake clips and blends into a single clip.

    """
    pass
    


def bakePartialHistory(allShapes=boolean, postSmooth=boolean, preCache=boolean, preDeformers=boolean, prePostDeformers=boolean):
    """
    bakePartialHistory is undoable, queryable, and editable.
    

    
This command is used to bake sections of the construction history of a shape node when possible. A typical usage would be on a shape that has both modelling operations and deformers in its history. Using this command with the -prePostDeformers flag will bake the modeling portions of the graph, so that only the deformers remain.
Note that not all modeling operations can be baked such that they create exactly the same effect after baking. For example, imagine the history contains a skinning operation followed by a smooth. Before baking, the smooth operation is performed each time the skin deforms, so it will smooth differently depending on the output of the skin. When the smooth operation is baked into the skinning, the skin will be reweighted based on the smooth points to attempt to approximate the original behavior. However, the skin node does not perform the smooth operation, it merely performs skinning with the newly calculated weights and the result will not be identical to before the bake.
In general, modeling operations that occur before deformers can be baked precisely. Those which occur after can only be approximated. The -pre and -post flags allow you to control whether only the operations before or after the deformers are baked.
When the command is used on an object with no deformers, the entire history will be deleted.

    """
    pass
    


def bakeResults( objects , animation=string, attribute=string, bakeOnOverrideLayer=boolean, controlPoints=boolean, destinationLayer=string, disableImplicitControl=boolean, float=floatrange, hierarchy=string, includeUpperBound=boolean, index=uint, minimizeRotation=boolean, oversamplingRate=uint, preserveOutsideKeys=boolean, removeBakedAttributeFromLayer=boolean, resolveWithoutLayer=string, sampleBy=time, shape=boolean, simulation=boolean, smart=, boolean, float, , sparseAnimCurveBake=boolean, time=timerange):
    """
    bakeResults is undoable, queryable, and editable.
    

    
This command allows the user to replace a chain of dependency nodes which define the value for an attribute with a single animation curve. Command allows the user to specify the range and frequency of sampling.
This command operates on a keyset. A keyset is defined as a group of keys within a specified time range on one or more animation curves.
The animation curves comprising a keyset depend on the value of the "-animation" flag:
keysOrObjects:
Any active keys, when no target objects or -attribute flags appear on the command line, or
All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
objects: Only act on specified objects. If there are no objects specified, don't do anything.
Note that the "-animation" flag can be used to override the curves uniquely identified by the multi-use "-attribute" flag, which takes an argument of the form attributeName, such as "translateX".
Keys on animation curves are identified by either their time values or their indices. Times and indices should be specified as a range, as shown below.
-time "10:20" means all keys in the range from 10 to 20, inclusive, in the current time unit.
-index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.

    """
    pass
    


def bakeSimulation( objects , animation=string, attribute=string, bakeOnOverrideLayer=boolean, controlPoints=boolean, destinationLayer=string, disableImplicitControl=boolean, float=floatrange, hierarchy=string, includeUpperBound=boolean, index=uint, minimizeRotation=boolean, preserveOutsideKeys=boolean, removeBakedAnimFromLayer=boolean, removeBakedAttributeFromLayer=boolean, resolveWithoutLayer=string, sampleBy=time, shape=boolean, simulation=boolean, smart=, boolean, float, , sparseAnimCurveBake=boolean, time=timerange):
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
    


def baseTemplate(string, exists=boolean, fileName=string, force=boolean, load=boolean, matchFile=string, silent=boolean, unload=boolean, viewList=string):
    """
    baseTemplate is NOT undoable, queryable, and editable.
    

    
This is the class for the commands that edit and/or query templates.

    """
    pass
    


def baseView(string, itemInfo=string, itemList=boolean, viewDescription=boolean, viewLabel=boolean, viewList=boolean, viewName=string):
    """
    baseView is NOT undoable, queryable, and editable.
    

    
A view defines the layout information for the attributes of a particular node type or container. Views can be selected from a set of built-in views or may be defined on an associated container template. This command queries the view-related information for a container node or for a given template. The information returned from this command will be based on the view-related settings in force on the container node at the time of the query (i.e. the container's view mode, template name, view name attributes), when applicable.

    """
    pass
    


def batchRender(filename=string, melCommand=string, numProcs=int, preRenderCommand=string, remoteRenderMachine=string, renderCommandOptions=string, showImage=boolean, useRemoteRender=boolean, useStandalone=boolean, verbosity=int):
    """
    batchRender is undoable, NOT queryable, and NOT editable.
    

    
The batchRender command is used to spawn off a separate rendering session of the current maya file. If no mayaFile is specified, it'll ask you whether you want the current job killed.
The batchRender will spawn a separate maya process in which commands will be communicated to it through a commandPort. If Maya is unable to find an available port an error will be produced. Maya will attempt to use ports 7835 through 7844.

    """
    pass
    


def bevel( object , bevelShapeType=int, caching=boolean, constructionHistory=boolean, cornerType=int, depth=linear, extrudeDepth=linear, name=string, nodeState=int, object=boolean, polygon=int, range=boolean, tolerance=linear, width=linear):
    """
    bevel is undoable, queryable, and editable.
    

    
The bevel command creates a new bevel surface for the specified curve. The curve can be any nurbs curves.

    """
    pass
    


def bevelPlus( curve curve curve... , capSides=int, constructionHistory=boolean, depth=linear, extrudeDepth=linear, innerStyle=int, joinSurfaces=boolean, name=string, normalsOutwards=boolean, numberOfSides=int, outerStyle=int, polyOutChordHeight=linear, polyOutChordHeightRatio=float, polyOutCount=int, polyOutCurveSamples=int, polyOutCurveType=int, polyOutExtrusionSamples=int, polyOutExtrusionType=int, polyOutMethod=int, polyOutUseChordHeight=boolean, polyOutUseChordHeightRatio=boolean, polygon=int, tolerance=linear, width=linear):
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
    


def bezierAnchorState(even=boolean, smooth=boolean):
    """
    bezierAnchorState is undoable, NOT queryable, and NOT editable.
    

    
The bezierAnchorState command provides an easy interface to modify anchor states:
- Smooth/Broken anchor tangents - Even/Uneven weighted anchor tangents

    """
    pass
    


def bezierCurveToNurbs( curve ):
    """
    bezierCurveToNurbs is undoable, NOT queryable, and NOT editable.
    

    
The bezierCurveToNurbs command attempts to convert an existing NURBS curve to a Bezier curve.

    """
    pass
    


def bezierInfo(anchorFromCV=int, cvFromAnchor=int, isAnchorSelected=boolean, isTangentSelected=boolean, onlyAnchorsSelected=boolean, onlyTangentsSelected=boolean):
    """
    bezierInfo is undoable, NOT queryable, and NOT editable.
    

    
This command provides a queryable interface for Bezier curve shapes.

    """
    pass
    


def bindSkin( objects , byClosestPoint=boolean, byPartition=boolean, colorJoints=boolean, delete=boolean, doNotDescend=boolean, enable=boolean, name=string, partition=string, toAll=boolean, toSelectedBones=boolean, toSkeleton=boolean, unbind=boolean, unbindKeepHistory=boolean, unlock=boolean):
    """
    bindSkin is undoable, queryable, and editable.
    

    
This command binds the currently selected objects to the currently selected skeletons. Shapes which can be bound are: meshes, nurbs curves, nurbs surfaces, lattices, subdivision surfaces, and API shapes. Multiple shapes and multiple skeletons can be bound at once by selecting them or specifying them on the command line. Selection order is not important.
The skin is bound using the so-called "rigid" bind, in which the components are rigidly attached to the closest bone in the skeleton. Flexors can later be added to the skeleton to smooth out the skinning around joints.
The skin(s) can be bound either to the entire skeleton hierarchy of the selected joint(s), or to only the selected joints. The entire hierarchy is the default. The -tsb/-toSelectedBones flag allows binding to only the selected bones.
This command can also be used to detach the skin from the skeleton. Detaching the skin is useful in a variety of situations, such as: inserting additional bones, deleting bones, changing the bind position of the skeleton or skin, or simply getting rid of the skinning nodes altogether. The options to use when detaching the skin depend on how much of the skinning info you want to get rid of. Namely: (1) -delete or -unbind: remove all skinning nodes, (2) -unbindKeepHistory: remove the skinning sets, but keep the weights, (3) -disable: disable the skinning but keep the skinning sets and the weights.

    """
    pass
    


def binMembership(addToBin=string, exists=string, inheritBinsFromNodes=name, isValidBinName=string, listBins=boolean, makeExclusive=string, notifyChanged=boolean, removeFromBin=string):
    """
    binMembership is undoable, queryable, and NOT editable.
    

    
Command to assign nodes to bins.

    """
    pass
    


def blend2( curve curve curve... , autoAnchor=boolean, autoNormal=boolean, caching=boolean, constructionHistory=boolean, flipLeftNormal=boolean, flipRightNormal=boolean, leftAnchor=float, leftEnd=float, leftStart=float, multipleKnots=boolean, name=string, nodeState=int, object=boolean, polygon=int, positionTolerance=float, reverseLeft=boolean, reverseRight=boolean, rightAnchor=float, rightEnd=float, rightStart=float, tangentTolerance=float):
    """
    blend2 is undoable, queryable, and editable.
    

    
This command creates a surface by blending between given curves. This is an enhancement (more user control) compared to blend which is now obsolete.

    """
    pass
    


def blendShape( objects , after=boolean, afterReference=boolean, before=boolean, deformerTools=boolean, envelope=float, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, inBetween=boolean, inBetweenIndex=uint, inBetweenType=string, includeHiddenSelections=boolean, name=string, normalizationGroups=boolean, origin=string, parallel=boolean, prune=boolean, remove=boolean, resetTargetDelta=uint, uint, split=boolean, tangentSpace=boolean, target=string, uint, string, float, topologyCheck=boolean, transform=string, weight=uint, float, weightCount=uint):
    """
    blendShape is undoable, queryable, and editable.
    

    
This command creates a blendShape deformer, which blends in specified amounts of each target shape to the initial base shape. Each base shape is deformed by its own set of target shapes. Every target shape has an index that associates it with one of the shape weight values.
In the create mode the first item on the selection list is treated as the base and the remaining inputs as targets. If the first item on the list has multiple shapes grouped beneath it, the targets must have an identical shape hierarchy. Additional base shapes can be added in edit mode using the deformers -g flag.

    """
    pass
    


def blendShapeEditor( string , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, selectionConnection=string, stateString=boolean, targetControlList=boolean, targetList=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string, verticalSliders=boolean):
    """
    blendShapeEditor is undoable, queryable, and editable.
    

    
This command creates an editor that derives from the base editor class that has controls for blendShape, control nodes.

    """
    pass
    


def blendShapePanel( string , blendShapeEditor=boolean, control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    blendShapePanel is undoable, queryable, and editable.
    

    
This command creates a panel that derives from the base panel class that houses a blendShapeEditor.

    """
    pass
    


def blendTwoAttr( objects , attribute=string, attribute0=name, attribute1=name, blender=name, controlPoints=boolean, driver=int, name=string, shape=boolean, time=timerange):
    """
    blendTwoAttr is undoable, queryable, and editable.
    

    
A blendTwoAttr nodes takes two inputs, and blends the values of the inputs from one to the other, into an output value. The blending of the two inputs uses a blending function, and the following formula:
     (1 - blendFunction) * input[0]  +  blendFunction * input[1] 
The blendTwoAttr command can be used to blend the animation of an object to transition smoothly between the animation of two other objects.
When the blendTwoAttr command is issued, it creates a blendTwoAttr node on the specified attributes, and reconnects whatever was previously connected to the attributes to the new blend nodes. You may also specify which two attributes should be used to blend together.
The driver is used when you want to keyframe an object after it is being animated by a blend node. The current driver index specifies which of the two blended attributes should be keyframed.

    """
    pass
    


def blindDataType(dataType=string, longDataName=string, longNames=boolean, query=boolean, shortDataName=string, shortNames=boolean, typeId=int, typeNames=boolean):
    """
    blindDataType is undoable, NOT queryable, and NOT editable.
    

    
This command creates a blind data type, which is represented by a blindDataTemplate node in the DG. A blind data type can have one or more attributes. On the command line, the attributes should be ordered by type for best memory utilization, largest first: string, binary, double, float, int, and finally boolean. Once a blind data type is created, blind data of that type may be assigned using the polyBlindData command. Note that as well as polygon components, blind data may be assigned to objects and to NURBS patches. A blind data type may not be modified after it is created: in order to do so it must be deleted and recreated. Any existing blind data of that type would also need to be deleted and recreated. When used with the query flag, this command will return information about the attributes of the specified blind data type.

    """
    pass
    


def boneLattice( objects , after=boolean, afterReference=boolean, before=boolean, bicep=float, deformerTools=boolean, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, joint=string, lengthIn=float, lengthOut=float, name=string, parallel=boolean, prune=boolean, remove=boolean, split=boolean, transform=string, tricep=float, widthLeft=float, widthRight=float):
    """
    boneLattice is undoable, queryable, and editable.
    

    
This command creates/edits/queries a boneLattice deformer. The name of the created/edited object is returned. Usually you would make use of this functionality through the higher level flexor command.

    """
    pass
    


def boundary( string string string string , caching=boolean, constructionHistory=boolean, endPoint=boolean, endPointTolerance=linear, name=string, nodeState=int, object=boolean, order=boolean, polygon=int, range=boolean):
    """
    boundary is undoable, queryable, and editable.
    

    
This command produces a boundary surface given 3 or 4 curves. This resulting boundary surface passes through two of the given curves in one direction, while in the other direction the shape is defined by the remaining curve(s). If the "endPoint" option is on, then the curve endpoints must touch before a surface will be created. This is the usual situation where a boundary surface is useful.
Note that there is no tangent continuity option with this command. Unless all the curve end points are touching, the resulting surface will not pass through all curves. Instead, use the birail command.

    """
    pass
    


def boxDollyCtx(alternateContext=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, toolName=string):
    """
    boxDollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a dolly context.

    """
    pass
    


def boxZoomCtx( object , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, zoomScale=float):
    """
    boxZoomCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a box zoom context. If this context is used on a perspective camera, the field of view and view direction are changed. If the camera is orthographic, the orthographic width and eye point are changed. The left and middle mouse interactively zoom the view. The control key can be used to enable box zoom. A box starting from left to right will zoom in, and a box starting from right to left will zoom out.

    """
    pass
    


def bufferCurve( animatedObject , animation=string, attribute=string, controlPoints=boolean, exists=boolean, float=floatrange, hierarchy=string, includeUpperBound=boolean, index=uint, overwrite=boolean, shape=boolean, swap=boolean, time=timerange, useReferencedCurve=boolean):
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
    


def buildBookmarkMenu( string , editor=string, type=string):
    """
    buildBookmarkMenu is undoable, NOT queryable, and NOT editable.
    

    
This command handles building the "dynamic" Bookmark menu, to show all bookmarks ("sets") of a specified type ("sets -text")
menuName is the string returned by the "menu" command.

    """
    pass
    


def buildKeyframeMenu( string ):
    """
    buildKeyframeMenu is undoable, NOT queryable, and NOT editable.
    

    
This command handles building the "dynamic" Keyframe menu, to show attributes of currently selected objects, filtered by the current manipulator.
menuName is the string returned by the "menu" command. The target menu will entries appended to it (and deleted from it) to always show what's currently keyframable.

    """
    pass
    


def button( string , actOnPress=boolean, actionIsSubstitute=boolean, align=string, annotation=string, backgroundColor=float, float, float, command=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, recomputeSize=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    button is undoable, queryable, and editable.
    

    
Create a button control capable of displaying a textual label and executing a command when selected by the user.

    """
    pass
    


def buttonManip( script selectionItem , icon=string):
    """
    buttonManip is undoable, NOT queryable, and NOT editable.
    

    
This creates a button manipulator. This manipulator has a position in space and a triad manip for positioning. When you click on the top part of the manip, the command defined by the first argument is executed. The command is associated with the manipulator when it is created.
If a dag object is included on the command line, the manip will be parented to the object. This means moving the object will move the manip. You can move the manip independently of the object using its triad.
Note that a buttonManip may not be parented to more than one object.

    """
    pass
    


def cacheFile(appendFrame=boolean, attachFile=boolean, cacheFileNode=string, cacheFormat=string, cacheInfo=string, cacheableAttrs=string, cacheableNode=string, channelIndex=boolean, channelName=string, convertPc2=boolean, createCacheNode=boolean, creationChannelName=string, dataSize=boolean, deleteCachedFrame=boolean, descriptionFileName=boolean, directory=string, doubleToFloat=boolean, endTime=time, fileName=string, format=string, geometry=boolean, inAttr=string, inTangent=string, interpEndTime=time, interpStartTime=time, noBackup=boolean, outAttr=string, outTangent=string, pc2File=string, pointCount=boolean, points=string, pointsAndNormals=string, prefix=boolean, refresh=boolean, replaceCachedFrame=boolean, replaceWithoutSimulating=boolean, runupFrames=int, sampleMultiplier=int, simulationRate=time, singleCache=boolean, startTime=time, staticCache=boolean, worldSpace=boolean):
    """
    cacheFile is undoable, queryable, and editable.
    

    
Creates one or more cache files on disk to store attribute data for a span of frames. The caches can be created for points/normals on a geometry (using the pts/points or pan/pointsAndNormals flag), for vectorArray output data (using the oa/outAttr flag), or for additional node specific data (using the cnd/cacheableNode flag for those nodes that support it).
When the ia/inAttr flag is used, connects a cacheFile node that associates the data file on disk with the attribute.
Frames can be replaced/appended to an existing cache with the rcf/replaceCachedFrame and apf/appendFrame flag. Replaced frames are never deleted. They are stored in the same directory as the original cache files with the name provided by the f/fileName flag. If no file name is provided, the cacheFile name is prefixed with "backup" followed by a unique number.
Single file caches are backed up in their entirety. To revert to an older version, simply attach to this cache. One file per frame caches only backup the description file and the frames that were replaced. To recover these types of caches, the user must rename these files to the original name.

    """
    pass
    


def cacheFileCombine(cacheIndex=boolean, channelName=string, connectCache=string, keepWeights=boolean, layerNode=boolean, nextAvailable=boolean, object=string, objectIndex=int):
    """
    cacheFileCombine is undoable, queryable, and editable.
    

    
Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles for a given object.

    """
    pass
    


def cacheFileMerge(endTime=time, geometry=boolean, startTime=time):
    """
    cacheFileMerge is undoable, queryable, and editable.
    

    
If selected/specified caches can be successfully merged, will return the start/end frames of the new cache followed by the start/end frames of any gaps in the merged cache for which no data should be written to file. In query mode, will return the names of geometry associated with the specified cache file nodes.

    """
    pass
    


def cacheFileTrack(insertTrack=uint, lock=boolean, mute=boolean, removeEmptyTracks=boolean, removeTrack=uint, solo=boolean, track=uint):
    """
    cacheFileTrack is undoable, queryable, and editable.
    

    
This command is used for inserting and removing tracks related to the caches displayed in the trax editor. It can also be used to modify the track state, for example, to lock or mute a track.

    """
    pass
    


def callbacks(addCallback=script, clearAllCallbacks=boolean, clearCallbacks=boolean, describeHooks=boolean, dumpCallbacks=boolean, executeCallbacks=boolean, hook=string, listCallbacks=boolean, owner=string, removeCallback=script):
    """
    callbacks is NOT undoable, NOT queryable, and NOT editable.
    

    
This command allows you to add callbacks at key times during UI creation so that the Maya UI can be extended. The list of standard Maya hooks, as well as the arguments which will be passed to the callback based on the context are enumerated in the describeHooks section below. Custom hooks can also be added if third parties want to add UI extensibility to their plugins.

    """
    pass
    


def camera( camera , aspectRatio=float, cameraScale=float, centerOfInterest=linear, clippingPlanes=boolean, depthOfField=boolean, displayFieldChart=boolean, displayFilmGate=boolean, displayFilmOrigin=boolean, displayFilmPivot=boolean, displayGateMask=boolean, displayResolution=boolean, displaySafeAction=boolean, displaySafeTitle=boolean, fStop=float, farClipPlane=linear, farFocusDistance=linear, filmFit=string, filmFitOffset=float, filmRollOrder=string, filmRollValue=angle, filmTranslateH=float, filmTranslateV=float, focalLength=float, focusDistance=linear, homeCommand=string, horizontalFieldOfView=angle, horizontalFilmAperture=float, horizontalFilmOffset=float, horizontalPan=float, horizontalRollPivot=float, horizontalShake=float, journalCommand=boolean, lensSqueezeRatio=float, lockTransform=boolean, motionBlur=boolean, nearClipPlane=linear, nearFocusDistance=linear, orthographic=boolean, orthographicWidth=linear, overscan=float, panZoomEnabled=boolean, position=linear, linear, linear, postScale=float, preScale=float, renderPanZoom=boolean, rotation=angle, angle, angle, shakeEnabled=boolean, shakeOverscan=float, shakeOverscanEnabled=boolean, shutterAngle=angle, startupCamera=boolean, stereoHorizontalImageTranslate=float, stereoHorizontalImageTranslateEnabled=boolean, verticalFieldOfView=angle, verticalFilmAperture=float, verticalFilmOffset=float, verticalLock=boolean, verticalPan=float, verticalRollPivot=float, verticalShake=float, worldCenterOfInterest=linear, linear, linear, worldUp=linear, linear, linear, zoom=float):
    """
    camera is undoable, queryable, and editable.
    

    
Create, edit, or query a camera with the specified properties.
The resulting camera can be repositioned using the viewPlace command. Many of the camera settings only affect the resulting rendered image. E.g. the F/Stop, shutter speed, the film related options, etc. Scaling the camera icon does not change any camera properties.

    """
    pass
    


def cameraSet(active=boolean, appendTo=boolean, camera=name, clearDepth=boolean, deleteAll=boolean, deleteLayer=boolean, insertAt=boolean, layer=uint, name=name, numLayers=boolean, objectSet=name, order=int):
    """
    cameraSet is undoable, queryable, and editable.
    

    
This command manages camera set nodes. Camera sets allow the users to break a single camera shot into layers. Instead of drawing all objects with a single camera, you can isolate the camera to only focus on certain objects and layer another camera into the viewport that draws the other objects. The situation to use camera sets primarily occurs when building stereoscopic scenes.
For example, a set of stereo parameters may make the background objects divergent beyond the tolerable range of the human perceptual system. However, you like the settings because the main focus is in the foreground and the depth is important to the visual look of the scene. You can use camera sets to break apart the shot into a foreground stereo camera and background stereo camera. The foreground stereo camera will retain the original parameters; however, it will only focus on the foreground elements. The background stereo camera will have a different set of stereo parameters and will only draw the background element.
Camera sets can be viewed using the stereo viewer and are currently only designed to work with stereo camera rigs.

    """
    pass
    


def cameraView( object , addBookmark=boolean, bookmarkType=int, camera=name, name=string, removeBookmark=boolean, setCamera=boolean, setView=boolean):
    """
    cameraView is undoable, NOT queryable, and editable.
    

    
This command creates a preset view for a camera which is then independent of the camera. The view stores a camera's eye point, center of interest point, up vector, tumble pivot, horizontal aperture, vertical aperature, focal length, orthographic width, and whether the camera is orthographic or perspective by default. Or you can only store 2D pan/zoom attributes by setting the bookmarkType to 1. These settings can be applied to any other camera through the set camera flag.
This command can be used for creation or edit of camera view objects. This command can only be executed with one of the add bookmark, or remove bookmark and one of set camera, or the set view flags set.

    """
    pass
    


def canCreateCaddyManip( object ):
    """
    canCreateCaddyManip is undoable, NOT queryable, and NOT editable.
    

    
This command returns true if there can be a manipulator made for the specified selection, false otherwise.

    """
    pass
    


def canCreateManip( object ):
    """
    canCreateManip is undoable, NOT queryable, and NOT editable.
    

    
This command returns true if there can be a manipulator made for the specified selection, false otherwise.

    """
    pass
    


def canvas( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, hsvValue=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, pressCommand=script, preventOverride=boolean, rgbValue=float, float, float, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    canvas is undoable, queryable, and editable.
    

    
Creates a control capable of displaying a color swatch. This control can also accept a command to be called when the colour swatch is pressed by the user.
Note: The -dgc/dragCallback and -dpc/dropCallback are not available for this control.

    """
    pass
    


def changeSubdivComponentDisplayLevel(level=int, relative=boolean):
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
    


def channelBox( string , annotation=string, attrBgColor=float, float, float, attrColor=float, float, float, attrFilter=string, attrRegex=string, attributeEditorMode=boolean, backgroundColor=float, float, float, containerAtTop=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, enableLabelSelection=boolean, execute=string, boolean, exists=boolean, fieldWidth=int, fixedAttrList=string,..., fullPathName=boolean, height=int, highlightColor=float, float, float, historyObjectList=boolean, hyperbolic=boolean, inputs=boolean, isObscured=boolean, labelWidth=int, longNames=boolean, mainListConnection=string, mainObjectList=boolean, manage=boolean, maxHeight=int, maxWidth=int, niceNames=boolean, noBackground=boolean, nodeRegex=string, numberOfPopupMenus=boolean, outputObjectList=boolean, outputs=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, select=boolean, selectedHistoryAttributes=boolean, selectedMainAttributes=boolean, selectedOutputAttributes=boolean, selectedShapeAttributes=boolean, shapeObjectList=boolean, shapes=boolean, showNamespace=boolean, showTransforms=boolean, speed=float, takeFocus=boolean, update=boolean, useManips=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    channelBox is undoable, queryable, and editable.
    

    
This command creates a channel box, which is sensitive to the active list. It displays certain attributes (channels) of the last node on the active list, and provides a two-way connection to keep the widget up to date.
Note: when setting the color of attribute names, that color is only valid for its current Maya session; each subsequent session will display the default color for the attribute name(s) listed in the Channel Box. Any subsequent attributes that are added to the Channel Box will be affected by prior regular expressions in their current Maya session.

    """
    pass
    


def character( objects , addElement=name, addOffsetObject=string, characterPlug=boolean, clear=name, empty=boolean, excludeDynamic=boolean, excludeRotate=boolean, excludeScale=boolean, excludeTranslate=boolean, excludeVisibility=boolean, flatten=name, forceElement=name, include=name, intersection=name, isIntersecting=name, isMember=name, library=boolean, memberIndex=uint, name=string, noWarnings=boolean, nodesOnly=boolean, offsetNode=boolean, remove=name, removeOffsetObject=string, root=string, scheduler=boolean, split=name, subtract=name, text=string, union=name, userAlias=name):
    """
    character is undoable, queryable, and editable.
    

    
This command is used to manage the membership of a character. Characters are a type of set that gathers together the attributes of a node or nodes that a user wishes to animate as a single entity.

    """
    pass
    


def characterize(activatePivot=boolean, addAuxEffector=boolean, addFloorContactPlane=boolean, addMissingEffectors=boolean, attributeFromHIKProperty=string, attributeFromHIKPropertyMode=string, autoActivateBodyPart=boolean, changePivotPlacement=boolean, effectors=string, fkSkeleton=string, name=string, pinHandFeet=boolean, placeNewPivot=boolean, posture=string, sourceSkeleton=string, stancePose=string, type=string):
    """
    characterize is undoable, queryable, and editable.
    

    
This command is used to scan a joint hierarchy for predefined joint names or labels. If the required joints are found, human IK effectors will be created to control the skeleton using full-body IK. Alternatively, you can manually create all of the components required for fullbody IK, and use this command to hook them up. Fullbody IK needs 3 major components: the user input skeleton (sk), the fk skeleton on which keys are set (fk) and the hik effectors (ik). Together fk and ik provide parameters to the fullbody IK engine, which solves for the output and plots it onto sk. This command usage is used internally by Maya when importing data from fbx files, but is not generally recommended.
Note that a minimum set of required joint names or joint labels must be found in order for the characterize command to succeed. Please refer to the Maya documentation for details on properly naming or labeling your skeleton. The skeleton should also be z-facing, with its y-axis up, its left hand parallel to positive x-axis and right hand parallel to negative x-axis. END_COMMENT

    """
    pass
    


def characterMap(mapAttr=string, string, mapMethod=string, mapNode=string, string, mapping=string, proposedMapping=boolean, unmapAttr=string, string, unmapNode=string, string):
    """
    characterMap is undoable, queryable, and editable.
    

    
This command is used to create a correlation between the attributes of 2 or more characters.

    """
    pass
    


def checkBox( string , align=string, annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, offCommand=script, onCommand=script, parent=string, popupMenuArray=boolean, preventOverride=boolean, recomputeSize=boolean, useTemplate=string, value=boolean, visible=boolean, visibleChangeCommand=script, width=int):
    """
    checkBox is undoable, queryable, and editable.
    

    
This command creates a check box. A check box is a simple control containing a text label and a state of either on or off. Commands can be attached to any or all of the following events: when the check box is turned on, turned off, or simply when it's state is changed.

    """
    pass
    


def checkBoxGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, changeCommand1=script, changeCommand2=script, changeCommand3=script, changeCommand4=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enable1=boolean, enable2=boolean, enable3=boolean, enable4=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, label1=string, label2=string, label3=string, label4=string, labelArray2=string, string, labelArray3=string, string, string, labelArray4=string, string, string, string, manage=boolean, noBackground=boolean, numberOfCheckBoxes=int, numberOfPopupMenus=boolean, offCommand=script, offCommand1=script, offCommand2=script, offCommand3=script, offCommand4=script, onCommand=script, onCommand1=script, onCommand2=script, onCommand3=script, onCommand4=script, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, useTemplate=string, value1=boolean, value2=boolean, value3=boolean, value4=boolean, valueArray2=boolean, boolean, valueArray3=boolean, boolean, boolean, valueArray4=boolean, boolean, boolean, boolean, vertical=boolean, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def choice( objects , attribute=string, controlPoints=boolean, index=uint, name=string, selector=name, shape=boolean, sourceAttribute=name, time=time):
    """
    choice is undoable, queryable, and editable.
    

    
The choice command provides a mechanism for changing the inputs to an attribute based on some (usually time-based) criteria. For example, an object could be animated from frames 1 to 30 by a motion path, then from frames 30 to 50 it follows keyframe animation, and after frame 50 it returns to the motion path. Or, a revolve surface could change its input curve depending on some transform's rotation value.
The choice command creates a choice node (if one does not already exist) on all specified attributes of the selected objects. If the attribute was already connected to something, that something is now reconnected to the i'th index of the choice node's input (or the next available input if the -in/index flag is not specified). If a source attribute is specified, then that attribute is connected to the choice node's i'th input instead.
The choice node operates by using the value of its selector attribute to determine which of its input attributes to pass through to its output. The input attributes can be of any type. For example, if the selector attribute was connected by an animation curve with keyframes at (1,1), (30,2) and (50,1), then that would mean that the choice node would pass on the data from input[1] from time 1 to 30, and after time 50, and the data from input[2] between times 30 and 50.
This command returns the names of the created or modified choice nodes, and if a keyframe was added to the animation curve, it specifies the index (or value on the animation curve).

    """
    pass
    


def circle(caching=boolean, center=linear, linear, linear, centerX=linear, centerY=linear, centerZ=linear, constructionHistory=boolean, degree=int, first=linear, linear, linear, firstPointX=linear, firstPointY=linear, firstPointZ=linear, fixCenter=boolean, name=string, nodeState=int, normal=linear, linear, linear, normalX=linear, normalY=linear, normalZ=linear, object=boolean, radius=linear, sections=int, sweep=angle, tolerance=linear, useTolerance=boolean):
    """
    circle is undoable, queryable, and editable.
    

    
The circle command creates a circle or partial circle (arc)

    """
    pass
    


def circularFillet( surface surface , caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, name=string, nodeState=int, object=boolean, positionTolerance=float, primaryRadius=linear, secondaryRadius=linear, tangentTolerance=float):
    """
    circularFillet is undoable, queryable, and editable.
    

    
The cmd is used to compute the rolling ball surface fillet ( circular fillet ) between two given NURBS surfaces. To generate trim curves on the surfaces, use -cos true.

    """
    pass
    


def clearCache(allNodes=boolean, computed=boolean, dirty=boolean):
    """
    clearCache is NOT undoable, NOT queryable, and NOT editable.
    

    
Even though dependency graph values are computed or dirty they may still occupy space temporarily within the nodes. This command goes in to all of the data that can be regenerated if required and removes it from the caches (datablocks), thus clearing up space in memory.

    """
    pass
    


def clip(absolute=boolean, absoluteRotations=boolean, active=string, addTrack=boolean, allAbsolute=boolean, allClips=boolean, allRelative=boolean, allSourceClips=boolean, animCurveRange=boolean, character=boolean, constraint=boolean, copy=boolean, defaultAbsolute=boolean, duplicate=boolean, endTime=time, expression=boolean, ignoreSubcharacters=boolean, isolate=boolean, leaveOriginal=boolean, mapMethod=string, name=string, newName=string, paste=boolean, pasteInstance=boolean, remove=boolean, removeTrack=boolean, rotationOffset=float, float, float, rotationsAbsolute=boolean, scheduleClip=boolean, sourceClipName=boolean, split=time, startTime=time, translationOffset=float, float, float, useChannel=string):
    """
    clip is undoable, queryable, and editable.
    

    
This command is used to create, edit and query character clips.

    """
    pass
    


def clipEditor( editorName , allTrackHeights=int, autoFit=string, clipDropCmd=string, clipStyle=int, control=boolean, defineTemplate=string, deleteCmd=string, deselectAll=boolean, displayActiveKeyTangents=string, displayActiveKeys=string, displayInfinities=string, displayKeys=string, displayTangents=string, displayValues=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, frameAll=boolean, frameRange=float, float, highlightConnection=string, highlightedBlend=string, string, highlightedClip=string, string, initialized=boolean, listAllCharacters=boolean, listCurrentCharacters=boolean, lockMainConnection=boolean, lookAt=string, mainListConnection=string, manageSequencer=boolean, menuContext=string, panel=string, parent=string, selectBlend=string, string, string, selectClip=string, string, selectionConnection=string, snapTime=string, snapValue=string, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    clipEditor is undoable, queryable, and editable.
    

    
Create a clip editor with the given name.

    """
    pass
    


def clipEditorCurrentTimeCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    clipEditorCurrentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the track area of a clip editor.

    """
    pass
    


def clipMatching(clipDst=string, float, clipSrc=string, float, matchRotation=uint, matchTranslation=uint):
    """
    clipMatching is undoable, NOT queryable, and NOT editable.
    

    
This command is used to compute an offset to apply on a source clip in order to automatically align it to a destination clip at a specified match element. For this command to work, offset objects must be specified for the character.

    """
    pass
    


def clipSchedule(allAbsolute=boolean, allRelative=boolean, blend=uint, uint, blendNode=uint, uint, blendUsingNode=string, character=boolean, clipIndex=uint, cycle=float, defaultAbsolute=boolean, enable=boolean, group=boolean, groupIndex=uint, groupName=string, hold=time, insertTrack=uint, instance=string, listCurves=boolean, listPairs=boolean, lock=boolean, mute=boolean, name=string, postCycle=float, preCycle=float, remove=boolean, removeBlend=uint, uint, removeEmptyTracks=boolean, removeTrack=uint, rotationsAbsolute=boolean, scale=float, shift=int, shiftIndex=uint, solo=boolean, sourceClipName=boolean, sourceEnd=time, sourceStart=time, start=time, track=uint, weight=float, weightStyle=uint):
    """
    clipSchedule is undoable, queryable, and editable.
    

    
This command is used to create, edit and query clips and blends in the Trax editor. It operates on the clipScheduler node attached to the character. In query mode, if no flags are specified, returns an array of strings in this form: (clipName,clipIndex,clipStart,clipSourceStart,clipSourceEnd,clipScale,clipPreCycle,clipPostCycle,clipHold)

    """
    pass
    


def clipSchedulerOutliner( string , annotation=string, backgroundColor=float, float, float, clipScheduler=string, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    clipSchedulerOutliner is undoable, queryable, and editable.
    

    
This command creates/edits/queries a clip scheduler outliner control.

    """
    pass
    


def closeCurve( curve , blendBias=float, blendKnotInsertion=boolean, caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, name=string, nodeState=int, object=boolean, parameter=float, preserveShape=int, replaceOriginal=boolean):
    """
    closeCurve is undoable, queryable, and editable.
    

    
The closeCurve command closes a curve, making it periodic. The pathname to the newly closed curve and the name of the resulting dependency node are returned. If a curve is not specified in the command, then the first active curve will be used.

    """
    pass
    


def closeSurface( surface|surfaceIsoparm , blendBias=float, blendKnotInsertion=boolean, caching=boolean, constructionHistory=boolean, direction=int, name=string, nodeState=int, object=boolean, parameter=float, preserveShape=int, replaceOriginal=boolean):
    """
    closeSurface is undoable, queryable, and editable.
    

    
The closeSurface command closes a surface in the U, V, or both directions, making it periodic. The close direction is controlled by the direction flag. If a surface is not specified in the command, then the first selected surface will be used.
The pathname to the newly closed surface and the name of the resulting dependency node are returned.
This command also handles selected surface isoparms. For example, if an isoparm is specified, surface1.u[0.33], then the surface will be closed in V, regardless of the direction flag.

    """
    pass
    


def cluster( objects , after=boolean, afterReference=boolean, before=boolean, bindState=boolean, deformerTools=boolean, envelope=float, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, name=string, parallel=boolean, prune=boolean, relative=boolean, remove=boolean, resetGeometry=boolean, split=boolean, weightedNode=string, string):
    """
    cluster is undoable, queryable, and editable.
    

    
The cluster command creates a cluster or edits the membership of an existing cluster. The command returns the name of the cluster node upon creation of a new cluster.
After creating a cluster, the cluster's weights can be modified using the percent command or the set editor window.

    """
    pass
    


def cmdFileOutput(close=uint, closeAll=boolean, open=string, status=uint):
    """
    cmdFileOutput is undoable, queryable, and NOT editable.
    

    
This command will open a text file to receive all of the commands and results that normally get printed to the Script Editor window or console. The file will stay open until an explicit -close with the correct file descriptor or a -closeAll, so care should be taken not to leave a file open.
To enable logging to commence as soon as Maya starts up, the environment variable MAYA_CMD_FILE_OUTPUT may be specified prior to launching Maya. Setting MAYA_CMD_FILE_OUTPUT to a filename will create and output to that given file. To access the descriptor after Maya has started, use the -query and -open flags together.

    """
    pass
    


def cmdScrollFieldExecuter(appendText=string, autoCloseBraces=boolean, clear=boolean, commandCompletion=boolean, copySelection=boolean, currentLine=uint, cutSelection=boolean, execute=boolean, executeAll=boolean, filterKeyPress=script, hasFocus=boolean, hasSelection=boolean, insertText=string, load=boolean, loadContents=string, numberOfLines=uint, objectPathCompletion=boolean, pasteSelection=boolean, redo=boolean, removeStoredContents=string, replaceAll=string, string, saveSelection=string, saveSelectionToShelf=boolean, searchAndSelect=boolean, searchDown=boolean, searchMatchCase=boolean, searchString=string, searchWraps=boolean, select=uint, uint, selectAll=boolean, selectedText=boolean, showLineNumbers=boolean, showTooltipHelp=boolean, source=boolean, sourceType=string, spacesPerTab=uint, storeContents=string, tabsForIndent=boolean, text=string, textLength=boolean, undo=boolean):
    """
    cmdScrollFieldExecuter is undoable, queryable, and editable.
    

    
A script editor executer control used to issue script commands to Maya.

    """
    pass
    


def cmdScrollFieldReporter(clear=boolean, copySelection=boolean, cutSelection=boolean, echoAllCommands=boolean, filterSourceType=string, hasFocus=boolean, lineNumbers=boolean, pasteSelection=boolean, receiveFocusCommand=script, saveSelection=string, saveSelectionToShelf=boolean, select=uint, uint, selectAll=boolean, stackTrace=boolean, suppressErrors=boolean, suppressInfo=boolean, suppressResults=boolean, suppressStackTrace=boolean, suppressWarnings=boolean, text=string, textLength=boolean):
    """
    cmdScrollFieldReporter is undoable, queryable, and editable.
    

    
A script editor reporter control used to receive and display the history of processed commmands.

    """
    pass
    


def cmdShell( string , annotation=string, backgroundColor=float, float, float, clear=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfHistoryLines=int, numberOfPopupMenus=boolean, numberOfSavedLines=int, parent=string, popupMenuArray=boolean, preventOverride=boolean, prompt=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def collision( objects , friction=float, name=string, resilience=float):
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
    


def color( objects , rgbColor=float, float, float, userDefined=int):
    """
    color is undoable, NOT queryable, and NOT editable.
    

    
This command sets the dormant wireframe color of the specified objects to be their class color or if the -ud/userDefined flag is specified, one of the user defined colors. The -rgb/rgbColor flags can be specified if the user requires floating point RGB colors.

    """
    pass
    


def colorAtPoint(coordU=float, coordV=float, maxU=float, maxV=float, minU=float, minV=float, output=string, samplesU=uint, samplesV=uint):
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
    


def colorEditor(hsvValue=float, float, float, mini=boolean, parent=string, position=boolean, result=boolean, rgbValue=float, float, float):
    """
    colorEditor is undoable, queryable, and NOT editable.
    

    
The colorEditor command displays a modal dialog that may be used to specify colors in RGB or HSV. The default behaviour when no arguments are specified is to provide an initial color of black (rgb 0.0 0.0 0.0).
The command will return the user's color component values along with a boolean to indicate whether the dialog was dismissed by pressing the "OK" button. As an alternative to responding to the colorEditor command's return string you can now query the -rgb/rgbValue, -hsv/hsvValue, and -r/result flags to get the same information.

    """
    pass
    


def colorIndex( int float float float , hueSaturationValue=boolean, resetToFactory=boolean, resetToSaved=boolean):
    """
    colorIndex is undoable, queryable, and NOT editable.
    

    
The index specifies a color index in the color palette. The r, g, and b values (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is used) for the color.

    """
    pass
    


def colorIndexSliderGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, fullPathName=boolean, height=int, highlightColor=float, float, float, invisible=int, isObscured=boolean, label=string, manage=boolean, maxValue=int, minValue=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, useTemplate=string, value=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    colorIndexSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a color slider group consisting of a label, a color canvas and a slider. The value of the slider defines a color index into the a color table. The corresponding color is displayed in the canvas.

    """
    pass
    


def colorInputWidgetGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, hsvValue=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rgbValue=float, float, float, rowAttach=int, string, int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    colorInputWidgetGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
Create a color slider group consisting of a label, a color canvas, RGB and HSV sliders. Clicking on the canvas will bring up the color editor.

    """
    pass
    


def colorManagementCatalog(addTransform=string, editUserTransformPath=string, listSupportedExtensions=boolean, listTransformConnections=boolean, path=string, queryUserTransformPath=boolean, removeTransform=string, transformConnection=string, type=string):
    """
    colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.
    

    
This non-undoable action performs additions and removals of custom color transforms from the Autodesk native color transform catalog. Once a custom color transform has been added to the catalog, it can be used in the same way as the builtin Autodesk native color transforms.

    """
    pass
    


def colorManagementConvert(toDisplaySpace=float, float, float):
    """
    colorManagementConvert is NOT undoable, NOT queryable, and NOT editable.
    

    
This command can be used to convert rendering (a.k.a. working) space color values to display space color values. This is useful if you create custom UI with colors painted to screen, where you need to handle color management yourself. The current view transform set in the Color Management user preferences will be used.

    """
    pass
    


def colorManagementFileRules(addRule=string, colorSpace=string, down=string, evaluate=string, extension=string, listRules=boolean, load=boolean, moveUp=string, pattern=string, remove=string, save=boolean):
    """
    colorManagementFileRules is NOT undoable, queryable, and editable.
    

    
This non-undoable action manages the list of rules that Maya uses to assign an initial input color space to dependency graph nodes that read in color information from a file. Rules are structured in a chain of responsibility, from highest priority rule to lowest priority rule, each rule matching a file path pattern and extension. If a rule matches a given file path, its color space is returned as the result of rules evaluation, and no further rule is considered. The lowest priority rule will always return a match. Rules can be added, removed, and changed in priority in the list. Each rule can have its file path pattern, extension, and color space changed. The rule list can be saved to user preferences, and loaded from user preferences.

    """
    pass
    


def colorManagementPrefs(cmConfigFileEnabled=boolean, cmEnabled=boolean, colorManagePots=boolean, colorManagedNodes=boolean, colorManagementSDKVersion=string, configFilePath=string, defaultInputSpaceName=string, equalsToPolicyFile=string, exportPolicy=string, inputSpaceNames=boolean, loadPolicy=string, loadedDefaultInputSpaceName=string, loadedOutputTransformName=string, loadedRenderingSpaceName=string, loadedViewTransformName=string, missingColorSpaceNodes=boolean, ocioRulesEnabled=boolean, outputTarget=string, outputTransformEnabled=boolean, outputTransformName=string, outputTransformNames=boolean, outputUseViewTransform=boolean, policyFileName=string, popupOnError=boolean, renderingSpaceName=string, renderingSpaceNames=boolean, restoreDefaults=boolean, viewTransformName=string, viewTransformNames=boolean):
    """
    colorManagementPrefs is undoable, queryable, and editable.
    

    
This command allows querying and editing the color management global data in a scene. It also allows for setting the view transform and rendering space which automatically configures the color processing in the enabled views.

    """
    pass
    


def colorSliderButtonGrp( string , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, buttonCommand=script, buttonLabel=string, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, hsvValue=float, float, float, image=string, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rgbValue=float, float, float, rowAttach=int, string, int, symbolButtonCommand=script, symbolButtonDisplay=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    colorSliderButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command object creates a new color slider group with a button and a symbol button. This control is primarily used in the rendering UI. In this context, the button brings up a dialog that allows the user to assign a texture map to this parameter. Once a texture map is available, a symbol button shows up. When this symbol button is pressed, the user is taken to another dialog to edit the texture map.

    """
    pass
    


def colorSliderGrp( name , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, hsvValue=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rgbValue=float, float, float, rowAttach=int, string, int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    colorSliderGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a color Slider group consisting of a label, a color canvas and a slider. Clicking on the canvas will bring up the color editor dialog.

    """
    pass
    


def columnLayout( string , adjustableColumn=boolean, annotation=string, backgroundColor=float, float, float, childArray=boolean, columnAlign=string, columnAttach=string, int, columnOffset=string, int, columnWidth=int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowSpacing=int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    columnLayout is undoable, queryable, and editable.
    

    
This command creates a layout that arranges its children in a single column.

    """
    pass
    


def commandEcho(addFilter=string,..., filter=string,..., lineNumbers=boolean, state=boolean):
    """
    commandEcho is undoable, queryable, and NOT editable.
    

    
This command controls what is echoed to the command window.

    """
    pass
    


def commandLine( name , annotation=string, backgroundColor=float, float, float, command=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, enterCommand=script, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, holdFocus=int, inputAnnotation=string, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfHistoryLines=int, numberOfPopupMenus=boolean, outputAnnotation=string, parent=string, popupMenuArray=boolean, preventOverride=boolean, sourceType=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    commandLine is undoable, queryable, and editable.
    

    
This command creates a single line for command input/output.
The left half is for input, the right half for output.

    """
    pass
    


def commandLogging(historySize=uint, logCommands=boolean, logFile=string, recordCommands=boolean, resetLogFile=boolean):
    """
    commandLogging is undoable, queryable, and NOT editable.
    

    
This command controls logging of Maya commands, in memory and on disk.
Note that if commands are logged in memory, they will be available to the crash reporter and appear in crash logs.

    """
    pass
    


def commandPort(bufferSize=int, close=boolean, echoOutput=boolean, name=string, noreturn=boolean, pickleOutput=boolean, prefix=string, returnNumCommands=boolean, securityWarning=boolean, sourceType=string):
    """
    commandPort is undoable, queryable, and NOT editable.
    

    
Opens or closes the Maya command port. The command port comprises a socket to which a client program may connect. An example command port client "mcp" is included in the Motion Capture developers kit.
It supports multi-byte commands and uses utf-8 as its transform format. It will receive utf8 command string and decode it to Maya native coding. The result will also be encoded to utf-8 before sending back.
Care should be taken regarding INET domain sockets as no user identification, or authorization is required to connect to a given socket, and all commands (including "system(...)") are allowed and executed with the user id and permissions of the Maya user. The prefix flag can be used to reduce this security risk, as only the prefix command is executed.
The query flag can be used to determine if a given command port exists. See examples below.

    """
    pass
    


def componentBox( name , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, execute=string, boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, labelWidth=int, manage=boolean, maxHeight=int, maxWidth=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowHeight=int, selectedAttr=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    componentBox is undoable, queryable, and editable.
    

    
This command creates a component box, which is sensitive to the active list. It displays certain components of the last node on the active list, and provides a two-way connection to keep the widget up to date.

    """
    pass
    


def componentEditor( name , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, floatField=string, floatSlider=string, forceMainConnection=string, hidePathName=boolean, hideZeroColumns=boolean, highlightConnection=string, lockInput=boolean, lockMainConnection=boolean, mainListConnection=string, newTab=string, string, string, operationCount=boolean, operationLabels=boolean, operationType=int, panel=string, parent=string, precision=int, removeTab=string, selected=boolean, selectionConnection=string, setOperationLabel=int, string, showObjects=boolean, showSelected=boolean, sortAlpha=boolean, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    componentEditor is undoable, queryable, and editable.
    

    
This command creates a new component editor in the current layout.

    """
    pass
    


def condition( string , delete=boolean, dependency=string, initialize=boolean, script=string, state=boolean):
    """
    condition is undoable, queryable, and editable.
    

    
This command creates a new named condition object whose true/false value is calculated by running a mel script. This new condition can then be used for dimming, or controlling other scripts, or whatever.

    """
    pass
    


def cone(axis=linear, linear, linear, caching=boolean, constructionHistory=boolean, degree=int, endSweep=angle, heightRatio=float, name=string, nodeState=int, object=boolean, pivot=linear, linear, linear, polygon=int, radius=linear, sections=int, spans=int, startSweep=angle, tolerance=linear, useOldInitBehaviour=boolean, useTolerance=boolean):
    """
    cone is undoable, queryable, and editable.
    

    
The cone command creates a new cone and/or a dependency node that creates one, and returns their names.

    """
    pass
    


def confirmDialog(annotation=string, backgroundColor=float, float, float, button=string, cancelButton=string, defaultButton=string, dismissString=string, icon=string, message=string, messageAlign=string, parent=string, title=string):
    """
    confirmDialog is undoable, NOT queryable, and NOT editable.
    

    
The confirmDialog command creates a modal dialog with a message to the user and a variable number of buttons to dismiss the dialog. The dialog is dismissed when the user presses any button or chooses the close item from the window menu. In the case where a button is pressed then the name of the button selected is returned. If the dialog is dismissed via the close item then the string returned is specified by the dismissString flag.
The default behaviour when no arguments are specified is to create an empty single button dialog.

    """
    pass
    


def connectAttr( attribute attribute , force=boolean, lock=boolean, nextAvailable=boolean, referenceDest=string):
    """
    connectAttr is undoable, NOT queryable, and NOT editable.
    

    
Connect the attributes of two dependency nodes and return the names of the two connected attributes. The connected attributes must be be of compatible types. First argument is the source attribute, second one is the destination.
Refer to dependency node documentation.

    """
    pass
    


def connectControl( string attribute... , fileName=boolean, index=uint, preventContextualMenu=boolean, preventOverride=boolean):
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
    


def connectDynamic( objects , addScriptHandler=script, collisions=string, delete=boolean, emitters=string, fields=string, removeScriptHandler=int):
    """
    connectDynamic is undoable, NOT queryable, and NOT editable.
    

    
Dynamic connection specifies that the force fields, emitters, or collisions of an object affect another dynamic object. The dynamic object that is connected to a field, emitter, or collision object is influenced by those fields, emitters and collision objects.
Connections are made to individual fields, emitters, collisions. So, if an object owns several fields, if the user wants some of the fields to affect an object, s/he can specify each field with a "-f" flag; but if the user wants to connect all the fields owned by an object, s/he can specify the object name with the "-f" flag. The same is true for emitters and collisions. Different connection types (i.e., for fields vs. emitters) between the same pair of objects are logically independent. In other words, an object can be influenced by another object's fields without being influenced by its emitters or collisions.
Each connected object must be a dynamic object. The object connected to can be any object that owns fields, emitters, etc.; it need not be dynamic. Objects that can own influences are particles, geometry objects (nurbs and polys) and lattices. You can specify either the shape name or the transform name of the object to be influenced.

    """
    pass
    


def connectionInfo( string , destinationFromSource=boolean, getExactDestination=boolean, getExactSource=boolean, getLockedAncestor=boolean, isDestination=boolean, isExactDestination=boolean, isExactSource=boolean, isLocked=boolean, isSource=boolean, sourceFromDestination=boolean):
    """
    connectionInfo is undoable, NOT queryable, and NOT editable.
    

    
The connectionInfo command is used to get information about connection sources and destinations. Unlike the isConnected command, this command needs only one end of the connection.

    """
    pass
    


def connectJoint( objects , connectMode=boolean, parentMode=boolean):
    """
    connectJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will connect two skeletons based on the two selected joints. The first selected joint can be made a child of the parent of the second selected joint or a child of the second selected joint, depending on the flags used.
Note1: The first selected joint must be the root of a skeleton. The second selected joint must have a parent.
Note2: If a joint name is specified in the command line, it is used as the child and the first selected joint will be the parent. If no joint name is given at the command line, two joints must be selected.

    """
    pass
    


def constrain(barrier=boolean, damping=float, directionalHinge=boolean, hinge=boolean, interpenetrate=boolean, nail=boolean, name=string, orientation=float, float, float, pinConstraint=boolean, position=float, float, float, restLength=float, spring=boolean, stiffness=float):
    """
    constrain is undoable, queryable, and editable.
    

    
This command constrains rigid bodies to the world or other rigid bodies.

    """
    pass
    


def constructionHistory(toggle=boolean):
    """
    constructionHistory is undoable, queryable, and NOT editable.
    

    
This command turns construction history on or off.

    """
    pass
    


def container( string... , addNode=string,..., asset=string,..., assetMember=string, bindAttr=string, string, connectionList=boolean, current=boolean, fileName=string,..., findContainer=string,..., force=boolean, includeHierarchyAbove=boolean, includeHierarchyBelow=boolean, includeNetwork=boolean, includeNetworkDetails=string, includeShaders=boolean, includeShapes=boolean, includeTransform=boolean, isContainer=boolean, name=string, nodeList=boolean, nodeNamePrefix=boolean, parentContainer=boolean, preview=boolean, publishAndBind=string, string, publishAsChild=string, string, publishAsParent=string, string, publishAsRoot=string, boolean, publishAttr=string, publishConnections=boolean, publishName=string, removeContainer=boolean, removeNode=string,..., type=string, unbindAndUnpublish=string, unbindAttr=string, string, unbindChild=string, unbindParent=string, unpublishChild=string, unpublishName=string, unpublishParent=string, unsortedOrder=boolean):
    """
    container is undoable, queryable, and editable.
    

    
This command can be used to create and query container nodes. It is also used to perform operations on containers such as:
add and remove nodes from the container
publish attributes from nodes inside the container
replace the connections and values from one container onto another one
remove a container without removing its member nodes

    """
    pass
    


def containerBind(allNames=boolean, bindingSet=string, bindingSetConditions=boolean, bindingSetList=boolean, force=boolean, preview=boolean):
    """
    containerBind is undoable, queryable, and editable.
    

    
This is an accessory command to the container command which is used for some automated binding operations on the container. A container's published interface can be bound using a bindingSet on the associated container template.

    """
    pass
    


def containerProxy(fromTemplate=string, type=string):
    """
    containerProxy is undoable, queryable, and editable.
    

    
Creates a new container with the same published interface, dynamic attributes and attribute values as the specified container but with fewer container members. This proxy container can be used as a reference proxy so that values can be set on container attributes without loading in the full container. The proxy container will contain one or more locator nodes. The first locator has dynamic attributes that serve as stand-ins for the original published attributes. The remaining locators serve as stand-ins for any dag nodes that have been published as parent or as child and will be placed at the world space location of the published parent/child nodes. The expected usage of container proxies is to serve as a reference proxy for a referenced container. For automated creation, export and setup of the proxy see the doExportContainerProxy.mel script which is invoked by the "Export Container Proxy" menu item.

    """
    pass
    


def containerPublish(bindNode=string, string, bindTemplateStandins=boolean, inConnections=boolean, mergeShared=boolean, outConnections=boolean, publishNode=string, string, unbindNode=string, unpublishNode=string):
    """
    containerPublish is undoable, queryable, and editable.
    

    
This is an accessory command to the container command which is used for some advanced publishing operations on the container. For example, the "publishConnections" flag on the container will publish all the connections, but this command can be used to publish just the inputs, outputs, or to collapse the shared inputs into a single attribute before publishing.

    """
    pass
    


def containerTemplate(addBindingSet=string, addNames=boolean, addView=string, allKeyable=boolean, attribute=string, attributeList=string, baseName=string, bindingSetList=string, childAnchor=boolean, delete=boolean, exists=boolean, expandCompounds=boolean, fileName=string, force=boolean, fromContainer=string, fromSelection=boolean, layoutMode=int, load=boolean, matchFile=string, matchName=string, parentAnchor=boolean, publishedNodeList=string, removeBindingSet=string, removeView=string, rootTransform=boolean, save=boolean, searchPath=string, silent=boolean, templateList=string, unload=boolean, updateBindingSet=string, useHierarchy=boolean, viewList=string):
    """
    containerTemplate is NOT undoable, queryable, and editable.
    

    
A container template is a description of a container's published interface. This command provides the ability to create and save a template file for a container or load an existing template file. Once a template exists, the user can query the template information.

    """
    pass
    


def containerView(itemInfo=string, itemList=boolean, viewDescription=boolean, viewLabel=boolean, viewList=boolean, viewName=string):
    """
    containerView is NOT undoable, queryable, and editable.
    

    
A container view defines the layout information for the published attributes of a particular container. Container views can be selected from a set of built-in views or may be defined on an associated container template. This command queries the view-related information for a container node. The information returned from this command will be based on the view-related settings in force on the container node at the time of the query (i.e. the container's view mode, template name, view name attributes).

    """
    pass
    


def contentBrowser( string , addContentPath=string, context=string, , string, , , string, , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, location=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, preview=boolean, refreshTreeView=boolean, removeContentPath=string, saveCurrentContext=boolean, selectionConnection=string, stateString=boolean, thumbnailView=boolean, treeView=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    contentBrowser is undoable, queryable, and editable.
    

    
This command is used to edit and query a Content Browser. The Content Browser is a unique panel, so only one instance of it can exist at a given time. The optional argument is the name of the control.

    """
    pass
    


def contextInfo( context name , c=boolean, escapeContext=boolean, exists=boolean, image1=boolean, image2=boolean, image3=boolean, title=boolean):
    """
    contextInfo is undoable, queryable, and editable.
    

    
This command allows you to get information on named contexts.

    """
    pass
    


def control( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    control is undoable, queryable, and editable.
    

    
This command allows you to edit or query the properties of any control.

    """
    pass
    


def controller(allControllers=boolean, children=boolean, group=boolean, index=int, isController=string, parent=boolean, pickWalkDown=boolean, pickWalkLeft=boolean, pickWalkRight=boolean, pickWalkUp=boolean, unparent=boolean):
    """
    controller is undoable, queryable, and editable.
    

    
Commands for managing animation sources

    """
    pass
    


def convertIffToPsd(iffFileName=string, psdFileName=string, xResolution=int, yResolution=int):
    """
    convertIffToPsd is NOT undoable, queryable, and NOT editable.
    

    
Converts iff file to PSD file of given size

    """
    pass
    


def convertLightmap( string object string object ... , bakeSetDefault=string, bakeSetOverride=string, camera=string, exportPathNames=string, file=string, help=boolean, miStream=boolean, notUndoable=boolean, project=string, separator=string, shadows=boolean, transferMapSpace=string, useLensBake=boolean, vertexMap=boolean):
    """
    convertLightmap is undoable, NOT queryable, and NOT editable.
    

    
Calculating global illumination is an expensive and time-consuming task that denies its usage in realtime rendering. As long as the lighting conditions in scenes do not change, illumination on objects can be precomputed and stored in appropriate data structures, like texture maps or vertex colors. These can then be applied in realtime applications like hardware rendering and game engines.
The Lightmap Rendering feature allows to prerender surface color or surface lighting (including global illumination) into file textures and per-vertex colors, respectively, on a per object basis. These file textures can then be used as regular texture maps to speed up subsequent software renderings and to apply the precomputed rendering effects even to hardware rendering.
For the purposes of baking and prelighting, mental ray for Maya supports the convertLightmap command.
Any given shading group must be assigned to (some components) of the given object. Any number of shading group - object combinations can be given. The given object should uniquely identify a single instance of a single shape node. If just a transform name or a shape name is given, the command will try to determine the first child shape or instance parent. If a single object should be baked that has multiple materials assigned (per-face assignment on mesh objects, per-instance assignment on multiply instanced shape nodes) then every shading group has to be provided separately referencing the same object. On the other hand, if the same material has been applied to multiple objects (shared materials) then this shading group needs to be given multiple times for all of the objects.
Besides the command flags, per-object settings are set through bakeset of each object. If an object does not have a bakeset, and -bo flag is not specified, default settings for a bakeset will be used. See node reference of TextureBakeSet and VertexBakeSet
Limitations
The lightmap rendering is done with the render quality currently set in the mental ray render globals. Especially, photon tracing and/or final gathering should be enabled to compute global illumination that will be considered during lightmap generation. But certain limitations apply to the current implementation:
motion blur may not appear in lightmaps
volumes and fog are not recognized in lightmaps
the alpha channel is always rendered into file textures

    """
    pass
    


def convertSolidTx( node|attribute object... , alpha=boolean, antiAlias=boolean, backgroundColor=int, int, int, backgroundMode=string, camera=name, componentRange=boolean, doubleSided=boolean, fileFormat=string, fileImageName=string, fillTextureSeams=boolean, force=boolean, fullUvRange=boolean, name=string, pixelFormat=string, resolutionX=int, resolutionY=int, reuseDepthMap=boolean, samplePlane=boolean, samplePlaneRange=float, float, float, float, shadows=boolean, uvBBoxIntersect=boolean, uvRange=float, float, float, float, uvSetName=string):
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
    


def convertTessellation(allCameras=boolean, camera=name):
    """
    convertTessellation is undoable, NOT queryable, and NOT editable.
    

    
Command to translate the basic tessellation attributes to advanced. If a camera flag is specified the translation will be based on the distance the surface is from the camera. The closer the surface is to the camera the more triangles there will be in the tessellation. If the "-allCameras" flags is specified, the renderable camera closest to the surface will be used to set the tessellation. The camera tessellation estimate is also dependent on the current render resolution; a higher resolution the result in a more finely tessellated surface. Multiple NURB surfaces may be specified on the command line, or if no command arguments are specified the surfaces on the active list will be used. This command operates by calculating the chord height such that smooth tessellation is achieved when the surface is rendered. The advanced tessellation setting will be enabled on each surface specified, the primary tessellation parameters will be set, and chord height will be used as the secondary criteria.

    """
    pass
    


def convertUnit( string , fromUnit=string, toUnit=string):
    """
    convertUnit is undoable, NOT queryable, and NOT editable.
    

    
This command converts values between different units of measure. The command takes a string, because a string can incorporate unit names as well as values (see examples).

    """
    pass
    


def copyAttr(attribute=string, containerParentChild=boolean, inConnections=boolean, keepSourceConnections=boolean, outConnections=boolean, renameTargetContainer=boolean, values=boolean):
    """
    copyAttr is undoable, queryable, and editable.
    

    
Given two nodes, transfer the connections and/or the values from the first node to the second for all attributes whose names and data types match. When values are transferred, they are transferred directly. They are not mapped or modified in any way. The transferAttributes command can be used to transfer and remap some mesh attributes. The attributes flag can be used to specify a list of attributes to be processed. If the attributes flag is unused, all attributes will be processed. For dynamic attributes, the values and/or connections will only be transferred if the attributes names on both nodes match. This command does not support geometry shape nodes such as meshes, subds and nurbs. This command does not support transfer of multi-attribute values such as weight arrays.

    """
    pass
    


def copyDeformerWeights(destinationDeformer=string, destinationShape=string, mirrorInverse=boolean, mirrorMode=string, noMirror=boolean, smooth=boolean, sourceDeformer=string, sourceShape=string, surfaceAssociation=string, uvSpace=string, string):
    """
    copyDeformerWeights is undoable, queryable, and editable.
    

    
Command to copy or mirror the deformer weights accross one of the three major axes. The command can be used to mirror weights either from one surface to another or within the same surface.

    """
    pass
    


def copyFlexor( objects ):
    """
    copyFlexor is undoable, NOT queryable, and NOT editable.
    

    
This command copies an existing bone or joint flexor from one bone (joint) to another. The attributes of the flexor and their connections as well as any tweaks in on the latticeFfd are copied from the original to the new flexor. If the selected bone (joint) appears to be a mirror reflection of the bone (joint) of the existing flexor then the transform of the ffd lattice group gets reflected to the new bone (joint). The arguments for the command are the name of the ffd Lattice and the name of the destination joint. If they are not specified at the command line, they will be picked up from the current selection list.

    """
    pass
    


def copyKey( objects , animLayer=string, animation=string, attribute=string, clipboard=string, controlPoints=boolean, float=floatrange, forceIndependentEulerAngles=boolean, hierarchy=string, includeUpperBound=boolean, index=uint, option=string, shape=boolean, time=timerange):
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
    


def copySkinWeights(destinationSkin=string, influenceAssociation=string, mirrorInverse=boolean, mirrorMode=string, noBlendWeight=boolean, noMirror=boolean, normalize=boolean, sampleSpace=uint, smooth=boolean, sourceSkin=string, surfaceAssociation=string, uvSpace=string, string):
    """
    copySkinWeights is undoable, queryable, and editable.
    

    
Command to copy or mirror the skinCluster weights accross one of the three major axes. The command can be used to mirror weights either from one surface to another or within the same surface.

    """
    pass
    


def createAttrPatterns(patternDefinition=string, patternFile=string, patternType=string):
    """
    createAttrPatterns is undoable, NOT queryable, and NOT editable.
    

    
Create a new instance of an attribute pattern given a pattern type (e.g. XML) and a string or data file containing the description of the attribute tree in the pattern's format.

    """
    pass
    


def createDisplayLayer(empty=boolean, makeCurrent=boolean, name=string, noRecurse=boolean, number=int):
    """
    createDisplayLayer is undoable, NOT queryable, and NOT editable.
    

    
Create a new display layer. The display layer number will be assigned based on the first unassigned number not less than the base index number found in the display layer global parameters. Normally all objects and their descendants will be added to the new display layer but if the '-nr' flag is specified then only the objects themselves will be added.

    """
    pass
    


def createEditor( string node , queueForDelete=boolean):
    """
    createEditor is undoable, NOT queryable, and NOT editable.
    

    
This command creates a property sheet for any dependency node. The second argument is the name of the node, and the first is the name of a layout into which the property sheet controls should be placed.
The property sheets created by this command can by user-customized using the editorTemplate command.

    """
    pass
    


def createLayeredPsdFile(imageFileName=string, string, string, psdFileName=string, xResolution=uint, yResolution=uint):
    """
    createLayeredPsdFile is undoable, NOT queryable, and NOT editable.
    

    
Creates a layered PSD file with image names as input to individual layers

    """
    pass
    


def createNode( string , name=string, parent=string, shared=boolean, skipSelect=boolean):
    """
    createNode is undoable, NOT queryable, and NOT editable.
    

    
This command creates a new node in the dependency graph of the specified type.

    """
    pass
    


def createRenderLayer(empty=boolean, g=boolean, makeCurrent=boolean, name=string, noRecurse=boolean, number=int):
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
    


def ctxEditMode(buttonDown=boolean, buttonUp=boolean):
    """
    ctxEditMode is undoable, NOT queryable, and NOT editable.
    

    
This command tells the current context to switch edit modes.
It acts as a toggle.

    """
    pass
    


def ctxTraverse(down=boolean, left=boolean, right=boolean, up=boolean):
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
    


def currentTime( time , update=boolean):
    """
    currentTime is NOT undoable, queryable, and editable.
    

    
When given a time argument (with or without the -edit flag) this command sets the current global time. The model updates and displays at the new time, unless "-update off" is present on the command line.

    """
    pass
    


def currentTimeCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    currentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the graph editor

    """
    pass
    


def currentUnit(angle=string, fullName=boolean, linear=string, time=string, updateAnimation=boolean):
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
    


def curve( string , append=boolean, bezier=boolean, degree=float, editPoint=linear, linear, linear, knot=float, objectSpace=boolean, periodic=boolean, point=linear, linear, linear, pointWeight=linear, linear, linear, float, replace=boolean, worldSpace=boolean):
    """
    curve is undoable, NOT queryable, and NOT editable.
    

    
The curve command creates a new curve from a list of control vertices (CVs). A string is returned containing the pathname to the newly created curve. You can create a curve from points either in world space or object (local) space, either with weights or without. You can replace an existing curve by using the "-r/replace" flag. You can append a point to an existing curve by using the "-a/append" flag.
To create a curve-on-surface, use the curveOnSurface command.
To change the degree of a curve, use the rebuildCurve command.
To change the of parameter range curve, use the rebuildCurve command.

    """
    pass
    


def curveAddPtCtx(exists=boolean, image1=string, image2=string, image3=string):
    """
    curveAddPtCtx is undoable, queryable, and editable.
    

    
The curveAddPtCtx command creates a new curve add points context, which adds either control vertices (CVs) or edit points to an existing curve.

    """
    pass
    


def curveCVCtx(degree=uint, exists=boolean, history=boolean, image1=string, image2=string, image3=string, multEndKnots=boolean, name=string, uniform=boolean):
    """
    curveCVCtx is undoable, queryable, and editable.
    

    
The curveCVCtx command creates a new context for creating curves by placing control vertices (CVs).

    """
    pass
    


def curveEditorCtx(direction=int, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, relativeTangentSize=float, title=string):
    """
    curveEditorCtx is undoable, queryable, and editable.
    

    
The curveEditorCtx command creates a new NURBS editor context, which is used to edit a NURBS curve or surface.

    """
    pass
    


def curveEPCtx(degree=uint, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, uniform=boolean):
    """
    curveEPCtx is undoable, queryable, and editable.
    

    
The curveEPCtx command creates a new context for creating curves by placing edit points.

    """
    pass
    


def curveIntersect( string string , constructionHistory=boolean, direction=linear, linear, linear, tolerance=linear, useDirection=boolean):
    """
    curveIntersect is undoable, queryable, and editable.
    

    
You must specify two curves to intersect.
This command either returns the parameter values at which the given pair of curves intersect, or returns a dependency node that provides the intersection information. If you want to find the intersection of the curves in a specific direction you must use BOTH the "-useDirection" flag and the "direction" flag.

    """
    pass
    


def curveMoveEPCtx(exists=boolean, image1=string, image2=string, image3=string):
    """
    curveMoveEPCtx is undoable, queryable, and editable.
    

    
The curveMoveEPCtx command creates a new context for moving curve edit points using a manipulator. Edit points can only be moved one at a time.

    """
    pass
    


def curveOnSurface( string , append=boolean, degree=float, knot=float, periodic=boolean, positionUV=float, float, replace=boolean):
    """
    curveOnSurface is undoable, NOT queryable, and NOT editable.
    

    
The curve-on-surface command creates a new curve-on-surface from a list of control vertices (CVs). A string is returned containing the pathname to the newly created curve-on-surface. You can replace an existing curve by using the "-r/replace" flag. You can append points to an existing curve-on-surface by using the "-a/append" flag. See also the curve command, which describes how to query curve attributes.

    """
    pass
    


def curveRGBColor(hueSaturationValue=boolean, list=boolean, listNames=boolean, remove=boolean, resetToFactory=boolean, resetToSaved=boolean):
    """
    curveRGBColor is undoable, queryable, and NOT editable.
    

    
This command creates, changes or removes custom curve colors, which are used to draw the curves in the Graph Editor. The custom curve names may contain the wildcards "?", which marches a single character, and "*", which matches any number of characters. These colors are part of the UI and not part of the saved data for a model. This command is not undoable.

    """
    pass
    


def curveSketchCtx( object , degree=uint, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    curveSketchCtx is undoable, queryable, and editable.
    

    
The curveSketchCtx command creates a new curve sketch context, also known as the "pencil context".

    """
    pass
    


def cutKey( targetList , animation=string, attribute=string, clear=boolean, controlPoints=boolean, float=floatrange, hierarchy=string, includeUpperBound=boolean, index=uint, option=string, selectKey=boolean, shape=boolean, time=timerange):
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
    


def cycleCheck( string , all=boolean, children=boolean, dag=boolean, evaluation=boolean, firstCycleOnly=boolean, firstPlugPerNode=boolean, lastPlugPerNode=boolean, list=boolean, listSeparator=string, parents=boolean, secondary=boolean, timeLimit=time):
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
    


def cylinder(axis=linear, linear, linear, caching=boolean, constructionHistory=boolean, degree=int, endSweep=angle, heightRatio=float, name=string, nodeState=int, object=boolean, pivot=linear, linear, linear, polygon=int, radius=linear, sections=int, spans=int, startSweep=angle, tolerance=linear, useTolerance=boolean):
    """
    cylinder is undoable, queryable, and editable.
    

    
The cylinder command creates a new cylinder and/or a dependency node that creates one, and returns their names.

    """
    pass
    


def dagObjectCompare(attribute=boolean, bail=string, connection=boolean, namespace=string, relative=boolean, short=boolean, type=boolean):
    """
    dagObjectCompare is NOT undoable, NOT queryable, and NOT editable.
    

    
dagObjectCompare can be used to compare to compare objects based on:
type - Currently supports transform nodes and shape nodes
relatives - Compares DAG objects' children and parents
connections - Checks to make sure the two dags are connected to the same sources and destinations
attributes - Checks to make sure that the properties of active attributes are the same

    """
    pass
    


def dagPose( objects , addToPose=boolean, atPose=boolean, bindPose=boolean, g=boolean, members=boolean, name=string, remove=boolean, reset=boolean, restore=boolean, save=boolean, selection=boolean, worldParent=boolean):
    """
    dagPose is undoable, queryable, and editable.
    

    
This command is used to save and restore the matrix information for a dag hierarchy. Specifically, the data stored will restore the translate, rotate, scale, scale pivot, rotate pivot, rotation order, and (for joints) joint order for all the objects on the hierarchy. Data for other attributes is not stored by this command.
This command can also be used to store a bindPose for an object. When you skin an object, a dagPose is automatically created for the skin.

    """
    pass
    


def dataStructure(asFile=string, asString=string, dataType=boolean, format=string, listMemberNames=string, name=string, remove=boolean, removeAll=boolean):
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
    


def date(date=boolean, format=string, shortDate=boolean, shortTime=boolean, time=boolean):
    """
    date is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns information about current time and date. Use the predefined formats, or the -format flag to specify the output format.

    """
    pass
    


def dbcount(enabled=boolean, file=string, keyword=string, list=boolean, maxdepth=uint, quick=boolean, reset=boolean, spreadsheet=boolean):
    """
    dbcount is NOT undoable, NOT queryable, and NOT editable.
    

    
The dbcount command is used to print and manage a list of statistics collected for counting operations. These statistics are displayed as a list of hits on a particular location in code, with added reference information for pointers/strings/whatever. If -reset is not specified then statistics are printed.

    """
    pass
    


def dbmessage(file=string, list=boolean, monitor=boolean, type=string):
    """
    dbmessage is NOT undoable, NOT queryable, and NOT editable.
    

    
The dbmessage command is used to install monitors for certain message types, dumping debug information as they are sent so that the flow of messages can be examined.

    """
    pass
    


def dbpeek(allObjects=boolean, argument=string, count=uint, evaluationGraph=boolean, operation=string, outputFile=string):
    """
    dbpeek is NOT undoable, queryable, and NOT editable.
    

    
The dbpeek command is used to analyze the Maya data for information of interest. See a description of the flags for details on what types of things can be analyzed.

    """
    pass
    


def dbtrace(filter=string, info=boolean, keyword=string, mark=boolean, off=boolean, output=string, timed=boolean, title=string, verbose=boolean):
    """
    dbtrace is NOT undoable, queryable, and NOT editable.
    

    
The dbtrace command is used to manipulate trace objects. The keyword is the only mandatory argument, indicating which trace object is to be altered.
Trace Objects to affect (keyword KEY)
Optional filtering criteria (filter FILTER)
Function (off, output FILE, mark, title TITLE, timed : default operation is to enable traces)
You can use the query mode to find out which keywords are currently active (query with no arguments) or inactive (query with the off argument). You can enhance that query with or without a keyword argument to find out where their output is going (query with the output argument), out what filters are currently applied (query with the filter argument), or if their output will be timestamped (query with the timed argument).

    """
    pass
    


def defaultLightListCheckBox(annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, shadingGroup=name, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    defaultLightListCheckBox is undoable, queryable, and editable.
    

    
This command creates a checkBox that controls whether a shadingGroup is connected/disconnected from the defaultLightList.

    """
    pass
    


def defaultNavigation(connectToExisting=boolean, createNew=boolean, defaultAttribute=boolean, defaultTraversal=boolean, defaultWorkingNode=boolean, delete=boolean, destination=name, force=boolean, ignore=boolean, navigatorDecisionString=string, quiet=boolean, relatedNodes=boolean, source=name, unignore=boolean):
    """
    defaultNavigation is undoable, NOT queryable, and NOT editable.
    

    
The defaultNavigation command defines default behaviours when creating or manipulating connections between nodes and when navigating between nodes via those connections. This command is primarily used by attribute editors.

    """
    pass
    


def defineDataServer(device=string, server=string, undefine=boolean):
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
    


def defineVirtualDevice(axis=int, channel=string, clear=boolean, create=boolean, device=string, parent=string, undefine=boolean, usage=string):
    """
    defineVirtualDevice is undoable, queryable, and NOT editable.
    

    
This command defines a virtual device. Virtual devices act like real devices and are useful to manipulate/playback data when an command device is not connected to the computer.

    """
    pass
    


def deformer( selectionList , after=boolean, afterReference=boolean, before=boolean, deformerTools=boolean, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, name=string, parallel=boolean, prune=boolean, remove=boolean, split=boolean, type=string):
    """
    deformer is undoable, queryable, and editable.
    

    
This command creates a deformer of the specified type. The deformer will deform the selected objects.

    """
    pass
    


def deformerEvaluator(chains=boolean, meshes=boolean):
    """
    deformerEvaluator is NOT undoable, queryable, and NOT editable.
    

    
Print debug information about deformer evaluator status. In query mode the debug information is returned as a string[], otherwise the information is displayed in the script editor.

    """
    pass
    


def deformerWeights(attribute=string, defaultValue=float, deformer=string, export=boolean, ignoreName=boolean, im=boolean, method=string, path=string, positionTolerance=float, remap=string, shape=string, skip=string, vertexConnections=boolean, weightPrecision=uint, weightTolerance=float, worldSpace=boolean):
    """
    deformerWeights is undoable, queryable, and editable.
    

    
Command to import and export deformer weights to and from a simple XML file. The weight data is stored in a per-vertex fashion along with a "point cloud" corresponding to the vertices from the geometry input to the deformer. For example a cluster deformer would have the following information: On import the weights are then mapped back to a specified deformer based on the specified mapping method. Note that the geometry used to perform the mapping association is not the visible shape but rather the incoming geometry to the deformer. For example, in the case of a skin cluster this would be the bind pose geometry.

    """
    pass
    


def delete( objects , all=boolean, attribute=string, channels=boolean, constraints=boolean, constructionHistory=boolean, controlPoints=boolean, expressions=boolean, hierarchy=string, inputConnectionsAndNodes=boolean, shape=boolean, staticChannels=boolean, timeAnimationCurves=boolean, unitlessAnimationCurves=boolean):
    """
    delete is undoable, NOT queryable, and NOT editable.
    

    
This command is used to delete selected objects, or all objects, or objects specified along with the command. Flags are available to filter the type of objects that the command acts on.
At times, more than just specified items will be deleted. For example, deleting two CVs in the same "row" on a NURBS surface will delete the whole row.

    """
    pass
    


def deleteAttr( node...|attribute... , attribute=string, name=string):
    """
    deleteAttr is undoable, queryable, and editable.
    

    
This command is used to delete a dynamic attribute from a node or nodes. The attribute can be specified by using either the long or short name. Only one dynamic attribute can be deleted at a time. Static attributes cannot be deleted. Children of a compound attribute cannot be deleted. You must delete the complete compound attribute. This command has no edit capabilities. The only query ability is to list all the dynamic attributes of a node.

    """
    pass
    


def deleteAttrPattern(allPatterns=boolean, patternName=string, patternType=string):
    """
    deleteAttrPattern is undoable, NOT queryable, and NOT editable.
    

    
After a while the list of attribute patterns could become cluttered. This command provides a way to remove patterns from memory so that only the ones of interest will show.

    """
    pass
    


def deleteExtension(attribute=string, forceDelete=boolean, nodeType=string):
    """
    deleteExtension is NOT undoable, NOT queryable, and NOT editable.
    

    
This command is used to delete an extension attribute from a node type. The attribute can be specified by using either the long or short name. Only one extension attribute can be deleted at a time. Children of a compound attribute cannot be deleted, you must delete the complete compound attribute. This command has no undo, edit, or query capabilities.

    """
    pass
    


def deleteUI( string string... , collection=boolean, control=boolean, editor=boolean, layout=boolean, menu=boolean, menuItem=boolean, panel=boolean, panelConfig=boolean, radioMenuItemCollection=boolean, toolContext=boolean, uiTemplate=boolean, window=boolean):
    """
    deleteUI is undoable, NOT queryable, and NOT editable.
    

    
This command deletes UI objects such as windows and controls. Deleting a layout or window will also delete all of its children. If a flag is used then all objects being deleted must be of the specified type. This command may not be edited or queried.
NOTE: it is recommended that the type flags be used to disambiguate different kinds of objects with the same name.

    """
    pass
    


def deltaMush( selectionList , after=boolean, afterReference=boolean, before=boolean, deformerTools=boolean, envelope=float, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, name=string, parallel=boolean, pinBorderVertices=boolean, prune=boolean, remove=boolean, smoothingIterations=uint, smoothingStep=float, split=boolean):
    """
    deltaMush is undoable, queryable, and editable.
    

    
This command is used to create, edit and query deltaMush nodes.

    """
    pass
    


def detachCurve( curve , caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, keep=boolean, name=string, nodeState=int, object=boolean, parameter=float, replaceOriginal=boolean):
    """
    detachCurve is undoable, queryable, and editable.
    

    
The detachCurve command detaches a curve into pieces, given a list of parameter values. You can also specify which pieces to keep and which to discard using the "-k" flag. The names of the newly detached curve(s) is returned. If history is on, then the name of the resulting dependency node is also returned.
You can use this command to open a periodic curve at a particular parameter value. You would use this command with only one "-p" flag.
If you are specifying "-k" flags, then you must specify one, none or all "-k" flags. If you are specifying all "-k" flags, there must be one more "-k" flag than "-p" flags.

    """
    pass
    


def detachDeviceAttr(all=boolean, attribute=string, axis=string, device=string, selection=boolean):
    """
    detachDeviceAttr is undoable, queryable, and NOT editable.
    

    
This command detaches connections between device axes and node attributes. The command line arguments are the same as for the corresponding attachDeviceAttr except for the clutch argument which can not be used in this command.

    """
    pass
    


def detachSurface( surface , caching=boolean, constructionHistory=boolean, direction=int, keep=boolean, name=string, nodeState=int, object=boolean, parameter=float, replaceOriginal=boolean):
    """
    detachSurface is undoable, queryable, and editable.
    

    
The detachSurface command detaches a surface into pieces, given a list of parameter values and a direction. You can also specify which pieces to keep and which to discard using the "-k" flag. The names of the newly detached surface(s) are returned. If history is on, the name of the resulting dependency node is also returned.
You can only detach in either U or V (not both) with a single detachSurface operation.
You can use this command to open a closed surface at a particular parameter value. You would use this command with only one "-p" flag.
If you are specifying "-k" flags, then you must specify one, none or all "-k" flags. If you are specifying all "-k" flags, there must be one more "-k" flag than "-p" flags.

    """
    pass
    


def deviceEditor(control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, selectionConnection=string, stateString=boolean, takePath=string, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    deviceEditor is undoable, queryable, and editable.
    

    
This creates an editor for creating/modifying attachments to input devices.

    """
    pass
    


def deviceManager(attachment=boolean, axisCoordChanges=boolean, axisIndex=int, axisName=boolean, axisOffset=boolean, axisScale=boolean, deviceIndex=int, deviceNameFromIndex=int, numAxis=boolean, numDevices=boolean):
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
    


def dgdirty(allPlugs=boolean, clean=boolean, implicit=boolean, list=string, propagation=boolean, showTiming=boolean, verbose=boolean):
    """
    dgdirty is NOT undoable, queryable, and NOT editable.
    

    
The dgdirty command is used to force a dependency graph dirty message on a node or plug. Used for debugging to find evaluation problems. If no nodes are specified then the current selection list is used. If the list flag is used it will return the list of things currently marked as dirty (or clean if the clean flag was also used). The returned values will be the names of plugs either clean/dirty themselves, at both ends of a clean/dirty connection, or representing the location of clean/dirty data on the node. Be careful using this option in conjunction with the all flag, the list could be huge.

    """
    pass
    


def dgeval( objects , src=boolean, verbose=boolean):
    """
    dgeval is undoable, NOT queryable, and NOT editable.
    

    
The dgeval command is used to force a dependency graph evaluate of a node or plug. Used for debugging to find propagation problems.
Normally the selection list is used to determine which objects to evaluate, but you can add to the selection list by specifying which objects you want on the command line.

    """
    pass
    


def dgfilter(attribute=string, list=boolean, logicalAnd=string, string, logicalNot=string, logicalOr=string, string, name=string, node=string, nodeType=string, plug=string):
    """
    dgfilter is NOT undoable, NOT queryable, and NOT editable.
    

    
The dgfilter command is used to define Dependency Graph filters that select DG objects based on certain criteria. The command itself can be used to filter objects or it can be attached to a dbtrace object to selectively filter what output is traced. If objects are specified then apply the filter to those objects and return a boolean indicating whether they passed or not, otherwise return then name of the filter. An invalid filter will pass all objects. For multiple objects the return value is the logical "AND" of all object's return values.

    """
    pass
    


def dgInfo(allNodes=boolean, connections=boolean, dirty=boolean, nodes=boolean, nonDeletable=boolean, outputFile=string, propagation=boolean, short=boolean, size=boolean, subgraph=boolean, type=string):
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
    


def dgtimer(combineType=boolean, hide=string, hierarchy=boolean, maxDisplay=int, name=string, noHeader=boolean, outputFile=string, overhead=boolean, rangeLower=float, rangeUpper=float, reset=boolean, returnCode=string, returnType=string, show=string, sortMetric=string, sortType=string, threshold=float, timerOff=boolean, timerOn=boolean, trace=boolean, type=string, uniqueName=boolean, updateHeatMap=int):
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
    


def dimWhen( string string , clear=boolean, false=boolean, true=boolean):
    """
    dimWhen is undoable, NOT queryable, and NOT editable.
    

    
This method attaches the named UI object (first argument) to the named condition (second argument) so that the object will be dimmed when the condition is in a particular state.
This command will fail if the object does not exist. If the condition does not exist (yet), that's okay --- a placeholder will be used until such a condition comes into existence.
The UI object should be one of two things, either a control or a menu item.

    """
    pass
    


def directionalLight(decayRate=int, discRadius=linear, intensity=float, name=string, rgb=float, float, float, shadowColor=float, float, float, shadowDither=float, shadowSamples=int, softShadow=boolean, useRayTraceShadows=boolean):
    """
    directionalLight is undoable, queryable, and editable.
    

    
The directionalLight command is used to edit the parameters of existing directionalLights, or to create new ones. The default behaviour is to create a new directionallight.

    """
    pass
    


def directKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, option=string, selectedOnly=boolean):
    """
    directKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to directly manipulate keyframes within the graph editor

    """
    pass
    


def dirmap( string string , convertDirectory=string, enable=boolean, getAllMappings=boolean, getMappedDirectory=string, mapDirectory=string, string, unmapDirectory=string):
    """
    dirmap is undoable, queryable, and NOT editable.
    

    
Use this command to map a directory to another directory. The first argument is the directory to map, and the second is the destination directory to map to.
Directories must both be absolute paths, and should be separated with forward slashes ('/'). The mapping is case-sensitive on all platforms. This command can be useful when moving projects to another machine where some textures may not be contained in the Maya project, or when a texture archive moves to a new location. This command is not necessary when moving a (self-contained) project from one machine to another - instead copy the entire project over and set the Maya project to the new location.
For one-time directory moves, if the command is enabled and the mapping configured correctly, when a scene is opened and saved the mapped locations will be reflected in the filenames saved with the file. To set up a permanent mapping the command should be enabled and the mappings set up in a script which is executed every time you launch Maya (userSetup.mel is sourced on startup). The directory mappings and enabled state are not preserved between Maya sessions. This command requires one "main" flag that specifies the action to take. Flags are:
-[m|um|gmd|gam|cd|en]

    """
    pass
    


def disable( string , value=boolean):
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
    


def disconnectAttr( attribute attribute , nextAvailable=boolean):
    """
    disconnectAttr is undoable, NOT queryable, and NOT editable.
    

    
Disconnects two connected attributes. First argument is the source attribute, second is the destination.

    """
    pass
    


def disconnectJoint(attachHandleMode=boolean, deleteHandleMode=boolean):
    """
    disconnectJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will break a skeleton at the selected joint and delete any associated handles.

    """
    pass
    


def diskCache(append=boolean, cacheType=string, close=string, closeAll=boolean, delete=string, deleteAll=boolean, empty=string, emptyAll=boolean, enabledCachesOnly=boolean, endTime=time, frameRangeType=string, overSample=boolean, samplingRate=int, startTime=time, tempDir=boolean):
    """
    diskCache is NOT undoable, queryable, and NOT editable.
    

    
Command to create, clear, or close disk cache(s).

    """
    pass
    


def displacementToPoly(findBboxOnly=boolean):
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
    


def displayColor(active=boolean, create=boolean, dormant=boolean, list=boolean, queryIndex=int, resetToFactory=boolean, resetToSaved=boolean):
    """
    displayColor is undoable, queryable, and NOT editable.
    

    
This command changes or queries the display color for anything in the application that allows the user to set its color. The color is defined by a color index into either the dormant or active color palette. These colors are part of the UI and not part of the saved data for a model. This command is not undoable.

    """
    pass
    


def displayCull( objects , backFaceCulling=boolean):
    """
    displayCull is undoable, queryable, and NOT editable.
    

    
This command is responsible for setting the display culling property of back faces of surfaces.

    """
    pass
    


def displayLevelOfDetail(levelOfDetail=boolean):
    """
    displayLevelOfDetail is undoable, queryable, and NOT editable.
    

    
This command is responsible for setting the display level-of-detail for edit refreshes. If enabled, objects will draw with lower detail based on their distance from the camera. When disabled objects will display at full resolution at all times. This is not an undoable command

    """
    pass
    


def displayPref(activeObjectPivots=boolean, displayAffected=boolean, displayGradient=boolean, ghostFrames=int, int, int, materialLoadingMode=string, maxHardwareTextureResolution=boolean, maxTextureResolution=int, purgeExistingTextures=boolean, regionOfEffect=boolean, shadeTemplates=boolean, textureDrawPixel=boolean, wireframeOnShadedActive=string):
    """
    displayPref is undoable, queryable, and NOT editable.
    

    
This command sets/queries the state of global display parameters.

    """
    pass
    


def displayRGBColor(create=boolean, hueSaturationValue=boolean, list=boolean, resetToFactory=boolean, resetToSaved=boolean):
    """
    displayRGBColor is undoable, queryable, and NOT editable.
    

    
This command changes or queries the display color for anything in the application that allows the user to set its color. These colors are part of the UI and not part of the saved data for a model. This command is not undoable.

    """
    pass
    


def displaySmoothness( objects , all=boolean, boundary=boolean, defaultCreation=boolean, divisionsU=int, divisionsV=int, full=boolean, hull=boolean, pointsShaded=int, pointsWire=int, polygonObject=int, renderTessellation=boolean, simplifyU=int, simplifyV=int):
    """
    displaySmoothness is undoable, queryable, and NOT editable.
    

    
This command is responsible for setting the display smoothness of NURBS curves and surfaces to either predefined or custom values. It also sets display modes for smoothness such as hulls and the hull simplification factors. At present, this command is NOT un-doable.

    """
    pass
    


def displayString(stringstringstringstring, delete=boolean, exists=boolean, keys=boolean, replace=boolean, value=string):
    """
    displayString is NOT undoable, queryable, and NOT editable.
    

    
Assign a string value to a string identifier. Allows you define a string in one location and then refer to it by its identifier in many other locations. Formatted strings are also supported (NOTE however, this functionality is now provided in a more general fashion by the format command, use of format is recommended). You may embed up to 3 special character sequences ^1s, ^2s, and ^3s to perform automatic string replacement. The embedded characters will be replaced with the extra command arguments. See example section for more detail. Note the extra command arguments do not need to be display string identifiers.

    """
    pass
    


def displaySurface( objects... , flipNormals=boolean, twoSidedLighting=boolean, xRay=boolean):
    """
    displaySurface is undoable, queryable, and NOT editable.
    

    
This command toggles display options on the specified or active surfaces. Typically this command applies to NURBS or poly mesh surfaces and ignores other type of objects.

    """
    pass
    


def distanceDimContext(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    distanceDimContext is undoable, queryable, and editable.
    

    
Command used to register the distanceDimCtx tool.

    """
    pass
    


def distanceDimension(endPoint=linear, linear, linear, startPoint=linear, linear, linear):
    """
    distanceDimension is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create a distance dimension to display the distance between two specified points.

    """
    pass
    


def doBlur(colorFile=string, length=float, sharpness=float, smooth=float, smoothColor=boolean, vectorFile=string):
    """
    doBlur is undoable, NOT queryable, and NOT editable.
    

    
The doBlur command will invoke the blur2d, which is a Maya stand-alone application to do 2.5 motion blur given the color image and the motion vector file. For a given input colorFile name, e.g. "xxx.iff", the output blurred image will be "xxx_blur.iff" in the same directory as the input colorFile. There is currently no control over the name of the output blurred image.

    """
    pass
    


def dockControl( name , allowedArea=string, annotation=string, area=string, backgroundColor=float, float, float, closeCommand=script, content=string, defineTemplate=string, docTag=string, dockStation=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, enablePopupOption=boolean, exists=boolean, fixedHeight=boolean, fixedWidth=boolean, floatChangeCommand=script, floating=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, moveable=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, r=boolean, retain=boolean, sizeable=boolean, splitLayout=string, state=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    dockControl is undoable, queryable, and editable.
    

    
Create a dockable control, also known as tool palette or utility window. Dock controls are secondary windows placed in the dock area around the central control in a main window. Dock windows can be moved inside their current area, moved into new areas and floated (e.g. undocked). Dock control consists of a title bar and the content area. The titlebar displays the dock control window title, a float button and a close button. Depending on the state of the dock control, the float and close buttons may be either disabled or not shown at all.

    """
    pass
    


def dolly( camera , absolute=boolean, distance=linear, dollyTowardsCenter=boolean, orthoScale=float, relative=boolean):
    """
    dolly is undoable, NOT queryable, and NOT editable.
    

    
The dolly command moves a camera along the viewing direction in the world space. The viewing-direction and up-direction of the camera are not altered. There are two modes of operation:
Relative mode: for a perspective camera, the camera is moved along its viewing direction, and the distance of travel is computed with respect to the current position of the camera in the world space. In relative mode, when the camera is moved, its COI is moved along with it, and is kept at the same distance, in front of the camera, as before applying the dolly operation. For orthographic camera, the viewing width of the camera is changed by scaling its ortho width by the new value specified on the command line.
Absolute mode: for a perspective camera, the camera is moved along its viewing direction, to the distance that is computed with respect to the current position of the world center of interest (COI) of the camera. In the absolute mode, when the camera is moved, the COI of the camera is not moved with the camera, but it is fixed at its current location in space. For orthographic camera, the viewing width of the camera is changed by replacing its ortho width with the new value specified on the command line. This command may be applied to more than one cameras; objects that are not cameras are ignored. When no camera name supplied on the command line, this command is applied to all currently active cameras.
The dolly command can be applied to either a perspective or an orthographic camera.

    """
    pass
    


def dollyCtx( object , alternateContext=boolean, boxDollyType=string, centerOfInterestDolly=boolean, dollyTowardsCenter=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, localDolly=boolean, name=string, orthoZoom=boolean, scale=float, toolName=string):
    """
    dollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a dolly context.

    """
    pass
    


def dopeSheetEditor( editorName , autoFit=string, control=boolean, defineTemplate=string, displayActiveKeyTangents=string, displayActiveKeys=string, displayInfinities=string, displayKeys=string, displayTangents=string, displayValues=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, hierarchyBelow=boolean, highlightConnection=string, lockMainConnection=boolean, lookAt=string, mainListConnection=string, outliner=string, panel=string, parent=string, selectionConnection=string, selectionWindow=float, float, float, float, showScene=boolean, showSummary=boolean, showTicks=boolean, snapTime=string, snapValue=string, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    dopeSheetEditor is undoable, queryable, and editable.
    

    
Edit a characteristic of a dope sheet editor

    """
    pass
    


def doubleProfileBirailSurface( curve curve curve curve , blendFactor=float, caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, polygon=int, tangentContinuityProfile1=boolean, tangentContinuityProfile2=boolean, transformMode=int):
    """
    doubleProfileBirailSurface is undoable, queryable, and editable.
    

    
The arguments are 4 cuves called "profile1" "profile2" "rail1" "rail2".
This command builds a railed surface by sweeping profile "profile1" along the two given rail curves "rail1", "rail2" until "profile2" is reached. By using the -blend control, the railed surface creation could be biased more towards one of the two profile curves. The curves ( both profiles and rails ) could also be surface curves ( isoparams, curve on surfaces ). If the profile curves are surface curves the surface constructed could be made tangent continuous to the surfaces underlying the profiles using the flags -tp1, -tp2 respectively. Current Limitation: Its necessary that the two profile curves intersect the rail curves for successful surface creation.

    """
    pass
    


def drag( objects , attenuation=float, directionX=float, directionY=float, directionZ=float, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear, useDirection=boolean):
    """
    drag is undoable, queryable, and editable.
    

    
Drag exerts a friction, or braking force proportional to the speed of a moving object. If direction is not enabled, the drag acts opposite to the current velocity of the object. If direction is enabled, it acts opposite to the component of the velocity in the specified direction. The force is independent of the position of the affected object.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def dragAttrContext( name , connectTo=name, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, reset=boolean):
    """
    dragAttrContext is undoable, queryable, and editable.
    

    
The dragAttrContext allows a user to manipulate the attributes of an object by using a virtual slider within the viewport. The virtual slider is used by dragging in a viewport with the middle mouse button. The speed at which the attributes are changed can be controlled by holding down the Ctrl key to slow it down and the Shift key to speed it up.

    """
    pass
    


def draggerContext( name , anchorPoint=float, float, float, button=int, currentStep=int, cursor=string, dragCommand=script, dragPoint=float, float, float, drawString=string, exists=boolean, finalize=script, history=boolean, holdCommand=script, image1=string, image2=string, image3=string, initialize=script, modifier=string, name=string, plane=float, float, float, prePressCommand=script, pressCommand=script, projection=string, releaseCommand=script, snapping=boolean, space=string, stepsCount=int, undoMode=string):
    """
    draggerContext is undoable, queryable, and editable.
    

    
The draggerContext allows the user to program the behavior of the mouse or an equivalent dragging device in MEL.

    """
    pass
    


def dropoffLocator( float float string selectionList ):
    """
    dropoffLocator is undoable, NOT queryable, and NOT editable.
    

    
This command adds one or more dropoff locators to a wire curve, one for each selected curve point. The dropoff locators can be used to provide localized tuning of the wire deformation about the curve point.
The arguments are two floats, the envelope and percentage, followed by the wire node name and then by the curve point(s).

    """
    pass
    


def duplicate( objects... , inputConnections=boolean, instanceLeaf=boolean, name=string, parentOnly=boolean, renameChildren=boolean, returnRootsOnly=boolean, smartTransform=boolean, upstreamNodes=boolean):
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
    


def duplicateCurve(constructionHistory=boolean, local=boolean, name=string, object=boolean, range=boolean):
    """
    duplicateCurve is undoable, queryable, and editable.
    

    
The duplicateCurve command takes a curve on a surface and and returns the 3D curve. The curve on a surface could be isoparam component, trimmed edge or curve on surface object.

    """
    pass
    


def duplicateSurface(constructionHistory=boolean, local=boolean, name=string, object=boolean):
    """
    duplicateSurface is undoable, queryable, and editable.
    

    
The duplicateSurface command takes a surface patch (face) and and returns the 3D surface. Connected patches are returned as a single surface.

    """
    pass
    


def dynamicLoad( string ):
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
    


def dynExport( objects , allObjects=boolean, attribute=string, format=string, maxFrame=time, minFrame=time, overSampling=int, path=string):
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
    


def dynExpression( selectionItem , creation=boolean, runtimeAfterDynamics=boolean, runtimeBeforeDynamics=boolean, string=string):
    """
    dynExpression is undoable, queryable, and editable.
    

    
This command describes an expression that belongs to the specified particle shape. The expression is a block of code of unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any numeric attribute(s) or per-particle attribute(s) in the scene. One expression can read and alter any number of these attributes. Every particle shape in your scene has three expressions, one for the runtimeBeforeDynamics, one for the runtimeAfterDynamics and one for creation time. The create expression gets executed for every particle in the object whose age is 0.0. The runtime expression gets executed for each particle with an age greater then 0.0. Unlike expressions created with the expression command, particle expressions always exist and are a part of the owning particle object's shape. They default to empty strings, but they are always there. Because of this, there is no need to use the '-e' flag. Every call to the dynExpression command is considered an edit by default. Per-particle attributes are those attributes of a particle shape that have a potentially different value for each particle in the object. Examples of these include position and velocity.
If this command is being sent by the command line or in a script, then the user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when reading them in the expression editor. Also, quotes in an expression must be escaped (\") so that they are not confused by the system as the end of your string. When using the expression editor, these characters are escaped for you unless they are already within quotes.
This type of expression is executed during the evaluation of the dynamics. If an output of the expression is requested before that, then the dynamics will be force to compute at that time. If dynamics is disabled, then these expressions will have no effect.

    """
    pass
    


def dynGlobals(active=boolean, listAll=boolean, overSampling=int):
    """
    dynGlobals is undoable, queryable, and editable.
    

    
This node edits and queries the attributes of the active dynGlobals node in the scene. There can be only one active node of this type. The active dynGlobals node is the first one that was created, either with a "createNode" command or by accessing/editing any of the attributes on the node through this command.

    """
    pass
    


def dynPaintEditor( editorName , activeOnly=boolean, autoSave=boolean, camera=string, canvasMode=boolean, canvasUndo=boolean, changeCommand=string, string, string, string, clear=float, float, float, control=boolean, currentCanvasSize=boolean, defineTemplate=string, displayAppearance=string, displayFog=boolean, displayImage=int, displayLights=string, displayStyle=string, displayTextures=boolean, docTag=string, doubleBuffer=boolean, drawAxis=boolean, drawContext=boolean, exists=boolean, fileName=string, filter=string, forceMainConnection=string, highlightConnection=string, iconGrab=boolean, loadImage=string, lockMainConnection=boolean, mainListConnection=string, menu=string, nbImages=boolean, newImage=int, int, float, float, float, paintAll=float, panel=string, parent=string, redrawLast=boolean, refresh=boolean, refreshMode=int, removeAllImages=boolean, removeImage=boolean, rollImage=float, float, saveAlpha=boolean, saveBumpmap=string, saveImage=boolean, scaleBlue=float, scaleGreen=float, scaleRed=float, selectionConnection=string, singleBuffer=boolean, snapShot=boolean, stateString=boolean, tileSize=int, unParent=boolean, undoCache=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string, wrap=boolean, boolean, writeImage=string, zoom=float):
    """
    dynPaintEditor is undoable, queryable, and editable.
    

    
Create a editor window that can be painted into

    """
    pass
    


def dynParticleCtx( string , conserve=float, cursorPlacement=boolean, exists=boolean, grid=boolean, gridSpacing=float, history=boolean, image1=string, image2=string, image3=string, jitterRadius=float, lowerLeftX=float, lowerLeftY=float, lowerLeftZ=float, name=string, nucleus=boolean, numJitters=int, particleName=string, sketch=boolean, sketchInterval=int, textPlacement=boolean, upperRightX=float, upperRightY=float, upperZ=float):
    """
    dynParticleCtx is undoable, queryable, and editable.
    

    
The particle context command creates a particle context. The particle context provides an interactive means to create particle objects. The particle context command also provides an interactive means to set the option values, through the Tool Property Sheet, for the "particle" command that the context will issue.

    """
    pass
    


def dynPref(autoCreate=boolean, echoCollision=boolean, runupFrom=int, runupToCurrentTime=boolean, saveOnQuit=boolean, saveRuntimeState=boolean):
    """
    dynPref is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current state of "autoCreate rigid bodies", "run up to current time", and "run up from" (previous time or start time).

    """
    pass
    


def editDisplayLayerGlobals(baseId=int, currentDisplayLayer=name, mergeType=int, useCurrent=boolean):
    """
    editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    

    
Edit the parameter values common to all display layers. Some of these paremeters, eg. baseId and mergeType, are stored as preferences and some, eg. currentDisplayLayer, are stored in the file.

    """
    pass
    


def editDisplayLayerMembers(fullNames=boolean, noRecurse=boolean):
    """
    editDisplayLayerMembers is undoable, queryable, and NOT editable.
    

    
This command is used to query and edit membership of display layers. No equivalent 'remove' command is necessary since all objects must be in exactly one display layer. Removing an object from a layer can be accomplished by adding it to a different layer.

    """
    pass
    


def editMetadata(channelName=string, channelType=string, endIndex=string, index=string, indexType=string, memberName=string, remove=boolean, scene=boolean, startIndex=string, streamName=string, stringValue=string, value=float):
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
    


def editor( editorName , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, selectionConnection=string, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    editor is undoable, queryable, and editable.
    

    
Edit the characteristic of an editor

    """
    pass
    


def editorTemplate(addAdskAssetControls=boolean, addComponents=boolean, addControl=boolean, addDynamicControl=boolean, addExtraControls=boolean, addSeparator=boolean, annotateFieldOnly=boolean, annotation=string, beginLayout=string, beginNoOptimize=boolean, beginScrollLayout=boolean, callCustom=boolean, collapse=boolean, dimControl=string, string, boolean, endLayout=boolean, endNoOptimize=boolean, endScrollLayout=boolean, extraControlsLabel=string, interruptOptimize=boolean, label=string, listExtraAttributes=string, preventOverride=boolean, queryControl=string, string, queryLabel=string, string, queryName=string, string, removeControl=string, string, suppress=string):
    """
    editorTemplate is undoable, NOT queryable, and NOT editable.
    

    
The editorTemplate command allows the user to specify the conceptual layout of an attribute editor and leave the details of exactly which UI elements are used in the final result to the automatic dialog generation mechanism.

    """
    pass
    


def editRenderLayerAdjustment(attributeLog=boolean, layer=name, nodeLog=boolean, remove=boolean):
    """
    editRenderLayerAdjustment is undoable, queryable, and NOT editable.
    

    
This command is used to create, edit, and query adjustments to render layers. An adjustment allows different attribute values or connections to be used depending on the active render layer.

    """
    pass
    


def editRenderLayerGlobals(baseId=int, currentRenderLayer=name, enableAutoAdjustments=boolean, mergeType=int, useCurrent=boolean):
    """
    editRenderLayerGlobals is undoable, queryable, and NOT editable.
    

    
Edit the parameter values common to all render layers. Some of these paremeters, eg. baseId and mergeType, are stored as preferences and some, eg. currentRenderLayer, are stored in the file.

    """
    pass
    


def editRenderLayerMembers(fullNames=boolean, noRecurse=boolean, remove=boolean):
    """
    editRenderLayerMembers is undoable, queryable, and NOT editable.
    

    
This command is used to query and edit memberships to render layers. Only transform and geometry nodes may be members. At render time, all descendants of the members of a render layer will also be included in the render layer.

    """
    pass
    


def effector( object , hide=boolean, name=string):
    """
    effector is undoable, queryable, and editable.
    

    
The effector command is used to set the name or hidden flag for the effector. The standard edit (-e) and query (-q) flags are used for edit and query functions.

    """
    pass
    


def emit(attribute=string, floatValue=float, object=string, position=float, float, float, vectorValue=float, float, float):
    """
    emit is undoable, NOT queryable, and NOT editable.
    

    
The emit action allows users to add particles to an existing particle object without the use of an emitter. At the same time, it allows them to set any per-particle attribute for the particles that are created with the action.
The particles created do not become a part of the initial state for the particle object, and will disappear when the scene is rewound unless they are saved into the initial state by the user explicitly. In addition, a particle object will accept particles from an emit action ONLY at frames greater than or equal to its start frame. For example, if you want to use the emit action to create particles at frame -5, you must set startFrame for that particle shape to -5 or less.
Unlike many commands or actions, the emit action uses the order of its flags as important information as to how it works. The -object and -position flags can appear anywhere in the argument list. The -attribute and the value flags are interpreted based on their order. Any value flags after an -attribute flag and before the next -attribute flag will set the values for the attribute specified by the closest -attribute flag before them in the argument list. See the Examples section below for more detail on how these flags work.
Currently, no creation expression is executed for the new particles unless they are created from within a particle expression defined with the dynExpression command or the Expression Editor. If you want any particular values put into the particles at the time they are created, then those values should be set using the -attribute, -vectorValue, and -floatValue flags.

    """
    pass
    


def emitter( objects , alongAxis=float, aroundAxis=float, awayFromAxis=float, awayFromCenter=float, cycleEmission=string, cycleInterval=int, directionX=linear, directionY=linear, directionZ=linear, directionalSpeed=float, maxDistance=linear, minDistance=linear, needParentUV=boolean, normalSpeed=float, position=linear, linear, linear, randomDirection=float, rate=float, scaleRateByObjectSize=boolean, scaleSpeedBySize=boolean, speed=float, speedRandom=float, spread=float, tangentSpeed=float, torusSectionRadius=linear, type=string, volumeOffset=linear, linear, linear, volumeShape=string, volumeSweep=angle):
    """
    emitter is undoable, queryable, and editable.
    

    
Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the named/selected object(s)in the scene. Particles will then be emitted from each. If no objects are named or selected, or if the -pos option is specified, creates a positional emitter.
If an emitter was created, the command returns the name of the object owning the emitter, and the name of emitter shape. If an emitter was queried, the command returns the results of the query.
Keyframeable attributes of the emitter node: rate, directionX, directionY, directionZ, minDistance, maxDistance, spread.

    """
    pass
    


def enableDevice(apply=boolean, device=string, enable=boolean, monitor=boolean, record=boolean):
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
    


def encodeString( string ):
    """
    encodeString is undoable, NOT queryable, and NOT editable.
    

    
This action will take a string and encode any character that would need to be escaped before being sent to some other command. Such characters include:
double quotes
newlines
tabs

    """
    pass
    


def error(noContext=boolean, showLineNumber=boolean):
    """
    error is NOT undoable, NOT queryable, and NOT editable.
    

    
The error command is provided so that the user can issue error messages from his/her scripts and control execution in the event of runtime errors.
The string argument is displayed in the command window (or stdout if running in batch mode) after being prefixed with an error message heading and surrounded by //.
The error command also causes execution to terminate with an error. Using error is like raising an exception because the error will propagate up through the call chain. You can use catch to handle the error from the caller side. If you don't want execution to end, then you probably want to use the warning command instead.

    """
    pass
    


def eval( string ):
    """
    eval is NOT undoable, NOT queryable, and NOT editable.
    

    
This function takes a string which contains MEL code and evaluates it using the MEL interpreter. The result is converted into a Python data type and is returned. If an error occurs during the execution of the MEL script, a Python exception is raised with the appropriate error message.

    """
    pass
    


def evalDeferred( script , list=boolean, lowPriority=boolean, lowestPriority=boolean):
    """
    evalDeferred is undoable, NOT queryable, and NOT editable.
    

    
This command takes the string it is given and evaluates it during the next available idle time. It is useful for attaching commands to controls that can change or delete the control.

    """
    pass
    


def evaluationManager(asyncUpdate=boolean, cycleCluster=string, downstreamFrom=string, enabled=boolean, idleBuild=boolean, invalidate=boolean, manipulation=boolean, mode=string, nodeTypeGloballySerialize=boolean, nodeTypeParallel=boolean, nodeTypeSerialize=boolean, nodeTypeUntrusted=boolean, safeMode=boolean, upstreamFrom=string):
    """
    evaluationManager is NOT undoable, queryable, and NOT editable.
    

    
Handles turning on and off the evaluation manager method of evaluating the DG. Query the 'mode' flag to see all available evaluation modes. The special mode 'off' disables the evaluation manager. The scheduling override flags 'nodeTypeXXX' force certain node types to use specific scheduling types, even though the node descriptions might indicate otherwise. Use with caution; certain nodes may not react well to alternative scheduling types. Only one scheduling type override will be in force at a time, the most restrictive one. In order, they are untrusted, globally serialized, locally serialized, and parallel. The node types will however remember all overrides. For example, if you set a node type override to be untrusted, then to be parallel it will continue to use the untrusted override. If you then turn off the untrusted override, the scheduling will advance to the parallel one. The actual node scheduling type is always superceded by the overrides. For example, a serial node will still be considered as parallel if the node type has the parallel override set, even though 'serial' is a more restrictive scheduling type. See the 'dbpeek' command 'graph' operation with arguments 'evaluationGraph' and 'scheduling' to see what scheduling type any particular node will end up using after the hierarchy of overrides and native scheduling types is applied.

    """
    pass
    


def evaluator(clusters=boolean, configuration=string, enable=boolean, info=boolean, name=string, nodeType=string, nodeTypeChildren=boolean, priority=boolean, valueName=string):
    """
    evaluator is NOT undoable, queryable, and NOT editable.
    

    
Handles turning on and off custom evaluation overrides used by the evaluation manager. Query no flag to see all available custom evaluators. Query the 'enable' flag to check if an evaluator is currently enabled. If the 'name' flag isn't used then return all modes and their current active state.

    """
    pass
    


def event( object , count=uint, delete=boolean, dieAtCollision=boolean, emit=uint, list=boolean, name=string, proc=script, random=boolean, rename=string, select=boolean, split=uint, spread=float, target=string):
    """
    event is undoable, queryable, and editable.
    

    
The event command assigns collision events to a particle object. Collision events are stored in multi-attributes in the particle shape. The event command returns the event name.

    """
    pass
    


def exactWorldBoundingBox( dagObject... , ignoreInvisible=boolean):
    """
    exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.
    

    
This command figures out an exact-fit bounding box for the specified objects (or selected objects if none are specified) This bounding box is always in world space.

    """
    pass
    


def exclusiveLightCheckBox(annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, light=name, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    exclusiveLightCheckBox is undoable, queryable, and editable.
    

    
This command creates a checkBox that controls a light's exclusive non-exclusive status. An exclusive light is one that is not hooked up to the default-light-list, thus it does not illuminate all objects be default. However an exclusive light can be linked to an object.

    """
    pass
    


def exportEdits(editCommand=string, excludeHierarchy=boolean, excludeNode=string, exportSelected=boolean, force=boolean, includeAnimation=boolean, includeConstraints=boolean, includeDeformers=boolean, includeNetwork=boolean, includeNode=string, includeSetAttrs=boolean, includeSetDrivenKeys=boolean, includeShaders=boolean, onReferenceNode=string, selected=boolean, type=string):
    """
    exportEdits is NOT undoable, queryable, and NOT editable.
    

    
Use this command to export edits made in the scene to a file. The exported file can be subsequently imported to another scene. Edits may include: nodes, connections and reference edits such as value changes. The nodes that are included in the exported file will be based on the options used. At least one option flag that describes the set of target nodes to include in the exported file must be specified (e.g. 'selected', 'onReferenceNode'). Use the inclusion flags ('includeAnimation', 'includeShaders', 'includeNetwork') to specify which additional related nodes will be added to the export list. In export mode, when the command completes successfully, the name of the exported file will be returned. In query mode, this command will return information about the contents of the exported file. The query mode will return the list of nodes that will be considered for inclusion in the exported file based on the specified flags.

    """
    pass
    


def expression(alwaysEvaluate=uint, name=string, object=string, safe=string, shortNames=boolean, string=string, timeDependent=string, unitConversion=string):
    """
    expression is undoable, queryable, and editable.
    

    
This command describes an expression that belongs to the current scene. The expression is a block of code of unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any numeric attribute(s) in the scene. One expression can read and alter any number of numeric attributes. Theoretically, every expression in a scene can be combined into one long expression, but it is recommended that they are separated for ease of use and editing, as well as efficiency.
If this command is being sent by the command line or in a script, then the user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when reading them in the expression editor. Also, quotes in an expression must be escaped (\") so that they are not confused by the system as the end of your string. When using the expression editor, these characters are escaped for you unless they are already within quotes.
Note, expressions that alter or use per-particle attributes of a particle shape should use the 'dynExpression' command.

    """
    pass
    


def expressionEditorListen(listenFile=string, listenForAttr=string, listenForExpression=string, listenForName=string, stopListenForAttr=string, stopListenForExpression=string, stopListenForName=string):
    """
    expressionEditorListen is undoable, NOT queryable, and NOT editable.
    

    
Listens for messages for the Expression Editor, at its request, and communicates them to it. This action is for internal use only and should not be called by users. This action should be called only by the Expression Editor.

    """
    pass
    


def extendCurve( object , caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, distance=linear, extendMethod=int, extensionType=int, inputPoint=linear, linear, linear, join=boolean, name=string, nodeState=int, object=boolean, pointX=linear, pointY=linear, pointZ=linear, range=boolean, removeMultipleKnots=boolean, replaceOriginal=boolean, start=int):
    """
    extendCurve is undoable, queryable, and editable.
    

    
This command extends a curve or creates a new curve as an extension

    """
    pass
    


def extendSurface( surface surface , caching=boolean, constructionHistory=boolean, distance=linear, extendDirection=int, extendMethod=int, extendSide=int, extensionType=int, join=boolean, name=string, nodeState=int, object=boolean, replaceOriginal=boolean):
    """
    extendSurface is undoable, queryable, and editable.
    

    
This command extends a surface or creates a new surface as an extension.

    """
    pass
    


def extrude( curve curve , caching=boolean, constructionHistory=boolean, degreeAlongLength=int, direction=linear, linear, linear, directionX=linear, directionY=linear, directionZ=linear, extrudeType=int, fixedPath=boolean, length=linear, name=string, nodeState=int, object=boolean, pivot=linear, linear, linear, polygon=int, range=boolean, rebuild=boolean, reverseSurfaceIfPathReversed=boolean, rotation=angle, scale=float, subCurveSubSurface=boolean, useComponentPivot=int, useProfileNormal=boolean):
    """
    extrude is undoable, queryable, and editable.
    

    
This command computes a surface given a profile curve and possibly a path curve. There are three ways to extrude a profile curve. The most basic method is called a "distance" extrude where direction and length are specified. No path curve is necessary in this case. The second method is called "flat" extrude. This method sweeps the profile curve down the path curve without changing the orientation of the profile curve. Finally, the third method is called "tube" extrude. This method sweeps a profile curve down a path curve while the profile curve rotates so that it maintains a relationship with the path curve.

    """
    pass
    


def falloffCurve( string , addControlVertex=string, annotation=string, asString=string, backgroundColor=float, float, float, changeCommand=script, currentKey=int, currentKeyValue=float, float, customCurveWidget=boolean, defineTemplate=string, deleteControlVertex=int, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, optionVar=string, parent=string, popupMenuArray=boolean, preventOverride=boolean, readOnly=boolean, snapToGrid=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    falloffCurve is undoable, queryable, and editable.
    

    
This command creates a control for editing a 2D control curve. The control attaches to an optionVar used to store and retrieve the encoded control points stored in a string.

    """
    pass
    


def falloffCurveAttr( string , addControlVertex=string, annotation=string, asString=string, attribute=name, backgroundColor=float, float, float, changeCommand=script, currentKey=int, currentKeyValue=float, float, customCurveWidget=boolean, defineTemplate=string, deleteControlVertex=int, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, readOnly=boolean, selectedPositionControl=string, selectedValueControl=string, snapToGrid=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def file( string , activate=boolean, activeProxy=boolean, add=boolean, anyModified=boolean, applyTo=string, buildLoadSettings=boolean, channels=boolean, cleanReference=string, command=string, string, compress=boolean, constraints=boolean, constructionHistory=boolean, copyNumberList=boolean, defaultExtensions=boolean, defaultNamespace=boolean, deferReference=boolean, editCommand=string, errorStatus=boolean, executeScriptNodes=boolean, exists=boolean, expandName=boolean, exportAll=boolean, exportAnim=boolean, exportAnimFromReference=boolean, exportAsReference=boolean, exportAsSegment=boolean, exportSelected=boolean, exportSelectedAnim=boolean, exportSelectedAnimFromReference=boolean, exportSelectedNoReference=boolean, exportUnloadedReferences=boolean, expressions=boolean, flushReference=string, force=boolean, groupLocator=boolean, groupName=string, groupReference=boolean, i=boolean, ignoreVersion=boolean, importReference=boolean, lastFileOption=boolean, lastTempFile=boolean, list=boolean, loadAllDeferred=boolean, loadAllReferences=boolean, loadNoReferences=boolean, loadReference=string, loadReferenceDepth=string, loadReferencePreview=string, loadSettings=string, location=boolean, lockContainerUnpublished=boolean, lockFile=boolean, lockReference=boolean, mapPlaceHolderNamespace=string, string, mergeNamespaceWithParent=boolean, mergeNamespaceWithRoot=boolean, mergeNamespacesOnClash=boolean, modified=boolean, moveSelected=boolean, namespace=string, newFile=boolean, open=boolean, options=string, parentNamespace=boolean, postSaveScript=string, preSaveScript=string, preserveName=boolean, preserveReferences=boolean, preview=boolean, prompt=boolean, proxyManager=string, proxyTag=string, reference=boolean, referenceDepthInfo=uint, referenceNode=string, relativeNamespace=string, removeDuplicateNetworks=boolean, removeReference=boolean, rename=string, renameAll=boolean, renameToSave=boolean, renamingPrefix=string, renamingPrefixList=boolean, replaceName=string, string, resetError=boolean, returnNewNodes=boolean, save=boolean, saveDiskCache=string, saveReference=boolean, saveReferencesUnloaded=boolean, saveTextures=string, sceneName=boolean, segment=string, selectAll=boolean, shader=boolean, sharedNodes=string, sharedReferenceFile=boolean, shortName=boolean, strict=boolean, swapNamespace=string, string, type=string, uiConfiguration=boolean, unloadReference=string, unresolvedName=boolean, usingNamespaces=boolean, withoutCopyNumber=boolean, writable=boolean):
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
    


def fileBrowserDialog(actionName=string, dialogStyle=int, fileCommand=script, fileType=string, filterList=string, includeName=string, mode=int, operationMode=string, tipMessage=string, windowTitle=string):
    """
    fileBrowserDialog is undoable, NOT queryable, and NOT editable.
    

    
The fileBrowserDialog and fileDialog commands have now been deprecated. Both commands are still callable, but it is recommended that the fileDialog2 command be used instead. To maintain some backwards compatibility, both fileBrowserDialog and fileDialog will convert the flags/values passed to them into the appropriate flags/values that the fileDialog2 command uses and will call that command internally. It is not guaranteed that this compatibility will be able to be maintained in future versions so any new scripts that are written should use fileDialog2.
See below for an example of how to change a script to use fileDialog2.

    """
    pass
    


def fileDialog(application=boolean, defaultFileName=string, directoryMask=string, mode=int, title=string):
    """
    fileDialog is undoable, NOT queryable, and NOT editable.
    

    
The fileBrowserDialog and fileDialog commands have now been deprecated. Both commands are still callable, but it is recommended that the fileDialog2 command be used instead. To maintain some backwards compatibility, both fileBrowserDialog and fileDialog will convert the flags/values passed to them into the appropriate flags/values that the fileDialog2 command uses and will call that command internally. It is not guaranteed that this compatibility will be able to be maintained in future versions so any new scripts that are written should use fileDialog2.
See below for an example of how to change a script to use fileDialog2.

    """
    pass
    


def fileDialog2(cancelCaption=string, caption=string, dialogStyle=int, fileFilter=string, fileMode=int, fileTypeChanged=string, okCaption=string, optionsUICancel=string, optionsUICommit=string, optionsUICommit2=string, optionsUICreate=boolean, optionsUIInit=string, returnFilter=boolean, selectFileFilter=string, selectionChanged=string, startingDirectory=string):
    """
    fileDialog2 is undoable, NOT queryable, and NOT editable.
    

    
This command provides a dialog that allows users to select files or directories.

    """
    pass
    


def fileInfo(stringstring, remove=string):
    """
    fileInfo is NOT undoable, queryable, and NOT editable.
    

    
fileInfo provides a mechanism for keeping information related to a Maya scene file. Each invocation of the command consists of a keyword/value pair, where both the keyword and the associated value are strings. The command may be invoked multiple times with different keywords. Maya emits this command several times into each file it creates, primarily to provide details such as which productization or packaging of the program was used (e.g "Complete", "Unlimited"), the specific version and build identification that was run, and the operating system on which it was run. Maya may make use of this information when present in files it reads. All keyword/value pairs defined by use of the fileInfo command are preserved when Maya saves the scene, whether to an ASCII or binary file.

    """
    pass
    


def filePathEditor(attributeOnly=boolean, attributeType=string, byType=string, copyAndRepath=string, string, deregisterType=string, force=boolean, listDirectories=string, listFiles=string, listRegisteredTypes=boolean, preview=boolean, recursive=boolean, refresh=boolean, registerType=string, relativeNames=boolean, repath=string, replaceAll=boolean, replaceField=string, replaceString=string, string, status=boolean, temporary=boolean, typeLabel=string, unresolved=boolean, withAttribute=boolean):
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
    


def filletCurve( curve curve , bias=linear, blendControl=boolean, caching=boolean, circular=boolean, constructionHistory=boolean, curveParameter1=float, curveParameter2=float, depth=linear, freeformBlend=boolean, name=string, nodeState=int, object=boolean, radius=linear, replaceOriginal=boolean):
    """
    filletCurve is undoable, queryable, and editable.
    

    
The curve fillet command creates a fillet curve between two curves. If no objects are specified in the command line, then the first two active curves are used. The fillet created can be circular (with a radius) or freeform (with a type of tangent or blend).

    """
    pass
    


def filter(name=string, type=string):
    """
    filter is undoable, queryable, and editable.
    

    
Creates or modifies a filter node. Filter nodes are used by applyTake to modify recorded device data before assigning it to the param curves for the attached attributes.

    """
    pass
    


def filterCurve(endTime=time, filter=string, kernel=string, maxTimeStep=float, minTimeStep=float, period=float, startTime=time, timeTolerance=float, tolerance=float):
    """
    filterCurve is undoable, NOT queryable, and NOT editable.
    

    
The filterCurve command takes a list of anim curve and filters them. Currently only a Euler filter is supported. The Euler filter demangles discontinous rotation anim curves into smooth curves.

    """
    pass
    


def filterExpand(expand=boolean, fullPath=boolean, selectionMask=int, symActive=boolean, symNegative=boolean, symPositive=boolean, symSeam=boolean):
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
    


def filterStudioImport(convertShellToPoly=boolean, includeCameras=boolean, includeLights=boolean, transferDirectoryName=string):
    """
    filterStudioImport is NOT undoable, NOT queryable, and NOT editable.
    

    
Directly sets the filter options on the studioImport plugin from anywhere in MEL without having to use the UI. This is used by ViCE.

    """
    pass
    


def findKeyframe( animatedObject , animation=string, attribute=string, controlPoints=boolean, curve=boolean, float=floatrange, hierarchy=string, includeUpperBound=boolean, index=uint, shape=boolean, time=timerange, timeSlider=boolean, which=string):
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
    


def findType(deep=boolean, exact=boolean, forward=boolean, type=string):
    """
    findType is NOT undoable, NOT queryable, and NOT editable.
    

    
The findType command is used to search through a dependency subgraph on a certain node to find all nodes of the given type. The search can go either upstream (input connections) or downstream (output connections). The plug/attribute dependencies are not taken into account when searching for matching nodes, only the connections.

    """
    pass
    


def fitBspline(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, tolerance=linear):
    """
    fitBspline is undoable, queryable, and editable.
    

    
The fitBspline command fits the CVs from an input curve and and returns a 3D curve.

    """
    pass
    


def flexor( objects , atBones=boolean, atJoints=boolean, deformerCommand=string, list=boolean, name=string, noScale=boolean, toSkeleton=boolean, type=string):
    """
    flexor is undoable, queryable, and editable.
    

    
This command creates a flexor. A flexor a deformer plus a set of driving attributes. For example, a flexor might be a sculpt object that is driven by a joint's x rotation and a cube's y position.

    """
    pass
    


def floatField( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, enterCommand=script, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, receiveFocusCommand=script, showTrailingZeros=boolean, step=float, useTemplate=string, value=float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    floatField is undoable, queryable, and editable.
    

    
Create a field control that accepts only float values and is bound by a minimum and maximum value. An invisible slider is attached to the field and accessed by holding down the Ctrl modifier key while pressing one of the mouse buttons. Dragging the invisible slider to the right with the middle mouse button increases the field value by the amount specified with the -s/step flag, while dragging to the left decreases the value by the same amount. The left and right mouse buttons apply a factor of 0.1 and 10 to the step value.

    """
    pass
    


def floatFieldGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enable1=boolean, enable2=boolean, enable3=boolean, enable4=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfFields=int, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowAttach=int, string, int, showTrailingZeros=boolean, step=float, useTemplate=string, value=float, float, float, float, value1=float, value2=float, value3=float, value4=float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    floatFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text and editable float fields. The label text is optional and one to four float fields can be created.

    """
    pass
    


def floatScrollBar( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontal=boolean, isObscured=boolean, largeStep=float, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, step=float, useTemplate=string, value=float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    floatScrollBar is undoable, queryable, and editable.
    

    
Create a scroll bar control that accepts only float values and is bound by a minimum and maximum value. The scroll bar displays a marker indicating the current value of the scroll bar relative to it's minimum and maximum values. Click and drag the marker or on the scroll bar itself to change the current value.

    """
    pass
    


def floatSlider( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontal=boolean, isObscured=boolean, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, step=float, useTemplate=string, value=float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    floatSlider is undoable, queryable, and editable.
    

    
Create a slider control that accepts only float values and is bound by a minimum and maximum value. The slider displays a marker indicating the current value of the slider relative to it's minimum and maximum values. Click and drag the marker or on the slider itself to change the current value.

    """
    pass
    


def floatSlider2( string , annotation=string, backgroundColor=float, float, float, changeCommand1=string, changeCommand2=string, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, maximum=float, minimum=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, polarity=int, popupMenuArray=boolean, positionControl1=string, positionControl2=string, preventOverride=boolean, useTemplate=string, value1=float, value2=float, values=float, float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    floatSlider2 is undoable, queryable, and editable.
    

    
This command creates a float slider containing two handles. The two handles are arranged such that they cannot pass one another, thus handle 1 will always have a value less than or or equal to handle 2 when you adjust the values. Each handle may have a MEL command associated with it which is issued when the handle moves and thus can be used to update the values of plugs such as via a setAttr command. Each handle can also be associated with a float textfield to display the current value of the handle.
Note: the floatSlider2 widget currently only supports vertical (columnLayout) orientation.

    """
    pass
    


def floatSliderButtonGrp( name , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, buttonCommand=script, buttonLabel=string, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, field=boolean, fieldMaxValue=float, fieldMinValue=float, fieldStep=float, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, isObscured=boolean, label=string, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowAttach=int, string, int, sliderStep=float, step=float, symbolButtonCommand=script, symbolButtonDisplay=boolean, useTemplate=string, value=float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    floatSliderButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a float slider component with optional button and symbol buttons.
TelfFloatSliderGrpCmd.cpp

    """
    pass
    


def floatSliderGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, field=boolean, fieldMaxValue=float, fieldMinValue=float, fieldStep=float, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, maxValue=float, minValue=float, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowAttach=int, string, int, sliderStep=float, step=float, useTemplate=string, value=float, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def flow( objects , divisions=uint, uint, uint, localCompute=boolean, localDivisions=uint, uint, uint, objectCentered=boolean):
    """
    flow is undoable, queryable, and editable.
    

    
The flow command creates a deformation lattice to `bend' the object that is animated along a curve of a motion path animation. The motion path animation has to have the follow option set to be on.

    """
    pass
    


def flowLayout( string , annotation=string, backgroundColor=float, float, float, childArray=boolean, columnSpacing=int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, vertical=boolean, visible=boolean, visibleChangeCommand=script, width=int, wrap=boolean):
    """
    flowLayout is undoable, queryable, and editable.
    

    
This command creates a layout that arranges its children along a single line (either horizontal or vertical). Depending on the value of the -wrap boolean flag (default is false), if the layout's parent cannot fit all the children on one line, the children will either wrap onto the next line(s) or be truncated.

    """
    pass
    


def fluidCacheInfo(attribute=string, cacheTime=time, endFrame=boolean, hasCache=boolean, hasData=boolean, initialConditions=boolean, playback=boolean, resolution=boolean, startFrame=boolean):
    """
    fluidCacheInfo is undoable, queryable, and editable.
    

    
A command to get information about the fluids cache. Get the startFrame and resolution for InitialConditions. Get the endFrame as well for a playback cache. Note that for the playback cache, it will look at the current time (or last frame if the current time is past end of cache)

    """
    pass
    


def fluidEmitter( selectionList , cycleEmission=string, cycleInterval=int, densityEmissionRate=float, fluidDropoff=float, fuelEmissionRate=float, heatEmissionRate=float, maxDistance=linear, minDistance=linear, position=linear, linear, linear, rate=float, torusSectionRadius=linear, type=string, volumeOffset=linear, linear, linear, volumeShape=string, volumeSweep=angle):
    """
    fluidEmitter is undoable, queryable, and editable.
    

    
Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the named/selected object(s)in the scene. Fluid will then be emitted from each. If no objects are named or selected, or if the -pos option is specified, creates a positional emitter.
If an emitter was created, the command returns the name of the object owning the emitter, and the name of emitter shape. If an emitter was queried, the command returns the results of the query.

    """
    pass
    


def fluidVoxelInfo(checkBounds=boolean, inBounds=int, int, int, objectSpace=boolean, radius=float, voxel=float, float, float, voxelCenter=boolean, xIndex=int, yIndex=int, zIndex=int):
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
    


def fontDialog(FontList=boolean, scalable=boolean):
    """
    fontDialog is undoable, NOT queryable, and NOT editable.
    

    
Displays a dialog of available fonts for the user to select from. The name of the selected font is returned, or an empty string if no font was selected.
When the FontList flag is used, no dialog is displayed. Instead the command returns an array of the available fonts.

    """
    pass
    


def format(stringArg=string):
    """
    format is NOT undoable, NOT queryable, and NOT editable.
    

    
This command takes a format string, where the format string contains format specifiers. The format specifiers have a number associated with them relating to which parameter they represent to allow for alternate ordering of the passed-in values for other languages by merely changing the format string

    """
    pass
    


def formLayout( string , annotation=string, attachControl=string, string, int, string, attachForm=string, string, int, attachNone=string, string, attachOppositeControl=string, string, int, string, attachOppositeForm=string, string, int, attachPosition=string, string, int, int, backgroundColor=float, float, float, childArray=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfDivisions=int, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def frameBufferName(autoTruncate=boolean, camera=string, renderLayer=string, renderPass=string):
    """
    frameBufferName is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns the frame buffer name for a given renderPass renderLayer and camera combination. Optionally, this command can apply a name truncation algorithm so that the frameBuffer name will respect the maximum length imposed by the destination file format, if applicable.

    """
    pass
    


def frameLayout( string , annotation=string, backgroundColor=float, float, float, backgroundShade=boolean, borderStyle=string, borderVisible=boolean, childArray=boolean, collapsable=boolean, collapse=boolean, collapseCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, expandCommand=script, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, labelIndent=int, labelVisible=boolean, manage=boolean, marginHeight=int, marginWidth=int, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preCollapseCommand=script, preExpandCommand=script, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    frameLayout is undoable, queryable, and editable.
    

    
This command creates frame layout control. A frame layout may draw a border around its child controls as well as a display a title. Frame layouts may also be collapsable. Collapsing a frame layout will make the child of the frame layout invisible and shrink the frame layout size. The frame layout may then be expanded to make its child visible. Note that the frame layout may have only one child control. If you wish to have more than one child inside a frame layout then you must use some other control layout as the immediate child of the frame layout.

    """
    pass
    


def freeFormFillet( surfaceIsoparm surfaceIsoparm , bias=float, caching=boolean, constructionHistory=boolean, depth=float, name=string, nodeState=int, object=boolean, polygon=int, positionTolerance=float, range=boolean, tangentTolerance=float):
    """
    freeFormFillet is undoable, queryable, and editable.
    

    
This command creates a free form surface fillet across two surface trim edges or isoparms or curve on surface. The fillet surface creation has blend controls in the form of bias and depth. The bias value scales the tangents at the two ends across the two selected curves. The depth values controls the curvature of the fillet across the two selected curves. The default values of depth, bias are 0.5 and 0.5 respectively.

    """
    pass
    


def freeze(allNodes=boolean, displayLayers=boolean, downstream=boolean, frozen=boolean, invisible=boolean, noFreeze=boolean, unfreeze=boolean, upstream=boolean):
    """
    freeze is undoable, queryable, and NOT editable.
    

    
When a node is frozen none of its inputs will be requested when they change, the node will use the inputs that existed at the time of freezing until such time as the node is unfrozen. A node can be frozen in one of two ways; either directly, via setting the "frozen" attribute on the node to be true, or indirectly, via setting the "frozenAffected" extension attribute on the node to be true. This command lets you freeze nodes based on various criteria. See the flags for the types of criteria the command uses to decide what to freeze or unfreeze. The nodes you select will be considered to be frozen directly. Those affected by it, as dictated by the argument settings, will be considered to be frozen indirectly. If the frozen attribute, visibililty, or display layer mode has an input connection then the frozen state will not propagate as we can't be sure the node won't unfreeze or become visible at playback time. In query mode this command will find the nodes with each of the frozen states set (frozen, frozenAffected, and neither).

    """
    pass
    


def geomBind(bindMethod=uint, falloff=float, geodesicVoxelParams=uint, boolean, maxInfluences=int):
    """
    geomBind is undoable, queryable, and editable.
    

    
This command is used to compute weights using the GeomBind lib.

    """
    pass
    


def geometryConstraint( target... object , layer=string, name=string, remove=boolean, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    geometryConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position based on the shape of the target surface(s) at the closest point(s) to the object.
A geometryConstraint takes as input one or more surface shapes (the targets) and a DAG transform node (the object). The geometryConstraint position constrained object such object lies on the surface of the target with the greatest weight value. If two targets have the same weight value then the one with the lowest index is chosen.

    """
    pass
    


def geomToBBox(bakeAnimation=boolean, combineMesh=boolean, endTime=time, keepOriginal=boolean, name=string, nameSuffix=string, sampleBy=time, shaderColor=float, float, float, single=boolean, startTime=time):
    """
    geomToBBox is undoable, NOT queryable, and NOT editable.
    

    
Create polygonal mesh bounding boxes for geometry. Can also create a single bounding box per hierarchy.

    """
    pass
    


def getAttr( attribute , asString=boolean, caching=boolean, channelBox=boolean, expandEnvironmentVariables=boolean, keyable=boolean, lock=boolean, multiIndices=boolean, settable=boolean, silent=boolean, size=boolean, time=time, type=boolean):
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
    


def getClassification( string , satisfies=string):
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
    


def getFileList(filespec=string, folder=string):
    """
    getFileList is undoable, NOT queryable, and NOT editable.
    

    
Returns a list of files matching an optional wildcard pattern. Note that this command works directly on raw system files and does not go through standard Maya file path resolution.

    """
    pass
    


def getFluidAttr(attribute=string, lowerFace=boolean, xIndex=int, xvalue=boolean, yIndex=int, yvalue=boolean, zIndex=int, zvalue=boolean):
    """
    getFluidAttr is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in the grid.

    """
    pass
    


def getInputDeviceRange(maxValue=boolean, minValue=boolean):
    """
    getInputDeviceRange is undoable, NOT queryable, and NOT editable.
    

    
This command lists the minimum and maximum values the device axis can return. This value is the raw device values before any mapping is applied. If you don't specify an axis the values for all axes of the device are returned.

    """
    pass
    


def getMetadata(channelName=string, channelType=string, dataType=boolean, endIndex=string, index=string, indexType=string, listChannelNames=boolean, listMemberNames=boolean, listStreamNames=boolean, memberName=string, scene=boolean, startIndex=string, streamName=string):
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
    


def getModulePath(moduleName=string):
    """
    getModulePath is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns the module path for a given module name.

    """
    pass
    


def getPanel(allConfigs=boolean, allPanels=boolean, allScriptedTypes=boolean, allTypes=boolean, atPosition=int, int, configWithLabel=string, containing=string, invisiblePanels=boolean, scriptType=string, type=string, typeOf=string, underPointer=boolean, visiblePanels=boolean, withFocus=boolean, withLabel=string):
    """
    getPanel is undoable, NOT queryable, and NOT editable.
    

    
This command returns panel and panel configuration information.

    """
    pass
    


def getParticleAttr( selectionItem , array=boolean, attribute=string, object=string):
    """
    getParticleAttr is undoable, NOT queryable, and NOT editable.
    

    
This action will return either an array of values, or the average value and maximum offset, for a specied per-particle attribute of a particle object or component. If a particle component is specified on the command line, values are returned for that component only. If an object name is given instead, values are returned for all particles in that object. If no object name is passed, but a particle object or component is selected, values are returned for the selection.
If you list components, they must all be from the same particle object; the action ignores all objects after the first. Likewise if you list more than one object, the actiion will return values only for the first one.

    """
    pass
    


def getRenderDependencies(string):
    """
    getRenderDependencies is NOT undoable, NOT queryable, and NOT editable.
    

    
Command to return dependencies of an image source. Image sources (such as render targets) can depend on other upstream image sources that result from renderings of 3D scene, or renderings of 2D compositing graphs. This command returns these dependencies, so that they can be analyzed and rendered.

    """
    pass
    


def getRenderTasks(string, camera=string, renderLayer=string):
    """
    getRenderTasks is NOT undoable, NOT queryable, and NOT editable.
    

    
Command to return render tasks to render an image source. Image source can depend on upstream image sources that result from renderings of 3D scene, or 2D renderings (e.g. render targets). This command obtains the graph of image source render dependencies, and creates render tasks according to these dependencies. A render task has context, which can be camera, render layer, and resolution, or other, renderer-specific context. Because of image source overrides, the render task context depends on the path through the render dependency graph, with the most upstream override for a context item applied. As there can be multiple paths through a render dependency graph to a render dependency, there can be multiple render tasks for a given render dependency.

    """
    pass
    


def globalStitch( surface surface... , caching=boolean, lockSurface=boolean, maxSeparation=linear, modificationResistance=float, nodeState=int, sampling=int, stitchCorners=int, stitchEdges=int, stitchPartialEdges=boolean, stitchSmoothness=int):
    """
    globalStitch is undoable, queryable, and editable.
    

    
This command computes a globalStitch of NURBS surfaces. There should be at least one NURBS surface. The NURBS surface(s) should be untrimmed.

    """
    pass
    


def glRender(accumBufferPasses=int, alphaSource=string, antiAliasMethod=string, cameraIcons=boolean, clearClr=float, float, float, collisionIcons=boolean, crossingEffect=boolean, currentFrame=boolean, drawStyle=string, edgeSmoothness=float, emitterIcons=boolean, fieldIcons=boolean, flipbookCallback=string, frameEnd=int, frameIncrement=int, frameStart=int, fullResolution=boolean, grid=boolean, imageDirectory=string, imageName=string, imageSize=int, int, float, lightIcons=boolean, lightingMode=string, lineSmoothing=boolean, offScreen=boolean, renderFrame=string, renderSequence=string, sharpness=float, shutterAngle=float, textureDisplay=boolean, transformIcons=boolean, useAccumBuffer=boolean, viewport=int, int, float, writeDepthMap=boolean):
    """
    glRender is undoable, queryable, and editable.
    

    
This command provides access to the Hardware Render Manager (HRM). There is one-and-only-one HRM in maya. The HRM controls the rendering performed in the hardware render buffer window. This command allows shell scripts, to modify the render state, and to initiate a render request.

    """
    pass
    


def glRenderEditor( name , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, lookThru=string, mainListConnection=string, panel=string, parent=string, selectionConnection=string, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string, viewCameraName=boolean):
    """
    glRenderEditor is undoable, queryable, and editable.
    

    
Create a glRender view. This is a special view used for hardware rendering. This command is used to create and reparent the view as needed to support panels. See the glRender command for controlling the specific behavior of the hardware rendering.

    """
    pass
    


def goal( selectionList , goal=string, index=boolean, useTransformAsGoal=boolean, weight=float):
    """
    goal is undoable, queryable, and NOT editable.
    

    
Specifies the given objects as being goals for the given particle object. If the goal objects are geometry, each particle in the particle object will each try to follow or match its position to that of a certain vertex/CV/lattice point of the goal. If the goal object is another particle object, each particle will try to follow a paricle of the goal. In any other case, all the particles will try to follow the current location of the goal object's transform. You can get this latter behavior for a geometry or particle object too by using -utr true.
The goal weight can be keyframed. It lives on the particle object to which the goal was added and is a multi-attribute.

    """
    pass
    


def grabColor(hsvValue=boolean, rgbValue=boolean):
    """
    grabColor is undoable, NOT queryable, and NOT editable.
    

    
This command changes the cursor and enters a modal state which will be exited by pressing a mouse button. The color component values of the pixel below the cursor at the time of the button press are returned.

    """
    pass
    


def gradientControl( string , adaptiveScaling=boolean, annotation=string, attribute=name, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfControls=uint, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, refreshOnRelease=uint, selectedColorControl=string, selectedInterpControl=string, selectedPositionControl=string, staticNumberOfControls=boolean, staticPositions=boolean, upperLimitControl=string, useTemplate=string, verticalLayout=boolean, visible=boolean, visibleChangeCommand=script, width=int):
    """
    gradientControl is undoable, queryable, and editable.
    

    
This command creates a control that displays the gradient attribute specified. The gradient attribute must be of the correct form and naming. It should be a multi attribute with each entry a compound composed of:
Either a color compound or a float value (the control will automatically detect which and display a ramp or graph accordingly).
A single float attribute for position.
An enum for the interpolation types.
Currently the routines to get the value of a ramp structure (with interpolation) are not available through MEL, which limits the use of this control by end users. The MEL command AEaddRampControl should be used to attach this control to an attribute from attribute editor templates.

    """
    pass
    


def gradientControlNoAttr( string , annotation=string, asString=string, backgroundColor=float, float, float, changeCommand=script, currentKey=int, currentKeyChanged=script, currentKeyColorValue=float, float, float, currentKeyCurveValue=boolean, currentKeyInterpValue=int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, optionVar=string, parent=string, popupMenuArray=boolean, preventOverride=boolean, rampAsColor=boolean, useTemplate=string, valueAtPoint=float, visible=boolean, visibleChangeCommand=script, width=int):
    """
    gradientControlNoAttr is undoable, queryable, and editable.
    

    
This command creates a control for editing a ramp (2D control curve). The control attaches to an optionVar used to store and retrieve the encoded gradient control points stored in a string.

    """
    pass
    


def graphDollyCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    graphDollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create a dolly context for the graph editor.

    """
    pass
    


def graphSelectContext(exists=boolean, image1=string, image2=string, image3=string):
    """
    graphSelectContext is undoable, queryable, and editable.
    

    
This command can be used to create a selection context for the hypergraph editor.

    """
    pass
    


def graphTrackCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    graphTrackCtx is undoable, queryable, and editable.
    

    
This command can be used to create a track context for the graph editor.

    """
    pass
    


def gravity( objects , attenuation=float, directionX=float, directionY=float, directionZ=float, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear):
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
    


def grid(default=boolean, displayAxes=boolean, displayAxesBold=boolean, displayDivisionLines=boolean, displayGridLines=boolean, displayOrthographicLabels=boolean, displayPerspectiveLabels=boolean, divisions=uint, orthographicLabelPosition=string, perspectiveLabelPosition=string, reset=boolean, size=linear, spacing=linear, style=uint, toggle=boolean):
    """
    grid is undoable, queryable, and NOT editable.
    

    
This command changes the size and spacing of lines on the ground plane displayed in the perspective and orthographic views.
This command lets you reset the ground plane, change its size and grid line spacing, grid subdivisions and display options.

    """
    pass
    


def gridLayout( string , allowEmptyCells=boolean, annotation=string, autoGrow=boolean, backgroundColor=float, float, float, cellHeight=int, cellWidth=int, cellWidthHeight=int, int, childArray=boolean, columnsResizable=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, gridOrder=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfColumns=int, numberOfPopupMenus=boolean, numberOfRows=int, numberOfRowsColumns=int, int, parent=string, popupMenuArray=boolean, position=string, int, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    gridLayout is undoable, queryable, and editable.
    

    
This layout arranges children in a grid fashion where every cell in the grid is the same size. You may specify the number of rows and columns as well as the width and height of the grid cells.

    """
    pass
    


def group( objects... , absolute=boolean, empty=boolean, name=string, parent=string, relative=boolean, useAsGroup=string, world=boolean):
    """
    group is undoable, NOT queryable, and NOT editable.
    

    
This command groups the specified objects under a new group and returns the name of the new group.
If the -em flag is specified, then an empty group (with no objects) is created.
If the -w flag is specified then the new group is placed under the world, otherwise if -p is specified it is placed under the specified node. If neither -w or -p is specified the new group is placed under the lowest common group they have in common. (or the world if no such group exists)
If an object is grouped with another object that has the same name then one of the objects will be renamed by this command.

    """
    pass
    


def hardenPointCurve( curve , caching=boolean, constructionHistory=boolean, multiplicity=int, name=string, nodeState=int, object=boolean, replaceOriginal=boolean):
    """
    hardenPointCurve is undoable, queryable, and editable.
    

    
The hardenPointCurve command changes the knots of a curve given a list of control point indices so that the knot corresponding to that control point gets the specified multiplicity. Multiplicity of -1 is the universal value used for multiplicity equal to the degree of the curve.
limitations
The CV whose multiplicity is being raised needs to have its neighbouring CVs of multiplicity 1. How many neighbours depends on the degree of the curve and the difference in CV multiplicities before and after this operation. For example, if you're changing a CV of multiplicity 1 into a CV of multiplicity 3, you will need the 4 neighbouring CVs (2 on each side) to be of multiplicity 1. The CVs that do not satisfy that requirement will be ignored.

    """
    pass
    


def hardware(brdType=boolean, cpuType=boolean, graphicsType=boolean, megaHertz=boolean, numProcessors=boolean):
    """
    hardware is undoable, NOT queryable, and NOT editable.
    

    
Return description of the hardware available in the machine.

    """
    pass
    


def hardwareRenderPanel( panelName , camera=string, control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, glRenderEditor=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    hardwareRenderPanel is undoable, queryable, and editable.
    

    
This command creates, edit and queries hardware render panels which contain only a hardware render editor.

    """
    pass
    


def hasMetadata(asList=boolean, channelName=string, channelType=string, endIndex=string, ignoreDefault=boolean, index=string, indexType=string, memberName=string, scene=boolean, startIndex=string, streamName=string):
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
    


def headsUpDisplay(string, allDescendants=boolean, allowOverlap=boolean, attachToRefresh=boolean, attributeChange=string, block=int, blockAlignment=string, blockSize=string, command=script, conditionChange=string, conditionFalse=string, conditionTrue=string, connectionChange=string, dataAlignment=string, dataFontSize=string, dataWidth=int, decimalPrecision=int, disregardIndex=boolean, event=string, exists=boolean, getOption=string, gridColor=int, label=string, labelFontSize=string, labelWidth=int, lastOccupiedBlock=int, layoutVisibility=boolean, listConditions=boolean, listEvents=boolean, listHeadsUpDisplays=boolean, listNodeChanges=boolean, listPresets=boolean, name=string, nextFreeBlock=int, nodeChanges=string, padding=int, preset=string, refresh=boolean, remove=boolean, removeID=int, removePosition=int, int, resetNodeChanges=string, scriptResult=boolean, section=int, setOption=string, string, showGrid=boolean, visible=boolean):
    """
    headsUpDisplay is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) object which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on information designated by a user script. The text string displayed on the viewport is formatted using the various flags of this command.
The only mandatory flags, on creation are the section and block flags. Note if the preset OR command/trigger flags are not present, only a label will be drawn on the viewport.
Upon creation of a HUD object, an ID number will be assigned to it. This can be used to remove the HUD object (-rid/removeID [int IDNumber]), if desired. Alternatively, HUD objects may be removed via their position (section and block), or their unique name.

    """
    pass
    


def headsUpMessage( message string , horizontalOffset=int, object=string, selection=boolean, time=float, verticalOffset=int):
    """
    headsUpMessage is undoable, NOT queryable, and NOT editable.
    

    
This command draws a message in the 3d view. The message is automatically erased at the next screen refresh.

    """
    pass
    


def help( string , documentation=boolean, language=string, list=boolean, popupDisplayTime=uint, popupMode=boolean, popupPauseTime=uint, popupSimpleMode=boolean, rolloverMode=boolean, syntaxOnly=boolean):
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
(ab)(CD)\2\1 matches abCDCDab (\1 to \9 available)

    """
    pass
    


def helpLine( name , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    helpLine is undoable, queryable, and editable.
    

    
This command creates a help line where tool help/hints are shown.

    """
    pass
    


def hide( objects , allObjects=boolean, clearSelection=boolean, invertComponents=boolean, returnHidden=boolean, testVisibility=boolean):
    """
    hide is undoable, NOT queryable, and NOT editable.
    

    
The hide command is used to make objects invisible. If no flags are used, the objects specified, or the active objects if none are specified, will be made invisible.

    """
    pass
    


def hikGlobals(releaseAllPinning=boolean):
    """
    hikGlobals is undoable, queryable, and editable.
    

    
Sets global HumanIK flags for the application.

    """
    pass
    


def hilite( objects , replace=boolean, toggle=boolean, unHilite=boolean):
    """
    hilite is undoable, NOT queryable, and NOT editable.
    

    
Hilites/Unhilites the specified object(s). Hiliting an object makes it possible to select the components of the object. If no objects are specified then the selection list is used.

    """
    pass
    


def hitTest(stringintint):
    """
    hitTest is NOT undoable, NOT queryable, and NOT editable.
    

    
The hitTest command hit-tests a point in the named control and returns a list of items underneath the point. The point is specified in pixels with the origin (0,0) at the top-left corner. This position is compatible with the coordinates provided by a drop-callback. The types of items that may be returned depends upon the specific control; not all controls currently support hit-testing.

    """
    pass
    


def hotBox(PaneOnlyMenus=boolean, PaneToggleMenus=boolean, animationOnlyMenus=boolean, animationToggleMenus=boolean, clothOnlyMenus=boolean, clothToggleMenus=boolean, commonOnlyMenus=boolean, commonToggleMenus=boolean, customMenuSetsToggleMenus=boolean, displayCenterOnly=boolean, displayHotbox=boolean, displayStyle=boolean, displayZonesOnly=boolean, dynamicsOnlyMenus=boolean, dynamicsToggleMenus=boolean, liveOnlyMenus=boolean, liveToggleMenus=boolean, modelingOnlyMenus=boolean, modelingToggleMenus=boolean, noClickCommand=script, noClickDelay=float, noClickPosition=boolean, noKeyPress=boolean, polygonsOnlyMenus=boolean, polygonsToggleMenus=boolean, position=uint, uint, release=boolean, renderingOnlyMenus=boolean, renderingToggleMenus=boolean, riggingOnlyMenus=boolean, riggingToggleMenus=boolean, rmbPopups=boolean, showAllToggleMenus=boolean, surfacesOnlyMenus=boolean, surfacesToggleMenus=boolean, transparenyLevel=int, updateMenus=boolean):
    """
    hotBox is undoable, queryable, and NOT editable.
    

    
This command controls parameters related to the hotBox menubar palette. When the command is invoked with no flags, the hotBox is popped up.

    """
    pass
    


def hotkey(altModifier=boolean, autoSave=boolean, commandModifier=boolean, ctrlModifier=boolean, ctxClient=string, dragPress=boolean, factorySettings=boolean, isModifier=boolean, keyShortcut=string, name=string, pressCommandRepeat=boolean, releaseCommandRepeat=boolean, releaseName=string, shiftModifier=boolean, sourceUserHotkeys=boolean):
    """
    hotkey is undoable, queryable, and NOT editable.
    

    
This command sets the single-key hotkeys for the entire application.

    """
    pass
    


def hotkeyCheck(altModifier=boolean, commandModifier=boolean, ctrlModifier=boolean, keyString=string, keyUp=boolean, optionModifier=boolean):
    """
    hotkeyCheck is undoable, NOT queryable, and NOT editable.
    

    
This command checks if the given hotkey is mapped to a nameCommand object. If so, the annotation of the nameCommand object is returned. Otherwise an empty string is returned.

    """
    pass
    


def hotkeyCtx(addClient=string, clientArray=boolean, currentClient=string, insertTypeAt=string, string, removeAllClients=boolean, removeClient=string, removeType=string, type=string, typeArray=boolean, typeExists=string):
    """
    hotkeyCtx is undoable, queryable, and NOT editable.
    

    
This command sets the hotkey context for the entire application.

    """
    pass
    


def hotkeyEditorPanel( name , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    hotkeyEditorPanel is undoable, queryable, and editable.
    

    
A hotkeyEditor creates a new hotkey editor in the current layout. The hotkey editor lets you assign predefined commands, MEL scripts, or marking menus to keys and key combinations.

    """
    pass
    


def hotkeySet( name , current=boolean, delete=boolean, exists=boolean, export=string, hotkeySetArray=boolean, ip=string, rename=string, source=string):
    """
    hotkeySet is undoable, queryable, and editable.
    

    
Manages hotkey sets in Maya. A hotkey set holds hotkey to command mapping information. Default hotkey sets are hotkey sets that are shipped together with Maya. They are locked and cannot be altered.
A new hotkey set is always duplicated from an existing hotkey set. In create mode, users can choose to specify which hotkey set to duplicate by using the -source flag. A duplicated hotkey set is independent from the source hotkey set.

    """
    pass
    


def hudButton(string, allowOverlap=boolean, block=int, blockAlignment=string, blockSize=string, buttonShape=string, buttonWidth=int, label=string, labelFontSize=string, padding=int, pressCommand=script, releaseCommand=script, section=int, visible=boolean):
    """
    hudButton is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) button control which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on interaction designated by a user script. The HUD button is derived from a generic HUD object and thus inherits a similar workflow.
Although this command provides much of the same functionality as the headsUpDisplay command, it does not provide headsUpDisplay layout controls such as layoutVisibility, nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality, please use the headsUpDisplay command. This command is focused solely around the creation and management of HUD button controls. Similarly, all operations performed by this command are limited to HUDs that are button controls.
The only mandatory flags, on creation are the section and block flags.
Like the headsUpDisplay command, upon creation of a HUD button, an ID number will be assigned to it. This can be used to remove the HUD via the headsUpDisplay command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay command can remove HUD objects via their position (section and block), or their unique name.

    """
    pass
    


def hudSlider(string, allowOverlap=boolean, block=int, blockAlignment=string, blockSize=string, decimalPrecision=int, dragCommand=script, internalPadding=int, label=string, labelFontSize=string, labelWidth=int, maxValue=float, minValue=float, padding=int, pressCommand=script, releaseCommand=script, section=int, sliderIncrement=float, sliderLength=int, type=string, value=float, valueAlignment=string, valueFontSize=string, valueWidth=int, visible=boolean):
    """
    hudSlider is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) slider control which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on interaction designated by a user script. The HUD slider is derived from a generic HUD object and thus inherits a similar workflow.
Although this command provides much of the same functionality as the headsUpDisplay command, it does not provide headsUpDisplay layout controls such as layoutVisibility, nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality, please use the headsUpDisplay command. This command is focused solely around the creation and management of HUD sliders. Similarly, all operations performed by this command are limited to HUDs that are sliders.
The only mandatory flags, on creation are the section and block flags.
Like the headsUpDisplay command, upon creation of a HUD slider, an ID number will be assigned to it. This can be used to remove the HUD slider via the headsUpDisplay command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay command can remove HUD objects via their position (section and block), or their unique name.

    """
    pass
    


def hudSliderButton(string, allowOverlap=boolean, block=int, blockAlignment=string, blockSize=string, buttonLabel=string, buttonLabelFontSize=string, buttonPressCommand=script, buttonReleaseCommand=script, buttonShape=string, buttonWidth=int, decimalPrecision=int, internalPadding=int, maxValue=float, minValue=float, padding=int, section=int, sliderDragCommand=script, sliderIncrement=float, sliderLabel=string, sliderLabelFontSize=string, sliderLabelWidth=int, sliderLength=int, sliderPressCommand=script, sliderReleaseCommand=script, type=string, value=float, valueAlignment=string, valueFontSize=string, valueWidth=int, visible=boolean):
    """
    hudSliderButton is NOT undoable, queryable, and editable.
    

    
This command creates a Heads-up Display (HUD) slider button control which is placed in a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on interaction designated by a user script. The HUD slider button control is derived from a generic HUD object and thus inherits a similar workflow.
Although this command provides much of the same functionality as the headsUpDisplay command, it does not provide headsUpDisplay layout controls such as layoutVisibility, nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality, please use the headsUpDisplay command. This command is focused solely around the creation and management of HUD slider button controls. Similarly, all operations performed by this command are limited to HUDs that are slider button controls.
The only mandatory flags, on creation are the section and block flags.
Like the headsUpDisplay command, upon creation of a HUD slider button, an ID number will be assigned to it. This can be used to remove the HUD slider via the headsUpDisplay command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay command can remove HUD objects via their position (section and block), or their unique name.

    """
    pass
    


def hwReflectionMap(backTextureName=string, bottomTextureName=string, cubeMap=boolean, decalMode=boolean, enable=boolean, frontTextureName=string, leftTextureName=string, rightTextureName=string, sphereMapTextureName=string, topTextureName=string):
    """
    hwReflectionMap is undoable, queryable, and editable.
    

    
This command creates a hwReflectionMap node for having reflection on textured surfaces that currently have their boolean attribute displayHWEnvironment set to true.

    """
    pass
    


def hwRender(acceleratedMultiSampleSupport=boolean, activeTextureCount=boolean, camera=string, currentFrame=boolean, currentView=boolean, edgeAntiAliasing=uint, uint, fixFileNameNumberPattern=boolean, frame=float, fullRenderSupport=boolean, height=uint, imageFileName=boolean, layer=name, limitedRenderSupport=boolean, lowQualityLighting=boolean, noRenderView=boolean, notWriteToFile=boolean, printGeometry=boolean, renderHardwareName=boolean, renderRegion=uint, uint, uint, uint, renderSelected=boolean, textureResolution=uint, width=uint, writeAlpha=boolean, writeDepth=boolean):
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
    


def hyperGraph( string , addBookmark=boolean, addDependGraph=name, addDependNode=name, animateTransition=boolean, attributeEditor=string, bookmarkName=boolean, clear=boolean, collapseContainer=boolean, connectionDrawStyle=string, control=boolean, defineTemplate=string, deleteBookmark=string, dependGraph=boolean, dependNode=string, docTag=string, down=boolean, downstream=boolean, dragAndDropBehaviorCommand=string, dropNode=string, dropTargetNode=string, edgeDblClickCommand=string, edgeDimmedDblClickCommand=string, enableAutomaticLayout=boolean, exists=boolean, expandContainer=boolean, feedbackGadget=string, feedbackNode=string, filter=string, filterDetail=string, boolean, fitImageToHeight=boolean, fitImageToWidth=boolean, focusCommand=string, fold=boolean, forceMainConnection=string, forceRefresh=boolean, frame=boolean, frameBranch=boolean, frameGraph=boolean, frameHierarchy=boolean, freeform=boolean, fromAttr=string, getNodeList=boolean, getNodePosition=string, graphLayoutStyle=string, graphType=string, highlightConnection=string, iconSize=string, image=string, imageEnabled=boolean, imageForContainer=boolean, imagePosition=float, float, imageScale=float, isHotkeyTarget=boolean, layout=boolean, layoutSelected=string, lockMainConnection=boolean, look=float, float, mainListConnection=string, mergeConnections=boolean, navigateHome=boolean, nextView=boolean, nodeDropCommand=string, nodePressCommand=string, nodeReleaseCommand=string, opaqueContainers=boolean, orientation=string, panel=string, parent=string, popupMenuScript=string, previousView=boolean, range=float, float, rebuild=boolean, removeNode=string, rename=boolean, resetFreeform=boolean, restoreBookmark=string, scrollUpDownNoZoom=boolean, selectionConnection=string, setNodePosition=string, float, float, showConnectionFromSelected=boolean, showConnectionToSelected=boolean, showConstraints=boolean, showDeformers=boolean, showExpressions=boolean, showInvisible=boolean, showRelationships=boolean, showShapes=boolean, showUnderworld=boolean, stateString=boolean, transitionFrames=int, unParent=boolean, unfold=boolean, unfoldAll=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, updateNodeAdded=boolean, updateSelection=boolean, upstream=boolean, useFeedbackList=boolean, useTemplate=string, viewOption=string, visibility=boolean, zoom=float):
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
    


def hyperPanel( panelName , control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, hyperEditor=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    hyperPanel is undoable, queryable, and editable.
    

    
This command creates, edit and queries hypergraph panels which contain only a hypergraph editor.

    """
    pass
    


def hyperShade(assign=string, clearWorkArea=boolean, collapse=string, createNode=string, dependGraphArea=boolean, downStream=boolean, duplicate=boolean, fixRenderSize=boolean, incremental=boolean, listDownstreamNodes=name, listDownstreamShaderNodes=name, listUpstreamNodes=name, name=string, networks=boolean, noSGShapes=boolean, noShapes=boolean, noTransforms=boolean, objects=string, renderCreateAndDrop=string, reset=boolean, resetGraph=boolean, resetSwatch=boolean, setAllowsRegraphing=boolean, setWorkArea=string, shaderNetwork=string, shaderNetworks=boolean, shaderNetworksSelectMaterialNodes=boolean, snapShot=boolean, uncollapse=string, upStream=boolean, userDefinedLayout=boolean, workAreaAddCmd=string, workAreaDeleteCmd=string, workAreaSelectCmd=string):
    """
    hyperShade is undoable, NOT queryable, and NOT editable.
    

    
Commands for shader editing in the hypergraph

    """
    pass
    


def iconTextButton( string , align=string, annotation=string, backgroundColor=float, float, float, command=script, commandRepeatable=boolean, defineTemplate=string, disabledImage=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, flat=boolean, flipX=boolean, flipY=boolean, font=string, fullPathName=boolean, handleNodeDropCallback=script, height=int, highlightColor=float, float, float, highlightImage=string, image=string, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, label=string, labelEditingCallback=script, labelOffset=int, ltVersion=string, manage=boolean, marginHeight=uint, marginWidth=uint, menuItem=string, string, noBackground=boolean, numberOfPopupMenus=boolean, overlayLabelBackColor=float, float, float, float, overlayLabelColor=float, float, float, parent=string, popupMenuArray=boolean, preventOverride=boolean, rotation=float, scaleIcon=boolean, selectionImage=string, sourceType=string, style=string, useAlpha=boolean, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    iconTextButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextButton that can be displayed with different icons, with or without accompanying text label. When an argument is passed, it is used to give a name to the iconTextButton.

    """
    pass
    


def iconTextCheckBox( string , align=string, annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, disabledImage=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, flat=boolean, flipX=boolean, flipY=boolean, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, highlightImage=string, image=string, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, label=string, labelOffset=int, ltVersion=string, manage=boolean, marginHeight=uint, marginWidth=uint, noBackground=boolean, numberOfPopupMenus=boolean, offCommand=script, onCommand=script, overlayLabelBackColor=float, float, float, float, overlayLabelColor=float, float, float, parent=string, popupMenuArray=boolean, preventOverride=boolean, rotation=float, selectionHighlightImage=string, selectionImage=string, style=string, useAlpha=boolean, useTemplate=string, value=boolean, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    iconTextCheckBox is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextCheckBox.

    """
    pass
    


def iconTextRadioButton( string , align=string, annotation=string, backgroundColor=float, float, float, changeCommand=script, collection=string, defineTemplate=string, disabledImage=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, flat=boolean, flipX=boolean, flipY=boolean, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, highlightImage=string, image=string, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, label=string, labelOffset=int, ltVersion=string, manage=boolean, marginHeight=uint, marginWidth=uint, noBackground=boolean, numberOfPopupMenus=boolean, offCommand=script, onCommand=script, overlayLabelBackColor=float, float, float, float, overlayLabelColor=float, float, float, parent=string, popupMenuArray=boolean, preventOverride=boolean, rotation=float, select=boolean, selectionHighlightImage=string, selectionImage=string, style=string, useAlpha=boolean, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    iconTextRadioButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates a iconTextRadioButton that is added to the most recently created iconTextRadioCollection unless the -cl/cluster flag is used.

    """
    pass
    


def iconTextRadioCollection( string , collectionItemArray=boolean, disableCommands=boolean, gl=boolean, numberOfCollectionItems=boolean, parent=string, select=string):
    """
    iconTextRadioCollection is undoable, queryable, and editable.
    

    
This command creates a cluster for iconTextRadioButtons. Clusters will be parented to the current default layout if no parent is specified with the -p/parent flag. As children of the layout they will be deleted when the layout is deleted. Clusters may also span more than one window if the -g/global flag is used. In this case the cluster has no parent so must be explicitly deleted with the 'deleteUI' command.

    """
    pass
    


def iconTextScrollList( string , allowMultiSelection=boolean, annotation=string, append=string, backgroundColor=float, float, float, defineTemplate=string, deselectAll=boolean, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, dropRectCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, itemAt=int, int, itemTextColor=int, float, float, float, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, numberOfRows=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, removeAll=boolean, selectCommand=script, selectIndexedItem=int, selectItem=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, visualRectAt=int, int, width=int):
    """
    iconTextScrollList is undoable, queryable, and editable.
    

    
This command creates/edits/queries a text scrolling list. The list can be in single select mode where only one item at at time is selected, or in multi-select mode where many items may be selected.

    """
    pass
    


def iconTextStaticLabel( string , align=string, annotation=string, backgroundColor=float, float, float, defineTemplate=string, disabledImage=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, flipX=boolean, flipY=boolean, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, label=string, labelOffset=int, ltVersion=string, manage=boolean, marginHeight=uint, marginWidth=uint, noBackground=boolean, numberOfPopupMenus=boolean, overlayLabelBackColor=float, float, float, float, overlayLabelColor=float, float, float, parent=string, popupMenuArray=boolean, preventOverride=boolean, rotation=float, style=string, useAlpha=boolean, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    iconTextStaticLabel is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextStaticLabel.

    """
    pass
    


def ikfkDisplayMethod(display=string):
    """
    ikfkDisplayMethod is NOT undoable, queryable, and NOT editable.
    

    
The ikfkDisplayMethod command is used to specify how ik/fk blending should be shown

    """
    pass
    


def ikHandle( object , autoPriority=boolean, connectEffector=boolean, createCurve=boolean, createRootAxis=boolean, curve=name, disableHandles=boolean, enableHandles=boolean, endEffector=string, exists=string, forceSolver=boolean, freezeJoints=boolean, jointList=boolean, name=string, numSpans=int, parentCurve=boolean, positionWeight=float, priority=int, rootOnCurve=boolean, rootTwistMode=boolean, setupForRPsolver=boolean, simplifyCurve=boolean, snapCurve=boolean, snapHandleFlagToggle=boolean, snapHandleToEffector=boolean, solver=string, startJoint=string, sticky=string, twistType=string, weight=float):
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
    


def ikHandleCtx( object , autoPriorityH=boolean, createCurve=boolean, createRootAxis=boolean, exists=boolean, forceSolverH=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, numSpans=int, parentCurve=boolean, poWeightH=float, priorityH=int, rootOnCurve=boolean, rootTwistMode=boolean, simplifyCurve=boolean, snapCurve=boolean, snapHandleH=boolean, solverTypeH=string, stickyH=string, twistType=string, weightH=float):
    """
    ikHandleCtx is undoable, queryable, and editable.
    

    
The ikHandle context command (ikHandleCtx) updates parameters of ikHandle tool. The options for the tool will be set to the flags that the user specifies.

    """
    pass
    


def ikHandleDisplayScale( float ):
    """
    ikHandleDisplayScale is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current display size of ikHandle. The default display scale is 1.0.

    """
    pass
    


def ikSolver( object , epsilon=float, maxIterations=int, name=string, solverType=string):
    """
    ikSolver is undoable, queryable, and editable.
    

    
The ikSolver command is used to set the attributes for an IK Solver or create a new one. The standard edit (-e) and query (-q) flags are used for edit and query functions.

    """
    pass
    


def ikSplineHandleCtx( object , autoPriorityH=boolean, createCurve=boolean, createRootAxis=boolean, exists=boolean, forceSolverH=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, numSpans=int, parentCurve=boolean, poWeightH=float, priorityH=int, rootOnCurve=boolean, rootTwistMode=boolean, simplifyCurve=boolean, snapCurve=boolean, snapHandleH=boolean, solverTypeH=string, stickyH=string, twistType=string, weightH=float):
    """
    ikSplineHandleCtx is undoable, queryable, and editable.
    

    
The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of ikSplineHandle tool. The options for the tool will be set to the flags the user specifies.

    """
    pass
    


def ikSystem( object , allowRotation=boolean, autoPriority=boolean, autoPriorityMC=boolean, autoPrioritySC=boolean, list=int, int, snap=boolean, solve=boolean, solverTypes=boolean):
    """
    ikSystem is undoable, queryable, and editable.
    

    
The ikSystem command is used to set the global snapping flag for handles and set the global solve flag for solvers. The standard edit (-e) and query (-q) flags are used for edit and query functions.

    """
    pass
    


def ikSystemInfo( boolean , globalSnapHandle=boolean):
    """
    ikSystemInfo is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current ikSystem controls.

    """
    pass
    


def illustratorCurves( string , constructionHistory=boolean, illustratorFilename=string, name=string, object=boolean, scaleFactor=float):
    """
    illustratorCurves is undoable, queryable, and editable.
    

    
The illustratorCurves command creates NURBS curves from an input Adobe(R) Illustrator(R) file.

    """
    pass
    


def image( imageName , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    image is undoable, queryable, and editable.
    

    
This command creates a static image for non-xpm files. Any image file format supported by the file texture node is supported by this command.

    """
    pass
    


def imagePlane(camera=string, counter=boolean, detach=boolean, dropFrame=boolean, fileName=string, frameDuration=int, height=float, imageSize=int, int, lookThrough=string, maintainRatio=boolean, name=string, negTimesOK=boolean, numFrames=int, quickTime=boolean, showInAllViews=boolean, timeCode=int, timeCodeTrack=boolean, timeScale=int, twentyFourHourMax=boolean, width=float):
    """
    imagePlane is undoable, queryable, and editable.
    

    
The imagePlane command allows querying of various properties of an image plane and any movie in use by the image plane. It also supports creating and edit. The object passed to the command may either be an imagePlane node, or a camera, in which case the command uses the image plane attached to the camera (if any). If no object is passed in, the current selection is used. Currently, most movie related queries work only on 64 bit Windows systems.

    """
    pass
    


def imfPlugins(string, extension=string, keyword=string, multiFrameSupport=string, pluginName=string, readSupport=string, writeSupport=string):
    """
    imfPlugins is NOT undoable, queryable, and NOT editable.
    

    
This command queries all the available imf plugins for its name, keyword or image file extension. Only one of the attributes (name, keyword or extension) can be queried at a time. If no flags are specified, this command returns a list of all available plugin names.

    """
    pass
    


def inheritTransform( objects... , preserve=boolean, toggle=boolean):
    """
    inheritTransform is undoable, queryable, and NOT editable.
    

    
This command toggles the inherit state of an object. If this flag is off the object will not inherit transformations from its parent. In other words transformations applied to the parent node will not affect the object and it will act as though it is under the world.
If the -p flag is specified then the object's transformation will be modified to compensate when changing the inherit flag so the object will not change its world-space location.

    """
    pass
    


def insertJoint( object ):
    """
    insertJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will insert a new joint under the given or selected joint. If the given joint has child joints, they will be reparented under the new inserted joint.
The given joint(or selected joint) should not have skin attached. The command works on the selected joint. No options or flags are necessary.

    """
    pass
    


def insertJointCtx(exists=boolean, image1=string, image2=string, image3=string):
    """
    insertJointCtx is undoable, queryable, and editable.
    

    
The command will create an insert joint context. The insert joint tool inserts joints into an existing chain of joints.

    """
    pass
    


def insertKeyCtx( contextName , breakdown=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    insertKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to insert keys within the graph editor

    """
    pass
    


def insertKnotCurve( curve , addKnots=boolean, caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, insertBetween=boolean, name=string, nodeState=int, numberOfKnots=int, object=boolean, parameter=float, replaceOriginal=boolean):
    """
    insertKnotCurve is undoable, queryable, and editable.
    

    
The insertKnotCurve command inserts knots into a curve given a list of parameter values. The number of knots to add at each parameter value and whether the knots are added or complemented can be specified. The name of the curve is returned. If construction history is on, the name of the resulting dependency node is also returned.
An edit point will appear where you insert the knot. Also, the number of spans and CVs in the curve will increase in the area where the knot is inserted.
You can insert up to "degree" knots at a curve parameter that isn't already an edit point. eg. for a degree three curve, you can insert up to 3 knots.
Use this operation if you need more CVs in a local area of the curve. Use this operation (or "hardenPoint") if you want to create a corner in a curve.

    """
    pass
    


def insertKnotSurface( surface , addKnots=boolean, caching=boolean, constructionHistory=boolean, direction=int, insertBetween=boolean, name=string, nodeState=int, numberOfKnots=int, object=boolean, parameter=float, replaceOriginal=boolean):
    """
    insertKnotSurface is undoable, queryable, and editable.
    

    
The insertKnotSurface command inserts knots (aka isoparms) into a surface given a list of parameter values. The number of knots to add at each parameter value and whether the knots are added or complemented can be specified. The name of the surface is returned and if history is on, the name of the resulting dependency node is also returned.
You must specify one, none or all number of knots with the "-nk" flag. eg. if you specify none, then the default (one) knot will be added at each specified parameter value. If you specify one "-nk" value then that number of knots will be added at each parameter value. Otherwise, you must specify the same number of "-nk" flags as "-p" flags, defining the number of knots to be added at each specified parameter value.
You can insert up to "degree" knots at a parameter value that isn't already an isoparm. eg. for a degree 3 surface, you can insert up to 3 knots.
Use this operation if you need more CVs in a local area of the surface. Use this operation if you want to create a corner in the surface.
Note: A single insertKnotSurface command cannot insert in both directions at once; you must use two separate commands to do this.

    """
    pass
    


def instance( objects , leaf=boolean, name=string, smartTransform=boolean):
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
    


def instanceable(allow=boolean, recursive=boolean, shape=boolean):
    """
    instanceable is undoable, queryable, and NOT editable.
    

    
Flags one or more DAG nodes so that they can (or cannot) be instanced. This command sets an internal state on the specified DAG nodes which is checked whenever Maya attempts an instancing operation. If no node names are provided on the command line then the current selection list is used.
Sets are automatically expanded to their constituent objects. Nodes which are already instanced (or have children which are already instanced) cannot be marked as non-instancable.

    """
    pass
    


def instancer(addObject=boolean, cycle=string, cycleStep=float, cycleStepUnits=string, index=int, levelOfDetail=string, name=string, object=string, objectPosition=string, objectRotation=string, objectScale=string, pointDataSource=boolean, removeObject=boolean, rotationOrder=string, rotationUnits=string, valueName=string):
    """
    instancer is undoable, queryable, and editable.
    

    
This command is used to create a instancer node and set the proper attributes in the node.

    """
    pass
    


def internalVar(userAppDir=boolean, userBitmapsDir=boolean, userHotkeyDir=boolean, userMarkingMenuDir=boolean, userPrefDir=boolean, userPresetsDir=boolean, userScriptDir=boolean, userShelfDir=boolean, userTmpDir=boolean, userWorkspaceDir=boolean):
    """
    internalVar is undoable, NOT queryable, and NOT editable.
    

    
This command returns the values of internal variables. No modification of these variables is supported.

    """
    pass
    


def intersect( surface surface , caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, firstSurface=boolean, name=string, nodeState=int, object=boolean, tolerance=linear):
    """
    intersect is undoable, queryable, and editable.
    

    
The intersect command creates a curve on surface where all surfaces intersect with each other. By default, the curve on surface is created for both surfaces. However, by using the -fs flag, only the first surface will have a curve on surface. Also, the intersection curve can be created as a 3D curve rather than a curve on surface.

    """
    pass
    


def intField( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, enterCommand=script, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, maxValue=int, minValue=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, receiveFocusCommand=script, step=int, useTemplate=string, value=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    intField is undoable, queryable, and editable.
    

    
Create a field control that accepts only integer values and is bound by a minimum and maximum value. An invisible slider is attached to the field and accessed by holding down the Ctrl modifier key while pressing one of the mouse buttons. Dragging the invisible slider to the right with the middle mouse button increases the field value by the amount specified with the -s/step flag, while dragging to the left decreases the value by the same amount. The left and right mouse buttons apply a factor of 0.1 and 10 to the step value.

    """
    pass
    


def intFieldGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enable1=boolean, enable2=boolean, enable3=boolean, enable4=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfFields=int, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, useTemplate=string, value=int, int, int, int, value1=int, value2=int, value3=int, value4=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    intFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text and editable integer fields. The label text is optional and one to four fields can be created.

    """
    pass
    


def intScrollBar( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontal=boolean, isObscured=boolean, largeStep=int, manage=boolean, maxValue=int, minValue=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, step=int, useTemplate=string, value=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    intScrollBar is undoable, queryable, and editable.
    

    
Create a scroll bar control that accepts only integer values and is bound by a minimum and maximum value. The scroll bar displays a marker indicating the current value of the scroll bar relative to it's minimum and maximum values. Click and drag the marker or on the scroll bar itself to change the current value.

    """
    pass
    


def intSlider( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontal=boolean, isObscured=boolean, manage=boolean, maxValue=int, minValue=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, step=int, useTemplate=string, value=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    intSlider is undoable, queryable, and editable.
    

    
Create a slider control that accepts only integer values and is bound by a minimum and maximum value. The slider displays a marker indicating the current value of the slider relative to it's minimum and maximum values. Click and drag the marker or on the slider itself to change the current value.

    """
    pass
    


def intSliderGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dragCommand=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, field=boolean, fieldMaxValue=int, fieldMinValue=int, fieldStep=int, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, maxValue=int, minValue=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, sliderStep=int, step=int, useTemplate=string, value=int, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def inViewEditor(visible=boolean):
    """
    inViewEditor is NOT undoable, queryable, and NOT editable.
    

    
Mel access to the In-View Editor. In-View Editors display a customizable subset of a node's attributes, letting you adjust attributes directly in a scene instead of opening the Channel Box or Attribute Editor.

    """
    pass
    


def inViewMessage(alpha=float, assistMessage=string, backColor=uint, clear=string, dragKill=boolean, fade=boolean, fadeInTime=uint, fadeOutTime=uint, fadeStayTime=uint, font=string, fontSize=uint, frameOffset=uint, hide=boolean, message=string, minimize=boolean, position=string, restore=boolean, show=boolean, statusMessage=string, textAlpha=float, textOffset=uint, uvEditor=boolean):
    """
    inViewMessage is undoable, NOT queryable, and NOT editable.
    

    
Used for displaying in-view messages.
Note: On Linux, the alpha and textAlpha flags for inViewMessage are only supported when running a window manager that supports compositing (transparency and opacity). Otherwise, they are ignored. In addition, the flags for message fading: -fade, -fadeInTime, -fadeStay and -fadeOutTime are supported, but the message will display without a fade effect if the window manager doesn't support compositing.

    """
    pass
    


def iprEngine(copy=string, defineTemplate=string, estimatedMemory=boolean, exists=boolean, iprImage=string, motionVectorFile=boolean, object=name, region=int, int, int, int, relatedFiles=boolean, releaseIprImage=boolean, resolution=boolean, scanlineIncrement=string, showProgressBar=boolean, startTuning=boolean, stopTuning=boolean, underPixel=int, int, update=boolean, updateDepthOfField=boolean, updateLightGlow=boolean, updateMotionBlur=boolean, updatePort=string, updateShaderGlow=boolean, updateShading=boolean, updateShadowMaps=boolean, useTemplate=string):
    """
    iprEngine is undoable, queryable, and editable.
    

    
Command to create or edit an iprEngine. A iprEngine is an object that watches for changes to shading networks and automatically reshades to generate an up-to-date image.

    """
    pass
    


def isConnected( string string , ignoreUnitConversion=boolean):
    """
    isConnected is undoable, NOT queryable, and NOT editable.
    

    
The isConnected command is used to check if two plugs are connected in the dependency graph. The return value is false if they are not and true if they are.

The first string specifies the source plug to check for connection.
The second one specifies the destination plug to check for connection.

    """
    pass
    


def isDirty( string... , connection=boolean, datablock=boolean):
    """
    isDirty is undoable, NOT queryable, and NOT editable.
    

    
The isDirty command is used to check if a plug is dirty. The return value is 0 if it is not and 1 if it is. If more than one plug is specified then the result is the logical "or" of all objects (ie. returns 1 if *any* of the plugs are dirty).

    """
    pass
    


def isolateSelect( string , addDagObject=name, addSelected=boolean, addSelectedObjects=boolean, loadSelected=boolean, removeDagObject=name, removeSelected=boolean, state=boolean, update=boolean, viewObjects=boolean):
    """
    isolateSelect is undoable, queryable, and NOT editable.
    

    
This command turns on/off isolate select mode in a specified modeling view, specified as the argument. Isolate select mode is a display mode where the currently selected objects are added to a list and only those objects are displayed in the view. It allows for selective viewing of specific objects and object components.

    """
    pass
    


def isTrue( string ):
    """
    isTrue is undoable, NOT queryable, and NOT editable.
    

    
This commmand returns the state of the named condition. If the condition is true, it returns 1. Otherwise it returns 0.

    """
    pass
    


def itemFilter( string , byBin=string, byName=string, byScript=string, byType=string, category=string, classification=string, clearByBin=boolean, clearByType=boolean, difference=string, string, exists=boolean, intersect=string, string, listBuiltInFilters=boolean, listOtherFilters=boolean, listUserFilters=boolean, negate=boolean, parent=string, pythonModule=string, secondScript=string, text=string, union=string, string, uniqueNodeNames=boolean):
    """
    itemFilter is undoable, queryable, and editable.
    

    
This command creates a named itemFilter object. This object can be attached to selectionConnection objects, or to editors, in order to filter the item lists going through them. Using union, intersection and difference filters, complex composite filters can be created.

    """
    pass
    


def itemFilterAttr( string , byName=string, byNameString=string, byScript=string, classification=string, hasCurve=boolean, hasDrivenKey=boolean, hasExpression=boolean, hidden=boolean, intersect=string, string, keyable=boolean, listBuiltInFilters=boolean, listOtherFilters=boolean, listUserFilters=boolean, negate=boolean, parent=string, published=boolean, readable=boolean, scaleRotateTranslate=boolean, secondScript=string, text=string, union=string, string, writable=boolean):
    """
    itemFilterAttr is undoable, queryable, and editable.
    

    
This command creates a named itemFilterAttr object. This object can be attached to editors, in order to filter the attributes going through them. Using union and intersection filters, complex composite filters can be created.

    """
    pass
    


def itemFilterType( string , text=string, type=boolean):
    """
    itemFilterType is undoable, queryable, and editable.
    

    
This command queries a named itemFilter object. This object can be attached to selectionConnection objects, or to editors, in order to filter the item lists going through them. Using union and intersection filters, complex composite filters can be created.

    """
    pass
    


def joint( objects , absolute=boolean, angleX=angle, angleY=angle, angleZ=angle, assumePreferredAngles=boolean, automaticLimits=boolean, children=boolean, component=boolean, degreeOfFreedom=string, exists=string, limitSwitchX=boolean, limitSwitchY=boolean, limitSwitchZ=boolean, limitX=angle, angle, limitY=angle, angle, limitZ=angle, angle, name=string, orientJoint=string, orientation=angle, angle, angle, position=linear, linear, linear, radius=float, relative=boolean, rotationOrder=string, scale=float, float, float, scaleCompensate=boolean, scaleOrientation=angle, angle, angle, secondaryAxisOrient=string, setPreferredAngles=boolean, stiffnessX=float, stiffnessY=float, stiffnessZ=float, symmetry=boolean, symmetryAxis=string, zeroScaleOrient=boolean):
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
    


def jointCluster( string , aboveBound=float, aboveCluster=boolean, aboveDropoffType=string, aboveValue=float, belowBound=float, belowCluster=boolean, belowDropoffType=string, belowValue=float, deformerTools=boolean, joint=string, name=string):
    """
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
    


def jointCtx( object , autoJointOrient=string, autoPriorityH=boolean, createIKHandle=boolean, degreeOfFreedomJ=string, exists=boolean, forceSolverH=boolean, image1=string, image2=string, image3=string, jointAutoLimits=boolean, jointOrientationJ=angle, angle, angle, largeBoneLength=float, largeBoneRadius=float, poWeightH=float, priorityH=int, scaleCompensateJ=boolean, scaleJ=float, float, float, scaleOrientationJ=angle, angle, angle, secondaryAxisOrient=string, smallBoneLength=float, smallBoneRadius=float, snapHandleH=boolean, solverTypeH=string, stickyH=string, symmetry=boolean, symmetryAxis=string, variableBoneSize=int, weightH=float):
    """
    jointCtx is undoable, queryable, and editable.
    

    
The joint context command (jointCtx) updates the parameters of the joint tool. The options for the tool will be set by the flags the user specifies.

    """
    pass
    


def jointDisplayScale( float , absolute=boolean, ikfk=boolean):
    """
    jointDisplayScale is undoable, queryable, and NOT editable.
    

    
This action modifies and queries the current display size of skelton joints. The joint display size is controlled by a scale factor; scale factor 1 puts the display size to its default, which is 1 in diameter. With the plain format, the float argument is the factor with respect to the default size. When -a/absolute is used, the float argument refers to the actual diameter of the joint display size.

    """
    pass
    


def jointLattice( selectionList , after=boolean, afterReference=boolean, before=boolean, creasing=float, deformerTools=boolean, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, joint=string, lengthIn=float, lengthOut=float, lowerBindSkin=string, lowerTransform=string, name=string, parallel=boolean, prune=boolean, remove=boolean, rounding=float, split=boolean, upperBindSkin=string, upperTransform=string, widthLeft=float, widthRight=float):
    """
    jointLattice is undoable, queryable, and editable.
    

    
This command creates/edits/queries a jointLattice deformer. The name of the created/edited object is returned. Usually you would make use of this functionality through the higher level flexor command.

    """
    pass
    


def keyframe( objects , absolute=boolean, adjustBreakdown=boolean, animation=string, attribute=string, breakdown=boolean, clipTime=time, time, float, controlPoints=boolean, eval=boolean, float=floatrange, floatChange=float, hierarchy=string, includeUpperBound=boolean, index=uint, indexValue=boolean, keyframeCount=boolean, lastSelected=boolean, name=boolean, option=string, relative=boolean, selected=boolean, shape=boolean, tickDrawSpecial=boolean, time=timerange, timeChange=time, valueChange=float):
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
    


def keyframeOutliner( string , animCurve=string, annotation=string, backgroundColor=float, float, float, defineTemplate=string, display=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    keyframeOutliner is undoable, queryable, and editable.
    

    
This command creates/edits/queries a keyframe outliner control.

    """
    pass
    


def keyframeRegionCurrentTimeCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    keyframeRegionCurrentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the keyframe region of the dope sheet editor.

    """
    pass
    


def keyframeRegionDirectKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, option=string):
    """
    keyframeRegionDirectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to directly manipulate keyframes within the dope sheet editor

    """
    pass
    


def keyframeRegionDollyCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    keyframeRegionDollyCtx is undoable, queryable, and editable.
    

    
This command can be used to create a dolly context for the dope sheet editor.

    """
    pass
    


def keyframeRegionInsertKeyCtx( contextName , breakdown=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    keyframeRegionInsertKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to insert keys within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionMoveKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, option=string):
    """
    keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to move keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionScaleKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, scaleSpecifiedKeys=boolean, type=string):
    """
    keyframeRegionScaleKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionSelectKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    keyframeRegionSelectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionSetKeyCtx( contextName , breakdown=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    keyframeRegionSetKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to set keys within the keyframe region of the dope sheet editor

    """
    pass
    


def keyframeRegionTrackCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    keyframeRegionTrackCtx is undoable, queryable, and editable.
    

    
This command can be used to create a track context for the dope sheet editor.

    """
    pass
    


def keyframeStats( string , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, animEditor=string, annotation=string, backgroundColor=float, float, float, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, precision=int, preventOverride=boolean, rowAttach=int, string, int, timeAnnotation=string, useTemplate=string, valueAnnotation=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    keyframeStats is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates, edits, queries a keyframe stats control.

    """
    pass
    


def keyingGroup( objects , activator=string, addElement=name, afterFilters=boolean, category=string, clear=name, color=int, copy=name, edges=boolean, editPoints=boolean, empty=boolean, excludeDynamic=boolean, excludeRotate=boolean, excludeScale=boolean, excludeTranslate=boolean, excludeVisibility=boolean, facets=boolean, flatten=name, forceElement=name, include=name, intersection=name, isIntersecting=name, isMember=name, layer=boolean, minimizeRotation=boolean, name=string, noSurfaceShader=boolean, noWarnings=boolean, nodesOnly=boolean, remove=name, removeActivator=string, renderable=boolean, setActiveFilter=string, size=boolean, split=name, subtract=name, text=string, union=name, vertices=boolean):
    """
    keyingGroup is undoable, queryable, and editable.
    

    
This command is used to manage the membership of a keying group. Keying groups allow users to effectively manage related keyframe data, allowing keys on attributes in the keying group to be set and edited as a single entity.

    """
    pass
    


def keyTangent( objects , absolute=boolean, animation=string, attribute=string, controlPoints=boolean, float=floatrange, g=boolean, hierarchy=string, inAngle=angle, inTangentType=string, inWeight=float, includeUpperBound=boolean, index=uint, ix=float, iy=float, lock=boolean, outAngle=angle, outTangentType=string, outWeight=float, ox=float, oy=float, pluginTangentTypes=string, relative=boolean, shape=boolean, stepAttributes=boolean, time=timerange, unify=boolean, weightLock=boolean, weightedTangents=boolean):
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
    


def lassoContext( string , drawClosed=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    lassoContext is undoable, queryable, and editable.
    

    
Creates a context to perform selection via a "lasso". Use for irregular selection regions, where the "marquee-style" select of the "selectContext" is inappropriate.

    """
    pass
    


def lattice( selectionList , after=boolean, afterReference=boolean, before=boolean, commonParent=boolean, deformerTools=boolean, divisions=uint, uint, uint, dualBase=boolean, exclusive=string, freezeMapping=boolean, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, latticeReset=boolean, ldivisions=uint, uint, uint, name=string, objectCentered=boolean, outsideFalloffDistance=float, outsideLattice=uint, parallel=boolean, position=linear, linear, linear, prune=boolean, remove=boolean, removeTweaks=boolean, rotation=angle, angle, angle, scale=linear, linear, linear, split=boolean):
    """
    lattice is undoable, queryable, and editable.
    

    
This command creates a lattice deformer that will deform the selected objects. If the object centered flag is used, the initial lattice will fit around the selected objects. The lattice will be selected when the command is completed. The lattice deformer has an associated base lattice. Only objects which are contained by the base lattice will be deformed by the lattice.

    """
    pass
    


def latticeDeformKeyCtx( contextName , envelope=float, exists=boolean, history=boolean, image1=string, image2=string, image3=string, latticeColumns=uint, latticeRows=uint, name=string, scaleLatticePts=boolean):
    """
    latticeDeformKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to deform key frames with lattice manipulator. This context only works in the graph editor.

    """
    pass
    


def launch(directory=string, movie=string, pdfFile=string, webPage=string):
    """
    launch is undoable, NOT queryable, and NOT editable.
    

    
Launch the appropriate application to open the document, web page or directory specified.

    """
    pass
    


def launchImageEditor( filename , editImageFile=string, viewImageFile=string):
    """
    launchImageEditor is undoable, NOT queryable, and NOT editable.
    

    
Launch the appropriate application to edit/view the image files specified. This command works only on the Macintosh and Windows platforms.

    """
    pass
    


def layerButton(annotation=string, backgroundColor=float, float, float, color=float, float, float, command=script, current=boolean, defineTemplate=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, hideOnPlaybackCommand=script, highlightColor=float, float, float, identification=int, isObscured=boolean, label=string, labelWidth=boolean, layerHideOnPlayback=boolean, layerState=string, layerVisible=boolean, manage=boolean, name=string, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, renameCommand=string, select=boolean, transparent=boolean, typeCommand=script, useTemplate=string, visible=boolean, visibleChangeCommand=script, visibleCommand=script, width=int):
    """
    layerButton is undoable, queryable, and editable.
    

    
Creates a layer bar button widget. This widget contains both the name of the layer to which it refers and a color swatch indicating it's color assignment. It is used primarily in the construction of the layerBar and layer Editor window, being the widget used for each layer in the respective lists.

    """
    pass
    


def layeredShaderPort( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, node=name, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, selectedColorControl=string, selectedTransparencyControl=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    layeredShaderPort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays an image representing the layered shader node specified.

    """
    pass
    


def layeredTexturePort( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, node=name, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, selectedAlphaControl=string, selectedBlendModeControl=string, selectedColorControl=string, selectedIsVisibleControl=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    layeredTexturePort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays an image representing the layered texture node specified.

    """
    pass
    


def layout( string , annotation=string, backgroundColor=float, float, float, childArray=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    layout is undoable, queryable, and editable.
    

    
This command allows you to edit or query the properties of any layout. The argument is the name of the layout.

    """
    pass
    


def layoutDialog(backgroundColor=float, float, float, dismiss=string, parent=string, title=string, uiScript=script):
    """
    layoutDialog is undoable, NOT queryable, and NOT editable.
    

    
The layoutDialog command creates a modal dialog containing a formLayout with 100 divisions. The formLayout can be populated with arbitrary UI elements through use of the '-ui/-uiScript' flag.
NOTE:
A layoutDialog is not a window and certain UI elements will not function properly within it. In particular menuBars and panels containing menuBars should not be used with the layoutDialog.

    """
    pass
    


def license(borrow=boolean, info=boolean, isBorrowed=boolean, isExported=boolean, isTrial=boolean, licenseMethod=boolean, productChoice=boolean, r=boolean, showBorrowInfo=boolean, showProductInfoDialog=boolean, usage=boolean):
    """
    license is undoable, NOT queryable, and NOT editable.
    

    
This command displays version information about the application if it is executed without flags. If one of the above flags is specified then the specified version information is returned.

    """
    pass
    


def lightlink( objects , b=boolean, hierarchy=boolean, light=name, make=boolean, object=name, sets=boolean, shapes=boolean, transforms=boolean):
    """
    lightlink is undoable, queryable, and NOT editable.
    

    
This command is used to make, break and query light linking relationships between lights/sets of lights and objects/sets of objects.
If no make, break or query flag is specified and both lights and objects flags are present, the make flag is assumed to be specified.
If no make, break or query flag is specified and only one of the lights and objects flags is present, the query flag is assumed to be specified.
You can specify as many lights and objects as you like, using the multiuse -light and -object flags.
A better way to perform light linking is to make sets of lights and sets of geometry. If you create a set which contains lights (such as the ceiling lights in your scene) and a set which contains geometry (such as the geometry of your character), you can then link the set containing lights with the set containing geometry in order to get those lights to illuminate those pieces of geometry. In addition, you can add and remove lights and geometry from their respective sets without having to make and break light links.

    """
    pass
    


def lightList(add=name, remove=name):
    """
    lightList is undoable, queryable, and editable.
    

    
Add/Remove a relationship between an object and the current light. Soon to be replaced by the connect-attribute command.

    """
    pass
    


def linearPrecision( int ):
    """
    linearPrecision is undoable, queryable, and NOT editable.
    

    
This command controls the display of linear strings in the interface. (See the linearField command). Setting this affects any linear strings displayed afterwards, formatting them so they will show at most the specified number of digits after the decimal point. Allowed values are 0 through 6.

    """
    pass
    


def listAnimatable(active=boolean, manip=boolean, manipHandle=boolean, shape=boolean, type=boolean):
    """
    listAnimatable is undoable, NOT queryable, and NOT editable.
    

    
This command list the animatable attributes of a node. Command flags allow filtering by the current manipulator, or node type.

    """
    pass
    


def listAttr( objects , array=boolean, caching=boolean, category=string, changedSinceFileOpen=boolean, channelBox=boolean, connectable=boolean, extension=boolean, fromPlugin=boolean, hasData=boolean, hasNullData=boolean, inUse=boolean, keyable=boolean, leaf=boolean, locked=boolean, multi=boolean, output=boolean, ramp=boolean, read=boolean, readOnly=boolean, scalar=boolean, scalarAndArray=boolean, settable=boolean, shortNames=boolean, string=string, unlocked=boolean, usedAsFilename=boolean, userDefined=boolean, visible=boolean, write=boolean):
    """
    listAttr is undoable, NOT queryable, and NOT editable.
    

    
This command lists the attributes of a node. If no flags are specified all attributes are listed.

    """
    pass
    


def listAttrPatterns(patternType=boolean, verbose=boolean):
    """
    listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.
    

    
Attribute patterns are plain text descriptions of an entire Maya attribute forest. ("forest" because there could be an arbitrary number of root level attributes, it's not restricted to having a single common parent though in general that practice is a good idea.) This command lists the various pattern types available, usually created via plugin, as well as any specific patterns that have already been instantiated. A pattern type is a thing that knows how to take some textual description of an attribute tree, e.g. XML or plaintext, and convert it into an attribute pattern that can be applied to any node or node type in Maya.

    """
    pass
    


def listCameras(orthographic=boolean, perspective=boolean):
    """
    listCameras is undoable, NOT queryable, and NOT editable.
    

    
Command to list all cameras. If no flags are given, both perspective and orthographic cameras will be displayed. This command returns an array of camera names. When the transform name uniquely identifies the camera it is used, otherwise the shape name will be returned.

    """
    pass
    


def listConnections(connections=boolean, destination=boolean, exactType=boolean, plugs=boolean, shapes=boolean, skipConversionNodes=boolean, source=boolean, type=string):
    """
    listConnections is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns a list of all attributes/objects of a specified type that are connected to the given object(s). If no objects are specified then the command lists the connections on selected nodes.

    """
    pass
    


def listDeviceAttachments(attribute=string, axis=string, clutch=string, device=string, file=string, selection=boolean, write=boolean):
    """
    listDeviceAttachments is undoable, NOT queryable, and NOT editable.
    

    
This command lists the current set of device attachments. The listing is in the form of the commands required to recreate them. This includes both attachments and device mappings.

    """
    pass
    


def listHistory( objects , allConnections=boolean, allFuture=boolean, allGraphs=boolean, breadthFirst=boolean, future=boolean, futureLocalAttr=boolean, futureWorldAttr=boolean, groupLevels=boolean, historyAttr=boolean, interestLevel=int, leaf=boolean, levels=uint, pruneDagObjects=boolean):
    """
    listHistory is undoable, queryable, and NOT editable.
    

    
This command traverses backwards or forwards in the graph from the specified node and returns all of the nodes whose construction history it passes through. The construction history consists of connections to specific attributes of a node defined as the creators and results of the node's main data, eg. the curve for a Nurbs Curve node.
For information on history connections through specific plugs use the "listConnections" command first to find where the history begins then use this command on the resulting node.

    """
    pass
    


def listInputDeviceAxes( string ):
    """
    listInputDeviceAxes is undoable, NOT queryable, and NOT editable.
    

    
This command lists all of the axes of the specified input device.

    """
    pass
    


def listInputDeviceButtons( string ):
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
    


def listNodeTypes( string , exclude=string):
    """
    listNodeTypes is undoable, NOT queryable, and NOT editable.
    

    
Lists dependency node types satisfying a specified classification string.
See the 'getClassification' command for a list of the standard classification strings.

    """
    pass
    


def listRelatives( objects , allDescendents=boolean, allParents=boolean, children=boolean, fullPath=boolean, noIntermediate=boolean, parent=boolean, path=boolean, shapes=boolean, type=string):
    """
    listRelatives is undoable, NOT queryable, and NOT editable.
    

    
This command lists parents and children of DAG objects. The flags -c/children, -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually exclusive. Only one can be used in a command.
When listing parents of objects directly under the world, the command will return an empty parent list. Listing parents of objects directly under a shape (underworld objects) will return their containing shape node in the list of parents. Listing parents of components of objects will return the object.
When listing children, shape nodes will return their underworld objects in the list of children. Listing children of components of objects returns nothing.
The -ni/noIntermediate flag works with the -s/shapes flag. It causes any intermediate shapes among the descendents to be ignored.

    """
    pass
    


def listSets( object , allSets=boolean, extendToShape=boolean, object=name, type=uint):
    """
    listSets is undoable, NOT queryable, and NOT editable.
    

    
The listSets command is used to get a list of all the sets an object belongs to. To get sets of a specific type for an object use the type flag as well.
To get a list of all sets in the scene then don't use an object in the command line but use one of the flags instead.

    """
    pass
    


def loadFluid(currentTime=boolean, frame=float, initialConditions=boolean):
    """
    loadFluid is undoable, queryable, and editable.
    

    
A command to set builtin fluid attributes such as Density, Velocity, etc for all cells in the grid from the initial state cache

    """
    pass
    


def loadModule(allModules=boolean, load=string, scan=boolean):
    """
    loadModule is NOT undoable, NOT queryable, and NOT editable.
    

    
Maya plug-ins may be installed individually within one of Maya's standard plug-in directories, or they may be packaged up with other resources in a "module". Each module resides in its own directory and provides a module definition file to make Maya aware of the plug-ins it provides. When Maya starts up it loads all of the module files it finds, making the module's plug-ins, scripts and other resources available for use. Note that the plug-ins themselves are not loaded at this time, Maya is simply made aware of them so that they can be loaded if needed. The loadModule command provides the ability to list and load any new modules which have been added since Maya started up, thereby avoiding the need to restart Maya before being able to use them.

    """
    pass
    


def loadPlugin( string string... , addCallback=script, allPlugins=boolean, name=string, quiet=boolean, removeCallback=script):
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
    


def loadUI(listTypes=boolean, uiFile=string, uiString=string, verbose=boolean, workingDirectory=string):
    """
    loadUI is undoable, NOT queryable, and NOT editable.
    

    
loadUI command allows loading of a user interface created in Trolltech Qt Designer.
Some Qt classes have equivalents in Maya. If a widget's class is recognized, the Maya-equivelent will be created instead.
Any dynamic properties on a widget which start with a '-' character will be treated as a MEL flag/value pair. Similarly, any which start with a '+' will be treated as a Python flag/value pair. Such pairs will be applied to the widget upon creation.

    """
    pass
    


def lockNode(ignoreComponents=boolean, lock=boolean, lockName=boolean, lockUnpublished=boolean):
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
    


def loft( curve curve curve... , autoReverse=boolean, caching=boolean, close=boolean, constructionHistory=boolean, createCusp=boolean, degree=int, name=string, nodeState=int, object=boolean, polygon=int, range=boolean, rebuild=boolean, reverse=boolean, reverseSurfaceNormals=boolean, sectionSpans=int, uniform=boolean):
    """
    loft is undoable, queryable, and editable.
    

    
This command computes a skinned (lofted) surface passing through a number of NURBS curves. There must be at least two curves present. The NURBS curves may be surface isoparms, curve on surfaces, trimmed edges or polygon edges.

    """
    pass
    


def lookThru( editorName object , farClip=float, nearClip=float):
    """
    lookThru is NOT undoable, queryable, and NOT editable.
    

    
This command sets a particular camera to look through in a view. This command may also be used to view the negative z axis of lights or other DAG objects. The standard camera tools can then be used to place the object.
Note: if there are multiple objects under the transform selected, cameras and lights take precedence.

    """
    pass
    


def ls(*args, **kwargs):
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
    


def lsThroughFilter( string , item=string, nodeArray=boolean, reverse=boolean, selection=boolean, sort=string):
    """
    lsThroughFilter is undoable, NOT queryable, and NOT editable.
    

    
List all objects in the world that pass a given filter.

    """
    pass
    


def lsUI( objects , cmdTemplates=boolean, collection=boolean, contexts=boolean, controlLayouts=boolean, controls=boolean, dumpWidgets=boolean, editors=boolean, head=int, long=boolean, menuItems=boolean, menus=boolean, numWidgets=boolean, panels=boolean, radioMenuItemCollections=boolean, tail=int, type=string, windows=boolean):
    """
    lsUI is undoable, NOT queryable, and NOT editable.
    

    
This command returns the names of UI objects.

    """
    pass
    


def makebot(checkdepends=boolean, checkres=uint, input=string, nooverwrite=boolean, output=string, verbose=boolean):
    """
    makebot is undoable, NOT queryable, and NOT editable.
    

    
The makebot command takes an image file and produces a block ordered texture (BOT) file, to be used for texture caching. If a relative pathname is specified for the input image file, project management rules apply. If a relative pathname is specified for the output BOT file, project management rules apply and gets put into the sourceImages directory.

    """
    pass
    


def makeIdentity( dagObject , apply=boolean, jointOrient=boolean, normal=uint, preserveNormals=boolean, rotate=boolean, scale=boolean, translate=boolean):
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
    


def makeLive( surface , none=boolean):
    """
    makeLive is undoable, NOT queryable, and NOT editable.
    

    
This commmand makes an object live. A live object defines the surface on which to create objects and to move object relative to. Only construction planes, nurbs surfaces and polygon meshes can be made live.
The makeLive command expects one of these types of objects as an explicit argument. If no argument is explicitly specified, then there are a number of default behaviours based on what is currently active. The command will fail if there is more than one object active or the active object is not one of the valid types of objects. If there is nothing active, the current live object will become dormant. Otherwise, the active object will become the live object.

    """
    pass
    


def makePaintable(stringstring, activate=boolean, activateAll=boolean, altAttribute=string, attrType=string, clearAll=boolean, remove=boolean, shapeMode=string, uiName=string):
    """
    makePaintable is NOT undoable, queryable, and NOT editable.
    

    
Make attributes of nodes paintable to Attribute Paint Tool. This command is used to register new attributes to the Attribute Paint tool as paintable. Once registered the attributes will be recognized by the Attribute Paint tool and the user will be able to paint them.

    """
    pass
    


def makeSingleSurface( surface , chordHeight=linear, chordHeightRatio=float, constructionHistory=boolean, delta=linear, edgeSwap=boolean, format=int, fractionalTolerance=float, matchNormalDir=boolean, minEdgeLength=linear, name=string, normalizeTrimmedUVRange=boolean, object=boolean, polygonCount=int, polygonType=int, stitchTolerance=float, uNumber=int, uType=int, useChordHeight=boolean, useChordHeightRatio=boolean, vNumber=int, vType=int):
    """
    makeSingleSurface is undoable, queryable, and editable.
    

    
This command performs a stitch and tessellate operation.

    """
    pass
    


def manipMoveContext( object , activeHandle=int, activeHandleNormal=int, alignAlong=float, float, float, constrainAlongNormal=boolean, currentActiveHandle=int, editPivotMode=boolean, editPivotPosition=boolean, exists=boolean, image1=string, image2=string, image3=string, interactiveUpdate=boolean, lastMode=int, manipVisible=boolean, mode=int, orientAxes=float, float, float, orientJoint=string, orientJointEnabled=boolean, orientObject=string, orientTowards=float, float, float, pinPivot=boolean, pivotOriHandle=boolean, position=boolean, postCommand=script, postDragCommand=script, string, preCommand=script, preDragCommand=script, string, preserveChildPosition=boolean, preserveUV=boolean, reflection=boolean, reflectionAbout=int, reflectionAxis=int, reflectionTolerance=float, secondaryAxisOrient=string, snap=boolean, snapComponentsRelative=boolean, snapLiveFaceCenter=boolean, snapLivePoint=boolean, snapPivotOri=boolean, snapPivotPos=boolean, snapRelative=boolean, snapValue=float, translate=float, float, float, tweakMode=boolean, xformConstraint=string):
    """
    manipMoveContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a move manip context. Note that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of all move manip context. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing move manip context.

    """
    pass
    


def manipMoveLimitsCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    manipMoveLimitsCtx is undoable, queryable, and editable.
    

    
Create a context for the translate limits manipulator.

    """
    pass
    


def manipOptions(forceRefresh=boolean, handleSize=float, hideManipOnCtrl=boolean, hideManipOnShift=boolean, hideManipOnShiftCtrl=boolean, linePick=float, lineSize=float, pivotRotateHandleOffset=int, planeHandleOffset=int, pointSize=float, preselectHighlight=boolean, refreshMode=int, relative=boolean, rememberActiveHandle=boolean, rememberActiveHandleAfterToolSwitch=boolean, scale=float, showPivotRotateHandle=int, showPlaneHandles=int):
    """
    manipOptions is undoable, queryable, and NOT editable.
    

    
Changes the global manipulator parameters

    """
    pass
    


def manipPivot(ori=float, float, float, oriValid=boolean, pinPivot=boolean, pos=float, float, float, posValid=boolean, reset=boolean, resetOri=boolean, resetPos=boolean, snapOri=boolean, snapPos=boolean, valid=boolean):
    """
    manipPivot is undoable, queryable, and NOT editable.
    

    
Changes transform component pivot used by the move/rotate/scale manipulators.

    """
    pass
    


def manipRotateContext( object , activeHandle=int, alignAlong=float, float, float, constrainAlongNormal=boolean, currentActiveHandle=int, editPivotMode=boolean, editPivotPosition=boolean, exists=boolean, image1=string, image2=string, image3=string, lastMode=int, manipVisible=boolean, mode=int, modifyTranslation=boolean, orientAxes=float, float, float, orientObject=string, orientTowards=float, float, float, pinPivot=boolean, pivotOriHandle=boolean, position=boolean, postCommand=script, postDragCommand=script, string, preCommand=script, preDragCommand=script, string, preserveChildPosition=boolean, preserveUV=boolean, reflection=boolean, reflectionAbout=int, reflectionAxis=int, reflectionTolerance=float, rotate=float, float, float, snapPivotOri=boolean, snapPivotPos=boolean, tweakMode=boolean, useCenterPivot=boolean, useManipPivot=boolean, useObjectPivot=boolean, xformConstraint=string):
    """
    manipRotateContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a rotate manip context.

    """
    pass
    


def manipRotateLimitsCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    manipRotateLimitsCtx is undoable, queryable, and editable.
    

    
Create a context for the rotate limits manipulator.

    """
    pass
    


def manipScaleContext( object , activeHandle=int, alignAlong=float, float, float, constrainAlongNormal=boolean, currentActiveHandle=int, editPivotMode=boolean, editPivotPosition=boolean, exists=boolean, image1=string, image2=string, image3=string, lastMode=int, manipVisible=boolean, mode=int, orientAxes=float, float, float, orientObject=string, orientTowards=float, float, float, pinPivot=boolean, pivotOriHandle=boolean, position=boolean, postCommand=script, postDragCommand=script, string, preCommand=script, preDragCommand=script, string, preserveChildPosition=boolean, preserveUV=boolean, preventNegativeScale=boolean, reflection=boolean, reflectionAbout=int, reflectionAxis=int, reflectionTolerance=float, scale=float, float, float, snapPivotOri=boolean, snapPivotPos=boolean, tweakMode=boolean, xformConstraint=string):
    """
    manipScaleContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a scale manip context.

    """
    pass
    


def manipScaleLimitsCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    manipScaleLimitsCtx is undoable, queryable, and editable.
    

    
Create a context for the scale limits manipulator.

    """
    pass
    


def marker( string , attach=boolean, detach=boolean, frontTwist=angle, orientationMarker=boolean, positionMarker=boolean, sideTwist=angle, time=time, upTwist=angle, valueU=float):
    """
    marker is undoable, queryable, and editable.
    

    
The marker command creates one or two markers, on a motion path curve, at the specified time and location. The optionnal string argument is the parent object name.
One can specify "-pm -om" option to create both, a position marker and an orientation marker.
Since there is only one keyframe for each marker of the same type, no more than one marker of the same type with the same time value can exist.
The default marker type is the position marker. The default time is the current time.

    """
    pass
    


def matchTransform( objects... , pivots=boolean, position=boolean, rotation=boolean, scale=boolean):
    """
    matchTransform is undoable, NOT queryable, and NOT editable.
    

    
This command modifies the source object's transform to match the target object's transform.
If no flags are specified then the command will match position, rotation and scaling.

    """
    pass
    


def mayaDpiSetting(mode=uint, realScaleValue=boolean, scaleValue=float, systemDpi=boolean):
    """
    mayaDpiSetting is NOT undoable, queryable, and NOT editable.
    

    
Provide Maya interface scaling based on system DPI or custom scale setting or no scaling. Please note that the change will only take effect after relaunching Maya.

    """
    pass
    


def Mayatomr(active=boolean, addHosts=string, addIncludes=string, addLinks=string, binary=boolean, camera=string, echo=boolean, exportFilter=int, exportFilterString=string, exportPathNames=string, exportStartFile=boolean, file=string, fragmentChildDag=boolean, fragmentExport=boolean, fragmentIncomingShdrs=boolean, fragmentMaterials=boolean, immediateModeRender=boolean, init=boolean, layer=string, license=string, listHosts=boolean, listLinks=boolean, logFile=boolean, miStream=boolean, padframe=uint, pauseTuning=boolean, perframe=uint, preview=boolean, previousView=boolean, project=string, region=boolean, regionRect=uint, uint, uint, uint, removeHosts=string, removeLinks=string, render=boolean, renderNoSlaves=boolean, renderTarget=string, renderThreads=uint, renderVerbosity=uint, tabstop=uint, updateHosts=boolean, updateRayrc=boolean, verbosity=uint, xResolution=uint, yResolution=uint):
    """
    Mayatomr is undoable, queryable, and NOT editable.
    

    
This mel command provides access to most functionalities of mental ray for maya plugin including .mi file export, preview and batch rendering, network rendering and shader management.

    """
    pass
    


def melInfo():
    """
    melInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
This command returns the names of all global MEL procedures that are currently defined as a string array. The user can query the definition of each MEL procedure using the "whatIs" command.

    """
    pass
    


def melOptions(duplicateVariableWarnings=boolean):
    """
    melOptions is NOT undoable, queryable, and NOT editable.
    

    
Set and query options that affect the behavior of Maya's Embedded Language (MEL).

    """
    pass
    


def memory(asFloat=boolean, freeMemory=boolean, gigaByte=boolean, heapMemory=boolean, kiloByte=boolean, megaByte=boolean, pageFaults=boolean, pageReclaims=boolean, physicalMemory=boolean, summary=boolean, swapFree=boolean, swapLogical=boolean, swapMax=boolean, swapPhysical=boolean, swapVirtual=boolean, swaps=boolean):
    """
    memory is undoable, NOT queryable, and NOT editable.
    

    
Used to query essential statistics on memory availability and usage.
By default memory sizes are returned in bytes. Since Maya's command engine only supports 32-bit signed integers, any returned value which cannot fit into 31 bits will be truncated to 2,147,483,647 and a warning message displayed. To avoid having memory sizes truncated use one of the memory size flags to return the value in larger units (e.g. megabytes) or use the asFloat flag to return the value as a float.

    """
    pass
    


def menu( string , allowOptionBoxes=boolean, deleteAllItems=boolean, docTag=string, enable=boolean, familyImage=string, helpMenu=boolean, itemArray=boolean, label=string, ltVersion=string, mnemonic=string, numberOfItems=boolean, parent=string, postMenuCommand=script, postMenuCommandOnce=boolean, tearOff=boolean, version=string, visible=boolean):
    """
    menu is undoable, queryable, and editable.
    

    
This command creates a new menu and adds it to the default window's menubar if no parent is specified. The menu can be enabled/disabled. Note that this command may also be used on menu objects created using the command menuItem -sm/subMenu true.

    """
    pass
    


def menuBarLayout( string , annotation=string, backgroundColor=float, float, float, childArray=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, menuArray=boolean, menuBarVisible=boolean, menuIndex=string, uint, noBackground=boolean, numberOfChildren=boolean, numberOfMenus=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    menuBarLayout is undoable, queryable, and editable.
    

    
Create a layout containing a menu bar. The menu bar will appear and behave similar to any menu bar created with the 'window -menuBar true' command. Menus may be created with a menuBarLayout as their parent. Child controls are simply positioned to fill the menuBarLayout area beneath the menu bar consequently, some other layout should be used as the immediate child.

    """
    pass
    


def menuEditor( string , annotation=string, backgroundColor=float, float, float, cellHeight=int, cellWidth=int, cellWidthHeight=int, int, checkBoxPresent=boolean, string, int, checkBoxState=boolean, string, int, command=string, string, int, defineTemplate=string, delete=string, int, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, iconMenuCallback=string, image=string, string, int, isObscured=boolean, label=string, string, int, manage=boolean, menuItemTypes=boolean, noBackground=boolean, numberOfPopupMenus=boolean, optionBoxCommand=string, string, int, optionBoxPresent=boolean, string, int, parent=string, popupMenuArray=boolean, preventOverride=boolean, radioButtonPresent=boolean, string, int, radioButtonState=boolean, string, int, separator=string, int, style=string, subMenuAt=string, int, subMenuEditorWindow=string, subMenuEditorsOpen=boolean, subMenuOf=string, string, int, topLevelMenu=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    menuEditor is undoable, queryable, and editable.
    

    
A menuEditor displays the contents of a popup menu and allows the menu's items to be edited. Menu items are represented by labelled icons which can be dragged around within the editor to change the menu's layout. Various objects can be dragged and dropped into the menuEditor to create new menu items: toolButtons from the shelf or toolbox, shelfButtons from the shelf, iconTextButtons with attached commands, and scripts from the command window.
When editing a Marking Menu, the radial menu items correspond to 8 icons arranged in a circle within the menuEditor. Overflow items in the Marking Menu (or linear items in a normal menu) are displayed in a column below the radial items.
To edit a submenu of a popup menu, a new menuEditor instance must be created (typically within its own window) and attached to its parent menuEditor.
Some flags require the position of a menu item to be passed in as an argument. For these, positions are specified with a (string,int) pair, where the string corresponds to a radial position (possibily "None") and the int corresponds to a linear position (possibly equal to 0 for none). Radial positions are specified by one of ("N",0), ("NE",0), ("E",0), ("SE",0), ("S",0), ("SW",0), ("W",0) or ("NW",0). Overflow, or linear positions, are specified with ("None",i), where i is a 1-based index giving the position of the item within the overflow column.
Note: This command is not meant to be called explicitly. It was created to support the Marking Menu editor. It is recommended that you use that editor to modify marking menus.

    """
    pass
    


def menuItem( string , allowOptionBoxes=boolean, altModifier=boolean, annotation=string, boldFont=boolean, checkBox=boolean, collection=string, command=script, commandModifier=boolean, ctrlModifier=boolean, data=int, divider=boolean, dividerLabel=string, docTag=string, dragDoubleClickCommand=script, dragMenuCommand=script, echoCommand=boolean, enable=boolean, enableCommandRepeat=boolean, familyImage=string, image=string, imageOverlayLabel=string, insertAfter=string, isCheckBox=boolean, isOptionBox=boolean, isRadioButton=boolean, italicized=boolean, keyEquivalent=string, label=string, longDivider=boolean, ltVersion=string, optionBox=boolean, optionBoxIcon=string, optionModifier=boolean, parent=string, postMenuCommand=script, postMenuCommandOnce=boolean, radialPosition=string, radioButton=boolean, shiftModifier=boolean, sourceType=string, subMenu=boolean, tearOff=boolean, version=string):
    """
    menuItem is undoable, queryable, and editable.
    

    
This command creates/edits/queries menu items.

    """
    pass
    


def menuSet( object , addMenu=string, allMenuSets=boolean, currentMenuSet=string, exists=string, hotBoxVisible=boolean, insertMenu=string, uint, label=string, menuArray=string,..., moveMenu=string, uint, moveMenuSet=string, uint, numberOfMenuSets=boolean, numberOfMenus=boolean, permanent=boolean, removeMenu=string, removeMenuSet=string):
    """
    menuSet is undoable, queryable, and editable.
    

    
Create a menu set which is used to logically order menus for display in the main menu bar. Such menu sets can be edited and reordered dynamically.

    """
    pass
    


def menuSetPref( object , exists=boolean, force=boolean, loadAll=boolean, removeAll=boolean, saveAll=boolean, saveBackup=boolean, version=boolean):
    """
    menuSetPref is undoable, queryable, and editable.
    

    
Provides the functionality to save and load menuSets between sessions of Maya. For Internal Use Only!

    """
    pass
    


def messageLine( name , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
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
    


def mirrorJoint( object , mirrorBehavior=boolean, mirrorXY=boolean, mirrorXZ=boolean, mirrorYZ=boolean, searchReplace=string, string):
    """
    mirrorJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will duplicate a branch of the skeleton from the selected joint symmetrically about a plane in world space. There are three mirroring modes(xy-, yz-, xz-plane).

    """
    pass
    


def modelCurrentTimeCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, percent=float):
    """
    modelCurrentTimeCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to change current time within the model views.

    """
    pass
    


def modelEditor( editorName , activeComponentsXray=boolean, activeCustomEnvironment=string, activeCustomGeometry=string, activeCustomLighSet=string, activeCustomOverrideGeometry=string, activeCustomRenderer=string, activeOnly=boolean, activeShadingGraph=string, activeView=boolean, addObjects=string, addSelected=boolean, allObjects=boolean, backfaceCulling=boolean, bufferMode=string, bumpResolution=uint, uint, camera=string, cameraName=string, cameraSetup=boolean, cameras=boolean, cmEnabled=boolean, colorMap=boolean, colorResolution=uint, uint, control=boolean, controlVertices=boolean, cullingOverride=string, default=boolean, defineTemplate=string, deformers=boolean, dimensions=boolean, displayAppearance=string, displayLights=string, displayTextures=boolean, docTag=string, dynamicConstraints=boolean, dynamics=boolean, editorChanged=script, exists=boolean, exposure=float, filter=string, filteredObjectList=boolean, fluids=boolean, fogColor=float, float, float, float, fogDensity=float, fogEnd=float, fogMode=string, fogSource=string, fogStart=float, fogging=boolean, follicles=boolean, forceMainConnection=string, gamma=float, grid=boolean, hairSystems=boolean, handles=boolean, headsUpDisplay=boolean, height=int, highlightConnection=string, hulls=boolean, ignorePanZoom=boolean, ikHandles=boolean, imagePlane=boolean, interactive=boolean, isFiltered=boolean, jointXray=boolean, joints=boolean, lights=boolean, lineWidth=float, locators=boolean, lockMainConnection=boolean, lowQualityLighting=boolean, mainListConnection=string, manipulators=boolean, maxConstantTransparency=float, modelPanel=string, motionTrails=boolean, nCloths=boolean, nParticles=boolean, nRigids=boolean, noUndo=boolean, nurbsCurves=boolean, nurbsSurfaces=boolean, objectFilter=script, objectFilterList=script, objectFilterListUI=script, objectFilterShowInHUD=boolean, objectFilterUI=script, occlusionCulling=boolean, panel=string, parent=string, pivots=boolean, planes=boolean, pluginObjects=string, boolean, pluginShapes=boolean, polymeshes=boolean, queryPluginObjects=string, removeSelected=boolean, rendererDeviceName=boolean, rendererList=boolean, rendererListUI=boolean, rendererName=string, rendererOverrideList=boolean, rendererOverrideListUI=boolean, rendererOverrideName=string, resetCustomCamera=boolean, sceneRenderFilter=string, selectionConnection=string, selectionHiliteDisplay=boolean, setSelected=boolean, shadows=boolean, smoothWireframe=boolean, sortTransparent=boolean, stateString=boolean, strokes=boolean, subdivSurfaces=boolean, textureAnisotropic=boolean, textureDisplay=string, textureHilight=boolean, textureMaxSize=int, textureMemoryUsed=boolean, textureSampling=int, textures=boolean, toggleExposure=boolean, toggleGamma=boolean, transpInShadows=boolean, transparencyAlgorithm=string, twoSidedLighting=boolean, unParent=boolean, unlockMainConnection=boolean, updateColorMode=boolean, updateMainConnection=boolean, useBaseRenderer=boolean, useColorIndex=boolean, useDefaultMaterial=boolean, useInteractiveMode=boolean, useRGBImagePlane=boolean, useTemplate=string, userNode=string, viewObjects=boolean, viewSelected=boolean, viewTransformName=string, viewType=boolean, width=int, wireframeBackingStore=boolean, wireframeOnShaded=boolean, xray=boolean):
    """
    modelEditor is undoable, queryable, and editable.
    

    
Create, edit or query a model editor.
Note that some of the flags of this command may have different settings for normal mode and for interactive/playback mode. For example, a modelEditor can be set to use shaded mode normally, but to use wireframe during playback for greater speed. Some flags also support having defaults set so that new model editors will be created with those settings.

    """
    pass
    


def modelPanel( panelName , barLayout=boolean, camera=string, control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, modelEditor=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    modelPanel is undoable, queryable, and editable.
    

    
This command creates a panel consisting of a model editor. See the modelEditor command documentation for more information.

    """
    pass
    


def moduleInfo(definition=boolean, listModules=boolean, moduleName=string, path=boolean, version=boolean):
    """
    moduleInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
Returns information on modules found by Maya.

    """
    pass
    


def mouse(enableScrollWheel=boolean, mouseButtonTracking=int, mouseButtonTrackingStatus=boolean, scrollWheelStatus=boolean):
    """
    mouse is undoable, NOT queryable, and NOT editable.
    

    
This command allows to configure mouse.

    """
    pass
    


def move( float float float objects , absolute=boolean, componentSpace=boolean, constrainAlongNormal=boolean, deletePriorHistory=boolean, localSpace=boolean, moveX=boolean, moveXY=boolean, moveXYZ=boolean, moveXZ=boolean, moveY=boolean, moveYZ=boolean, moveZ=boolean, objectSpace=boolean, orientJoint=string, parameter=boolean, preserveChildPosition=boolean, preserveGeometryPosition=boolean, preserveUV=boolean, reflection=boolean, reflectionAboutBBox=boolean, reflectionAboutOrigin=boolean, reflectionAboutX=boolean, reflectionAboutY=boolean, reflectionAboutZ=boolean, reflectionTolerance=float, relative=boolean, rotatePivotRelative=boolean, scalePivotRelative=boolean, secondaryAxisOrient=string, symNegative=boolean, worldSpace=boolean, worldSpaceDistance=boolean, xformConstraint=string):
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
    


def moveKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, moveFunction=string, name=string, option=string):
    """
    moveKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to move keyframes within the graph editor

    """
    pass
    


def moveVertexAlongDirection(direction=float, float, float, magnitude=linear, normalDirection=linear, uDirection=linear, uvNormalDirection=linear, linear, linear, vDirection=linear):
    """
    moveVertexAlongDirection is undoable, NOT queryable, and NOT editable.
    

    
The command moves the selected vertex ( control vertex ) in the specified unit direction by the given magnitude. The vertex(ices) may also be moved in the direction of unit normal ( -n flag ). For NURBS surface vertices the direction of movement could also be either in tangent along U or tangent along V. The flags -n, -u, -v and -d are mutually exclusive, ie. the selected vertices can be all moved in only -n or -u or -v or -d.

    """
    pass
    


def movieInfo(string, counter=boolean, dropFrame=boolean, frameCount=boolean, frameDuration=boolean, height=boolean, movieTexture=boolean, negTimesOK=boolean, numFrames=boolean, quickTime=boolean, timeCode=boolean, timeCodeTrack=boolean, timeScale=boolean, twentyFourHourMax=boolean, width=boolean):
    """
    movieInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
movieInfo provides a mechanism for querying information about movie files.

    """
    pass
    


def movIn( attributeList , file=string, startTime=time):
    """
    movIn is undoable, NOT queryable, and NOT editable.
    

    
Imports a .mov file into animation curves connected to the listed attributes. The attribute must be writable, since an animation curve will be created and connected to the attribute. If an animation curve already is connected to the attribute, the imported data is pasted onto that curve.
The starting time used for the .mov file importation is the current time when the command is executed.
Valid attribute types are numeric attributes; time attributes; linear attributes; angular attributes; compound attributes made of the types listed previously; and multi attributes composed of the types listed previously. If an unsuppoted attribute type is requested, the command will fail and no data will be imported. It is important that your user units are set to the same units used in the .mov file, otherwise linear and angular values will be incorrect.
To export a .mov file, use the movOut command.

    """
    pass
    


def movOut( targetList , comment=boolean, file=string, precision=uint, time=timerange):
    """
    movOut is undoable, NOT queryable, and NOT editable.
    

    
Exports a .mov file from the listed attributes. Valid attribute types are numeric attributes; time attributes; linear attributes; angular attributes; compound attributes made of the types listed previously; and multi attributes composed of the types listed previously.
Length, angle, and time values will be written to the file in the user units.
If an unsupported attribute type is requested, the action will fail. The .mov file may be read back into Maya using the movIn command.

    """
    pass
    


def multiProfileBirailSurface( curve curve curve... curve curve , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, polygon=int, tangentContinuityProfile1=boolean, tangentContinuityProfile2=boolean, transformMode=int):
    """
    multiProfileBirailSurface is undoable, queryable, and editable.
    

    
The cmd creates a railed surface by sweeping the profiles using two rail curves. The two rails are the last two arguments. For examples, if 5 curves are specified, they will correspond to "curve1" "curve2" "curve3" "rail1" "rail2".
In this case, the cmd creates a railed surface by sweeping the profile "curve1" to profile "curve2", profile "curve2" to profile "curve3" along the two rail curves "rail1", "rail2". There must be atleast 3 profile curves followed by the two rail curves. The profile curves must intersect the two rail curves. The constructed may be made tangent continuous to the first and last profile using the flags -tp1, -tp2 provided the profiles are surface curves i.e. isoparms, curve on surface or trimmed edge.

    """
    pass
    


def multiTouch(gestures=boolean, trackpad=uint):
    """
    multiTouch is undoable, queryable, and NOT editable.
    

    
Used to interact with the Gestura (multi-touch) library.

    """
    pass
    


def mute(disable=boolean, force=boolean):
    """
    mute is undoable, queryable, and NOT editable.
    

    
The mute command is used to disable and enable playback on a channel. When a channel is muted, it retains the value that it was at prior to being muted.

    """
    pass
    


def nameCommand( string , annotation=string, command=script, data1=string, data2=string, data3=string, default=boolean, sourceType=string):
    """
    nameCommand is undoable, NOT queryable, and NOT editable.
    

    
This command creates a nameCommand object. Each nameCommand object can be connected to a hotkey. Thereafter, the nameCommand's command string will be executed whenever the hotkey is pressed (or released, as specified by the user).

    """
    pass
    


def nameField( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, drawInactiveFrame=boolean, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, nameChangeCommand=script, noBackground=boolean, numberOfPopupMenus=boolean, object=string, parent=string, popupMenuArray=boolean, preventOverride=boolean, receiveFocusCommand=script, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    nameField is undoable, queryable, and editable.
    

    
This command creates an editable field that can be linked to the name of a Maya object. The field will always show the name of the object.

    """
    pass
    


def namespace( string , absoluteName=boolean, addNamespace=string, collapseAncestors=string, deleteNamespaceContent=boolean, exists=string, force=boolean, isRootNamespace=string, mergeNamespaceWithParent=boolean, mergeNamespaceWithRoot=boolean, moveNamespace=string, string, parent=string, recurse=boolean, relativeNames=boolean, removeNamespace=string, rename=string, string, setNamespace=string, validateName=string):
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
    


def namespaceInfo( string , absoluteName=boolean, baseName=boolean, currentNamespace=boolean, dagPath=boolean, fullName=boolean, internal=boolean, isRootNamespace=string, listNamespace=boolean, listOnlyDependencyNodes=boolean, listOnlyNamespaces=boolean, parent=boolean, recurse=boolean, shortName=boolean):
    """
    namespaceInfo is undoable, NOT queryable, and NOT editable.
    

    
This command displays information about a namespace. The target namespace can optionally be specified on the command line. If no namespace is specified, the command will display information about the current namespace.
A namespace is a simple grouping of objects under a given name. Each item in a namespace can then be identified by its own name, along with what namespace it belongs to. Namespaces can contain other namespaces like sets, with the restriction that all namespaces are disjoint.
Namespaces are primarily used to resolve name-clash issues in Maya, where a new object has the same name as an existing object (from importing a file, for example). Using namespaces, you can have two objects with the same name, as long as they are contained in different namespaces.
Note that namespaces are a simple grouping of names, so they do not effect selection, the DAG, the Dependency Graph, or any other aspect of Maya. All namespace names are colon-separated.
The namespace format flags are: "baseName"("shortName"), "fullName" and "absoluteName". The flags are used in conjunction with the main query flags to specify the desired namespace format of the returned result. They can also be used to return the different formats of a specified namespace. By default, when no format is specified, the result will be returned as a full name.

    """
    pass
    


def nBase(clearCachedTextureMap=string, clearStart=boolean, stuffStart=boolean, textureToVertex=string):
    """
    nBase is undoable, queryable, and editable.
    

    
Edits one or more nBase objects. Note that nBase objects include nCloth, nRigid and nParticle objects, but the options on this command do not currently apply to nParticle objects.

    """
    pass
    


def newton( selectionList , attenuation=float, magnitude=float, maxDistance=linear, minDistance=float, name=string, perVertex=boolean, position=linear, linear, linear):
    """
    newton is undoable, queryable, and editable.
    

    
A Newton field pulls an object towards the exerting object with force dependent on the exerting object's mass, using Newton's universal law of gravitation.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def nodeCast(stringstring, copyDynamicAttrs=boolean, disableAPICallbacks=boolean, disableScriptJobCallbacks=boolean, disconnectUnmatchedAttrs=boolean, force=boolean, swapNames=boolean, swapValues=boolean):
    """
    nodeCast is undoable, NOT queryable, and NOT editable.
    

    
Given two nodes, a source node of type A and a target node of type B, where type A is either type B or a sub-type of B, this command will replace the target node with the source node. That is, all node connections, DAG hierarchy and attribute values on the target node will be removed from the target node and placed on the source node. This operation will fail if either object is referenced, locked or if the nodes do not share a common sub-type. This operation is atomic. If the given parameters fail, then the source and target nodes will remain in their initial state prior to execution of the command. IMPORTANT: the command will currently ignore instance connections and instance objects. It will also ignore reference nodes.

    """
    pass
    


def nodeEditor( string , activeTab=int, addNewNodes=boolean, addNode=string, additiveGraphingMode=boolean, allAttributes=boolean, allNodes=boolean, allowNewTabs=boolean, allowTabTearoff=boolean, autoSizeNodes=boolean, backToParentView=boolean, beginCreateNode=boolean, beginNewConnection=string, breakSelectedConnections=boolean, closeAllTabs=boolean, closeTab=int, consistentNameSize=boolean, contentsChangedCommand=script, control=boolean, createInfo=string, createNodeCommand=script, createTab=int, , string, , customAttributeListEdit=string, , string, , cycleHUD=boolean, defaultPinnedState=boolean, defineTemplate=string, deleteSelected=boolean, docTag=string, dotFormat=string, downstream=boolean, duplicateTab=int, , int, , exists=boolean, extendToShapes=boolean, feedbackConnection=boolean, feedbackNode=boolean, feedbackPlug=boolean, feedbackTabIndex=boolean, feedbackType=boolean, filter=string, filterCreateNodeTypes=script, focusCommand=script, forceMainConnection=string, frameAll=boolean, frameModelSelection=boolean, frameSelected=boolean, getNodeList=boolean, graphSelectedConnections=boolean, graphSelection=boolean, gridSnap=boolean, gridVisibility=boolean, highlightConnection=string, hudMessage=string, int, float, ignoreAssets=boolean, inContainerView=boolean, isContainerNode=string, island=boolean, keyPressCommand=script, keyReleaseCommand=script, layout=boolean, layoutCommand=script, lockMainConnection=boolean, mainListConnection=string, nodeSwatchSize=string, nodeTitleMode=string, nodeViewMode=string, openContainerView=string, boolean, panView=float, float, panel=string, parent=string, pinSelectedNodes=boolean, popupMenuScript=script, primary=boolean, redockTab=boolean, removeDownstream=boolean, removeNode=string, removeUnselected=boolean, removeUpstream=boolean, renameNode=string, renameTab=int, , string, , restoreInfo=string, restoreLastClosedTab=boolean, rootNode=string, rootsFromSelection=boolean, scaleView=float, selectAll=boolean, selectConnectionNodes=boolean, selectDownstream=boolean, selectFeedbackConnection=boolean, selectNode=string, selectUpstream=boolean, selectionConnection=string, settingsChangedCallback=script, shaderNetworks=boolean, showAllNodeAttributes=string, showNamespace=boolean, showSGShapes=boolean, showShapes=boolean, showTabs=boolean, showTransforms=boolean, stateString=boolean, syncedSelection=boolean, tabChangeCommand=script, toggleAttrFilter=boolean, toggleSelectedPins=boolean, toggleSwatchSize=string, toolTipCommand=script, traversalDepthLimit=int, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, upstream=boolean, useAssets=boolean, useTemplate=string, vnnCompound=boolean, vnnDgContainer=boolean, vnnRuntime=boolean):
    """
    nodeEditor is undoable, queryable, and editable.
    

    
This command creates/edits/queries a nodeEditor editor. The optional argument is the name of the control.

    """
    pass
    


def nodeIconButton( string , align=string, annotation=string, backgroundColor=float, float, float, command=script, defineTemplate=string, disabledImage=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, flipX=boolean, flipY=boolean, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, label=string, labelOffset=int, ltVersion=string, manage=boolean, marginHeight=uint, marginWidth=uint, noBackground=boolean, numberOfPopupMenus=boolean, overlayLabelBackColor=float, float, float, float, overlayLabelColor=float, float, float, parent=string, popupMenuArray=boolean, preventOverride=boolean, rotation=float, style=string, useAlpha=boolean, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    nodeIconButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates a button that can be displayed with different icons, with or without a text label. If the button is drag and dropped onto other controls (e.g., HyperShade), the command will be executed and the return string will be used as the name of a dropped node.

    """
    pass
    


def nodeOutliner( string , addCommand=script, addObject=name, attrAlphaOrder=string, connectivity=name, currentSelection=boolean, lastMenuChoice=string, longNames=boolean, menuCommand=script, menuMultiOption=boolean, multiSelect=boolean, niceNames=boolean, noConnectivity=boolean, nodesDisplayed=boolean, pressHighlightsUnconnected=boolean, remove=string, removeAll=boolean, replace=name, selectCommand=script, showConnectedOnly=boolean, showHidden=boolean, showInputs=boolean, showNonConnectable=boolean, showNonKeyable=boolean, showOutputs=boolean, showPublished=boolean, showReadOnly=boolean):
    """
    nodeOutliner is undoable, queryable, and editable.
    

    
The nodeOutliner command creates, edits and queries an outline control that shows dependency nodes and their attributes. Compound attributes are further expandable to show their children. Additional configure flags allow multi selection, customizable commands to issue upon selection, and showing connections (and connectability) to a single input attribute. There are also the abilities to add/remove/replace nodes through the command line interface, and drag/add.
In some configurations, dragging a connected attribute of a node will load the node at the other end of the connection.
There is a right mouse button menu and a flag to attach a command to it. The menu is used to list the specific connections of a connected attribute. Clicking over any spot but the row of a connected attribute will show an empty menu. By default, there is no command attached to the menu.

    """
    pass
    


def nodePreset(attributes=string, custom=string, delete=name, string, exists=name, string, isValidName=string, list=name, load=name, string, save=name, string):
    """
    nodePreset is NOT undoable, NOT queryable, and NOT editable.
    

    
Command to save and load preset settings for a node. This command allows you to take a snapshot of the values of all attributes of a node and save it to disk as a preset with user specified name. Later the saved preset can be loaded and applied onto a different node of the same type. The end result is that the node to which the preset is applied takes on the same values as the node from which the preset was generated had at the time of the snapshot.

    """
    pass
    


def nodeTreeLister( string , addFavorite=string, addItem=string, string, script, addVnnItem=string, string, string, annotation=string, backgroundColor=float, float, float, clearContents=boolean, collapsePath=string, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, executeItem=string, exists=boolean, expandPath=string, expandToDepth=int, favoritesCallback=script, favoritesList=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, itemScript=string, manage=boolean, noBackground=boolean, nodeLibrary=string, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, refreshCommand=script, removeFavorite=string, removeItem=string, resultsPathUnderCursor=boolean, selectPath=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, vnnString=boolean, width=int):
    """
    nodeTreeLister is undoable, queryable, and editable.
    

    
This command creates/edits/queries the node tree lister control. nodeTreeLister is a treeLister, but items are assumed to have commands which return dependency node names. Dragging from the results pane is supported.
The optional argument is the name of the control.

    """
    pass
    


def nodeType( string , apiType=boolean, derived=boolean, inherited=boolean, isTypeName=boolean):
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
    


def nonLinear( objects , after=boolean, afterReference=boolean, autoParent=boolean, before=boolean, commonParent=boolean, defaultScale=boolean, deformerTools=boolean, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, name=string, parallel=boolean, prune=boolean, remove=boolean, split=boolean, type=string):
    """
    nonLinear is undoable, queryable, and editable.
    

    
This command creates a functional deformer of the specified type that will deform the selected objects. The deformer consists of three nodes: The deformer driver that gets connected to the history of the selected objects, the deformer handle transform that controls position and orientation of the axis of the deformation and the deformer handle that maintains the deformation parameters. The type of the deformer handle shape created depends on the specified type of the deformer. The deformer handle will be positioned at the center of the selected objects' bounding box and oriented to match the orientation of the leading object in the selection list. The deformer handle transform will be selected when the command is completed.
The nonLinear command has some flags which are specific to the nonLinear type specified with the -type flag. The flags correspond to the primary keyable attributes related to the specific type of nonLinear node. For example, if the type is "bend", then the flags "-curvature", "-lowBound" and "-highBound" may be used to initialize, edit or query those attribute values on the bend node. Examples of this are covered in the example section below.

    """
    pass
    


def normalConstraint( target... object , aimVector=float, float, float, layer=string, name=string, remove=boolean, targetList=boolean, upVector=float, float, float, weight=float, weightAliasList=boolean, worldUpObject=name, worldUpType=string, worldUpVector=float, float, float):
    """
    normalConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation based on the normal of the target surface(s) at the closest point(s) to the object.
A normalConstraint takes as input one or more surface shapes (the targets) and a DAG transform node (the object). The normalConstraint orients the constrained object such that the aimVector (in the object's local coordinate system) aligns in world space to combined normal vector. The upVector (again the the object's local coordinate system) is aligned in world space with the worldUpVector. The combined normal vector is a weighted average of the normal vector for each target surface at the point closest to the constrained object.

    """
    pass
    


def nParticle( selectionItem , attribute=string, cache=boolean, conserve=float, count=boolean, deleteCache=boolean, dynamicAttrList=boolean, floatValue=float, gridSpacing=linear, inherit=float, jitterBasePoint=linear, linear, linear, jitterRadius=linear, lowerLeft=linear, linear, linear, name=string, numJitters=uint, order=int, particleId=int, perParticleDouble=boolean, perParticleVector=boolean, position=linear, linear, linear, shapeName=string, upperRight=linear, linear, linear, vectorValue=float, float, float):
    """
    nParticle is undoable, queryable, and editable.
    

    
The nParticle command creates a new nParticle object from a list of world space points. If an nParticle object is created, the command returns the names of the new particle shape and its associated particle object dependency node. If an object was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.

    """
    pass
    


def nSoft( selectionList , convert=boolean, duplicate=boolean, duplicateHistory=boolean, goal=float, hideOriginal=boolean):
    """
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
    


def nurbsBoolean( surface surface , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, nsrfsInFirstShell=int, object=boolean, operation=int, smartConnection=boolean, tolerance=linear):
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
    


def nurbsCube(axis=linear, linear, linear, caching=boolean, constructionHistory=boolean, degree=int, heightRatio=float, lengthRatio=float, name=string, nodeState=int, object=boolean, patchesU=int, patchesV=int, pivot=linear, linear, linear, polygon=int, width=linear):
    """
    nurbsCube is undoable, queryable, and editable.
    

    
The nurbsCube command creates a new NURBS Cube made up of six planes. It creates an unit cube with center at origin by default.

    """
    pass
    


def nurbsCurveToBezier( curve ):
    """
    nurbsCurveToBezier is undoable, NOT queryable, and NOT editable.
    

    
The nurbsCurveToBezier command attempts to convert an existing NURBS curve to a Bezier curve.

    """
    pass
    


def nurbsEditUV(angle=float, pivotU=float, pivotV=float, relative=boolean, rotation=boolean, scale=boolean, scaleU=float, scaleV=float, uValue=float, vValue=float):
    """
    nurbsEditUV is undoable, queryable, and NOT editable.
    

    
Command edits uvs on NURBS objects. When used with the query flag, it returns the uv values associated with the specified components.

    """
    pass
    


def nurbsPlane(axis=linear, linear, linear, caching=boolean, constructionHistory=boolean, degree=int, lengthRatio=float, name=string, nodeState=int, object=boolean, patchesU=int, patchesV=int, pivot=linear, linear, linear, polygon=int, width=linear):
    """
    nurbsPlane is undoable, queryable, and editable.
    

    
The nurbsPlane command creates a new NURBS Plane and return the name of the new surface. It creates an unit plane with center at origin by default.

    """
    pass
    


def nurbsSelect(borderSelection=boolean, bottomBorder=boolean, growSelection=int, leftBorder=boolean, rightBorder=boolean, shrinkSelection=int, topBorder=boolean):
    """
    nurbsSelect is NOT undoable, NOT queryable, and NOT editable.
    

    
Performs selection operations on NURBS objects.
If any of the border flags is set, then the appropriate borders are selected. Otherwise the current CV selection is used, or all CVs if the surfaces is selected as an object.
The growSelection, shrinkSelection, borderSelection flags are then applied in that order.
In practice, it is recommended to use one flag at a time, except for the border flags.

    """
    pass
    


def nurbsSquare(caching=boolean, center=linear, linear, linear, centerX=linear, centerY=linear, centerZ=linear, constructionHistory=boolean, degree=int, name=string, nodeState=int, normal=linear, linear, linear, normalX=linear, normalY=linear, normalZ=linear, object=boolean, sideLength1=linear, sideLength2=linear, spansPerSide=int):
    """
    nurbsSquare is undoable, queryable, and editable.
    

    
The nurbsSquare command creates a square

    """
    pass
    


def nurbsToPoly( surface , chordHeight=linear, chordHeightRatio=float, constructionHistory=boolean, delta=linear, edgeSwap=boolean, format=int, fractionalTolerance=float, matchNormalDir=boolean, minEdgeLength=linear, name=string, normalizeTrimmedUVRange=boolean, object=boolean, polygonCount=int, polygonType=int, uNumber=int, uType=int, useChordHeight=boolean, useChordHeightRatio=boolean, vNumber=int, vType=int):
    """
    nurbsToPoly is undoable, queryable, and editable.
    

    
This command tesselates a NURBS surface and produces a polygonal surface. The name of the new polygonal surface is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def nurbsToPolygonsPref(chordHeight=float, chordHeightRatio=float, delta3D=float, edgeSwap=boolean, format=uint, fraction=float, matchRenderTessellation=uint, merge=uint, mergeTolerance=float, minEdgeLen=float, polyCount=uint, polyType=uint, uNumber=uint, uType=uint, useChordHeight=boolean, useChordHeightRatio=boolean, vNumber=uint, vType=uint):
    """
    nurbsToPolygonsPref is undoable, queryable, and NOT editable.
    

    
This command sets the values used by the nurbs-to-polygons (or "tesselate") preference. This preference is used by Maya menu items and is saved between Maya sessions. To query any of the flags, use the "-query" flag. For more information on the flags, see the node documentation for the "nurbsTessellate" node.

    """
    pass
    


def nurbsToSubdiv( surface , constructionHistory=boolean, name=string, object=boolean):
    """
    nurbsToSubdiv is undoable, queryable, and editable.
    

    
This command converts a NURBS surface and produces a subd surface. The name of the new subdivision surface is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def nurbsToSubdivPref(bridge=int, capType=int, collapsePoles=boolean, matchPeriodic=boolean, maxPolyCount=int, offset=linear, reverseNormal=boolean, solidType=int, trans00=float, trans01=float, trans02=float, trans10=float, trans11=float, trans12=float, trans20=float, trans21=float, trans22=float, trans30=float, trans31=float, trans32=float):
    """
    nurbsToSubdivPref is undoable, queryable, and NOT editable.
    

    
This command sets the values used by the nurbs-to-subdivision surface preference. This preference is used by the nurbs creation commands and is saved between Maya sessions.
To query any of the flags, use the "-query" flag.
For more information on the flags, see the node documentation for the "nurbsToSubdivProc" node.

    """
    pass
    


def nurbsUVSet(create=boolean, useExplicit=boolean):
    """
    nurbsUVSet is undoable, queryable, and editable.
    

    
Allows user to toggle between implicit and explicit UVs on a NURBS object. Also provides a facility to create, delete, rename and set the current explicit UVSet. An implicit UVSet is non-editable. It uses the parametric make-up of the NURBS object to determine the location of UVs (isoparm intersections). NURBS objects also support explicit UVSets which are similar to the UVs of a polygonal object. UVs are created at the knots (isoparm intersections) of the object and are fully editable. In order to access UV editing capabilities on a NURBS object an explicit UVSet must be created and set as the current UVSet.

    """
    pass
    


def objectCenter( object , gl=boolean, local=boolean, x=boolean, y=boolean, z=boolean):
    """
    objectCenter is undoable, NOT queryable, and NOT editable.
    

    
This command returns the coordinates of the center of the bounding box of the specified object. If one coordinate only is specified, it will be returned as a float. If no coordinates are specified, an array of floats is returned, containing x, y, and z. If you specify multiple coordinates, only one will be returned.

    """
    pass
    


def objectType( object , isAType=string, isType=string, tagFromType=string, typeFromTag=int, typeTag=boolean):
    """
    objectType is undoable, NOT queryable, and NOT editable.
    

    
This command returns the type of elements. Warning: This command is incomplete and may not be supported by all object types.

    """
    pass
    


def objectTypeUI( string , isType=string, listAll=boolean, superClasses=boolean):
    """
    objectTypeUI is undoable, NOT queryable, and NOT editable.
    

    
This command returns the type of UI element such as button, sliders, etc.

    """
    pass
    


def objExists( string ):
    """
    objExists is undoable, NOT queryable, and NOT editable.
    

    
This command simply returns true or false depending on whether an object with the given name exists.

    """
    pass
    


def offsetCurve( curve , caching=boolean, connectBreaks=int, constructionHistory=boolean, cutLoop=boolean, cutRadius=linear, distance=linear, name=string, nodeState=int, normal=linear, linear, linear, object=boolean, range=boolean, reparameterize=boolean, stitch=boolean, subdivisionDensity=int, tolerance=linear, useGivenNormal=boolean):
    """
    offsetCurve is undoable, queryable, and editable.
    

    
The offset command creates new offset curves from the selected curves. The connecting type for breaks in offsets is off (no connection), circular (connect with an arc) or linear (connect linearly resulting in a sharp corner). If loop cutting is on then any loops in the offset curves are trimmed away. For the default cut radius of 0.0 a sharp corner is created at each intersection. For values greater than 0.0 a small arc of that radius is created at each intersection. The cut radius value is only valid when loop cutting is on. Offsets (for planar curves) are calculated in the plane of that curve and 3d curves are offset in 3d. The subdivisionDensity flag is the maximum number of times the offset object can be subdivided (i.e. calculate the offset until the offset comes within tolerance or the iteration reaches this maximum.) The reparameterize option allows the offset curve to have a different parameterization to the original curve. This avoids uneven parameter distributions in the offset curve that can occur with large offsets of curves, but is more expensive to compute.

    """
    pass
    


def offsetCurveOnSurface( curve , caching=boolean, checkPoints=int, connectBreaks=int, constructionHistory=boolean, cutLoop=boolean, distance=linear, name=string, nodeState=int, object=boolean, range=boolean, stitch=boolean, subdivisionDensity=int, tolerance=linear):
    """
    offsetCurveOnSurface is undoable, queryable, and editable.
    

    
The offsetCurveOnSurface command offsets a curve on surface resulting in another curve on surface. The connecting type for breaks in offsets is off (no connection), circular (connect with an arc) or linear (connect linearly resulting in a sharp corner). If loop cutting is on then any loops in the offset curves are trimmed away and a sharp corner is created at each intersection. The subdivisionDensity flag is the maximum number of times the offset object can be subdivided (i.e. calculate the offset until the offset comes within tolerance or the iteration reaches this maximum.) The checkPoints flag sets the number of points per span at which the distance of the offset curve from the original curve is determined. The tolerance flag determines how accurately the offset curve should satisfy the required offset distance. A satisfactory offset curve is one for which all of the checkpoints are within the given tolerance of the required offset.

    """
    pass
    


def offsetSurface( surface , caching=boolean, constructionHistory=boolean, distance=linear, method=int, name=string, nodeState=int, object=boolean):
    """
    offsetSurface is undoable, queryable, and editable.
    

    
The offset command creates new offset surfaces from the selected surfaces. The default method is a surface offset, which offsets relative to the surface itself. The CV offset method offsets the CVs directly rather than the surface, so is usually slightly less accurate but is faster. The offset surface will always have the same degree, number of CVs and knot spacing as the original surface.

    """
    pass
    


def ogs(deviceInformation=boolean, disposeReleasableTextures=boolean, dumpTexture=string, enableHardwareInstancing=boolean, fragmentEditor=string, fragmentXML=string, gpuMemoryUsed=boolean, pause=boolean, rebakeTextures=boolean, regenerateUVTilePreview=string, reloadTextures=boolean, reset=boolean, shaderSource=string, toggleTexturePaging=boolean, traceRenderPipeline=boolean):
    """
    ogs is NOT undoable, queryable, and NOT editable.
    

    
OGS is one of the viewport renderers. As there is a lot of effort involved in migrating functionality it will evolve over several releases. As it evolves it is prudent to provide safeguards to get the database back to a known state. That is the function of this command, similar to how 'dgdirty' is used to restore state to the dependency graph.

    """
    pass
    


def ogsRender(activeMultisampleType=string, activeRenderOverride=string, activeRenderTargetFormat=string, availableFloatingPointTargetFormat=boolean, availableMultisampleType=boolean, availableRenderOverrides=boolean, camera=string, currentFrame=boolean, currentView=boolean, enableFloatingPointRenderTarget=boolean, enableMultisample=boolean, frame=float, height=uint, layer=name, noRenderView=boolean, width=uint):
    """
    ogsRender is NOT undoable, queryable, and editable.
    

    
Renders an image or a sequence using the OGS rendering engine

    """
    pass
    


def openGLExtension(extension=string, renderer=boolean, vendor=boolean, version=boolean):
    """
    openGLExtension is NOT undoable, NOT queryable, and NOT editable.
    

    
Command returns the extension name depending on whether a given OpenGL extension is supported or not. The input is the extension string to the -extension flag. If the -extension flag is not used, or if the string argument to this flag is an empty string than all extension names are returned in a single string. If the extension exists it is not necessary true that the extension is supported. This command can only be used when a modeling view has been created. Otherwise no extensions will have been initialized and the resulting string will always be the empty string.

    """
    pass
    


def openMayaPref(errlog=boolean, lazyLoad=boolean, oldPluginWarning=boolean):
    """
    openMayaPref is undoable, queryable, and editable.
    

    
Set or query API preferences.

    """
    pass
    


def optionMenu( string , annotation=string, backgroundColor=float, float, float, beforeShowPopup=script, changeCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, itemListLong=boolean, itemListShort=boolean, label=string, manage=boolean, noBackground=boolean, numberOfItems=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, select=int, useTemplate=string, value=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    optionMenu is undoable, queryable, and editable.
    

    
This command creates a popup menu control. The command creates the control and provides its menu. Subsequent calls to the menuItem command will place them in the popup. Note that commands attached to menu items will not get called. Attach any commands via the -cc/changedCommand flag.

    """
    pass
    


def optionMenuGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, extraLabel=string, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, itemListLong=boolean, itemListShort=boolean, label=string, manage=boolean, noBackground=boolean, numberOfItems=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, select=int, useTemplate=string, value=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    optionMenuGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text, option menu and an extra label. Both the label and extra label are optional. Subsequent calls to the menuItem command will place them in the option menu. When adding menu items to the option menu after the initialization step, use the name of the options menu itself. See the example below for more details. Note that commands attached to menu items will not get called. Use the -cc/changedCommand flag to be notified when the user changes the value of the option menu.

    """
    pass
    


def optionVar(arraySize=string, clearArray=string, exists=string, floatValue=string, float, floatValueAppend=string, float, intValue=string, int, intValueAppend=string, int, list=boolean, remove=string, removeFromArray=string, int, stringValue=string, string, stringValueAppend=string, string, version=int):
    """
    optionVar is undoable, queryable, and NOT editable.
    

    
This command allows you to set and query variables which are persistent between different invocations of Maya. These variables are stored as part of the preferences.

    """
    pass
    


def orbit( camera , horizontalAngle=angle, pivotPoint=linear, linear, linear, rotationAngles=angle, angle, verticalAngle=angle):
    """
    orbit is undoable, NOT queryable, and NOT editable.
    

    
The orbit command revolves the camera(s) horizontally and/or vertically in the perspective window. The rotation axis is with respect to the camera.
To revolve horizontally: the rotation axis is the camera up direction vector. To revolve vertically: the rotation axis is the camera left direction vector.
When both the horizontal and the vertical angles are supplied on the command line, the camera is firstly revolved horizontally, then revolved vertically.
This command may be applied to more than one camera; objects that are not cameras are ignored. When no camera name supplied, this command is applied to all currently active cameras.

    """
    pass
    


def orbitCtx(alternateContext=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, localOrbit=boolean, name=string, orbitScale=float, toolName=string):
    """
    orbitCtx is undoable, queryable, and editable.
    

    
Create, edit, or query an orbit context.

    """
    pass
    


def orientConstraint( target ... object , createCache=float, float, deleteCache=boolean, layer=string, maintainOffset=boolean, name=string, offset=float, float, float, remove=boolean, skip=string, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    orientConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation to match the orientation of the target or the average of a number of targets.
An orientConstraint takes as input one or more "target" DAG transform nodes to control the orientation of the single "constraint object" DAG transform The orientConstraint orients the constrained object to match the weighted average of the target world space orientations.

    """
    pass
    


def outlinerEditor( editorName , allowMultiSelection=boolean, alwaysToggleSelect=boolean, animLayerFilterOptions=string, attrAlphaOrder=string, attrFilter=string, autoExpand=boolean, autoExpandLayers=boolean, autoSelectNewObjects=boolean, containersIgnoreFilters=boolean, control=boolean, defineTemplate=string, directSelect=boolean, displayMode=string, doNotSelectNewObjects=boolean, docTag=string, dropIsParent=boolean, editAttrName=boolean, exists=boolean, expandAllItems=boolean, expandAllSelectedItems=boolean, expandAttribute=boolean, expandConnections=boolean, expandObjects=boolean, feedbackItemName=boolean, feedbackRowNumber=boolean, filter=string, forceMainConnection=string, getCurrentSetOfItem=int, highlightActive=boolean, highlightConnection=string, highlightSecondary=boolean, ignoreDagHierarchy=boolean, ignoreHiddenAttribute=boolean, ignoreOutlinerColor=boolean, isChildSelected=name, isSet=int, isSetMember=int, lockMainConnection=boolean, longNames=boolean, mainListConnection=string, mapMotionTrails=boolean, masterOutliner=string, niceNames=boolean, object=name, organizeByLayer=boolean, panel=string, parent=string, parentObject=boolean, pinPlug=name, refresh=boolean, removeFromCurrentSet=int, renameItem=int, renameSelectedItem=boolean, renderFilterActive=boolean, renderFilterIndex=int, renderFilterVisible=boolean, selectCommand=script, selectionConnection=string, selectionOrder=string, setFilter=string, setsIgnoreFilters=boolean, showAnimCurvesOnly=boolean, showAnimLayerWeight=boolean, showAssets=boolean, showAssignedMaterials=boolean, showAttrValues=boolean, showAttributes=boolean, showCompounds=boolean, showConnected=boolean, showContainedOnly=boolean, showContainerContents=boolean, showDagOnly=boolean, showLeafs=boolean, showNamespace=boolean, showNumericAttrsOnly=boolean, showPinIcons=boolean, showPublishedAsConnected=boolean, showReferenceMembers=boolean, showReferenceNodes=boolean, showSelected=boolean, showSetMembers=boolean, showShapes=boolean, showTextureNodesOnly=boolean, showUVAttrsOnly=boolean, showUnitlessCurves=boolean, showUpstreamCurves=boolean, sortOrder=string, stateString=boolean, transmitFilters=boolean, unParent=boolean, unlockMainConnection=boolean, unpinPlug=name, updateMainConnection=boolean, useTemplate=string):
    """
    outlinerEditor is undoable, queryable, and editable.
    

    
This command creates an outliner editor which can be used to display a list of objects.
WARNING: some flag combinations may not behave as you expect. The command is really intended for internal use for creating the outliner used by the various editors.

    """
    pass
    


def outlinerPanel( panelName , control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, outlinerEditor=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    outlinerPanel is undoable, queryable, and editable.
    

    
This command creates, edit and queries outliner panels which contain only an outliner editor.

    """
    pass
    


def overrideModifier(clear=boolean, press=string, release=string):
    """
    overrideModifier is undoable, NOT queryable, and NOT editable.
    

    
This command allows you to assign modifier key behaviour to other parts of the system. For example you can use a hotkey or input device instead of a modifer key to perform the same action.
Note that the original modifier key behaviour is not altered in anyway. For example, if you've assigned "Ctrl" key behaviour to the "c" key then the "Ctrl" key will still work as you expect, all you've done is allowed yourself to use the "c" key as an alternative to the "Ctrl" key.

    """
    pass
    


def paintEffectsDisplay(meshDrawEnable=boolean):
    """
    paintEffectsDisplay is NOT undoable, queryable, and NOT editable.
    

    
Command to set the global display methods for paint effects items

    """
    pass
    


def pairBlend(attribute=string, input1=boolean, input2=boolean, node=string):
    """
    pairBlend is undoable, queryable, and editable.
    

    
The pairBlend node allows a weighted combinations of 2 inputs to be blended together. It is created automatically when keying or constraining an attribute which is already connected.
Alternatively, the pairBlend command can be used to connect a pairBlend node to connected attributes of a node. The previously existing connections are rewired to input1 of the pairBlend node. Additional connections can then be made manually to input2 of the pairBlend node.
The pairBlend command can also be used to query the inputs to an existing pairBlend node.

    """
    pass
    


def palettePort( string , actualTotal=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, colorEditable=boolean, colorEdited=script, defineTemplate=string, dimensions=int, int, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, hsvValue=int, int, float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, redraw=boolean, rgbValue=int, float, float, float, setCurCell=int, topDown=boolean, transparent=int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    palettePort is undoable, queryable, and editable.
    

    
This command creates an array of color cells. It could be used to to store an retrieve some colors you want to manage during your working session.

    """
    pass
    


def panel( string , control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    panel is undoable, queryable, and editable.
    

    
This command allows editing or querying properties of any panels. Not all of the common properites of panels can be used with this command. Flags such as -tearOff and -replacePanel require that you use the explicit panel command. The command 'getPanel -typeOf panelName' will return the explicit type of a panel.

    """
    pass
    


def paneLayout( string , activeFrameThickness=int, activePane=string, activePaneIndex=int, annotation=string, backgroundColor=float, float, float, childArray=boolean, configuration=string, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, numberOfVisiblePanes=boolean, pane1=boolean, pane2=boolean, pane3=boolean, pane4=boolean, paneSize=int, int, int, paneUnderPointer=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, separatorMovedCommand=script, separatorThickness=int, setPane=string, int, staticHeightPane=int, staticWidthPane=int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    paneLayout is undoable, queryable, and editable.
    

    
This command creates a pane layout. A pane layout may have any number of children but at any one time only certain children may be visible, as determined by the current layout configuration. For example a horizontally split pane shows only two children, one on top of the other and a visible separator between the two. The separator may be moved to vary the size of each pane. Various other pane configurations are available and all display a moveable separator that define the size of each pane in the layout.

    """
    pass
    


def panelConfiguration( name , addPanel=boolean, string, string, string, string, configString=string, createStrings=boolean, defaultImage=string, defineTemplate=string, editStrings=boolean, exists=boolean, image=string, isFixedState=boolean, label=string, labelStrings=boolean, numberOfPanels=boolean, removeAllPanels=boolean, removeLastPanel=boolean, replaceCreateString=int, string, replaceEditString=int, string, replaceFixedState=int, boolean, replaceLabel=int, string, replacePanel=int, boolean, string, string, string, string, replaceTypeString=int, string, sceneConfig=boolean, typeStrings=boolean, useTemplate=string):
    """
    panelConfiguration is undoable, queryable, and editable.
    

    
This command creates a panel configuration object. Typically you would not call this method command directly. Instead use the Panel Editor.
Once a panel configuration is created you can make it appear in the main Maya window by selecting it from any panel's "Panels->Saved Layouts" menu.

    """
    pass
    


def panelHistory( name , back=boolean, clear=boolean, defineTemplate=string, exists=boolean, forward=boolean, historyDepth=int, isEmpty=boolean, suspend=boolean, targetPane=string, useTemplate=string, wrap=boolean):
    """
    panelHistory is undoable, queryable, and editable.
    

    
This command creates a panel history object. The object is targeted on a particular paneLayout and thereafter notes changes in panel configurations within that paneLayout, building up a history list. The list can be stepped through backwards or forwards.

    """
    pass
    


def panZoom( camera , absolute=boolean, downDistance=linear, leftDistance=linear, relative=boolean, rightDistance=linear, upDistance=linear, zoomRatio=float):
    """
    panZoom is undoable, NOT queryable, and NOT editable.
    

    
The panZoom command pans/zooms the 2D film.
The panZoom command can be applied to either a perspective or an orthographic camera.
When no camera name is supplied, this command is applied to the camera in the active view.

    """
    pass
    


def panZoomCtx(alternateContext=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, panMode=boolean, toolName=string, zoomMode=boolean, zoomScale=float):
    """
    panZoomCtx is undoable, queryable, and editable.
    

    
This command can be used to create camera 2D pan/zoom context.

    """
    pass
    


def paramDimContext(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    paramDimContext is undoable, queryable, and editable.
    

    
Command used to register the paramDimCtx tool.

    """
    pass
    


def paramDimension( curve|surface ):
    """
    paramDimension is undoable, NOT queryable, and NOT editable.
    

    
This command is used to create a param dimension to display the parameter value of a curve/surface at a specified point on the curve/surface.

    """
    pass
    


def paramLocator( object , position=boolean):
    """
    paramLocator is undoable, queryable, and editable.
    

    
The command creates a locator in the underworld of a NURBS curve or NURBS surface at the specified parameter value. If no object is specified, then a locator will be created on the first valid selected item (either a curve point or a surface point).

    """
    pass
    


def parent( dagObject... dagObject , absolute=boolean, addObject=boolean, noConnections=boolean, noInvScale=boolean, relative=boolean, removeObject=boolean, shape=boolean, world=boolean):
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
    


def parentConstraint( target ... object , createCache=float, float, decompRotationToChild=boolean, deleteCache=boolean, layer=string, maintainOffset=boolean, name=string, remove=boolean, skipRotate=string, skipTranslate=string, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    parentConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s). In the case of multiple targets, the overall position and rotation of the constrained object is the weighted average of each target's contribution to the position and rotation of the object.
A parentConstraint takes as input one or more "target" DAG transform nodes at which to position and rotate the single "constraint object" DAG transform node. The parentConstraint positions and rotates the constrained object at the weighted average of the world space position, rotation and scale target objects.

    """
    pass
    


def particle( object , attribute=string, cache=boolean, conserve=float, count=boolean, deleteCache=boolean, dynamicAttrList=boolean, floatValue=float, gridSpacing=linear, inherit=float, jitterBasePoint=linear, linear, linear, jitterRadius=linear, lowerLeft=linear, linear, linear, name=string, numJitters=uint, order=int, particleId=int, perParticleDouble=boolean, perParticleVector=boolean, position=linear, linear, linear, shapeName=string, upperRight=linear, linear, linear, vectorValue=float, float, float):
    """
    particle is undoable, queryable, and editable.
    

    
The particle command creates a new particle object from a list of world space points. If a particle object is created, the command returns the names of the new particle shape and its associated particle object dependency node. If an object was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.

    """
    pass
    


def particleExists( string ):
    """
    particleExists is undoable, NOT queryable, and NOT editable.
    

    
This command is used to query if a particle or soft object with the given name exists. Either the transform or shape name can be used as well as the name of the soft object.

    """
    pass
    


def particleFill(closePacking=boolean, doubleWalled=boolean, maxX=float, maxY=float, maxZ=float, minX=float, minY=float, minZ=float, particleDensity=float, resolution=int):
    """
    particleFill is NOT undoable, NOT queryable, and NOT editable.
    

    
This command generates an nParticle system that fills the selected object with a grid of particles.

    """
    pass
    


def particleInstancer(addObject=boolean, aimAxis=string, aimDirection=string, aimPosition=string, aimUpAxis=string, aimWorldUp=string, attributeMapping=boolean, cycle=string, cycleStartObject=string, cycleStep=float, cycleStepUnits=string, index=int, instanceId=string, levelOfDetail=string, name=string, object=string, objectIndex=string, particleAge=string, position=string, removeObject=boolean, rotation=string, rotationOrder=string, rotationType=string, rotationUnits=string, scale=string, shear=string, visibility=string):
    """
    particleInstancer is undoable, queryable, and editable.
    

    
This command is used to create a particle instancer node and set the proper attributes in the particle shape and in the instancer node. It will also create the connections needed between the particle shape and the instancer node.

    """
    pass
    


def particleRenderInfo(attrList=int, attrListAll=boolean, name=int, renderTypeCount=boolean):
    """
    particleRenderInfo is undoable, queryable, and NOT editable.
    

    
This action provides information access to the particle render subclasses. These are derived from TdynRenderBase. This action is used primarily by the Attribute Editor to gather information about attributes used for rendering.

    """
    pass
    


def partition( string string... , addSet=name, name=string, removeSet=name, render=boolean):
    """
    partition is undoable, queryable, and editable.
    

    
This command is used to create, query or add/remove sets to a partition. If a partition name needs to be specified, it is the first argument, other arguments represent the set names.
Without any flags, the command will create a partition with a default name. Any sets which are arguments to the command will be added to the partition.
A set can be added to a partition only if none of its members are in any of the other sets in the partition. If the -re/render flag is specified when the partition is created, only 'renderable' sets can be added to the partition.
Sets can be added and removed from a partition by using the -addSet or -removeSet flags.
Note: If a set is already selected, and the partition command is executed, the set will be added to the created partition.

    """
    pass
    


def pasteKey( objects , animLayer=string, animation=string, attribute=string, clipboard=string, connect=boolean, copies=uint, float=floatrange, floatOffset=float, includeUpperBound=boolean, index=uint, matchByName=boolean, option=string, time=timerange, timeOffset=time, valueOffset=float):
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
    


def pathAnimation( objects , bank=boolean, bankScale=float, bankThreshold=angle, curve=string, endTimeU=time, endU=float, follow=boolean, followAxis=string, fractionMode=boolean, inverseFront=boolean, inverseUp=boolean, name=string, startTimeU=time, startU=float, upAxis=string, useNormal=boolean, worldUpObject=name, worldUpType=string, worldUpVector=float, float, float):
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
    


def perCameraVisibility(camera=name, exclusive=boolean, hide=boolean, remove=boolean, removeAll=boolean, removeCamera=boolean):
    """
    perCameraVisibility is NOT undoable, queryable, and NOT editable.
    

    
The perCameraVisibility command creates, queries and removes visibility relationships between DAG objects and cameras. These relationships are applied in any viewport that uses the cameras involved. (They are not used e.g. in rendering.) Objects can be set to be exclusive to a camera (meaning they will only be displayed in viewports using that camera; they will be hidden in other viewports) or hidden from a camera (meaning they will be not visible in any viewport using the camera).

    """
    pass
    


def percent( node objects , addPercent=boolean, dropoffAxis=linear, linear, linear, dropoffCurve=string, dropoffDistance=linear, dropoffPosition=linear, linear, linear, dropoffType=string, multiplyPercent=boolean, value=float):
    """
    percent is undoable, queryable, and NOT editable.
    

    
This command sets percent values on members of a weighted node such as a cluster or a jointCluster. With no flags specified the command sets the percent value for selected components of the specified node to the specified percent value. A dropoff from the specified percent value to 0 can be specified from a point, plane or curve using a dropoff distance around that shape. The percent value can also be added or multiplied with existing percent values of the node components.

    """
    pass
    


def performanceOptions(clusterResolution=float, disableStitch=string, disableTrimDisplay=string, latticeResolution=float, passThroughBindSkinAndFlexors=string, passThroughBlendShape=string, passThroughCluster=string, passThroughDeltaMush=string, passThroughFlexors=string, passThroughLattice=string, passThroughPaintEffects=string, passThroughSculpt=string, passThroughWire=string, skipHierarchyTraversal=boolean, useClusterResolution=string, useLatticeResolution=string):
    """
    performanceOptions is undoable, queryable, and NOT editable.
    

    
Sets the global performance options for the application. The options allow the disabling of features such as stitch surfaces or deformers to cut down on computation time in the scene.
Performance options that are in effect may be on all the time, or they can be turned on only for interaction. In the latter case, the options will only take effect during UI interaction or playback.
Note that none of these performance options will affect rendering.

    """
    pass
    


def pfxstrokes(filename=string, postCallback=boolean, selected=boolean):
    """
    pfxstrokes is NOT undoable, NOT queryable, and NOT editable.
    

    
This command will loop through all the Paint Effects strokes, including pfxHair nodes, and write the current state of all the tubes to a file. For normal stroke nodes tubes must be ON in the brush or there will be no output. For pfxHair nodes there will always be output, but the format is different than for stroke nodes(however one can assign a brush with tubes = ON to a pfxHair node, in which case it will output the same format as strokes). The general file format is ASCII, using commas to separate numerical values and newlines between blocks of data. The format used for pfxHair nodes presents the hair curves points in order from root to tip of the hair. The hairs follow sequentially in the following fashion: NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc... NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc.. The format used to output files for brushes with tubes=ON is more complex. The tubes can branch and the order the segments are written is the same order they are drawn in. Slowly drawing a tall grass brush in the paint effects panel can help to illustrate the order the segments will appear in the file. New tubes can start "growing" before others are finished. There is no line for "NumCvs". Instead all data for each segment appears on each line. The data on each line is the same as passed into the paint effects runtime function. See the argument list of paintRuntimeFunc.mel for the order and a description of these parameters. The parameters match up exactly in the order they appear on a line of the output file with the order of arguments to this function. If one wishes to parse the output file and connect the segments together into curves the branchId, parentId and siblingCnt parameters can help when sorting which segment connects to which line. Using the -postCallback option will write out the tubes data after it has been proessed by the runTime callback.

    """
    pass
    


def pickWalk( objects , direction=string, type=string):
    """
    pickWalk is undoable, NOT queryable, and NOT editable.
    

    
The pickWalk command allows you to quickly change the selection list relative to the nodes that are currently selected. It is called pickWalk, because it walks from one selection list to another by unselecting what's currently selected, and selecting nodes that are in the specified direction from the currently selected list. If you specify objects on the command line, the pickWalk command will walk from those objects instead of the selected list.
If the -type flag is instances, then the left and right direction will walk to the previous or next instance of the same selected dag node.

    """
    pass
    


def picture( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, tile=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    picture is undoable, queryable, and editable.
    

    
This command creates a static image.

    """
    pass
    


def pixelMove( float float ):
    """
    pixelMove is undoable, NOT queryable, and NOT editable.
    

    
The pixelMove command moves objects by what appears as pixel units based on the current view. It takes two integer arguments which specify the direction in screen space an object should appear to move. The vector between the center pixel of the view and the specified offset is mapped to some world space vector which defines the relative amount to move the selected objects. The mapping is dependent upon the view.

    """
    pass
    


def planarSrf( objects , caching=boolean, constructionHistory=boolean, degree=int, keepOutside=boolean, name=string, nodeState=int, object=boolean, polygon=int, range=boolean, tolerance=linear):
    """
    planarSrf is undoable, queryable, and editable.
    

    
This command computes a planar trimmed surface given planar boundary curves that form a closed region.

    """
    pass
    


def plane(length=linear, name=string, position=linear, linear, linear, rotation=angle, angle, angle, size=linear, width=linear):
    """
    plane is undoable, NOT queryable, and NOT editable.
    

    
The command creates a sketch plane (also known as a "construction plane") in space. To create an object (such as a NURBS curve, joint chain or polygon) on a construction plane, you need to first make the plane live. See also the makeLive command.

    """
    pass
    


def play(forward=boolean, playSound=boolean, record=boolean, sound=string, state=boolean, wait=boolean):
    """
    play is undoable, queryable, and NOT editable.
    

    
This command starts and stops playback. In order to change the frame range of playback, see the playbackOptions command.

    """
    pass
    


def playbackOptions(animationEndTime=time, animationStartTime=time, blockingAnim=boolean, by=float, framesPerSecond=boolean, loop=string, maxPlaybackSpeed=float, maxTime=time, minTime=time, playbackSpeed=float, view=string):
    """
    playbackOptions is undoable, queryable, and editable.
    

    
This command sets/queries certain values associated with playback: looping style, start/end times, etc. Only commands modifying the -minTime/maxTime, the -animationStartTime/animationEndTime, or the -by value are undoable.

    """
    pass
    


def playblast( filename , activeEditor=boolean, cameraSetup=string, string, clearCache=boolean, codecOptions=boolean, combineSound=boolean, completeFilename=string, compression=string, editorPanelName=string, endTime=time, filename=string, forceOverwrite=boolean, format=string, frame=time, framePadding=int, height=int, indexFromZero=boolean, offScreen=boolean, options=boolean, percent=int, quality=int, rawFrameNumbers=boolean, replaceAudioOnly=boolean, replaceEndTime=time, replaceFilename=boolean, replaceStartTime=time, sequenceTime=boolean, showOrnaments=boolean, sound=string, startTime=time, viewer=boolean, width=int, widthHeight=int, int):
    """
    playblast is undoable, NOT queryable, and NOT editable.
    

    
This command playblasts the current playback range. Sound is optional.
Note that the playblast command registers a condition called "playblasting" so that users can monitor whether playblasting is occurring. You may monitor the condition using the API (MConditionMessage) or a script (scriptJob and condition commands).

    """
    pass
    


def pluginDisplayFilter(classification=string, deregister=boolean, exists=string, label=string, listFilters=boolean, register=boolean):
    """
    pluginDisplayFilter is NOT undoable, queryable, and NOT editable.
    

    
Register, deregister or query a plugin display filter. Plug-ins can use this command to register their own display filters which will appear in the 'Show' menus on Maya's model panels.

    """
    pass
    


def pluginInfo( string , activeFile=boolean, animCurveInterp=string, apiVersion=boolean, autoload=boolean, cacheFormat=boolean, changedCommand=script, command=string, constraintCommand=string, controlCommand=string, data=string, string, dependNode=boolean, dependNodeByType=string, dependNodeId=string, device=boolean, dragAndDropBehavior=boolean, iksolver=boolean, listPlugins=boolean, listPluginsPath=boolean, loadPluginPrefs=boolean, loaded=boolean, modelEditorCommand=string, name=string, path=string, pluginsInUse=boolean, registered=boolean, remove=boolean, renderer=boolean, savePluginPrefs=boolean, serviceDescriptions=boolean, settings=boolean, tool=string, translator=boolean, unloadOk=boolean, userNamed=boolean, vendor=string, version=boolean, writeRequires=boolean):
    """
    pluginInfo is undoable, queryable, and editable.
    

    
This command provides access to the plug-in registry of the application. It is used mainly to query the characteristics of registered plug-ins. Plugins automatically become registered the first time that they are loaded.
The argument is either the internal name of the plug-in or the path to access it.

    """
    pass
    


def pointConstraint( target... object , layer=string, maintainOffset=boolean, name=string, offset=float, float, float, remove=boolean, skip=string, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    pointConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position to the position of the target object or to the average position of a number of targets.
A pointConstraint takes as input one or more "target" DAG transform nodes at which to position the single "constraint object" DAG transform node. The pointConstraint positions the constrained object at the weighted average of the world space position target objects.

    """
    pass
    


def pointCurveConstraint( selectionItem , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, pointConstraintUVW=float, float, float, pointWeight=float, position=float, float, float, replaceOriginal=boolean, weight=float):
    """
    pointCurveConstraint is undoable, queryable, and editable.
    

    
The command enables direct manipulation of a NURBS curve. It does so by apply a position constraint at the specified parameter location on the NURBS curve.
If construction history for the cmd is enabled, a locator is created to enable subsequent interactive manipulation of the curve. The locator position may be key framed or transformed and the "curve1" will try to match the position of the locator.
The argument is a curve location

    """
    pass
    


def pointLight(decayRate=int, discRadius=linear, exclusive=boolean, intensity=float, name=string, position=linear, linear, linear, rgb=float, float, float, rotation=angle, angle, angle, shadowColor=float, float, float, shadowDither=float, shadowSamples=int, softShadow=boolean, useRayTraceShadows=boolean):
    """
    pointLight is undoable, queryable, and editable.
    

    
The pointLight command is used to edit the parameters of existing pointLights, or to create new ones. The default behaviour is to create a new pointlight.

    """
    pass
    


def pointOnCurve( objects , constructionHistory=boolean, curvatureCenter=boolean, curvatureRadius=boolean, normal=boolean, normalizedNormal=boolean, normalizedTangent=boolean, parameter=float, position=boolean, tangent=boolean, turnOnPercentage=boolean):
    """
    pointOnCurve is undoable, queryable, and editable.
    

    
This command returns information for a point on a NURBS curve. If no flag is specified, it assumes p/position by default.

    """
    pass
    


def pointOnPolyConstraint( target... object , layer=string, maintainOffset=boolean, name=string, offset=float, float, float, remove=boolean, skip=string, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    pointOnPolyConstraint is undoable, queryable, and editable.
    

    
Constrain an object's position to the position of the target object or to the average position of a number of targets.
A pointOnPolyConstraint takes as input one or more "target" DAG transform nodes at which to position the single "constraint object" DAG transform node. The pointOnPolyConstraint positions the constrained object at the weighted average of the world space position target objects.

    """
    pass
    


def pointOnSurface( objects , constructionHistory=boolean, normal=boolean, normalizedNormal=boolean, normalizedTangentU=boolean, normalizedTangentV=boolean, parameterU=float, parameterV=float, position=boolean, tangentU=boolean, tangentV=boolean, turnOnPercentage=boolean):
    """
    pointOnSurface is undoable, queryable, and editable.
    

    
This command returns information for a point on a surface. If no flag is specified, this command assumes p/position by default. If more than one flag is specifed, then a string array is returned.

    """
    pass
    


def pointPosition( object , local=boolean, world=boolean):
    """
    pointPosition is undoable, NOT queryable, and NOT editable.
    

    
This command returns the world or local space position for any type of point object. Valid selection items are: - curve and surface CVs - poly vertices - lattice points - particles - curve and surface edit points - curve and surface parameter points - poly uvs - rotate/scale/joint pivots - selection handles - locators, param locators and arc length locators
It works on the selected object or you can specify the object in the command. By default, if no flag is specified then the world position is returned.

    """
    pass
    


def poleVectorConstraint( target ... object , layer=string, name=string, remove=boolean, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    poleVectorConstraint is undoable, queryable, and editable.
    

    
Constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number of targets.
An poleVectorConstraint takes as input one or more "target" DAG transform nodes at which to aim pole vector for an IK handle using the rotate plane solver. The pole vector is adjust such that the in weighted average of the world space position target objects lies is the "rotate plane" of the handle.

    """
    pass
    


def polyAppend(append=, float, float, float, , constructionHistory=boolean, edge=int, hole=boolean, name=string, point=float, float, float, subdivision=int, texture=int):
    """
    polyAppend is undoable, queryable, and editable.
    

    
Appends a new face to the selected polygonal object. The first argument must be a border edge. The new face will be automatically closed.
Only works with one object selected.

    """
    pass
    


def polyAppendFacetCtx(append=boolean, isRotateAvailable=boolean, maximumNumberOfPoints=int, planarConstraint=boolean, rotate=float, subdivision=int):
    """
    polyAppendFacetCtx is undoable, queryable, and editable.
    

    
Create a new context to append facets on polygonal objects

    """
    pass
    


def polyAppendVertex(append=, float, float, float, , constructionHistory=boolean, hole=boolean, name=string, point=float, float, float, texture=int, vertex=int):
    """
    polyAppendVertex is undoable, queryable, and editable.
    

    
Appends a new face to the selected polygonal object. The direction of the normal is given by the vertex order: the face normal points towards the user when the vertices rotate counter clockwise. Note that holes must be described in the opposite direction.
Only works with one object selected.

    """
    pass
    


def polyAutoProjection(caching=boolean, constructionHistory=boolean, createNewMap=boolean, insertBeforeDeformers=boolean, layout=int, layoutMethod=int, name=string, nodeState=int, optimize=int, percentageSpace=float, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, planes=int, projectBothDirections=boolean, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleMode=int, scaleX=float, scaleY=float, scaleZ=float, skipIntersect=boolean, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, uvSetName=string, worldSpace=boolean):
    """
    polyAutoProjection is undoable, queryable, and editable.
    

    
Projects a map onto an object, using several orthogonal projections simultaneously.

    """
    pass
    


def polyAverageNormal(allowZeroNormal=boolean, distance=float, postnormalize=boolean, prenormalize=boolean, replaceNormalXYZ=float, float, float):
    """
    polyAverageNormal is undoable, NOT queryable, and NOT editable.
    

    
Set normals of vertices or vertex-faces to an average value when the vertices within a given threshold. First, it sorts out the containing edges, and set them to be soft, if it is possible, so to let the normals appear to be "merged". The remained components then are sorted into lumps where vertices in each lump are within the given threshold. For all vertices and vertex-faces, set their normals to the average normal in the lump. Selected vertices may or may not on the same object. If objects are selected, it is assumed that all vertices are selected. If edges or faces are selected, it is assumed that the related vertex-faces are selected.

    """
    pass
    


def polyAverageVertex( selectionList , caching=boolean, constructionHistory=boolean, iterations=int, name=string, nodeState=int, worldSpace=boolean):
    """
    polyAverageVertex is undoable, queryable, and editable.
    

    
Moves the selected vertices of a polygonal object to round its shape. Translate, move, rotate or scale vertices.

    """
    pass
    


def polyBevel(angleTolerance=float, autoFit=boolean, caching=boolean, constructionHistory=boolean, name=string, nodeState=int, offset=linear, offsetAsFraction=boolean, roundness=float, segments=int, worldSpace=boolean):
    """
    polyBevel is undoable, queryable, and editable.
    

    
Bevel edges.

    """
    pass
    


def polyBevel3(angleTolerance=float, autoFit=boolean, caching=boolean, constructionHistory=boolean, name=string, nodeState=int, offset=linear, offsetAsFraction=boolean, roundness=float, segments=int, worldSpace=boolean):
    """
    polyBevel3 is undoable, queryable, and editable.
    

    
Bevel edges.

    """
    pass
    


def polyBlendColor(baseColorName=string, blendFunc=int, blendWeightA=float, blendWeightB=float, blendWeightC=float, blendWeightD=float, caching=boolean, constructionHistory=boolean, dstColorName=string, name=string, nodeState=int, srcColorName=string):
    """
    polyBlendColor is undoable, queryable, and editable.
    

    
Takes two color sets and blends them together into a third specified color set.

    """
    pass
    


def polyBlindData(associationType=string, binaryData=string, booleanData=boolean, delete=boolean, doubleData=float, int64Data=int64, intData=int, longDataName=string, rescan=boolean, reset=boolean, shape=boolean, shortDataName=string, stringData=string, typeId=int):
    """
    polyBlindData is undoable, NOT queryable, and editable.
    

    
Command creates blindData types (basically creates an instance of TdnPolyBlindData). When used with the query flag, it returns the data types that define this blindData type. This command is to be used create a blindData node *and* to edit the same.. The associationType flag *has* to be specified at all times.. This is because if an instance of the specified BD typeId exists in the history chain but if the associationType is not the same, then a new polyBlindData node is created.. For object level blind data, only the object itself must be specified. A new compound attribute BlindDataNNNN will be created on the object. Blind data attribute names must be unique across types for object level blind data. So, the command will require the following to be specified: - typeId, - associationType - longDataName or shortDataName of data being edited. - The actual data being specified. - The components that this data is to be attached to.

    """
    pass
    


def polyBoolOp( poly poly , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, operation=int):
    """
    polyBoolOp is undoable, queryable, and editable.
    

    
This command creates a new poly as the result of a boolean operation on input polys : union, intersection, difference.
Only for difference, the order of the selected objects is important :
result = object1 - object2.
If no objects are specified in the command line, then the objects from the active list are used.

    """
    pass
    


def polyBridgeEdge(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, worldSpace=boolean):
    """
    polyBridgeEdge is undoable, queryable, and editable.
    

    
Bridges two sets of edges.

    """
    pass
    


def polyCacheMonitor(cacheValue=boolean, nodeName=string):
    """
    polyCacheMonitor is NOT undoable, NOT queryable, and NOT editable.
    

    
When the cacheInput attribute has a positive value the midModifier node caches the output mesh improving performance in computations of downstream nodes. When the counter has a zero value the midModifier releases the cached data.

    """
    pass
    


def polyCBoolOp( poly poly , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, operation=int):
    """
    polyCBoolOp is undoable, queryable, and editable.
    

    
This command creates a new poly as the result of a boolean operation on input polys : union, intersection, difference.
Only for difference, the order of the selected objects is important :
result = object1 - object2.
If no objects are specified in the command line, then the objects from the active list are used.

    """
    pass
    


def polyCheck( poly poly... , edge=boolean, face=boolean, openFile=string):
    """
    polyCheck is undoable, NOT queryable, and NOT editable.
    

    
Dumps a description of internal memory representation of poly objects.
If no objects are specified in the command line, the objects from the active list are used.
Default behaviour is to print only a summary. Use the flags above to get more details on a specific part of the object.

    """
    pass
    


def polyChipOff(attraction=float, caching=boolean, constructionHistory=boolean, duplicate=boolean, gravity=linear, linear, linear, gravityX=linear, gravityY=linear, gravityZ=linear, keepFacesTogether=boolean, localDirection=linear, linear, linear, localDirectionX=linear, localDirectionY=linear, localDirectionZ=linear, localRotate=angle, angle, angle, localRotateX=angle, localRotateY=angle, localRotateZ=angle, localScale=float, float, float, localScaleX=float, localScaleY=float, localScaleZ=float, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, magnX=linear, magnY=linear, magnZ=linear, magnet=linear, linear, linear, name=string, nodeState=int, offset=float, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, random=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleX=float, scaleY=float, scaleZ=float, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, weight=float, worldSpace=boolean):
    """
    polyChipOff is undoable, queryable, and editable.
    

    
Extract facets. Faces can be extracted separately or together, and manipulations can be performed either in world or object space.

    """
    pass
    


def polyClean(caching=boolean, cleanEdges=boolean, cleanPartialUVMapping=boolean, cleanVertices=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyClean is undoable, queryable, and editable.
    

    
polyClean will attempt to remove components that are invalid in the description of a poly mesh.

    """
    pass
    


def polyClipboard(clear=boolean, color=boolean, copy=boolean, paste=boolean, shader=boolean, uvCoordinates=boolean):
    """
    polyClipboard is undoable, NOT queryable, and NOT editable.
    

    
The command allows the user to copy and paste certain polygonal attributes to a clipboard. These attributes are: 1) Shader (shading engine) assignment. 2) Texture coordinate (UV) assignment. 3) Color value assignment. Any combination of attributes can be chosen for the copy or paste operation. If the attribute has not been copied to the clipboard, then naturally it cannot be pasted from the clipboard. The copy option will copy the attribute assignments from a single source polygonal dag object or polygon component. If the source does not have the either UV or color attributes, then nothing will be copied to the clipboard. The paste option will paste the attribute assignments to one or more polygon components or polygonal dag objects. If the destination does not have either UV or color attributes, then new values will be assigned as needed. Additionally, there is the option to clear the clipboard contents

    """
    pass
    


def polyCloseBorder(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyCloseBorder is undoable, queryable, and editable.
    

    
Closes open borders of objects. For each border edge given, a face is created to fill the hole the edge lies on.

    """
    pass
    


def polyCollapseEdge(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyCollapseEdge is undoable, queryable, and editable.
    

    
Turns each selected edge into a point.

    """
    pass
    


def polyCollapseFacet(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyCollapseFacet is undoable, queryable, and editable.
    

    
Turns each selected facet into a point.

    """
    pass
    


def polyCollapseTweaks(hasVertexTweaks=boolean):
    """
    polyCollapseTweaks is undoable, queryable, and NOT editable.
    

    
A command that updates a mesh's vertex tweaks by applying its tweak data (stored on the mesh node) onto its respective vertex data.
This command is only useful in cases where no construction history is associated with the shape node.
If a mesh name is not specified as input, a singly selected mesh (if any) will have its tweaked vertices baked.

    """
    pass
    


def polyColorBlindData(aboveMaxColorBlue=float, aboveMaxColorGreen=float, aboveMaxColorRed=float, attrName=string, belowMinColorBlue=float, belowMinColorGreen=float, belowMinColorRed=float, clashColorBlue=float, clashColorGreen=float, clashColorRed=float, colorBlue=float, colorGreen=float, colorRed=float, dataType=string, enableFalseColor=boolean, maxColorBlue=float, maxColorGreen=float, maxColorRed=float, maxValue=float, minColorBlue=float, minColorGreen=float, minColorRed=float, minValue=float, mode=int, noColorBlue=float, noColorGreen=float, noColorRed=float, numIdTypes=int, queryMode=boolean, typeId=int, useMax=boolean, useMin=boolean, value=string):
    """
    polyColorBlindData is NOT undoable, NOT queryable, and NOT editable.
    

    
This command applies false color to the selected polygonal components and objects, depending on whether or not blind data exists for the selected components (or, in the case of poly objects, dynamic attributes), and, depending on the color mode indicated, what the values are. It is possible to color objects based on whether or not the data exists, if the data matches a specific value or range of values, or grayscale color the data according to what the actual value is in relation to the specified min and max. This command also has a query mode in which the components and/or objects are returned in a string array to allow for selection filtering.

    """
    pass
    


def polyColorDel(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyColorDel is undoable, queryable, and editable.
    

    
Deletes color from selected components.

    """
    pass
    


def polyColorMod(baseColorName=string, caching=boolean, constructionHistory=boolean, huev=float, name=string, nodeState=int, satv=float, value=float):
    """
    polyColorMod is undoable, queryable, and editable.
    

    
Modifies the attributes of a poly color set.

    """
    pass
    


def polyColorPerVertex(alpha=float, clamped=boolean, colorB=float, colorDisplayOption=boolean, colorG=float, colorR=float, colorRGB=float, float, float, notUndoable=boolean, relative=boolean, remove=boolean, representation=int):
    """
    polyColorPerVertex is undoable, queryable, and editable.
    

    
Command associates color(rgb and alpha) with vertices on polygonal objects. When used with the query flag, it returns the color associated with the specified components.

    """
    pass
    


def polyColorSet(allColorSets=boolean, clamped=boolean, colorSet=string, copy=boolean, create=boolean, currentColorSet=boolean, currentPerInstanceSet=boolean, delete=boolean, newColorSet=string, perInstance=boolean, rename=boolean, representation=string, shareInstances=boolean, unshared=boolean):
    """
    polyColorSet is undoable, queryable, and editable.
    

    
Command to do the following to color sets: - delete an existing color set. - rename an existing color set. - create a new empty color set. - set the current color set to a pre-existing color set. - modify sharing between instances of per-instance color sets - query the current color set. - query the names of all color sets. - query the name(s) along with representation value(s) or clamped value(s) of all color sets - query the representation value or clamped value of the current color set

    """
    pass
    


def polyCompare( poly poly , colorSetIndices=boolean, colorSets=boolean, edges=boolean, faceDesc=boolean, userNormals=boolean, uvSetIndices=boolean, uvSets=boolean, vertices=boolean):
    """
    polyCompare is undoable, NOT queryable, and NOT editable.
    

    
Compares two Polygonal Geometry objects with a fine control on what to compare.
If no objects are specified in the command line, then the objects from the active list are used.
Default behaviour is to compare all flags.
Use MEL script polyCompareTwoObjects.mel to get formatted output from this command.

    """
    pass
    


def polyCone(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, height=linear, name=string, radius=linear, subdivisionsX=int, subdivisionsY=int, subdivisionsZ=int, texture=boolean):
    """
    polyCone is undoable, queryable, and editable.
    

    
The cone command creates a new polygonal cone.

    """
    pass
    


def polyConnectComponents(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyConnectComponents is undoable, queryable, and editable.
    

    
Splits polygon edges according to the selected components. The selected components are gathered into connected 'paths' that define continuous splits. Mixed components (vertices, edges and faces) can be used at once. The connection rules are: * Edges can connect to other edges in the same face or to vertices in the same face (that are not in the edge itself) or to faces connected to other edges in the same face. * Vertices can connect to edges (as above) or to vertices in the same face (that are not joined to the first vertex by an edge) or to faces adjacent to a face that uses the vertex (except those that also use the vertex). * Faces can connect to vertices or edges (as above) or to adjacent faces.

    """
    pass
    


def polyContourProjection(caching=boolean, constructionHistory=boolean, createNewMap=boolean, flipRails=boolean, insertBeforeDeformers=boolean, method=int, name=string, nodeState=int, offset0=linear, offset1=linear, offset2=linear, offset3=linear, reduceShear=float, smoothness0=float, smoothness1=float, smoothness2=float, smoothness3=float, userDefinedCorners=boolean, worldSpace=boolean):
    """
    polyContourProjection is undoable, queryable, and editable.
    

    
Performs a contour stretch UV projection onto an object.

    """
    pass
    


def polyCopyUV( selectionList , caching=boolean, constructionHistory=boolean, createNewMap=boolean, name=string, nodeState=int, uvSetName=string, uvSetNameInput=string):
    """
    polyCopyUV is undoable, queryable, and editable.
    

    
Copy some UVs from a UV set into another.

    """
    pass
    


def polyCrease(createHistory=boolean, operation=uint, relativeValue=float, value=float, vertexValue=float):
    """
    polyCrease is undoable, queryable, and editable.
    

    
Command to set the crease values on the edges or vertices of a poly. The crease values are used by the smoothing algorithm.

    """
    pass
    


def polyCreaseCtx(createSet=string, extendSelection=boolean, relative=boolean):
    """
    polyCreaseCtx is undoable, queryable, and editable.
    

    
Create a new context to crease components on polygonal objects

    """
    pass
    


def polyCreateFacet(constructionHistory=boolean, hole=boolean, name=string, point=, float, float, float, , subdivision=int, texture=int):
    """
    polyCreateFacet is undoable, queryable, and editable.
    

    
Create a new polygonal object with the specified face, which will be closed. List of arguments must have at least 3 points.

    """
    pass
    


def polyCreateFacetCtx(append=boolean, maximumNumberOfPoints=int, planarConstraint=boolean, subdivision=int):
    """
    polyCreateFacetCtx is undoable, queryable, and editable.
    

    
Create a new context to create polygonal objects

    """
    pass
    


def polyCube(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, depth=linear, height=linear, name=string, subdivisionsX=int, subdivisionsY=int, subdivisionsZ=int, texture=int, width=linear):
    """
    polyCube is undoable, queryable, and editable.
    

    
The cube command creates a new polygonal cube.

    """
    pass
    


def polyCut(caching=boolean, constructionHistory=boolean, cutPlaneCenter=linear, linear, linear, cutPlaneCenterX=linear, cutPlaneCenterY=linear, cutPlaneCenterZ=linear, cutPlaneHeight=linear, cutPlaneRotate=angle, angle, angle, cutPlaneRotateX=angle, cutPlaneRotateY=angle, cutPlaneRotateZ=angle, cutPlaneSize=linear, linear, cutPlaneWidth=linear, cuttingDirection=string, deleteFaces=boolean, extractFaces=boolean, extractOffset=linear, linear, linear, extractOffsetX=linear, extractOffsetY=linear, extractOffsetZ=linear, name=string, nodeState=int, worldSpace=boolean):
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
    


def polyCylinder(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, height=linear, name=string, radius=linear, subdivisionsX=int, subdivisionsY=int, subdivisionsZ=int, texture=int):
    """
    polyCylinder is undoable, queryable, and editable.
    

    
The cylinder command creates a new polygonal cylinder.

    """
    pass
    


def polyCylindricalProjection(caching=boolean, constructionHistory=boolean, createNewMap=boolean, imageCenter=float, float, imageCenterX=float, imageCenterY=float, imageScale=float, float, imageScaleU=float, imageScaleV=float, insertBeforeDeformers=boolean, name=string, nodeState=int, projectionCenter=linear, linear, linear, projectionCenterX=linear, projectionCenterY=linear, projectionCenterZ=linear, projectionScale=float, float, projectionScaleU=float, projectionScaleV=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, rotationAngle=angle, seamCorrect=boolean, smartFit=boolean, worldSpace=boolean):
    """
    polyCylindricalProjection is undoable, queryable, and editable.
    

    
Projects a cylindrical map onto an object.

    """
    pass
    


def polyDelEdge(caching=boolean, cleanVertices=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyDelEdge is undoable, queryable, and editable.
    

    
Deletes selected edges, and merges neighboring faces. If deletion leaves winged vertices, they may be deleted as well.
Notice : only non border edges can be deleted.

    """
    pass
    


def polyDelFacet(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyDelFacet is undoable, queryable, and editable.
    

    
Deletes faces. If the result is split into disconnected pieces, the pieces (so-called shells) are still considered to be one object.
Notice : The last face cannot be deleted.

    """
    pass
    


def polyDelVertex(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyDelVertex is undoable, queryable, and editable.
    

    
Deletes vertices. Joins two edges which have a common vertex. The vertices must be connected to exactly two edges (so-called "winged").

    """
    pass
    


def polyDuplicateAndConnect( object , removeOriginalFromShaders=boolean, renameChildren=boolean):
    """
    polyDuplicateAndConnect is undoable, NOT queryable, and NOT editable.
    

    
This command duplicates the input polygonal object, connects up the outMesh attribute of the original polygonal shape to the inMesh attribute of the newly created duplicate shape and copies over the shader assignments from the original shape to the new duplicated shape.
The command will fail if no objects are selected or sent as argument or if the object sent as argument is not a polygonal object.

    """
    pass
    


def polyDuplicateEdge(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, offset=float, smoothingAngle=angle, splitType=int):
    """
    polyDuplicateEdge is undoable, queryable, and editable.
    

    
Duplicates a series of connected edges (edgeLoop)

    """
    pass
    


def polyEditEdgeFlow(adjustEdgeFlow=float, caching=boolean, constructionHistory=boolean, edgeFlow=boolean, name=string, nodeState=int):
    """
    polyEditEdgeFlow is undoable, queryable, and editable.
    

    
Edit edges of a polygonal object to respect surface curvature.

    """
    pass
    


def polyEditUV(angle=float, pivotU=float, pivotV=float, relative=boolean, rotation=boolean, scale=boolean, scaleU=float, scaleV=float, uValue=float, uvSetName=string, vValue=float):
    """
    polyEditUV is undoable, queryable, and NOT editable.
    

    
Command edits uvs on polygonal objects. When used with the query flag, it returns the uv values associated with the specified components.

    """
    pass
    


def polyEditUVShell(angle=float, pivotU=float, pivotV=float, relative=boolean, rotation=boolean, scale=boolean, scaleU=float, scaleV=float, uValue=float, uvSetName=string, vValue=float):
    """
    polyEditUVShell is undoable, queryable, and NOT editable.
    

    
Command edits uv shells on polygonal objects. When used with the query flag, it returns the transformation values associated with the specified components.

    """
    pass
    


def polyEvaluate( poly poly... , accurateEvaluation=boolean, area=boolean, boundingBox=boolean, boundingBox2d=boolean, boundingBoxComponent=boolean, boundingBoxComponent2d=boolean, displayStats=boolean, edge=boolean, edgeComponent=boolean, face=boolean, faceComponent=boolean, format=boolean, shell=boolean, triangle=boolean, triangleComponent=boolean, uvComponent=boolean, uvSetName=string, uvcoord=boolean, vertex=boolean, vertexComponent=boolean, worldArea=boolean):
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
    


def polyExtrudeEdge(caching=boolean, constructionHistory=boolean, divisions=int, inputCurve=name, keepFacesTogether=boolean, localDirection=linear, linear, linear, localDirectionX=linear, localDirectionY=linear, localDirectionZ=linear, localRotate=angle, angle, angle, localRotateX=angle, localRotateY=angle, localRotateZ=angle, localScale=float, float, float, localScaleX=float, localScaleY=float, localScaleZ=float, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, name=string, nodeState=int, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, random=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleX=float, scaleY=float, scaleZ=float, smoothingAngle=angle, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, worldSpace=boolean):
    """
    polyExtrudeEdge is undoable, queryable, and editable.
    

    
Extrude edges separately or together.

    """
    pass
    


def polyExtrudeFacet(attraction=float, caching=boolean, constructionHistory=boolean, divisions=int, gravity=linear, linear, linear, gravityX=linear, gravityY=linear, gravityZ=linear, inputCurve=name, keepFacesTogether=boolean, localDirection=linear, linear, linear, localDirectionX=linear, localDirectionY=linear, localDirectionZ=linear, localRotate=angle, angle, angle, localRotateX=angle, localRotateY=angle, localRotateZ=angle, localScale=float, float, float, localScaleX=float, localScaleY=float, localScaleZ=float, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, magnX=linear, magnY=linear, magnet=linear, linear, linear, name=string, nodeState=int, offset=float, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, random=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleX=float, scaleY=float, scaleZ=float, smoothingAngle=angle, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, weight=float, worldSpace=boolean):
    """
    polyExtrudeFacet is undoable, queryable, and editable.
    

    
Extrude faces. Faces can be extruded separately or together, and manipulations can be performed either in world or object space.

    """
    pass
    


def polyExtrudeVertex(caching=boolean, constructionHistory=boolean, divisions=int, length=float, name=string, nodeState=int, width=float, worldSpace=boolean):
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
    


def polyFlipUV(caching=boolean, constructionHistory=boolean, createNewMap=boolean, flipType=int, insertBeforeDeformers=boolean, local=boolean, name=string, nodeState=int, uvSetName=string):
    """
    polyFlipUV is undoable, queryable, and editable.
    

    
Flip (mirror) the UVs (in texture space) of input polyFaces, about either the U or V axis..

    """
    pass
    


def polyForceUV(cameraProjection=boolean, createNewMap=boolean, flipHorizontal=boolean, flipVertical=boolean, g=boolean, local=boolean, normalize=string, numItems=uint, preserveAspectRatio=boolean, unitize=boolean, unshare=boolean, uvSetName=string):
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
    


def polyGeoSampler(alphaBlend=string, averageColor=boolean, clampAlphaMax=float, clampAlphaMin=float, clampRGBMax=float, float, float, clampRGBMin=float, float, float, colorBlend=string, colorDisplayOption=boolean, computeShadows=boolean, displaceGeometry=boolean, flatShading=boolean, ignoreDoubleSided=boolean, lightingOnly=boolean, reuseShadows=boolean, sampleByFace=boolean, scaleFactor=float, shareUV=boolean, useLightShadows=boolean):
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
    


def polyHelix(axis=linear, linear, linear, coils=float, constructionHistory=boolean, createUVs=int, direction=int, height=linear, name=string, radius=linear, subdivisionsAxis=int, subdivisionsCaps=int, subdivisionsCoil=int, texture=int, width=linear):
    """
    polyHelix is undoable, queryable, and editable.
    

    
The polyHelix command creates a new polygonal helix.

    """
    pass
    


def polyHole(assignHole=boolean, createHistory=boolean):
    """
    polyHole is undoable, queryable, and editable.
    

    
Command to set and clear holes on given faces.

    """
    pass
    


def polyInfo(edgeToFace=boolean, edgeToVertex=boolean, faceNormals=boolean, faceToEdge=boolean, faceToVertex=boolean, invalidEdges=boolean, invalidVertices=boolean, laminaFaces=boolean, nonManifoldEdges=boolean, nonManifoldUVEdges=boolean, nonManifoldUVs=boolean, nonManifoldVertices=boolean, vertexToEdge=boolean, vertexToFace=boolean):
    """
    polyInfo is NOT undoable, NOT queryable, and NOT editable.
    

    
Command queries topological information on polygonal objects and components. So, the command will require the following to be specified: - selection list to query

    """
    pass
    


def polyInstallAction( name , commandName=boolean, convertSelection=boolean, installConstraint=boolean, installDisplay=boolean, keepInstances=boolean, uninstallConstraint=boolean, uninstallDisplay=boolean):
    """
    polyInstallAction is undoable, queryable, and NOT editable.
    

    
Installs/uninstalls several things to help the user to perform the specified action :
Pickmask
Internal selection constraints
Display attributes

    """
    pass
    


def polyLayoutUV(caching=boolean, constructionHistory=boolean, flipReversed=boolean, layout=int, layoutMethod=int, name=string, nodeState=int, percentageSpace=float, rotateForBestFit=int, scale=int, separate=int, uvSetName=string, worldSpace=boolean):
    """
    polyLayoutUV is undoable, queryable, and editable.
    

    
Move UVs in the texture plane to avoid overlaps.

    """
    pass
    


def polyListComponentConversion( selectionItem , border=boolean, fromEdge=boolean, fromFace=boolean, fromUV=boolean, fromVertex=boolean, fromVertexFace=boolean, internal=boolean, toEdge=boolean, toFace=boolean, toUV=boolean, toVertex=boolean, toVertexFace=boolean, vertexFaceAllEdges=boolean):
    """
    polyListComponentConversion is undoable, NOT queryable, and NOT editable.
    

    
This command converts poly components from one or more types to another one or more types, and returns the list of the conversion. It doesn't change anything of the current database.

    """
    pass
    


def polyMapCut(caching=boolean, constructionHistory=boolean, moveratio=float, name=string, nodeState=int):
    """
    polyMapCut is undoable, queryable, and editable.
    

    
Cut along edges of the texture mapping. The cut edges become map borders.

    """
    pass
    


def polyMapDel(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyMapDel is undoable, queryable, and editable.
    

    
Deletes texture coordinates (UVs) from selected faces.

    """
    pass
    


def polyMapSew(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyMapSew is undoable, queryable, and editable.
    

    
Sew border edges in texture space. Selected edges must be map borders.

    """
    pass
    


def polyMapSewMove(caching=boolean, constructionHistory=boolean, limitPieceSize=boolean, name=string, nodeState=int, numberFaces=int, uvSetName=string):
    """
    polyMapSewMove is undoable, queryable, and editable.
    

    
This command can be used to Move and Sew together separate UV pieces along geometric edges. UV pieces that correspond to the same geometric edge, are merged together by moving the smaller piece to the larger one.

    """
    pass
    


def polyMergeEdge(caching=boolean, constructionHistory=boolean, firstEdge=int, mergeMode=int, name=string, nodeState=int, secondEdge=int):
    """
    polyMergeEdge is undoable, queryable, and editable.
    

    
Sews two border edges together.
The new edge is located either on the first, last, or between both selected edges, depending on the mode.
Both edges must belong to the same object, and orientations must match (i.e. normals on corresponding faces must point in the same direction).
Edge flags are mandatory.

    """
    pass
    


def polyMergeEdgeCtx(activeNodes=boolean, exists=boolean, image1=string, image2=string, image3=string, immediate=boolean, mergeMode=int, name=string, previous=boolean, reset=boolean, toolNode=boolean):
    """
    polyMergeEdgeCtx is undoable, queryable, and editable.
    

    
Create a new context to merge edges on polygonal objects

    """
    pass
    


def polyMergeFacet(caching=boolean, constructionHistory=boolean, firstFacet=int, mergeMode=int, name=string, nodeState=int, secondFacet=int):
    """
    polyMergeFacet is undoable, queryable, and editable.
    

    
The second face becomes a hole in the first face.
The new holed face is located either on the first, last, or between both selected faces, depending on the mode.
Both faces must belong to the same object.
Facet flags are mandatory.

    """
    pass
    


def polyMergeFacetCtx(activeNodes=boolean, exists=boolean, image1=string, image2=string, image3=string, immediate=boolean, mergeMode=int, name=string, previous=boolean, reset=boolean, toolNode=boolean):
    """
    polyMergeFacetCtx is undoable, queryable, and editable.
    

    
Create a new context to merge facets on polygonal objects

    """
    pass
    


def polyMergeUV(caching=boolean, constructionHistory=boolean, distance=float, name=string, nodeState=int, uvSetName=string):
    """
    polyMergeUV is undoable, queryable, and editable.
    

    
Merge UVs of an object based on their distance. UVs are merge only if they belong to the same 3D vertex.

    """
    pass
    


def polyMergeVertex(alwaysMergeTwoVertices=boolean, caching=boolean, constructionHistory=boolean, distance=linear, mergeToComponents=string, name=string, nodeState=int, texture=boolean):
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
    


def polyMirrorFace(caching=boolean, constructionHistory=boolean, direction=int, mergeMode=int, mergeThreshold=linear, mergeThresholdType=int, mirrorAxis=int, mirrorPosition=linear, name=string, nodeState=int, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, worldSpace=boolean):
    """
    polyMirrorFace is undoable, queryable, and editable.
    

    
Mirror all the faces of the selected object.

    """
    pass
    


def polyMoveEdge(caching=boolean, constructionHistory=boolean, localCenter=int, localDirection=linear, linear, linear, localDirectionX=linear, localDirectionY=linear, localDirectionZ=linear, localRotate=angle, angle, angle, localRotateX=angle, localRotateY=angle, localRotateZ=angle, localScale=float, float, float, localScaleX=float, localScaleY=float, localScaleZ=float, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, name=string, nodeState=int, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, random=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleX=float, scaleY=float, scaleZ=float, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, worldSpace=boolean):
    """
    polyMoveEdge is undoable, queryable, and editable.
    

    
Modifies edges of a polygonal object. Translate, move, rotate or scale edges.

    """
    pass
    


def polyMoveFacet(attraction=float, caching=boolean, constructionHistory=boolean, gravity=linear, linear, linear, gravityX=linear, gravityY=linear, gravityZ=linear, localDirection=linear, linear, linear, localDirectionX=linear, localDirectionY=linear, localDirectionZ=linear, localRotate=angle, angle, angle, localRotateX=angle, localRotateY=angle, localRotateZ=angle, localScale=float, float, float, localScaleX=float, localScaleY=float, localScaleZ=float, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, magnX=linear, magnY=linear, magnZ=linear, magnet=linear, linear, linear, name=string, nodeState=int, offset=float, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, random=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleX=float, scaleY=float, scaleZ=float, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, weight=float, worldSpace=boolean):
    """
    polyMoveFacet is undoable, queryable, and editable.
    

    
Modifies facet of a polygonal object. Translate, move, rotate or scale facets.

    """
    pass
    


def polyMoveFacetUV(axisLen=float, float, axisLenX=float, axisLenY=float, caching=boolean, constructionHistory=boolean, name=string, nodeState=int, pivot=float, float, pivotU=float, pivotV=float, random=float, rotationAngle=angle, scale=float, float, scaleU=float, scaleV=float, translate=float, float, translateU=float, translateV=float):
    """
    polyMoveFacetUV is undoable, queryable, and editable.
    

    
Modifies the map by moving all UV values associated with the selected face(s).
The UV coordinates of the model are manipulated without changing the vertices of the 3D object.

    """
    pass
    


def polyMoveUV(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, pivot=float, float, pivotU=float, pivotV=float, random=float, rotationAngle=angle, scale=float, float, scaleU=float, scaleV=float, translate=float, float, translateU=float, translateV=float):
    """
    polyMoveUV is undoable, queryable, and editable.
    

    
Moves selected UV coordinates in 2D space. As the selected UVs are adjusted, the way the image is mapped onto the object changes accordingly. This command manipulates the UV values without changing the 3D geometry of the object.

    """
    pass
    


def polyMoveVertex(caching=boolean, constructionHistory=boolean, localDirection=linear, linear, linear, localDirectionX=linear, localDirectionY=linear, localDirectionZ=linear, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, name=string, nodeState=int, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, random=float, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, scale=float, float, float, scaleX=float, scaleY=float, scaleZ=float, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, worldSpace=boolean):
    """
    polyMoveVertex is undoable, queryable, and editable.
    

    
Modifies vertices of a polygonal object. Translate, rotate or scale vertices in local or world space.

    """
    pass
    


def polyMultiLayoutUV(flipReversed=boolean, gridU=int, gridV=int, layout=int, layoutMethod=int, offsetU=float, offsetV=float, percentageSpace=float, prescale=int, rotateForBestFit=int, scale=int, sizeU=float, sizeV=float, uvSetName=string):
    """
    polyMultiLayoutUV is undoable, NOT queryable, and NOT editable.
    

    
place the UVs of the selected polygonal objects so that they do not overlap.

    """
    pass
    


def polyNormal(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, normalMode=int):
    """
    polyNormal is undoable, queryable, and editable.
    

    
Control the normals of an object. This command works on faces or polygonal objects.

    """
    pass
    


def polyNormalizeUV(caching=boolean, constructionHistory=boolean, createNewMap=boolean, insertBeforeDeformers=boolean, name=string, nodeState=int, normalizeType=int, preserveAspectRatio=boolean, uvSetName=string):
    """
    polyNormalizeUV is undoable, queryable, and editable.
    

    
Normalizes the UVs of input polyFaces. The existing UVs of the faces are normalized between 0 and 1.

    """
    pass
    


def polyNormalPerVertex(allLocked=boolean, deformable=boolean, freezeNormal=boolean, normalX=float, normalXYZ=float, float, float, normalY=float, normalZ=float, relative=boolean, unFreezeNormal=boolean):
    """
    polyNormalPerVertex is undoable, queryable, and editable.
    

    
Command associates normal(x, y, z) with vertices on polygonal objects. When used with the query flag, it returns the normal associated with the specified components. However, when queried, the command returns all normals (all vtx-face combinations) on the vertex, regardless of whether they are shared or not.

    """
    pass
    


def polyOptions(activeObjects=boolean, allEdges=boolean, backCullVertex=boolean, backCulling=boolean, colorMaterialChannel=string, colorShadedDisplay=boolean, displayAlphaAsGreyScale=boolean, displayBorder=boolean, displayCenter=boolean, displayCreaseEdge=boolean, displayCreaseVertex=boolean, displayGeometry=boolean, displayInvisibleFaces=boolean, displayItemNumbers=boolean, boolean, boolean, boolean, displayMapBorder=boolean, displayMetadata=boolean, boolean, boolean, displayNormal=boolean, displaySubdComps=boolean, displayTriangle=boolean, displayUVTopology=boolean, displayUVs=boolean, displayVertex=boolean, displayWarp=boolean, facet=boolean, fullBack=boolean, gl=boolean, hardBack=boolean, hardEdge=boolean, hardEdgeColor=boolean, materialBlend=string, newPolymesh=boolean, point=boolean, pointFacet=boolean, relative=boolean, reuseTriangles=boolean, sizeBorder=float, sizeNormal=float, sizeUV=float, sizeVertex=float, smoothDrawType=int, softEdge=boolean, vertexNormalMethod=int, wireBackCulling=boolean):
    """
    polyOptions is undoable, queryable, and NOT editable.
    

    
Changes the global display polygonal attributes.

    """
    pass
    


def polyOptUvs( selectionList , applyToShell=boolean, areaWeight=float, caching=boolean, constructionHistory=boolean, globalBlend=float, globalMethodBlend=float, iterations=int, name=string, nodeState=int, optimizeAxis=int, pinSelected=boolean, pinUvBorder=boolean, scale=float, stoppingThreshold=float, useScale=boolean, uvSetName=string):
    """
    polyOptUvs is undoable, queryable, and editable.
    

    
Optimizes selected UVs.

    """
    pass
    


def polyOutput( poly poly... , allValues=boolean, color=boolean, colorDesc=boolean, edge=boolean, edgeFace=boolean, face=boolean, faceNorm=boolean, force=boolean, group=boolean, noOutput=boolean, normDesc=boolean, triangle=boolean, uvDesc=boolean, uvValue=boolean, vert=boolean, vertEdge=boolean, vertNorm=boolean):
    """
    polyOutput is undoable, NOT queryable, and NOT editable.
    

    
Dumps a description of internal memory representation of poly objects. If no objects are specified in the command line, then the objects from the active list are used. If information on the geometry in the history of a poly shape is desired, then the plug of interest needs to be specified in the command line. Default behaviour is to print only a summary. Use the flags above to get more details on a specific part of the object.

    """
    pass
    


def polyPinUV(createHistory=boolean, operation=uint, uvSetName=string, value=float):
    """
    polyPinUV is undoable, queryable, and editable.
    

    
This command is used to pin and unpin UVs. A "pinned" UV is one which should not be modified.
Each UV has an associated pin weight, that defaults to 0.0 meaning that the UV is not pinned. If pin weight is set to 1.0 then it becomes fully pinned and UV tools should not modify that UV. If the pin weight is set to a value between 0.0 and 1.0 then UV tools should weight their changes to that UV accordingly.
UV pinning is not enforced by the shape node: it is up to each tool to decide whether it will obey the pin weights.

    """
    pass
    


def polyPipe(axis=linear, linear, linear, constructionHistory=boolean, createUVs=boolean, height=linear, name=string, radius=linear, subdivisionsCaps=int, subdivisionsHeight=int, texture=boolean, thickness=linear):
    """
    polyPipe is undoable, queryable, and editable.
    

    
The polyPipe command creates a new polygonal pipe.

    """
    pass
    


def polyPlanarProjection(caching=boolean, constructionHistory=boolean, createNewMap=boolean, imageCenter=float, float, imageCenterX=float, imageCenterY=float, imageScale=float, float, imageScaleU=float, imageScaleV=float, insertBeforeDeformers=boolean, mapDirection=string, name=string, nodeState=int, projectionCenter=linear, linear, linear, projectionCenterX=linear, projectionCenterY=linear, projectionCenterZ=linear, projectionScale=linear, linear, projectionScaleU=linear, projectionScaleV=linear, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, rotationAngle=angle, worldSpace=boolean):
    """
    polyPlanarProjection is undoable, queryable, and editable.
    

    
Projects a map onto an object, using an orthogonal projection. The piece of the map defined from isu, isv, icx, icy area, is placed at pcx, pcy, pcz location.

    """
    pass
    


def polyPlane(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, height=linear, name=string, subdivisionsX=int, subdivisionsY=int, texture=int, width=linear):
    """
    polyPlane is undoable, queryable, and editable.
    

    
The mesh command creates a new polygonal plane.

    """
    pass
    


def polyPlatonicSolid(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, name=string, radius=linear, sideLength=linear, solidType=int, texture=int):
    """
    polyPlatonicSolid is undoable, queryable, and editable.
    

    
The polyPlatonicSolid command creates a new polygonal platonic solid.

    """
    pass
    


def polyPoke( selectionList , caching=boolean, constructionHistory=boolean, localTranslate=linear, linear, linear, localTranslateX=linear, localTranslateY=linear, localTranslateZ=linear, name=string, nodeState=int, translate=linear, linear, linear, translateX=linear, translateY=linear, translateZ=linear, worldSpace=boolean):
    """
    polyPoke is undoable, queryable, and editable.
    

    
Introduces a new vertex in the middle of the selected face, and connects it to the rest of the vertices of the face.

    """
    pass
    


def polyPrimitive(axis=linear, linear, linear, constructionHistory=boolean, name=string, polyType=int, radius=linear, sideLength=linear):
    """
    polyPrimitive is undoable, queryable, and editable.
    

    
Create a polygon primative

    """
    pass
    


def polyPrism(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, length=linear, name=string, numberOfSides=int, sideLength=linear, subdivisionsCaps=int, subdivisionsHeight=int, texture=int):
    """
    polyPrism is undoable, queryable, and editable.
    

    
The prism command creates a new polygonal prism.

    """
    pass
    


def polyProjectCurve( curve poly , caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyProjectCurve is undoable, queryable, and editable.
    

    
The polyProjectCurve command creates curves by projecting a selected curve onto a selected poly mesh. The direction of projection will be the current view direction unless the direction vector is specified with the -direction/-d flag.

    """
    pass
    


def polyProjection(constructionHistory=boolean, createNewMap=boolean, imageCenterX=float, imageCenterY=float, imageScaleU=float, imageScaleV=float, insertBeforeDeformers=boolean, keepImageRatio=boolean, mapDirection=string, projectionCenterX=float, projectionCenterY=float, projectionCenterZ=float, projectionScaleU=float, projectionScaleV=float, rotateX=float, rotateY=float, rotateZ=float, rotationAngle=float, seamCorrect=boolean, smartFit=boolean, type=string, uvSetName=string):
    """
    polyProjection is undoable, NOT queryable, and NOT editable.
    

    
Creates a mapping on the selected polygonal faces. When construction history is created, the name of the new node is returned. In other cases, the command returns nothing.

    """
    pass
    


def polyPyramid(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, name=string, numberOfSides=int, sideLength=linear, subdivisionsCaps=int, subdivisionsHeight=int, texture=boolean):
    """
    polyPyramid is undoable, queryable, and editable.
    

    
The pyramid command creates a new polygonal pyramid.

    """
    pass
    


def polyQuad(angle=angle, caching=boolean, constructionHistory=boolean, keepGroupBorder=boolean, keepHardEdges=boolean, keepTextureBorders=boolean, name=string, nodeState=int, worldSpace=boolean):
    """
    polyQuad is undoable, queryable, and editable.
    

    
Merges selected triangles of a polygonal object into four-sided faces.

    """
    pass
    


def polyQueryBlindData(associationType=string, binaryData=string, booleanData=boolean, doubleData=float, intData=int, longDataName=string, maxValue=float, minValue=float, shortDataName=string, showComp=boolean, stringData=string, subString=string, typeId=int):
    """
    polyQueryBlindData is NOT undoable, NOT queryable, and NOT editable.
    

    
Command query's blindData associated with particular polygonal components. So, the command will require the following to be specified: - selection list to query Optional are the: - typeId - associationType - longDataName or shortDataName of data being queried. - The actual data being specified. - showComponent flag Note that for object level blind data, the showComponent flag will be ignored. If no components are selected, the assocation flag will be ignored and object level data will be queried.

    """
    pass
    


def polyReduce(caching=boolean, cachingReduce=boolean, colorWeights=float, compactness=float, constructionHistory=boolean, geomWeights=float, invertVertexWeights=boolean, keepBorder=boolean, keepBorderWeight=float, keepColorBorder=boolean, keepColorBorderWeight=float, keepCreaseEdge=boolean, keepCreaseEdgeWeight=float, keepFaceGroupBorder=boolean, keepFaceGroupBorderWeight=float, keepHardEdge=boolean, keepHardEdgeWeight=float, keepMapBorder=boolean, keepMapBorderWeight=float, keepOriginalVertices=boolean, keepQuadsWeight=float, name=string, nodeState=int, percentage=float, preserveLocation=boolean, preserveTopology=boolean, replaceOriginal=boolean, sharpness=float, symmetryPlaneW=float, symmetryPlaneX=float, symmetryPlaneY=float, symmetryPlaneZ=float, symmetryTolerance=float, termination=int, triangleCount=int, triangulate=boolean, useVirtualSymmetry=int, uvWeights=float, version=int, vertexCount=int, vertexMapName=string, vertexWeightCoefficient=float, weightCoefficient=float):
    """
    polyReduce is undoable, queryable, and editable.
    

    
Simplify a polygonal object by reducing geometry while preserving the overall shape of the mesh.
The algorithm for polyReduce was changed in 2014 to use a new algorithm derived from Softimage. However, the command still defaults to using the old algorithm for backwards compatibility. Therefore, we recommend setting the version flag to 1 for best results as the new algorithm is better at preserving geometry features. Additionally, some flags only apply to a specific algorithm and this is documented for each flag.

    """
    pass
    


def polyRemesh(caching=boolean, constructionHistory=boolean, interpolationType=int, name=string, nodeState=int, reduceThreshold=float, refineThreshold=float, smoothStrength=float, tessellateBorders=boolean):
    """
    polyRemesh is undoable, queryable, and editable.
    

    
Triangulates, then remeshes the given mesh through edge splitting and collapsing. Edges longer than the specified refinement threshold are split, and edges shorter than the reduction threshold are collapsed.

    """
    pass
    


def polySelect(add=boolean, addFirst=boolean, asSelectString=boolean, deselect=boolean, edgeBorder=uint, edgeBorderPath=int, int, edgeBorderPattern=int, int, edgeLoop=uint, edgeLoopOrBorder=uint, edgeLoopOrBorderPattern=int, int, edgeLoopPath=int, int, edgeLoopPattern=int, int, edgeRing=uint, edgeRingPath=int, int, edgeRingPattern=int, int, edgeUVLoopOrBorder=uint, extendToShell=uint, noSelection=boolean, replace=boolean, shortestEdgePath=int, int, shortestEdgePathUV=int, int, shortestFacePath=int, int, toggle=boolean):
    """
    polySelect is undoable, queryable, and NOT editable.
    

    
This command makes different types of poly component selections. The return value is an integer array containing the id's of the components in the selection in order. If a given type of selection loops back on itself then this is indicated by the start id appearing twice, once at the start and once at the end.

    """
    pass
    


def polySelectConstraint(angle=int, anglePropagation=boolean, angleTolerance=float, anglebound=angle, angle, border=boolean, borderPropagation=boolean, convexity=int, crease=boolean, disable=boolean, dist=int, distaxis=float, float, float, distbound=float, float, distpoint=float, float, float, edgeDistance=uint, geometricarea=int, geometricareabound=float, float, holes=int, length=int, lengthbound=float, float, loopPropagation=boolean, max2dAngle=float, max3dAngle=float, mode=int, nonmanifold=int, order=int, orderbound=int, int, orient=int, orientaxis=float, float, float, orientbound=float, float, planarity=int, propagate=int, random=int, randomratio=float, returnSelection=boolean, ringPropagation=boolean, shell=boolean, size=int, smoothness=int, stateString=boolean, textured=int, texturedarea=int, texturedareabound=float, float, textureshared=int, topology=int, type=int, uvShell=boolean, visibility=int, visibilityangle=angle, visibilitypoint=float, float, float, where=int, wholeSensitive=boolean):
    """
    polySelectConstraint is undoable, queryable, and NOT editable.
    

    
Changes the global polygonal selection constraints.

    """
    pass
    


def polySelectConstraintMonitor( string , changeCommand=string, string, create=boolean, delete=boolean):
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
    


def polySeparate( poly , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean):
    """
    polySeparate is undoable, queryable, and editable.
    

    
This command creates new objects from the given poly. A new object will be created for each section of the mesh that is distinct (no edges connect it to the rest of the mesh).
This command can only separate one object at a time.

    """
    pass
    


def polySetToFaceNormal(setUserNormal=boolean):
    """
    polySetToFaceNormal is undoable, NOT queryable, and NOT editable.
    

    
This command takes selected polygonal vertices or vertex-faces and changes their normals. If the option userNormal is used, the new normal values will be the face normals arround the vertices/vertex-faces. Otherwise the new normal values will be default values according to the internal calculation.

    """
    pass
    


def polySewEdge(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, texture=boolean, tolerance=linear, worldSpace=boolean):
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
    


def polySlideEdge(absolute=boolean, direction=uint, edgeDirection=float, symmetry=boolean):
    """
    polySlideEdge is undoable, NOT queryable, and NOT editable.
    

    
Moves an edge loop selection along the edges connected to the sides of its vertices.

    """
    pass
    


def polySmooth(caching=boolean, constructionHistory=boolean, continuity=float, divisions=int, keepBorder=boolean, keepHardEdge=boolean, keepSelectionBorder=boolean, keepTessellation=boolean, name=string, nodeState=int, osdCreaseMethod=int, osdFvarBoundary=int, osdFvarPropagateCorners=boolean, osdSmoothTriangles=boolean, osdVertBoundary=int, propagateEdgeHardness=boolean, subdivisionType=int):
    """
    polySmooth is undoable, queryable, and editable.
    

    
Smooth a polygonal object. This command works on polygonal objects or faces.

    """
    pass
    


def polySoftEdge(angle=angle, caching=boolean, constructionHistory=boolean, name=string, nodeState=int, worldSpace=boolean):
    """
    polySoftEdge is undoable, queryable, and editable.
    

    
Selectively makes edges soft or hard.

An edge will be made hard if the angle between two owning faces is sharper (larger) than the smoothing angle.
An edge wil be made soft if the angle between two owning facets is flatter (smaller) than the smoothing angle.

    """
    pass
    


def polySphere(axis=linear, linear, linear, constructionHistory=boolean, createUVs=int, name=string, radius=linear, subdivisionsX=int, subdivisionsY=int, texture=int):
    """
    polySphere is undoable, queryable, and editable.
    

    
The sphere command creates a new polygonal sphere.

    """
    pass
    


def polySphericalProjection(caching=boolean, constructionHistory=boolean, createNewMap=boolean, imageCenter=float, float, imageCenterX=float, imageCenterY=float, imageScale=float, float, imageScaleU=float, imageScaleV=float, insertBeforeDeformers=boolean, name=string, nodeState=int, projectionCenter=linear, linear, linear, projectionCenterX=linear, projectionCenterY=linear, projectionCenterZ=linear, projectionScale=linear, linear, projectionScaleU=linear, projectionScaleV=linear, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, rotationAngle=angle, seamCorrect=boolean, smartFit=boolean, worldSpace=boolean):
    """
    polySphericalProjection is undoable, queryable, and editable.
    

    
Projects a spherical map onto an object.

    """
    pass
    


def polySplit(constructionHistory=boolean, edgepoint=int, float, facepoint=int, float, float, float, insertpoint=int, float, , float, float, , name=string, smoothingangle=angle, subdivision=int):
    """
    polySplit is undoable, queryable, and editable.
    

    
Split facets/edges of a polygonal object.
The first and last arguments must be edges. Intermediate points may lie on either a shared face or an edge which neighbors the previous point.

    """
    pass
    


def polySplitCtx(enablesnap=boolean, magnetsnap=int, precsnap=float, smoothingangle=angle, snaptoedge=boolean, subdivision=int):
    """
    polySplitCtx is undoable, queryable, and editable.
    

    
Create a new context to split facets on polygonal objects

    """
    pass
    


def polySplitCtx2(constrainToEdges=boolean, edgeMagnets=int, snapTolerance=float):
    """
    polySplitCtx2 is undoable, queryable, and editable.
    

    
Create a new context to split facets on polygonal objects

    """
    pass
    


def polySplitEdge(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
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
    


def polySplitRing(caching=boolean, constructionHistory=boolean, direction=boolean, divisions=int, name=string, nodeState=int, rootEdge=int, smoothingAngle=angle, splitType=int, weight=float):
    """
    polySplitRing is undoable, queryable, and editable.
    

    
Splits a series of ring edges of connected quads and inserts connecting edges between them.

    """
    pass
    


def polySplitVertex(caching=boolean, constructionHistory=boolean, name=string, nodeState=int, worldSpace=boolean):
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
    


def polyStraightenUVBorder( selectionList , blendOriginal=float, caching=boolean, constructionHistory=boolean, curvature=float, gapTolerance=int, name=string, nodeState=int, preserveLength=float, uvSetName=string):
    """
    polyStraightenUVBorder is undoable, queryable, and editable.
    

    
Move border UVs along a simple curve.

    """
    pass
    


def polySubdivideEdge(caching=boolean, constructionHistory=boolean, divisions=int, name=string, nodeState=int, size=linear, worldSpace=boolean):
    """
    polySubdivideEdge is undoable, queryable, and editable.
    

    
Subdivides an edge into two or more subedges.

Default : divide edge into two edges of equal length.

    """
    pass
    


def polySubdivideFacet(caching=boolean, constructionHistory=boolean, divisions=int, mode=int, name=string, nodeState=int):
    """
    polySubdivideFacet is undoable, queryable, and editable.
    

    
Subdivides a face into quads or triangles.

In quad mode, a center point is introduced at the center of each face and midpoints are inserted on all the edges of each face. New faces (all quadrilaterals) are built by adding edges from the midpoints towards the center.
In triangle mode, only the center point is created; new faces (all triangles) are created by connecting the center point to all the existing vertices of the face.
Default : one subdivision step in quad mode (polySubdFacet -dv 1 -m 0;)

    """
    pass
    


def polyTorus(axis=linear, linear, linear, constructionHistory=boolean, createUVs=boolean, name=string, radius=linear, sectionRadius=linear, subdivisionsX=int, subdivisionsY=int, texture=boolean, twist=angle):
    """
    polyTorus is undoable, queryable, and editable.
    

    
The torus command creates a new polygonal torus.

    """
    pass
    


def polyToSubdiv( poly , absolutePosition=boolean, applyMatrixToResult=boolean, caching=boolean, constructionHistory=boolean, maxEdgesPerVert=int, maxPolyCount=int, name=string, nodeState=int, object=boolean, preserveVertexOrdering=boolean, quickConvert=boolean, uvPoints=float, float, uvPointsU=float, uvPointsV=float, uvTreatment=int):
    """
    polyToSubdiv is undoable, queryable, and editable.
    

    
This command converts a polygon and produces a subd surface. The name of the new subdivision surface is returned. If construction history is ON, then the name of the new dependency node is returned as well.

    """
    pass
    


def polyTransfer(alternateObject=string, caching=boolean, constructionHistory=boolean, name=string, nodeState=int, uvSets=boolean, vertexColor=boolean, vertices=boolean):
    """
    polyTransfer is undoable, queryable, and editable.
    

    
Transfer information from one polygonal object to another one. Both objects must have identical topology, that is same vertex, edge, and face numbering. The flags specify which of the vertices, UV sets or vertex colors will be copied.

    """
    pass
    


def polyTriangulate(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyTriangulate is undoable, queryable, and editable.
    

    
Triangulation breaks polygons down into triangles, ensuring that all faces are planar and non-holed. Triangulation of models can be beneficial in many areas.

    """
    pass
    


def polyUnite( poly poly poly ... , caching=boolean, constructionHistory=boolean, mergeUVSets=int, name=string, nodeState=int):
    """
    polyUnite is undoable, queryable, and editable.
    

    
This command creates a new poly as an union of a list of polys If no objects are specified in the command line, then the objects from the active list are used.

    """
    pass
    


def polyUniteSkinned(centerPivot=boolean, constructionHistory=boolean, mergeUVSets=int, objectPivot=boolean):
    """
    polyUniteSkinned is undoable, queryable, and editable.
    

    
Command to combine poly mesh objects (as polyUnite) while retaining the smooth skinning setup on the combined object.

    """
    pass
    


def polyUVRectangle(caching=boolean, constructionHistory=boolean, name=string, nodeState=int):
    """
    polyUVRectangle is undoable, queryable, and editable.
    

    
Given two vertices, does one of the following: 1) If the vertices define opposite corners of a rectangular area of quads, assigns a grid of UVs spanning the 0-1 area to that rectangle. 2) If the vertices define an edge in a rectangular and topologically cylindrical area of quads, assigns UVs spanning the 0-1 area to that cylindrical patch, using the defined edge as the U=0 edge.

    """
    pass
    


def polyUVSet(allUVSets=boolean, allUVSetsIndices=boolean, allUVSetsWithCount=boolean, copy=boolean, create=boolean, currentLastUVSet=boolean, currentPerInstanceUVSet=boolean, currentUVSet=boolean, delete=boolean, newUVSet=string, perInstance=boolean, projections=boolean, rename=boolean, shareInstances=boolean, unshared=boolean, uvSet=string):
    """
    polyUVSet is undoable, queryable, and editable.
    

    
Command to do the following to uv sets: - delete an existing uv set. - rename an existing uv set. - create a new empty uv set. - copy the values from one uv set to a another pre-existing uv set. - set the current uv set to a pre-existing uv set. - modify sharing between instances of per-instance uv sets - query the current uv set. - set the current uv set to the last uv set added to an object. - query the names of all uv sets.

    """
    pass
    


def polyWedgeFace(axis=float, float, float, caching=boolean, center=float, float, float, constructionHistory=boolean, divisions=int, edge=int, name=string, nodeState=int, wedgeAngle=angle, worldSpace=boolean):
    """
    polyWedgeFace is undoable, queryable, and editable.
    

    
Extrude faces about an axis. The axis is the average of all the selected edges. If the edges are not aligned, the wedge may not look intuitive. To separately wedge faces about different wedge axes, the command should be issued as many times as the wedge axes. (as in the second example)

    """
    pass
    


def popupMenu( string , allowOptionBoxes=boolean, altModifier=boolean, button=int, ctrlModifier=boolean, deleteAllItems=boolean, itemArray=boolean, markingMenu=boolean, numberOfItems=boolean, postMenuCommand=script, postMenuCommandOnce=boolean, shiftModifier=boolean):
    """
    popupMenu is undoable, queryable, and editable.
    

    
This command creates a popup menu and attaches it to the current control if no parent is specified. The popup menu is posted with the right mouse button by default.
Popup menus can be added to any kind of control, however, on some widgets, only the standard menu button (3rd mouse button) can be used to trigger popup menus. This is to meet generally accepted UI guidelines that assign the 3rd mouse button and only this one to popup menus, and also to prevent unexpected behavior of controls like text fields, that expect 1st and 2nd button to be reserved for contextual operations like text or item selection...

    """
    pass
    


def pose(allPoses=boolean, apply=boolean, name=string):
    """
    pose is undoable, queryable, and editable.
    

    
This command is used to create character poses.

    """
    pass
    


def poseEditor( string , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, selectionConnection=string, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    poseEditor is undoable, queryable, and editable.
    

    
This command creates an editor that derives from the base editor class that has controls for deformer and control nodes.

    """
    pass
    


def posePanel( string , control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, poseEditor=boolean, replacePanel=string, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    posePanel is undoable, queryable, and editable.
    

    
This command creates a panel that derives from the base panel class that houses a poseEditor.

    """
    pass
    


def preloadRefEd(control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, selectFileNode=boolean, selectionConnection=string, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    preloadRefEd is undoable, queryable, and editable.
    

    
This creates an editor for managing which references will be read in (loaded) and which deferred (unloaded) upon opening a file.

    """
    pass
    


def prepareRender(defaultTraversalSet=string, deregister=string, invokePostRender=boolean, invokePostRenderFrame=boolean, invokePostRenderLayer=boolean, invokePreRender=boolean, invokePreRenderFrame=boolean, invokePreRenderLayer=boolean, invokeSettingsUI=boolean, label=string, listTraversalSets=boolean, postRender=script, postRenderFrame=script, postRenderLayer=script, preRender=script, preRenderFrame=script, preRenderLayer=script, restore=boolean, saveAssemblyConfig=boolean, settingsUI=script, setup=boolean, traversalSet=string, traversalSetInit=script):
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
    


def profiler(addCategory=string, allCategories=boolean, bufferSize=int, categoryIndex=int, categoryIndexToName=int, categoryName=string, categoryNameToIndex=string, categoryRecording=boolean, clearAllMelInstrumentation=boolean, colorIndex=int, eventCPUId=boolean, eventCategory=boolean, eventColor=boolean, eventCount=boolean, eventDescription=boolean, eventDuration=boolean, eventIndex=int, eventName=boolean, eventStartTime=boolean, eventThreadId=boolean, instrumentMel=boolean, load=string, output=string, procedureDescription=string, procedureName=string, removeCategory=string, reset=boolean, sampling=boolean, signalEvent=boolean, signalMelEvent=boolean):
    """
    profiler is NOT undoable, queryable, and NOT editable.
    

    
The profiler is used to record timing information from key events within Maya, as an aid in tuning the performance of scenes, scripts and plug-ins. User written plug-ins and Python scripts can also generate profiling information for their own code through the MProfilingScope and MProfiler classes in the API.
This command provides the ability to control the collection of profiling data and to query information about the recorded events. The recorded information can also be viewed graphically in the Profiler window.
The buffer size cannot be changed while sampling is active, it will return an error The reset flag cannot be called while sampling is active, it will return an error. Any changes to the buffer size will only be applied on start of the next recording. You can't save and load in the same command, save has priority, load would be ignored.

    """
    pass
    


def profilerTool(categoryView=boolean, cpuView=boolean, destroy=boolean, exists=boolean, findNext=boolean, findPrevious=boolean, frameAll=boolean, frameSelected=boolean, isolateSegment=int, make=boolean, matchWholeWord=boolean, searchEvent=string, segmentCount=boolean, showAllEvent=boolean, showSelectedEvents=boolean, showSelectedEventsRepetition=boolean, threadView=boolean, unisolateSegment=boolean):
    """
    profilerTool is NOT undoable, queryable, and editable.
    

    
This script is intended to be used by the profilerPanel to interact with the profiler tool's view (draw region). It can be used to control some behaviors about the profiler Tool.

    """
    pass
    


def progressBar( string , annotation=string, backgroundColor=float, float, float, beginProgress=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, endProgress=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isCancelled=boolean, isInterruptable=boolean, isMainProgressBar=boolean, isObscured=boolean, manage=boolean, maxValue=int, minValue=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, progress=int, status=string, step=int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    progressBar is undoable, queryable, and editable.
    

    
Creates a progress bar control that graphically fills in as its progress value increases.

    """
    pass
    


def progressWindow(endProgress=boolean, isCancelled=boolean, isInterruptable=boolean, maxValue=int, minValue=int, progress=int, status=string, step=int, title=string):
    """
    progressWindow is undoable, queryable, and editable.
    

    
The progressWindow command creates a window containing a status message, a graphical progress gauge, and optionally a "Hit ESC to Cancel" label for interruptable operations.
Only one progress window is allowed on screen at a time. While the window is visible, the busy cursor is shown.

    """
    pass
    


def projectCurve( curve surface , caching=boolean, constructionHistory=boolean, direction=linear, linear, linear, directionX=linear, directionY=linear, directionZ=linear, name=string, nodeState=int, object=boolean, range=boolean, tolerance=linear, useNormal=boolean):
    """
    projectCurve is undoable, queryable, and editable.
    

    
The projectCurve command creates curves on surface where all selected curves project onto the selected surfaces. Projection can be done using the surface normals or the user can specify the vector to project along. Note: the user does not have to specify the curves and surfaces in any particular order in the command line.

    """
    pass
    


def projectionContext(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    projectionContext is undoable, queryable, and editable.
    

    
Set the context for projection manips

    """
    pass
    


def projectionManip(fitBBox=boolean, projType=int, switchType=boolean):
    """
    projectionManip is undoable, queryable, and NOT editable.
    

    
Various commands to set the manipulator to interesting positions.

    """
    pass
    


def projectTangent( curve curve curve | surface , caching=boolean, constructionHistory=boolean, curvature=boolean, curvatureScale=linear, ignoreEdges=boolean, name=string, nodeState=int, object=boolean, replaceOriginal=boolean, reverseTangent=boolean, rotate=angle, tangentDirection=int, tangentScale=linear):
    """
    projectTangent is undoable, queryable, and editable.
    

    
The project tangent command is used to align (for tangents) a curve to two other curves or a surface. A surface isoparm may be selected to define the direction (U or V) to align to. The end of the curve must intersect with these other objects. Curvature continuity may also be applied if required.
Tangent continuity means the end of the curve is modified to be tangent at the point it meets the other objects.
Curvature continuity means the end of the curve is modified to be curvature continuous as well as tangent.
If the normal tangent direction is used, the curvature continuity and rotation do not apply. Also, curvature continuity is only available if align to a surface (not with 2 curves).

    """
    pass
    


def promptDialog(backgroundColor=float, float, float, button=string, cancelButton=string, defaultButton=string, dismissString=string, message=string, messageAlign=string, parent=string, scrollableField=boolean, style=string, text=string, title=string):
    """
    promptDialog is undoable, queryable, and NOT editable.
    

    
The promptDialog command creates a modal dialog with a message to the user, a text field in which the user may enter a response, and a variable number of buttons to dismiss the dialog. The dialog is dismissed when the user presses any button or chooses the close item from the window menu. In the case where a button is pressed then the name of the button selected is returned. If the dialog is dismissed via the close item then the string returned is specified by the -ds/dismissString flag.
The default behaviour when no arguments are specified is to create an empty single button dialog.
To obtain the text entered by the user simply query the -tx/text flag.

    """
    pass
    


def propModCtx( string , animCurve=string, animCurveFalloff=float, float, animCurveParam=string, direction=float, float, float, exists=boolean, image1=string, image2=string, image3=string, linear=float, linearParam=float, float, nurbsCurve=string, powerCutoff=float, powerCutoffParam=float, float, powerDegree=float, powerDegreeParam=float, script=string, scriptParam=string, type=int, worldspace=boolean):
    """
    propModCtx is undoable, queryable, and editable.
    

    
Controls the proportional move context.

    """
    pass
    


def propMove( objects , percent=float, percentX=float, percentY=float, percentZ=float, pivot=float, float, float, rotate=angle, angle, angle, scale=float, float, float, translate=linear, linear, linear):
    """
    propMove is undoable, NOT queryable, and NOT editable.
    

    
Performs a proportional translate, scale or rotate operation on any number of objects. The percentages to rotate, scale or translate by can be specified using either the -p flags or -px, -py, -pz flags. Each selected object must have a corresponding -p or -px, -py, -pz flag. The rotate, scale or translate performed is relative.

    """
    pass
    


def psdChannelOutliner( string , addChild=string, string, allItems=boolean, annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, doubleClickCommand=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfItems=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, psdParent=string, removeAll=boolean, removeChild=string, selectCommand=string, selectItem=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    psdChannelOutliner is undoable, queryable, and editable.
    

    
Create a psdChannelOutliner control which is capable of displaying a tree structure upto one level.

    """
    pass
    


def psdEditTextureFile(addChannel=string, addChannelColor=string, float, float, float, addChannelImage=string, string, deleteChannel=string, psdFileName=string, snapShotImage=string, uvSnapPostionTop=boolean):
    """
    psdEditTextureFile is undoable, NOT queryable, and NOT editable.
    

    
Edits the existing PSD file. Addition and deletion of the channels (layer sets) are supported.

    """
    pass
    


def psdExport(alphaChannelIdx=int, bytesPerChannel=int, emptyLayerSet=boolean, format=string, layerName=string, layerSetName=string, outFileName=string, preMultiplyAlpha=boolean, psdFileName=string):
    """
    psdExport is NOT undoable, queryable, and NOT editable.
    

    
Writes the Photoshop file layer set into different formats. The output file depth (bit per channel ) can be different from that of the input. If the input is 16 bpc and output is 8 bpc, there will be data loss.

    """
    pass
    


def psdTextureFile(channelRGB=string, uint, uint, uint, uint, channels=string, uint, boolean, imageFileName=string, string, uint, psdFileName=string, snapShotImageName=string, uvSnapPostionTop=boolean, xResolution=uint, yResolution=uint):
    """
    psdTextureFile is undoable, NOT queryable, and NOT editable.
    

    
Creates a Photoshop file with UVSnap shot image and the layer set names as the input.

    """
    pass
    


def querySubdiv(action=int, level=int, relative=boolean):
    """
    querySubdiv is undoable, NOT queryable, and NOT editable.
    

    
Queries a subdivision surface based on a set of query parameters and updates the selection list with the results.

    """
    pass
    


def quit(abort=boolean, exitCode=uint, force=boolean):
    """
    quit is undoable, NOT queryable, and NOT editable.
    

    
This command is used to exit the application.

    """
    pass
    


def radial( selectionList , attenuation=float, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear, type=float):
    """
    radial is undoable, queryable, and editable.
    

    
A radial field pushes objects directly towards or directly away from it, like a magnet.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def radioButton( string , align=string, annotation=string, backgroundColor=float, float, float, changeCommand=script, collection=string, data=int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, offCommand=script, onCommand=script, parent=string, popupMenuArray=boolean, preventOverride=boolean, recomputeSize=boolean, select=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    radioButton is undoable, queryable, and editable.
    

    
This command creates a radio button that is added to the most recently created radio collection if the -cl/collection flag is not used.

    """
    pass
    


def radioButtonGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, annotation1=string, annotation2=string, annotation3=string, annotation4=string, backgroundColor=float, float, float, changeCommand=script, changeCommand1=script, changeCommand2=script, changeCommand3=script, changeCommand4=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, data1=int, data2=int, data3=int, data4=int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enable1=boolean, enable2=boolean, enable3=boolean, enable4=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, label1=string, label2=string, label3=string, label4=string, labelAnnotation=string, labelArray2=string, string, labelArray3=string, string, string, labelArray4=string, string, string, string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, numberOfRadioButtons=int, offCommand=script, offCommand1=script, offCommand2=script, offCommand3=script, offCommand4=script, onCommand=script, onCommand1=script, onCommand2=script, onCommand3=script, onCommand4=script, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, select=int, shareCollection=string, useTemplate=string, vertical=boolean, visible=boolean, visibleChangeCommand=script, width=int):
    """
    radioButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates from one to four radio buttons in a single row. By default the radio buttons will share a single collection, but they can also share the collection of another radio button group. The buttons can also have an optional text label.

    """
    pass
    


def radioCollection( string , collectionItemArray=boolean, defineTemplate=string, exists=boolean, gl=boolean, numberOfCollectionItems=boolean, parent=string, select=string, useTemplate=string):
    """
    radioCollection is undoable, queryable, and editable.
    

    
This command creates a radio button collection. Collections are parented to the current default layout if no parent is specified with the -p/parent flag. As children of the layout they will be deleted when the layout is deleted. Collections may also span more than one window if the -gl/global flag is used. In this case the collection has no parent and must be explicitly deleted with the deleteUI command when it is no longer wanted.

    """
    pass
    


def radioMenuItemCollection( string , defineTemplate=string, exists=boolean, gl=boolean, parent=string, useTemplate=string):
    """
    radioMenuItemCollection is undoable, queryable, and editable.
    

    
This command creates a radioMenuItemCollection. Attach radio menu items to radio menu item collection objects to get radio button behaviour. Radio menu item collections will be parented to the current menu if no parent is specified with the -p/parent flag. As children of the menu they will be deleted when the menu is deleted. Collections may also span more than one menu if the -g/global flag is used. In this case the collection has no parent menu and must be explicitly deleted with the deleteUI command when it is no longer wanted.

    """
    pass
    


def rampColorPort( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, node=name, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, selectedColorControl=string, selectedInterpControl=string, selectedPositionControl=string, useTemplate=string, verticalLayout=boolean, visible=boolean, visibleChangeCommand=script, width=int):
    """
    rampColorPort is undoable, queryable, and editable.
    

    
This command creates a control that displays an image representing the ramp node specified, and supports editing of that node.

    """
    pass
    


def rangeControl( name , annotation=string, backgroundColor=float, float, float, changedCommand=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, maxRange=time, minRange=time, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int, widthHeight=int, int):
    """
    rangeControl is undoable, queryable, and editable.
    

    
This command creates a control used for displaying and modifying the current playback range. Note: only one master rangeControl may exist. Any addition rangeControls that a user creates are slaved to the master range control widget.

    """
    pass
    


def readTake(angle=string, device=string, frequency=float, linear=string, noTime=boolean, take=string):
    """
    readTake is undoable, NOT queryable, and NOT editable.
    

    
This action reads a take (.mov) file to a defined device.
See also: writeTake, applyTake

    """
    pass
    


def rebuildCurve( curve curve , caching=boolean, constructionHistory=boolean, degree=int, endKnots=int, fitRebuild=boolean, keepControlPoints=boolean, keepEndPoints=boolean, keepRange=int, keepTangents=boolean, name=string, nodeState=int, object=boolean, range=boolean, rebuildType=int, replaceOriginal=boolean, smartSurfaceCurveRebuild=boolean, spans=int, tolerance=linear):
    """
    rebuildCurve is undoable, queryable, and editable.
    

    
This command rebuilds a curve by modifying its parameterization. In some cases the shape may also change. The rebuildType (-rt) determines how the curve is to be rebuilt.
The optional second curve can be used to specify a reference parameterization.

    """
    pass
    


def rebuildSurface( surface surface , caching=boolean, constructionHistory=boolean, degreeU=int, degreeV=int, direction=int, endKnots=int, fitRebuild=int, keepControlPoints=boolean, keepCorners=boolean, keepRange=int, name=string, nodeState=int, object=boolean, polygon=int, rebuildType=int, replaceOriginal=boolean, spansU=int, spansV=int, tolerance=linear):
    """
    rebuildSurface is undoable, queryable, and editable.
    

    
This command rebuilds a surface by modifying its parameterization. In some cases the shape of the surface may also change. The rebuildType (-rt) attribute determines how the surface is rebuilt.
The optional second surface can be used to specify a reference parameterization.

    """
    pass
    


def recordAttr(attribute=string, delete=boolean):
    """
    recordAttr is undoable, queryable, and NOT editable.
    

    
This command sets up an attribute to be recorded. When the record command is executed, any changes to this attribute are recorded. When recording stops these changes are turned into keyframes.
If no attributes are specified all attributes of the node are recorded.
When the query flag is used, a list of the attributes being recorded will be returned.

    """
    pass
    


def recordDevice(cleanup=boolean, data=boolean, device=string, duration=int, playback=boolean, state=boolean, wait=boolean):
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
    


def referenceEdit(applyFailedEdits=boolean, changeEditTarget=string, string, editCommand=string, failedEdits=boolean, onReferenceNode=string, removeEdits=boolean, successfulEdits=boolean):
    """
    referenceEdit is NOT undoable, NOT queryable, and NOT editable.
    

    
Use this command to remove and change the modifications which have been applied to references. A valid commandTarget is either a reference node, a reference file, a node in a reference, or a plug from a reference. Only modifications that have been made from the currently open scene can be changed or removed. The 'referenceQuery -topReference' command can be used to determine what modifications have been made to a given commandTarget. Additionally only unapplied edits will be affected. Edits are unapplied when the node(s) which they affect are unloaded, or when they could not be successfully applied. By default this command only works on failed edits (this can be adjusted using the "-failedEdits" and "-successfulEdits" flags). Specifying a reference node as the command target is equivalent to specifying every node in the target reference file as a target. In this situation the results may differ depending on whether the target reference is loaded or unloaded. When it is unloaded, edits that affect both a node in the target reference and a node in one of its descendant references may be missed (e.g. those edits may not be removed). This is because when a reference is unloaded Maya no longer retains detailed information about which nodes belong to it. However, edits that only affect nodes in the target reference or in one of its ancestral references should be removed as expected. When the flags -removeEdits and -editCommand are used together, by default all connectAttr edits are removed from the specified source object. To remove only edits that connect to a specific target object, the target object can be passed as an additional argument to the command. This narrows the match criteria, so that only edits that connect the source object to the provided target in this additional argument are removed. See the example below. NOTE: When specifying a plug it is important to use the appropriate long attribute name.

    """
    pass
    


def referenceQuery(child=boolean, dagPath=boolean, editAttrs=boolean, editCommand=string, editNodes=boolean, editStrings=boolean, failedEdits=boolean, filename=boolean, isExportEdits=boolean, isLoaded=boolean, isNodeReferenced=boolean, isPreviewOnly=boolean, liveEdits=boolean, namespace=boolean, nodes=boolean, onReferenceNode=string, parent=boolean, parentNamespace=boolean, referenceNode=boolean, shortName=boolean, showDagPath=boolean, showNamespace=boolean, successfulEdits=boolean, topReference=boolean, unresolvedName=boolean, withoutCopyNumber=boolean):
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
    


def refresh(currentView=boolean, force=boolean, suspend=boolean):
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
    


def regionSelectKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    regionSelectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the graph editor using the region select tool.

    """
    pass
    


def relationship(b=boolean, relationshipData=string):
    """
    relationship is undoable, queryable, and editable.
    

    
This is primarily for use with file IO. Rather than write out the specific attributes/connections required to maintain a relationship, a description of the related nodes/plugs is written instead. The relationship must have an owner node, and have a specific type. During file read, maya will make the connections and/or set the data necessary to represent the realtionship in the dependency graph.

    """
    pass
    


def reloadImage( string string ):
    """
    reloadImage is undoable, NOT queryable, and NOT editable.
    

    
This command reloads an xpm image from disk. This can be used when the file has changed on disk and needs to be reloaded.
The first string argument is the file name of the .xpm file. The second string argument is the name of a control using the specified pixmap.

    """
    pass
    


def removeJoint( object ):
    """
    removeJoint is undoable, NOT queryable, and NOT editable.
    

    
This command will remove the selected joint or the joint given at the command line from the skeleton.
The given (or selected) joint should not be the root joint of the skeleton, and not have skin attached. The command works on the given (or selected) joint. No options or flags are necessary.

    """
    pass
    


def removeMultiInstance( attribute , b=boolean):
    """
    removeMultiInstance is undoable, NOT queryable, and NOT editable.
    

    
Removes a particular instance of a multiElement. This is only useful for input attributes since outputs will get regenerated the next time the node gets executed. This command will remove the instance and optionally break all incoming and outgoing connections to that instance. If the connections are not broken (with the -b true) flag, then the command will fail if connections exist.

    """
    pass
    


def rename( object string , ignoreShape=boolean, uuid=boolean):
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
    


def renameUI( string string ):
    """
    renameUI is undoable, NOT queryable, and NOT editable.
    

    
This command renames the UI object passed as first arument to the new name specified as second argument. If the new name is a duplicate, or not valid, then re-naming fails and the old name is returned.
Notes
This command does not update other objects or commands that reference this object by name, so use this command at your own risk.

    """
    pass
    


def render( camera , abortMissingTexture=boolean, batch=boolean, keepPreImage=boolean, layer=string, nglowpass=boolean, nshadows=boolean, replace=boolean, xresolution=int, yresolution=int):
    """
    render is NOT undoable, NOT queryable, and NOT editable.
    

    
The render command is used to start off a MayaSoftware rendering session of the currently active camera. If a rendering is already in progress, then this command stops the rendering. This command is not undoable.

    """
    pass
    


def renderer(string, addGlobalsNode=string, addGlobalsTab=string, string, string, batchRenderOptionsProcedure=string, batchRenderOptionsStringProcedure=string, batchRenderProcedure=string, cancelBatchRenderProcedure=string, changeIprRegionProcedure=string, commandRenderProcedure=string, exists=boolean, globalsNodes=boolean, globalsTabCreateProcNames=boolean, globalsTabLabels=boolean, globalsTabUpdateProcNames=boolean, iprOptionsMenuLabel=string, iprOptionsProcedure=string, iprOptionsSubMenuProcedure=string, iprRenderProcedure=string, iprRenderSubMenuProcedure=string, isRunningIprProcedure=string, logoCallbackProcedure=string, logoImageName=string, materialViewRendererList=boolean, materialViewRendererPause=boolean, materialViewRendererSuspend=boolean, namesOfAvailableRenderers=boolean, pauseIprRenderProcedure=string, polyPrelightProcedure=string, refreshIprRenderProcedure=string, renderDiagnosticsProcedure=string, renderGlobalsProcedure=string, renderMenuProcedure=string, renderOptionsProcedure=string, renderProcedure=string, renderRegionProcedure=string, rendererUIName=string, renderingEditorsSubMenuProcedure=string, showBatchRenderLogProcedure=string, showBatchRenderProcedure=string, showRenderLogProcedure=string, startIprRenderProcedure=string, stopIprRenderProcedure=string, textureBakingProcedure=string, unregisterRenderer=boolean):
    """
    renderer is NOT undoable, queryable, and editable.
    

    
Command to register renders. This command allows you to specify the UI name and procedure names for renderers. The command also allow you to query the UI name and the procedure names for the registered renders.

    """
    pass
    


def renderGlobalsNode(renderQuality=string, renderResolution=string):
    """
    renderGlobalsNode is undoable, NOT queryable, and NOT editable.
    

    
The renderGlobalsNode creates a render globals node and registers it with the model. The createNode command will not register nodes of this type correctly.

    """
    pass
    


def renderInfo(castShadows=boolean, chordHeight=float, chordHeightRatio=float, doubleSided=boolean, edgeSwap=boolean, minScreen=float, opposite=boolean, smoothShading=boolean, unum=int, useChordHeight=boolean, useChordHeightRatio=boolean, useDefaultLights=boolean, useMinScreen=boolean, utype=int, vnum=int, vtype=int):
    """
    renderInfo is undoable, queryable, and editable.
    

    
The renderInfo commands sets geometric properties of surfaces of the selected object.

    """
    pass
    


def renderLayerPostProcess(keepImages=boolean, sceneName=string):
    """
    renderLayerPostProcess is NOT undoable, queryable, and NOT editable.
    

    
Post process the results when rendering is done with. Presently this generates a layered PSD file using individual iff files.

    """
    pass
    


def renderManip( object , camera=boolean, boolean, boolean, boolean, boolean, light=boolean, boolean, boolean, spotLight=boolean, boolean, boolean, boolean, boolean, boolean, boolean, state=boolean):
    """
    renderManip is undoable, queryable, and editable.
    

    
This command creates manipulators for cameras or lights.

    """
    pass
    


def renderPartition( string ):
    """
    renderPartition is undoable, queryable, and NOT editable.
    

    
Set or query the model's current partition. When flag q is not used, a partion name must be passed as an argument. In this case the current partition is set to that name.

    """
    pass
    


def renderPassRegistry(channels=int, isPassSupported=boolean, passID=string, passName=boolean, renderer=string, supportedChannelCounts=boolean, supportedDataTypes=boolean, supportedPassSemantics=boolean, supportedRenderPassNames=boolean, supportedRenderPasses=boolean):
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
    


def renderSettings(camera=string, customTokenString=string, firstImageName=boolean, fullPath=boolean, fullPathTemp=boolean, genericFrameImageName=string, imageGenericName=boolean, lastImageName=boolean, layer=string, leaveUnmatchedTokens=boolean):
    """
    renderSettings is NOT undoable, NOT queryable, and NOT editable.
    

    
Query interface to the common tab of the render settings

    """
    pass
    


def renderThumbnailUpdate( boolean , forceUpdate=string):
    """
    renderThumbnailUpdate is undoable, queryable, and NOT editable.
    

    
Toggle the updating of object thumbnails. These are visible in tools like the Attribute Editor and Hypershade. All thumbnails everywhere will not update to reflect changes to the object until this command is used to toggle to true unless a specific thumbnail is forced to render using the -forceUpdate flag.

    """
    pass
    


def renderWindowEditor( editorName , autoResize=boolean, blendMode=int, caption=string, changeCommand=string, string, string, string, clear=int, int, float, float, float, cmEnabled=boolean, colorManage=boolean, compDisplay=int, compImageFile=string, control=boolean, currentCamera=string, currentCameraRig=string, defineTemplate=string, displayImage=int, displayImageViewCount=int, displayStyle=string, docTag=string, doubleBuffer=boolean, drawAxis=boolean, editorName=boolean, exists=boolean, exposure=float, filter=string, forceMainConnection=string, frameImage=boolean, frameRegion=boolean, gamma=float, highlightConnection=string, loadImage=string, lockMainConnection=boolean, mainListConnection=string, marquee=float, float, float, float, nbImages=boolean, nextViewImage=boolean, panel=string, parent=string, pcaption=string, realSize=boolean, refresh=boolean, removeAllImages=boolean, removeImage=boolean, resetRegion=boolean, resetViewImage=boolean, saveImage=boolean, scaleBlue=float, scaleGreen=float, scaleRed=float, selectionConnection=string, showRegion=int, int, singleBuffer=boolean, snapshot=string, int, int, stateString=boolean, stereo=int, stereoImageOrientation=string, string, stereoMode=string, toggle=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string, viewImageCount=int, viewTransformName=string, writeImage=string):
    """
    renderWindowEditor is undoable, queryable, and editable.
    

    
Create a editor window that can receive the result of the rendering process

    """
    pass
    


def renderWindowSelectContext(exists=boolean, image1=string, image2=string, image3=string):
    """
    renderWindowSelectContext is undoable, queryable, and editable.
    

    
Set the selection context for the render view panel.

    """
    pass
    


def reorder( objects... , back=boolean, front=boolean, relative=int):
    """
    reorder is undoable, NOT queryable, and NOT editable.
    

    
This command reorders (moves) objects relative to their siblings.
For relative moves, both positive and negative numbers may be specified. Positive numbers move the object forward and negative numbers move the object backward amoung its siblings. When an object is at the end (beginning) of the list of siblings, a relative move of 1 (-1) will put the object at the beginning (end) of the list of siblings. That is, relative moves will wrap if necessary.
If a shape is specified and it is the only child then its parent will be reordered.

    """
    pass
    


def reorderContainer(back=boolean, front=boolean, relative=int):
    """
    reorderContainer is undoable, queryable, and editable.
    

    
This command reorders (moves) objects relative to their siblings in a container.
For relative moves, both positive and negative numbers may be specified. Positive numbers move the object forward and negative numbers move the object backward amoung its siblings. When an object is at the end (beginning) of the list of siblings, a relative move of 1 (-1) will put the object at the beginning (end) of the list of siblings. That is, relative moves will wrap if necessary.
Only nodes within one container can be moved at a time. Note: The container command's -nodeList flag will return a sorted list of contained nodes. To see the effects of reordering, use the -unsortedOrder flag in conjunction with the -nodeList flag.

    """
    pass
    


def reorderDeformers( string string selectionList , name=string):
    """
    reorderDeformers is undoable, NOT queryable, and NOT editable.
    

    
This command changes the order in which 2 deformation nodes affect the output geometry. The first string argument is the name of deformer1, the second is deformer2, followed by the list of objects they deform.
It inserts deformer2 before deformer1. Currently supported deformer nodes include: sculpt, cluster, jointCluster, lattice, wire, jointLattice, boneLattice, blendShape.

    """
    pass
    


def requires( string string , dataType=string, nodeType=string):
    """
    requires is undoable, NOT queryable, and NOT editable.
    

    
This command is used during file I/O to specify the requirements needed to load the given file. It defines what file format version was used to write the file, or what plug-ins are required to load the scene.
The first string names a product (either "maya", or a plug-in name)
The second string gives the version. This command is only useful during file I/O, so users should not have any need to use this command themselves.
The flags "-nodeType" and "-dataType" specify the node types and data types defined by the plug-in. When Maya open a scene file, it runs "requires" command in the file and load required plug-ins. But some plug-ins may be not loaded because they are missing. The flags "-nodeType" and "-dataType" are used by the missing plug-ins. If one plug-in is missing, nodes and data created by this plug-in are created as unknown nodes and unknown data. Maya records their original types for these unknown nodes and data. When these nodes and data are saved back to file, it will be possible to determine the associated missing plug-ins. And when export selected nodes, Maya can write out the exact required plug-ins. The flags "-nodeType" and "-dataType" is optional. In this command, if these flags are not given for one plug-in and the plug-in is missing, the "requires" command of this plug-in will always be saved back.

    """
    pass
    


def reroot( object ):
    """
    reroot is undoable, NOT queryable, and NOT editable.
    

    
This command will reroot a skeleton. The selected joint or the given joint at the command line will be the new root of the skeleton. All ikHandles passing through the selected joint or above it will be deleted.
The given(or selected) joint should not have skin attached. The command works on the given or selected joint. No options or flags are necessary.

    """
    pass
    


def resampleFluid(resampleDepth=int, resampleHeight=int, resampleWidth=int):
    """
    resampleFluid is undoable, queryable, and editable.
    

    
A command to extend the fluid grid, keeping the voxels the same size, and keeping the existing contents of the fluid in the same place. Note that the fluid transform is also modified to make this possible.

    """
    pass
    


def resetTool( string ):
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
    


def resourceManager(nameFilter=string, saveAs=string, string):
    """
    resourceManager is NOT undoable, NOT queryable, and NOT editable.
    

    
List resources matching certain properties.

    """
    pass
    


def retimeKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, moveByFrame=int, name=string, snapOnFrame=boolean):
    """
    retimeKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the graph editor using the retime tool.

    """
    pass
    


def reverseCurve( curve , caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, name=string, nodeState=int, object=boolean, range=boolean, replaceOriginal=boolean):
    """
    reverseCurve is undoable, queryable, and editable.
    

    
The reverseCurve command reverses the direction of a curve or curve-on-surface. A string is returned containing the pathname of the newly reversed curve and the name of the resulting dependency node. The reversed curve has the same parameter range as the original curve.

    """
    pass
    


def reverseSurface( surface , caching=boolean, constructionHistory=boolean, direction=int, name=string, nodeState=int, object=boolean, replaceOriginal=boolean):
    """
    reverseSurface is undoable, queryable, and editable.
    

    
The reverseSurface command reverses one or both directions of a surface or can be used to "swap" the U and V directions (this creates the effect of reversing the surface normal). The name of the newly reversed surface and the name of the resulting dependency node is returned. The resulting surface has the same parameter ranges as the original surface.
This command also handles selected surface isoparms. For a selected isoparm, imagine that the isoparm curve is reversed after the operation. E.g. reverseSurface surface.v[0.1] will reverse in the U direction.

    """
    pass
    


def revolve( curve , autoCorrectNormal=boolean, axis=linear, linear, linear, axisChoice=int, axisX=linear, axisY=linear, axisZ=linear, bridge=boolean, caching=boolean, computePivotAndAxis=int, constructionHistory=boolean, degree=int, endSweep=angle, name=string, nodeState=int, object=boolean, pivot=linear, linear, linear, pivotX=linear, pivotY=linear, pivotZ=linear, polygon=int, radius=linear, radiusAnchor=float, range=boolean, rebuild=boolean, sections=int, startSweep=angle, tolerance=linear, useLocalPivot=boolean, useTolerance=boolean):
    """
    revolve is undoable, queryable, and editable.
    

    
This command creates a revolved surface by revolving the given profile curve about an axis. The profile curve can be a curve, curve-on-surface, surface isoparm, or trim edge.

    """
    pass
    


def rigidBody(active=boolean, angularVelocity=boolean, applyForceAt=string, bounciness=float, cache=boolean, centerOfMass=float, float, float, collisions=boolean, contactCount=boolean, contactName=boolean, contactPosition=boolean, damping=float, deleteCache=boolean, dynamicFriction=float, force=boolean, ignore=boolean, impulse=float, float, float, impulsePosition=float, float, float, initialAngularVelocity=float, float, float, initialVelocity=float, float, float, layer=int, lockCenterOfMass=boolean, mass=float, name=string, orientation=float, float, float, particleCollision=boolean, passive=boolean, position=float, float, float, solver=string, spinImpulse=float, float, float, standInObject=string, staticFriction=float, tesselationFactor=int, velocity=boolean):
    """
    rigidBody is undoable, queryable, and editable.
    

    
This command creates a rigid body from a polygonal or nurbs surface.

    """
    pass
    


def rigidSolver(autoTolerances=boolean, bounciness=boolean, cacheData=boolean, collide=boolean, collisionTolerance=float, contactData=boolean, create=boolean, current=boolean, deleteCache=boolean, displayCenterOfMass=boolean, displayConstraint=boolean, displayVelocity=boolean, dynamics=boolean, friction=boolean, interpenetrate=boolean, interpenetrationCheck=boolean, rigidBodies=boolean, rigidBodyCount=boolean, showCollision=boolean, showInterpenetration=boolean, solverMethod=int, startTime=float, state=boolean, statistics=boolean, stepSize=float, velocityVectorScale=float):
    """
    rigidSolver is undoable, queryable, and editable.
    

    
This command sets the attributes for the rigid solver

    """
    pass
    


def roll( camera , absolute=boolean, degree=angle, relative=boolean):
    """
    roll is undoable, NOT queryable, and NOT editable.
    

    
The roll command rotates a camera about its viewing direction, a positive angle produces clockwise camera rotation, while a negative angle produces counter-clockwise camera rotation.
The default mode is relative and the rotation is applied with respect to the current orientation of the camera. When mode is set to absolute, the rotation is applied with respect to the plane constructed from the following three vectors in the world space: the world up vector, the camera view vector, and the camera up vector.
The rotation angle is specified in degrees.
The roll command can be applied to either a perspective or an orthographic camera.
This command may be applied to more than one camera; objects that are not cameras are ignored. When no camera name supplied, this command is applied to all currently active cameras.

    """
    pass
    


def rollCtx( context , alternateContext=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, rollScale=float, toolName=string):
    """
    rollCtx is undoable, queryable, and editable.
    

    
Create, edit, or query a roll context.

    """
    pass
    


def rotate( float float float objects , absolute=boolean, centerPivot=boolean, constrainAlongNormal=boolean, deletePriorHistory=boolean, euler=boolean, forceOrderXYZ=boolean, objectCenterPivot=boolean, objectSpace=boolean, pivot=linear, linear, linear, preserveChildPosition=boolean, preserveGeometryPosition=boolean, preserveUV=boolean, reflection=boolean, reflectionAboutBBox=boolean, reflectionAboutOrigin=boolean, reflectionAboutX=boolean, reflectionAboutY=boolean, reflectionAboutZ=boolean, reflectionTolerance=float, relative=boolean, rotateX=boolean, rotateXY=boolean, rotateXYZ=boolean, rotateXZ=boolean, rotateY=boolean, rotateYZ=boolean, rotateZ=boolean, symNegative=boolean, translate=boolean, worldSpace=boolean, xformConstraint=string):
    """
    rotate is undoable, NOT queryable, and NOT editable.
    

    
The rotate command is used to change the rotation of geometric objects. The rotation values are specified as Euler angles (rx, ry, rz). The values are interpreted based on the current working unit for Angular measurements. Most often this is degrees.
The default behaviour, when no objects or flags are passed, is to do a absolute rotate on each currently selected object in the world space.

    """
    pass
    


def rotationInterpolation(convert=string):
    """
    rotationInterpolation is undoable, queryable, and NOT editable.
    

    
The rotationInterpolation command converts the rotation curves to the desired rotation interpolation representation. For example, an Euler-angled representation can be converted to Quaternion.

    """
    pass
    


def roundConstantRadius( string string string string , append=boolean, constructionHistory=boolean, name=string, object=boolean, radiuss=linear, side=string, int, sidea=int, sideb=int):
    """
    roundConstantRadius is undoable, queryable, and editable.
    

    
This command generates constant radius NURBS fillets and NURBS corner surfaces for matching edge pairs on NURBS surfaces. An edge pair is a matching pair of surface isoparms or trim edges. This command can handle more than one edge pair at a time. This command can also handle compound edges, which is where an edge pair is composed of more than two surfaces. Use the "-sa" and "-sb" flags in this case.
The results from this command are three surface var groups plus the name of the new roundConstantRadius dependency node, if history was on. The 1st var group contains trimmed copies of the original surfaces. The 2nd var group contains the new NURBS fillet surfaces. The 3rd var group contains the new NURBS corners (if any).
A simple example of an edge pair is an edge of a NURBS cube, where two faces of the cube meet. This command generates a NURBS fillet at the edge and trims back the faces.
Another example is a NURBS cylinder with a planar trim surface cap. This command will create a NURBS fillet where the cap meets the the cylinder and will trim back the cap and the cylinder.
Another example involves all 12 edges of a NURBS cube. NURBS fillets are created where any face meets another face. NURBS corners are created whenever 3 edges meet at a corner.

    """
    pass
    


def rowColumnLayout( string , annotation=string, backgroundColor=float, float, float, childArray=boolean, columnAlign=int, string, columnAttach=int, string, int, columnOffset=int, string, int, columnSpacing=int, int, columnWidth=int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfColumns=int, numberOfPopupMenus=boolean, numberOfRows=int, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAlign=int, string, rowAttach=int, string, int, rowHeight=int, int, rowOffset=int, string, int, rowSpacing=int, int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    rowColumnLayout is undoable, queryable, and editable.
    

    
This command creates a rowColumn layout. A rowColumn layout positions children in either a row or column format. A column layout, specified with the -nc/numberOfColumns flag, allows you set text alignment, attachments and offsets for each column in the layout. Every member of a column will have the same alignment, attachment and offsets. Likewise the row format, specified by the -nr/numberOfRows flag, allows setting of these attributes for each row in the layout. Every member of a row will have the same attributes. The layout must be either a row or column format. This layout does not support both, or the specification of attributes on an individual child basis.
Some flags only make sense for one of either the row format or the column format. For example the -rh/rowHeight flag can only be specified in row format. In column format the row height is determined by the tallest child in the row, plus offsets.

    """
    pass
    


def rowLayout( string , adjustableColumn=int, adjustableColumn1=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, childArray=boolean, columnAlign=int, string, columnAlign1=string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach1=string, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset1=int, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfColumns=int, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    rowLayout is undoable, queryable, and editable.
    

    
This command creates a layout capable of positioning children into a single horizontal row.

    """
    pass
    


def runup(cache=boolean, fromPreviousFrame=boolean, fromStartFrame=boolean, maxFrame=time, state=boolean):
    """
    runup is undoable, NOT queryable, and NOT editable.
    

    
runup plays the scene through a frame of frames, forcing dynamic objects to evaluate as it does so. If no max frame is specified, runup runs up to the current time.

    """
    pass
    


def sampleImage(fastSample=boolean, resolution=int, name):
    """
    sampleImage is undoable, NOT queryable, and NOT editable.
    

    
The sampleImage command is used to control parameters of sample images, such as swatches in the multilister. The fast option turns on or off some rendering cheats which speed up the render but may cause edges to look ragged. The resolution option specifies the width in pixels of the image which will be rendered for the specified node. Note that the width of the image is also the height of the image since sample images are square.

    """
    pass
    


def saveAllShelves( string ):
    """
    saveAllShelves is undoable, NOT queryable, and NOT editable.
    

    
This command writes all shelves that are immediate children of the specified control layout to the prefs directory.

    """
    pass
    


def saveFluid(currentTime=int, endTime=int, startTime=int):
    """
    saveFluid is undoable, queryable, and editable.
    

    
A command to save the current state of the fluid to the initial state cache. The grids to be saved are determined by the cache attributes: cacheDensity, cacheVelocity, etc. These attributes are normally set from the options on Set Initial State. The cache must be set up before invoking this command.

    """
    pass
    


def saveImage( imageName , annotation=string, backgroundColor=float, float, float, currentView=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, objectThumbnail=string, parent=string, popupMenuArray=boolean, preventOverride=boolean, sceneFile=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    saveImage is undoable, queryable, and editable.
    

    
This command creates a static image control for non-xpm files used to display a thumbnail image of the scene file.

    """
    pass
    


def saveInitialState( selectionList , attribute=string, saveall=boolean):
    """
    saveInitialState is undoable, NOT queryable, and NOT editable.
    

    
saveInitialState saves the current state of dynamics objects as the initial state. A dynamic object is a particle shape, rigid body, rigid constraint or rigid solver. If no objects are specified, it saves the initial state for any selected objects. It returns the names of the objects for which initial state was saved.

    """
    pass
    


def saveMenu( string string ):
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
    


def savePrefs(colors=boolean, general=boolean, hotkeys=boolean, plugins=boolean, uiLayout=boolean):
    """
    savePrefs is undoable, NOT queryable, and NOT editable.
    

    
This command saves preferences to disk. If no flags are specified then all pref types get saved out.

    """
    pass
    


def saveShelf( string string ):
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
    


def scale( float float float objects , absolute=boolean, centerPivot=boolean, constrainAlongNormal=boolean, deletePriorHistory=boolean, distanceOnly=boolean, objectCenterPivot=boolean, pivot=linear, linear, linear, preserveChildPosition=boolean, preserveGeometryPosition=boolean, preserveUV=boolean, reflection=boolean, reflectionAboutBBox=boolean, reflectionAboutOrigin=boolean, reflectionAboutX=boolean, reflectionAboutY=boolean, reflectionAboutZ=boolean, reflectionTolerance=float, relative=boolean, scaleX=boolean, scaleXY=boolean, scaleXYZ=boolean, scaleXZ=boolean, scaleY=boolean, scaleYZ=boolean, scaleZ=boolean, symNegative=boolean, xformConstraint=string):
    """
    scale is undoable, NOT queryable, and NOT editable.
    

    
The scale command is used to change the sizes of geometric objects.
The default behaviour, when no objects or flags are passed, is to do a relative scale on each currently selected object object using each object's existing scale pivot point.

    """
    pass
    


def scaleComponents( float float float objects , pivot=linear, linear, linear, rotation=angle, angle, angle):
    """
    scaleComponents is undoable, NOT queryable, and NOT editable.
    

    
This is a limited version of the scale command. First, it only works on selected components. You provide a pivot in world space, and you can provide a rotation. This rotation affects the scaling, so that rather than scaling in X, Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given rotation.
This allows selected components to be scaled in any arbitrary space, not just object or world space as the regular scale allows.
Scale values are always relative, not absolute.

    """
    pass
    


def scaleConstraint( target... object , layer=string, maintainOffset=boolean, name=string, offset=float, float, float, remove=boolean, scaleCompensate=boolean, skip=string, targetList=boolean, weight=float, weightAliasList=boolean):
    """
    scaleConstraint is undoable, queryable, and editable.
    

    
Constrain an object's scale to the scale of the target object or to the average scale of a number of targets.
A scaleConstraint takes as input one or more "target" DAG transform nodes to which to scale the single "constraint object" DAG transform node. The scaleConstraint scales the constrained object at the weighted geometric mean of the world space target scale factors.

    """
    pass
    


def scaleKey( objects , animation=string, attribute=string, controlPoints=boolean, float=floatrange, floatPivot=float, floatScale=float, hierarchy=string, includeUpperBound=boolean, index=uint, newEndFloat=float, newEndTime=time, newStartFloat=float, newStartTime=time, scaleSpecifiedKeys=boolean, shape=boolean, time=timerange, timePivot=time, timeScale=float, valuePivot=float, valueScale=float):
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
    


def scaleKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, scaleSpecifiedKeys=boolean, type=string):
    """
    scaleKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to scale keyframes within the graph editor

    """
    pass
    


def sceneEditor(control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, onlyParents=boolean, panel=string, parent=string, refreshReferences=boolean, selectCommand=script, selectItem=int, selectReference=string, selectionConnection=string, shortName=boolean, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, unresolvedName=boolean, updateMainConnection=boolean, useTemplate=string, withoutCopyNumber=boolean):
    """
    sceneEditor is undoable, queryable, and editable.
    

    
This creates an editor for managing the files in a scene.

    """
    pass
    


def sceneUIReplacement(clear=boolean, deleteRemaining=boolean, getNextFilter=string, string, getNextPanel=string, string, getNextScriptedPanel=string, string, update=string):
    """
    sceneUIReplacement is undoable, NOT queryable, and NOT editable.
    

    
This command returns existing scene based UI that can be utilized by the scene that is being loaded. It can also delete any such UI that is not used by the loading scene.

    """
    pass
    


def scmh( float float... , absolute=boolean, ignore=uint, quiet=boolean, relative=boolean):
    """
    scmh is undoable, NOT queryable, and NOT editable.
    

    
Set the current manipulator handle value(s). In UI units (where applicable), though the syntax is set to handle the unit type of the current manipulator handle (if available).

    """
    pass
    


def scriptCtx( string , baseClassName=string, cumulativeLists=boolean, enableRootSelection=boolean, exists=boolean, exitUponCompletion=boolean, expandSelectionList=boolean, finalCommandScript=script, forceAddSelect=boolean, history=boolean, ignoreInvalidItems=boolean, image1=string, image2=string, image3=string, lastAutoComplete=boolean, name=string, setAllowExcessCount=boolean, setAutoComplete=boolean, setAutoToggleSelection=boolean, setDoneSelectionPrompt=string, setNoSelectionHeadsUp=string, setNoSelectionPrompt=string, setSelectionCount=int, setSelectionHeadsUp=string, setSelectionPrompt=string, showManipulators=boolean, title=string, toolCursorType=string, toolFinish=script, toolStart=script, totalSelectionSets=int):
    """
    scriptCtx is undoable, queryable, and editable.
    

    
This command allows a user to create their own tools based on the selection tool. A number of selection lists can be collected, the behaviour of the selection and the selection masks are fully customizable, etc.
The command is processed prior to being executed. The keyword "$Selection#" where # is a number 1 or greater specifies a selection set. The context can specify several selection sets which are substituted in place of the $Selection# keyword in the form of a Mel string array. Items that are specific per set need to be specified in each set, if they are going to be specified for any of the sets. See examples below.
In addition, in order to specify the type of selection you need to be making, any of the selection type flags from "selectType" command can be used here.

    """
    pass
    


def scriptEditorInfo(clearHistory=boolean, clearHistoryFile=boolean, historyFilename=string, input=string, suppressErrors=boolean, suppressInfo=boolean, suppressResults=boolean, suppressStackWindow=boolean, suppressWarnings=boolean, writeHistory=boolean):
    """
    scriptEditorInfo is undoable, queryable, and editable.
    

    
Use this command to directly manipulate and query the contents of the Command Window window.
Note: Due to recent changes, certain flags will no longer work on the Script Editor Window. All flags will continue to work with the CommandWindow (old Script Editor).
Note: This command cannot be used to create a new script editor window.

    """
    pass
    


def scriptedPanel( panelName , control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, tearOff=boolean, tearOffCopy=string, type=string, unParent=boolean, useTemplate=string):
    """
    scriptedPanel is undoable, queryable, and editable.
    

    
This command will create an instance of the specified scriptedPanelType. A panel is a collection of UI objects (buttons, fields, graphical views) that are grouped together. A panel can be moved around as a group within the application interface, and torn off to exist in its own window. The panel takes care of maintaining the state of its UI when it is relocated, or recreated. A scripted panel is a panel that is defined in MEL, with all of the required callbacks available as MEL proc's.

    """
    pass
    


def scriptedPanelType( string , addCallback=string, copyStateCallback=string, createCallback=string, customView=boolean, defineTemplate=string, deleteCallback=string, exists=boolean, initCallback=string, obsolete=boolean, removeCallback=string, retainOnFileOpen=boolean, saveStateCallback=string, unique=boolean, useTemplate=string):
    """
    scriptedPanelType is undoable, queryable, and editable.
    

    
This command defines the callbacks for a type of scripted panel. The panel type created by this command is then used when creating a scripted panel. See also the 'scriptedPanel' command.

    """
    pass
    


def scriptJob(allChildren=boolean, attributeAdded=string, script, attributeChange=string, script, attributeDeleted=string, script, compressUndo=boolean, conditionChange=string, script, conditionFalse=string, script, conditionTrue=string, script, connectionChange=string, script, disregardIndex=boolean, event=string, script, exists=int, force=boolean, idleEvent=script, kill=int, killAll=boolean, killWithScene=boolean, listConditions=boolean, listEvents=boolean, listJobs=boolean, nodeDeleted=string, script, nodeNameChanged=string, script, parent=string, permanent=boolean, protected=boolean, replacePrevious=boolean, runOnce=boolean, timeChange=script, uiDeleted=string, script):
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
    


def scriptNode( attributeList , afterScript=string, beforeScript=string, executeAfter=boolean, executeBefore=boolean, ignoreReferenceEdits=boolean, name=string, scriptType=int, sourceType=string):
    """
    scriptNode is undoable, queryable, and editable.
    

    
scriptNodes contain scripts that are executed when a file is loaded or when the script node is deleted. If a script modifies a referenced node, the changes will be tracked as reference edits unless the scriptNode was created with the ignoreReferenceEdits flag. The scriptNode command is used to create, edit, query, and test scriptNodes.

    """
    pass
    


def scriptTable( name , afterCellChangedCmd=script, annotation=string, backgroundColor=float, float, float, cellBackgroundColorCommand=script, cellChangedCmd=script, cellForegroundColorCommand=script, cellIndex=int, int, cellValue=string, clearRow=int, clearTable=boolean, columnFilter=int, string, columnWidth=int, int, columns=int, defineTemplate=string, deleteRow=int, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, excludingHeaders=boolean, exists=boolean, fullPathName=boolean, getCellCmd=script, height=int, highlightColor=float, float, float, insertRow=int, isObscured=boolean, label=int, string, manage=boolean, multiEditEnabled=int, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, rowHeight=boolean, rows=int, rowsRemovedCmd=script, rowsToBeRemovedCmd=script, selectedCells=int,..., selectedColumns=int,..., selectedRow=boolean, selectedRows=int,..., selectionBehavior=int, selectionChangedCmd=script, selectionMode=int, sortEnabled=boolean, underPointerColumn=boolean, underPointerRow=boolean, useDoubleClickEdit=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    scriptTable is undoable, queryable, and editable.
    

    
This command creates/edits/queries the script table control.

    """
    pass
    


def scrollField( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, clear=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, enterCommand=script, exists=boolean, font=string, fontPointSize=int, fullPathName=boolean, height=int, highlightColor=float, float, float, insertText=string, insertionPosition=int, isObscured=boolean, keyPressCommand=script, manage=boolean, noBackground=boolean, numberOfLines=int, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, qtFont=string, selection=boolean, text=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int, wordWrap=boolean):
    """
    scrollField is undoable, queryable, and editable.
    

    
This command creates a scrolling field that handles multiple lines of text.

    """
    pass
    


def scrollLayout( string , annotation=string, backgroundColor=float, float, float, borderVisible=boolean, childArray=boolean, childResizable=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontalScrollBarThickness=int, isObscured=boolean, manage=boolean, minChildWidth=int, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, panEnabled=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, resizeCommand=script, scrollAreaHeight=boolean, scrollAreaValue=boolean, scrollAreaWidth=boolean, scrollByPixel=string, int, scrollPage=string, useTemplate=string, verticalScrollBarAlwaysVisible=boolean, verticalScrollBarThickness=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    scrollLayout is undoable, queryable, and editable.
    

    
This command creates a scroll layout. A scroll layout is useful for when you have a number of controls which cannot all be visible at a time. This layout will display a horizontal and/or vertical scroll bar when necessary to bring into view the hidden controls. Since the scroll layout provides no real positioning of children you should use another control layout as the immediate child.

    """
    pass
    


def sculpt( selectionList , after=boolean, afterReference=boolean, before=boolean, deformerTools=boolean, dropoffDistance=linear, dropoffType=string, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, groupWithLocator=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, insideMode=string, maxDisplacement=linear, mode=string, name=string, objectCentered=boolean, parallel=boolean, prune=boolean, remove=boolean, sculptTool=string, split=boolean):
    """
    sculpt is undoable, queryable, and editable.
    

    
This command creates/edits/queries a sculpt object deformer. By default for creation mode an implicit sphere will be used as the sculpting object if no sculpt tool is specified. The name of the created/edited object is returned.

    """
    pass
    


def sculptMeshCacheCtx(adjustSize=boolean, adjustStrength=boolean, affectAllLayers=boolean, brushDirection=int, brushSize=float, brushStrength=float, buildUpRate=float, constrainToSurface=boolean, direction=int, displayFrozen=boolean, displayWireframe=boolean, falloffType=int, flood=float, floodFreeze=float, frame=boolean, freezeSelection=boolean, grabFollowPath=boolean, grabSilhouette=boolean, grabTwist=boolean, inverted=boolean, lastMode=string, lockShellBorder=boolean, minSize=float, minStrength=float, mirror=int, mode=string, orientToSurface=boolean, sculptFalloffCurve=string, size=float, stampDistance=float, stampFile=string, stampFlipX=boolean, stampFlipY=boolean, stampOrientToStroke=boolean, stampPlacement=int, stampRandomization=boolean, stampRandomizeFlipX=boolean, stampRandomizeFlipY=boolean, stampRandomizePosX=float, stampRandomizePosY=float, stampRandomizeRotation=float, stampRandomizeScale=float, stampRandomizeStrength=float, stampRotation=float, steadyStrokeDistance=float, strength=float, updatePlane=boolean, useGlobalSize=boolean, useScreenSpace=boolean, useStampDistance=boolean, useStampImage=boolean, useSteadyStroke=boolean, wholeStroke=boolean, wireframeAlpha=float, wireframeColor=float, float, float):
    """
    sculptMeshCacheCtx is undoable, queryable, and editable.
    

    
This is a tool context command for mesh cache sculpting tool.

    """
    pass
    


def sculptTarget( int , inbetweenWeight=float, regenerate=boolean, snapshot=int, target=float):
    """
    sculptTarget is undoable, NOT queryable, and editable.
    

    
This command is used to specify the blend shape target to be modified by the sculpting tools and transform manipulators.

    """
    pass
    


def select( objects... , add=boolean, addFirst=boolean, all=boolean, allDagObjects=boolean, allDependencyNodes=boolean, clear=boolean, containerCentric=boolean, deselect=boolean, hierarchy=boolean, noExpand=boolean, replace=boolean, symmetry=boolean, symmetrySide=int, toggle=boolean, visible=boolean):
    """
    select is undoable, NOT queryable, and NOT editable.
    

    
This command is used to put objects onto or off of the active list. If none of the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to replace the objects on the active list with the given list of objects.
When selecting a set as in "select set1", the behaviour is for all the members of the set to become selected instead of the set itself. If you want to select a set, the "-ne/noExpand" flag must be used.
With the advent of namespaces, selection by name may be confusing. To clarify, without a qualified namespace, name lookup is limited to objects in the root namespace ":". There are really two parts of a name: the namespace and the name itself which is unique within the namespace. If you want to select objects in a specific namespace, you need to include the namespace separator ":".
For example, 'select -r "foo*"' is trying to look for an object with the "foo" prefix in the root namespace. It is not trying to look for all objects in the namespace with the "foo" prefix. If you want to select all objects in a namespace (foo), use 'select "foo:*"'.
Note: When the application starts up, there are several dependency nodes created by the system which must exist. These objects are not deletable but are selectable. All objects (dag and dependency nodes) in the scene can be obtained using the "ls" command without any arguments. When using the "-all", "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only the deletable objects are selected. The non deletable object can still be selected by explicitly specifying their name as in "select time1;".

    """
    pass
    


def selectContext( string , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    selectContext is undoable, queryable, and editable.
    

    
Creates a context to perform selection.

    """
    pass
    


def selectionConnection( string , activeCacheList=boolean, activeCharacterList=boolean, activeList=boolean, addScript=script, addTo=string, characterList=boolean, clear=boolean, connectionList=boolean, defineTemplate=string, deselect=name, editor=string, exists=boolean, filter=string, findObject=name, g=boolean, highlightList=boolean, identify=boolean, keyframeList=boolean, lock=boolean, modelList=boolean, object=name, parent=string, remove=string, removeScript=script, select=name, setList=boolean, switch=boolean, useTemplate=string, worldList=boolean):
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
    


def selectKey( targetList , addTo=boolean, animation=string, attribute=string, clear=boolean, controlPoints=boolean, float=floatrange, hierarchy=string, inTangent=boolean, includeUpperBound=boolean, index=uint, keyframe=boolean, outTangent=boolean, remove=boolean, replace=boolean, shape=boolean, time=timerange, toggle=boolean, unsnappedKeys=float):
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
    


def selectKeyCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    selectKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to select keyframes within the graph editor

    """
    pass
    


def selectKeyframeRegionCtx( contextName , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    selectKeyframeRegionCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor

    """
    pass
    


def selectMode(component=boolean, hierarchical=boolean, leaf=boolean, object=boolean, preset=boolean, root=boolean, template=boolean):
    """
    selectMode is undoable, queryable, and NOT editable.
    

    
The selectMode command is used to change the selection mode. Object, component, root, leaf and template modes are mutually exclusive.

    """
    pass
    


def selectPref(affectsActive=boolean, allowHiliteSelection=boolean, autoSelectContainer=boolean, autoUseDepth=boolean, clickBoxSize=uint, clickDrag=boolean, containerCentricSelection=boolean, disableComponentPopups=boolean, expandPopupList=boolean, ignoreSelectionPriority=boolean, manipClickBoxSize=uint, paintSelect=boolean, paintSelectWithDepth=boolean, popupMenuSelection=boolean, preSelectBackfacing=boolean, preSelectClosest=boolean, preSelectDeadSpace=uint, preSelectHilite=boolean, preSelectHiliteSize=float, preSelectTweakDeadSpace=uint, selectionChildHighlightMode=int, singleBoxSelection=boolean, trackSelectionOrder=boolean, useDepth=boolean, xformNoSelect=boolean):
    """
    selectPref is undoable, queryable, and NOT editable.
    

    
This command controls state variables used to selection UI behavior.

    """
    pass
    


def selectPriority(allComponents=uint, allObjects=uint, animBreakdown=uint, animCurve=uint, animInTangent=uint, animKeyframe=uint, animOutTangent=uint, byName=string, boolean, camera=uint, cluster=uint, collisionModel=uint, controlVertex=uint, curve=uint, curveKnot=uint, curveOnSurface=uint, curveParameterPoint=uint, dimension=uint, dynamicConstraint=uint, edge=uint, editPoint=uint, emitter=uint, facet=uint, field=uint, fluid=uint, follicle=uint, hairSystem=uint, handle=uint, hull=uint, ikEndEffector=uint, ikHandle=uint, imagePlane=uint, implicitGeometry=uint, isoparm=uint, joint=uint, jointPivot=uint, lattice=uint, latticePoint=uint, light=uint, localRotationAxis=uint, locator=uint, locatorUV=uint, locatorXYZ=uint, meshUVShell=boolean, motionTrailPoint=uint, motionTrailTangent=uint, nCloth=uint, nParticle=uint, nParticleShape=uint, nRigid=uint, nonlinear=uint, nurbsCurve=uint, nurbsSurface=uint, orientationLocator=uint, particle=uint, particleShape=uint, plane=uint, polymesh=uint, polymeshEdge=uint, polymeshFace=uint, polymeshFreeEdge=uint, polymeshUV=uint, polymeshVertex=uint, polymeshVtxFace=uint, queryByName=string, rigidBody=uint, rigidConstraint=uint, rotatePivot=uint, scalePivot=uint, sculpt=uint, selectHandle=uint, spring=uint, springComponent=uint, stroke=uint, subdiv=uint, subdivMeshEdge=uint, subdivMeshFace=uint, subdivMeshPoint=uint, subdivMeshUV=uint, surfaceEdge=uint, surfaceFace=uint, surfaceKnot=uint, surfaceParameterPoint=uint, surfaceRange=uint, texture=uint, vertex=uint):
    """
    selectPriority is undoable, queryable, and NOT editable.
    

    
The selectPriority command is used to change the selection priority of particular types of objects that can be selected when using the select tool. It accepts no other arguments besides the flags. These flags are the same as used by the 'selectType' command.

    """
    pass
    


def selectType(allComponents=boolean, allObjects=boolean, animBreakdown=boolean, animCurve=boolean, animInTangent=boolean, animKeyframe=boolean, animOutTangent=boolean, byName=string, boolean, camera=boolean, cluster=boolean, collisionModel=boolean, controlVertex=boolean, curve=boolean, curveKnot=boolean, curveOnSurface=boolean, curveParameterPoint=boolean, dimension=boolean, dynamicConstraint=boolean, edge=boolean, editPoint=boolean, emitter=boolean, facet=boolean, field=boolean, fluid=boolean, follicle=boolean, hairSystem=boolean, handle=boolean, hull=boolean, ikEndEffector=boolean, ikHandle=boolean, imagePlane=boolean, implicitGeometry=boolean, isoparm=boolean, joint=boolean, jointPivot=boolean, lattice=boolean, latticePoint=boolean, light=boolean, localRotationAxis=boolean, locator=boolean, locatorUV=boolean, locatorXYZ=boolean, meshUVShell=boolean, motionTrailPoint=boolean, motionTrailTangent=boolean, nCloth=boolean, nParticle=boolean, nParticleShape=boolean, nRigid=boolean, nonlinear=boolean, nurbsCurve=boolean, nurbsSurface=boolean, objectComponent=boolean, orientationLocator=boolean, particle=boolean, particleShape=boolean, plane=boolean, polymesh=boolean, polymeshEdge=boolean, polymeshFace=boolean, polymeshFreeEdge=boolean, polymeshUV=boolean, polymeshVertex=boolean, polymeshVtxFace=boolean, queryByName=string, rigidBody=boolean, rigidConstraint=boolean, rotatePivot=boolean, scalePivot=boolean, sculpt=boolean, selectHandle=boolean, spring=boolean, springComponent=boolean, stroke=boolean, subdiv=boolean, subdivMeshEdge=boolean, subdivMeshFace=boolean, subdivMeshPoint=boolean, subdivMeshUV=boolean, surfaceEdge=boolean, surfaceFace=boolean, surfaceKnot=boolean, surfaceParameterPoint=boolean, surfaceRange=boolean, surfaceUV=boolean, texture=boolean, vertex=boolean):
    """
    selectType is undoable, queryable, and NOT editable.
    

    
The selectType command is used to change the set of allowable types of objects that can be selected when using the select tool. It accepts no other arguments besides the flags.
There are basically two different types of items that are selectable when interactively selecting objects in the 3D views. They are classified as objects (entire objects) or components (parts of objects). The object and component command flags control which class of objects are selectable.
It is possible to select components while in the object selection mode. To set the components which are selectable in object selection mode you must use the -ocm flag when specifying the component flags.

    """
    pass
    


def selLoadSettings(activeProxy=string, deferReference=boolean, fileName=string, numSettings=uint, proxyManager=string, proxySetFiles=string, proxySetTags=string, proxyTag=string, referenceNode=string, shortName=boolean, unresolvedName=boolean):
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
    


def separator( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontal=boolean, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, style=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    separator is undoable, queryable, and editable.
    

    
This command creates a separator widget in a variety of drawing styles.

    """
    pass
    


def sequenceManager(addSequencerAudio=string, attachSequencerAudio=string, currentShot=string, currentTime=time, listSequencerAudio=string, listShots=boolean, modelPanel=string, node=string, writableSequencer=string):
    """
    sequenceManager is undoable, queryable, and editable.
    

    
The sequenceManager command manages sequences, shots, and their related scenes.

    """
    pass
    


def setAttr( attribute Any Any... , alteredValue=boolean, caching=boolean, capacityHint=uint, channelBox=boolean, clamp=boolean, keyable=boolean, lock=boolean, size=uint, type=string):
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
    


def setAttrMapping(absolute=boolean, attribute=string, axis=string, clutch=string, device=string, offset=float, relative=boolean, scale=float, selection=boolean):
    """
    setAttrMapping is undoable, queryable, and NOT editable.
    

    
This command applies an offset and scale to a specified device attachment. This command is different than the setInputDeviceMapping command, which applies a mapping to a device axis.
The value from the device is multiplied by the scale and the offset is added to this product. With an absolute mapping, the attached attribute gets the resulting value. If the mapping is relative, the resulting value is added to the previous calculated value. The calculated value will also take into account the setInputDeviceMapping, if it was defined.
As an example, if the space ball is setup with absolute attachment mappings, pressing in one direction will cause the attached attribute to get a constant value. If a relative mapping is used, and the spaceball is pressed in one direction, the attached attribute will get a constantly increasing (or constantly decreasing) value.
Note that the definition of relative is different than the definition used by the setInputDeviceMapping command. In general, both a relative attachment mapping (this command) and a relative device mapping (setInputDeviceMapping) should not be used together one the same axis.

    """
    pass
    


def setDefaultShadingGroup( string ):
    """
    setDefaultShadingGroup is undoable, queryable, and NOT editable.
    

    
The setDefaultShadingGroup command is used to change which shading group is considered the current default shading group. Subsequently created objects will be assigned to the new default group.

    """
    pass
    


def setDrivenKeyframe( objects , attribute=string, controlPoints=boolean, currentDriver=string, driven=boolean, driver=boolean, driverValue=float, hierarchy=string, inTangentType=string, insert=boolean, insertBlend=boolean, outTangentType=string, shape=boolean, value=float):
    """
    setDrivenKeyframe is undoable, queryable, and editable.
    

    
This command sets a driven keyframe. A driven keyframe is similar to a regular keyframe. However, while a standard keyframe always has an x-axis of time in the graph editor, for a drivenkeyframe the user may choose any attribute as the x-axis of the graph editor.

For example, you can keyframe the emission of a faucet so that so that it emits whenever the faucet handle is rotated around y. The faucet emission in this example is called the driven attribute. The handle rotation is called the driver. Once you have used setDrivenKeyframe to set up the relationship between the emission and the rotation, you can go to the graph editor and modify the relationship between the attributes just as you would modify the animation curve on any keyframed object.

In the case of an attribute driven by a single driver, the dependency graph is connected like this:

driver attribute ---> animCurve ---> driven attribute

You can set driven keyframes with more than a single driver. The effects of the multiple drivers are combined together by a blend node.

    """
    pass
    


def setDynamic( selectionList , allOnWhenRun=boolean, disableAllOnWhenRun=boolean, setAll=boolean, setOff=boolean, setOn=boolean):
    """
    setDynamic is undoable, NOT queryable, and NOT editable.
    

    
setDynamic sets the isDynamic attribute of particle objects on or off. If no objects are specified, it sets the attribute for any selected objects. If -all is thrown, it sets the attribute for all particle objects in the scene. By default it sets the attribute true (on); if the -off flag is thrown, it sets the attribute false (off).
WARNING: setDynamic is obsolescent. This is the last version of Maya in which it will be supported.

    """
    pass
    


def setEditCtx( name , exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    setEditCtx is undoable, queryable, and editable.
    

    
This command creates a tool that can be used to modify set membership.

    """
    pass
    


def setFluidAttr(addValue=boolean, attribute=string, clear=boolean, floatRandom=float, floatValue=float, lowerFace=boolean, reset=boolean, vectorRandom=float, float, float, vectorValue=float, float, float, xIndex=int, xvalue=boolean, yIndex=int, yvalue=boolean, zIndex=int, zvalue=boolean):
    """
    setFluidAttr is NOT undoable, NOT queryable, and NOT editable.
    

    
Sets values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in the grid.

    """
    pass
    


def setFocus( string ):
    """
    setFocus is undoable, NOT queryable, and NOT editable.
    

    
Give keyboard focus to a specific control or panel, passed as an argument.

    """
    pass
    


def setInfinity(attribute=string, controlPoints=boolean, hierarchy=string, postInfinite=string, preInfinite=string, shape=boolean):
    """
    setInfinity is undoable, queryable, and editable.
    

    
Set the infinity type before (after) a paramCurve's first (last) keyframe.

    """
    pass
    


def setInputDeviceMapping(absolute=boolean, axis=string, device=string, offset=float, relative=boolean, scale=float, view=boolean, world=boolean):
    """
    setInputDeviceMapping is undoable, NOT queryable, and NOT editable.
    

    
The command sets a scale and offset for all attachments made to a specified device axis. Any attachment made to a mapped device axis will have the scale and offset applied to its values.
The value from the device is multiplied by the scale and the offset is added to this product. With an absolute mapping, the attached attribute gets the resulting value. If the mapping is relative, the final value is the offset added to the scaled difference between the current device value and the previous device value.
This mapping will be applied to the device data before any mappings defined by the setAttrMapping command. A typical use would be to scale a device's input so that it is within a usable range. For example, the device mapping can be used to calibrate a spaceball to work in a specific section of a scene.
As an example, if the space ball is setup with absolute device mappings, constantly pressing in one direction will cause the attached attribute to get a constant value. If a relative mapping is used, and the spaceball is pressed in one direction, the attached attribute will jump a constantly increasing (or constantly decreasing) value and will find a rest value equal to the offset.
There are important differences between how the relative flag is handled by this command and the setAttrMapping command. (See the setAttrMapping documentation for specifics on how it calculates relative values). In general, both a relative device mapping (this command) and a relative attachment mapping (setAttrMapping) should not be used together on the same axis.

    """
    pass
    


def setKeyCtx( contextName , breakdown=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    setKeyCtx is undoable, queryable, and editable.
    

    
This command creates a context which may be used to set keys within the graph editor

    """
    pass
    


def setKeyframe( objects , animLayer=string, animated=boolean, attribute=string, breakdown=boolean, clip=string, controlPoints=boolean, float=float, hierarchy=string, identity=boolean, inTangentType=string, insert=boolean, insertBlend=boolean, minimizeRotation=boolean, noResolve=boolean, outTangentType=string, respectKeyable=boolean, shape=boolean, time=time, useCurrentLockedWeights=boolean, value=float):
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
    


def setKeyPath( object ):
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
    


def setNodeTypeFlag( string , display=boolean, threadSafe=boolean):
    """
    setNodeTypeFlag is undoable, queryable, and NOT editable.
    

    
This command sets static data on the specified node type. This will affect the class of node type as a whole. The argument passed may be the name of the node type or the node type tag. Node type tags may be found using the objectType command.

    """
    pass
    


def setParent( string , defineTemplate=string, menu=boolean, topLevel=boolean, upLevel=boolean, useTemplate=string):
    """
    setParent is undoable, queryable, and NOT editable.
    

    
This command changes the default parent to be the specified parent. Two special parents are "|" which indicates the top level layout of the window hierarchy, or ".." which indicates one level up in the hierarchy. Trying to move above the top level has no effect.
A control must be parented to a control layout. A control layout may be parented to another control layout or a window. A menu may be parented to a window or a menu bar layout. For all of these cases the setParent command (with no flags) will indicate the current default parent.
A menu item must be parented to a menu. To specify the default menu parent use the command setParent -m/menu. Note that all menu item objects created using the -sm/subMenu may also be treated as menu objects.
The default parent is ignored by any object that explicitly sets the -p/parent flag when it is created.

    """
    pass
    


def setParticleAttr( selectionList , attribute=string, floatValue=float, object=string, randomFloat=float, randomVector=float, float, float, relative=boolean, vectorValue=float, float, float):
    """
    setParticleAttr is undoable, NOT queryable, and NOT editable.
    

    
This action will set the value of the chosen attribute for every particle or selected component in the selected or passed particle object. Components should not be passed to the command line. For setting the values of components, the components must be selected and only the particle object's names should be passed to this action. If the attribute is a vector attribute and the -vv flag is passed, then the three floats passed will be used to set the values. If the attribute is a vector and the -fv flag is pass and the -vv flag is not passed, then the float will be repeated for each of the X, Y, and Z values of the attribute. Similarly, if the attribute is a float attribute and a vector value is passed, then the length of the vector passed will be used for the value. Note: The attribute passed must be a Per-Particle attribute.

    """
    pass
    


def setRenderPassType(defaultDataType=boolean, numChannels=int, type=string):
    """
    setRenderPassType is undoable, NOT queryable, and NOT editable.
    

    
This command will set the passID of a renderPass node and create the custom attributes specified by the corresponding render pass definition. If the render pass node already has a passID assigned to it, attributes that are no longer required become hidden, and new attributes are unhidden and/or created as needed. This allows passIDs to be changed back and forth without losing attribute data. It also allows common attributes to be transported from one render pass type to another.

    """
    pass
    


def sets( selectionList , addElement=name, afterFilters=boolean, clear=name, color=int, copy=name, edges=boolean, editPoints=boolean, empty=boolean, facets=boolean, flatten=name, forceElement=name, include=name, intersection=name, isIntersecting=name, isMember=name, layer=boolean, name=string, noSurfaceShader=boolean, noWarnings=boolean, nodesOnly=boolean, remove=name, renderable=boolean, size=boolean, split=name, subtract=name, text=string, union=name, vertices=boolean):
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
    


def setStartupMessage( string ):
    """
    setStartupMessage is undoable, NOT queryable, and NOT editable.
    

    
Update the startup window message. Also know as the 'Splash Screen', this is the window that appears while the application is starting up.

    """
    pass
    


def setToolTo( string ):
    """
    setToolTo is undoable, NOT queryable, and NOT editable.
    

    
This command switches control to the named context.

    """
    pass
    


def setUITemplate( string , popTemplate=boolean, pushTemplate=boolean):
    """
    setUITemplate is undoable, queryable, and NOT editable.
    

    
This command sets the current(default) command template for the ELF commands. The special name NONE can be used to set no templates current. See "uiTemplate" command also.

    """
    pass
    


def setXformManip(showUnits=boolean, suppress=boolean, useRotatePivot=boolean, worldSpace=boolean):
    """
    setXformManip is undoable, queryable, and NOT editable.
    

    
This command changes some of the settings of the xform manip, to control its appearance.

    """
    pass
    


def shadingConnection( attribute , connectionState=boolean):
    """
    shadingConnection is undoable, queryable, and editable.
    

    
Sets the connection state of a connection between nodes that are used in shading. Specify the destination attribute of the connection.

    """
    pass
    


def shadingGeometryRelCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, offCommand=string, onCommand=string, shadingCentric=boolean):
    """
    shadingGeometryRelCtx is undoable, queryable, and editable.
    

    
This command creates a context that can be used for associating geometry to shading groups. You can put the context into shading-centric mode by using the -shadingCentric flag and specifying true. This means that the shading group is selected first then geometry associated with the shading group are highlighted. Subsequent selections result in assignments.
Specifying -shadingCentric false means that the geometry is to be selected first. The shading group associated with the geometry will then be selected and subsequent selections will result in assignments being made.

    """
    pass
    


def shadingLightRelCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, offCommand=string, onCommand=string, shadingCentric=boolean):
    """
    shadingLightRelCtx is undoable, queryable, and editable.
    

    
This command creates a context that can be used for associating lights to shading groups. You can put the context into shading-centric mode by using the -shadingCentric flag and specifying true. This means that the shading group is selected first then lights associated with the shading group are highlighted. Subsequent selections result in assignments.
Specifying -shadingCentric false means that the light is to be selected first. The shading groups associated with the light will then be selected and subsequent selections will result in assignments being made.

    """
    pass
    


def shadingNetworkCompare(byName=boolean, byValue=boolean, delete=boolean, equivalent=boolean, network1=boolean, network2=boolean, upstreamOnly=boolean):
    """
    shadingNetworkCompare is NOT undoable, queryable, and NOT editable.
    

    
This command allows you to compare two shading networks.

    """
    pass
    


def shadingNode( node , asLight=boolean, asPostProcess=boolean, asRendering=boolean, asShader=boolean, asTexture=boolean, asUtility=boolean, isColorManaged=boolean, name=string, parent=string):
    """
    shadingNode is undoable, NOT queryable, and NOT editable.
    

    
The shadingNode command classifies any DG node as a shader, texture light, post process, or utility so that it can be properly organized in the multi-lister. Recall that any DG node can be used a part of a a shader, texture or light - regardless of how it is classified by this. command. These classifications are provided for convenience in the UI.

    """
    pass
    


def shapeCompare(*args, **kwargs):
    """
    shapeCompare is undoable, NOT queryable, and NOT editable.
    

    
Compares two shapes. If no shapes are specified in the command line, then the shapes from the active list are used.

    """
    pass
    


def shapeEditor( string , control=boolean, defineTemplate=string, docTag=string, exists=boolean, filter=string, forceMainConnection=string, highlightConnection=string, lockMainConnection=boolean, mainListConnection=string, panel=string, parent=string, selectionConnection=string, stateString=boolean, targetControlList=boolean, targetList=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string, verticalSliders=boolean):
    """
    shapeEditor is undoable, queryable, and editable.
    

    
This command creates an editor that derives from the base editor class that has controls for deformer, control nodes.

    """
    pass
    


def shapePanel( string , control=boolean, copy=string, defineTemplate=string, docTag=string, exists=boolean, init=boolean, isUnique=boolean, label=string, menuBarVisible=boolean, needsInit=boolean, parent=string, popupMenuProcedure=script, replacePanel=string, shapeEditor=boolean, tearOff=boolean, tearOffCopy=string, unParent=boolean, useTemplate=string):
    """
    shapePanel is undoable, queryable, and editable.
    

    
This command creates a panel that derives from the base panel class that houses a shapeEditor.

    """
    pass
    


def shelfButton( string , align=string, annotation=string, backgroundColor=float, float, float, command=script, commandRepeatable=boolean, defineTemplate=string, disabledImage=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, flat=boolean, flipX=boolean, flipY=boolean, font=string, fullPathName=boolean, handleNodeDropCallback=script, height=int, highlightColor=float, float, float, highlightImage=string, image=string, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, label=string, labelEditingCallback=script, labelOffset=int, ltVersion=string, manage=boolean, marginHeight=uint, marginWidth=uint, menuItem=string, string, noBackground=boolean, noDefaultPopup=boolean, numberOfPopupMenus=boolean, overlayLabelBackColor=float, float, float, float, overlayLabelColor=float, float, float, parent=string, popupMenuArray=boolean, preventOverride=boolean, rotation=float, scaleIcon=boolean, selectionImage=string, sourceType=string, style=string, useAlpha=boolean, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    shelfButton is undoable, queryable, and editable.
    

    
This control supports up to 3 icon images and 4 different display styles. The icon image displayed is the one that best fits the current size of the control given its current style.
This command creates an iconTextButton that is designed to be on the shelf. The button contains a command that can be drag'n'dropped.

    """
    pass
    


def shelfLayout( string , alignment=string, annotation=string, backgroundColor=float, float, float, cellHeight=int, cellWidth=int, cellWidthHeight=int, int, childArray=boolean, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, ltVersion=string, manage=boolean, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, position=string, int, preventOverride=boolean, spacing=int, style=string, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    shelfLayout is undoable, queryable, and editable.
    

    
This command creates a new empty shelf layout. The shelf layout can accept drops of commands scripts.

    """
    pass
    


def shelfTabLayout( string , annotation=string, backgroundColor=float, float, float, borderStyle=string, changeCommand=script, childArray=boolean, childResizable=boolean, defineTemplate=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontalScrollBarThickness=int, image=string, imageVisible=boolean, innerMarginHeight=int, innerMarginWidth=int, isObscured=boolean, manage=boolean, minChildWidth=int, moveTab=int, int, newTabCommand=script, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preSelectCommand=script, preventOverride=boolean, scrollable=boolean, scrollableTabs=boolean, selectCommand=script, selectTab=string, selectTabIndex=int, showNewTab=boolean, tabLabel=string, string, tabLabelIndex=int, string, tabsClosable=boolean, tabsVisible=boolean, useTemplate=string, verticalScrollBarThickness=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    shelfTabLayout is undoable, queryable, and editable.
    

    
This command creates/edits/queries a shelf tab group which is essentially a normal tabLayout with some drop behaviour in the tab bar. A garbage can icon can appear in the top right corner to dispose of buttons dragged to it from shelves.

    """
    pass
    


def shot(audio=string, clip=string, clipDuration=time, clipOpacity=float, clipSyncState=boolean, clipZeroOffset=time, copy=boolean, createCustomAnim=boolean, currentCamera=string, customAnim=boolean, deleteCustomAnim=boolean, determineTrack=boolean, endTime=time, favorite=boolean, flag1=boolean, flag10=boolean, flag11=boolean, flag12=boolean, flag2=boolean, flag3=boolean, flag4=boolean, flag5=boolean, flag6=boolean, flag7=boolean, flag8=boolean, flag9=boolean, hasCameraSet=boolean, hasStereoCamera=boolean, linkAudio=string, lock=boolean, mute=boolean, paste=boolean, pasteInstance=boolean, postHoldTime=time, preHoldTime=time, scale=float, selfmute=boolean, sequenceDuration=time, sequenceEndTime=time, sequenceStartTime=time, shotName=string, sourceDuration=time, startTime=time, track=int, transitionInLength=time, transitionInType=int, transitionOutLength=time, transitionOutType=int, unlinkAudio=boolean):
    """
    shot is undoable, queryable, and editable.
    

    
Use this command to create a shot node or manipulate that node.

    """
    pass
    


def shotRipple(deleted=boolean, endDelta=time, endTime=time, startDelta=time, startTime=time):
    """
    shotRipple is undoable, queryable, and editable.
    

    
When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated are moved in sequence time to either make way or close up gaps corresponding to that node's editing. Given some parameters about the shot edit that just took place, this command will choose which other shots to move, and move them the appropriate amounts If no shot name is provided, the command will attempt to use the first selected shot.

    """
    pass
    


def shotTrack(insertTrack=uint, lock=boolean, mute=boolean, numTracks=uint, removeEmptyTracks=boolean, removeTrack=uint, selfmute=boolean, solo=boolean, swapTracks=uint, uint, title=string, track=uint, unsolo=boolean):
    """
    shotTrack is undoable, queryable, and editable.
    

    
This command is used for inserting and removing tracks related to the shots displayed in the Sequencer. It can also be used to modify the track state, for example, to lock or mute a track.

    """
    pass
    


def showHelp(string, absolute=boolean, docs=boolean, helpTable=boolean, version=boolean):
    """
    showHelp is NOT undoable, queryable, and NOT editable.
    

    
Invokes a web browser to open the on-line documentation and help files. It will open the help page for a given topic, or open a browser to a specific URL.

    """
    pass
    


def showHidden( objects... , above=boolean, allObjects=boolean, below=boolean, lastHidden=boolean):
    """
    showHidden is undoable, NOT queryable, and NOT editable.
    

    
The showHidden command is used to make invisible objects visible. If no flags are specified, only the objects given to the command will be made visible. If a parent of an object is invisible, the object will still be invisible. Invisibility is inherited. To ensure the object becomes visible, use the -a/above flag. This forces all invisible ancestors of the object(s) to be visible. If the -b/below flag is used, any invisible objects below the object will be made visible. To make all objects visible, use the -all/allObjects flag.
See also: hide

    """
    pass
    


def showManipCtx( string , currentNodeName=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, incSnap=uint, boolean, incSnapRelative=uint, boolean, incSnapUI=boolean, incSnapValue=uint, float, lockSelection=boolean, name=string, toggleIncSnap=boolean, toolFinish=script, toolStart=script):
    """
    showManipCtx is undoable, queryable, and editable.
    

    
This command can be used to create a show manip context. The show manip context will display manips for all selected objects that have valid manips defined for them.

    """
    pass
    


def showMetadata(auto=boolean, dataType=string, interpolation=boolean, isActivated=boolean, listAllStreams=boolean, listMembers=boolean, listValidMethods=boolean, listVisibleStreams=boolean, member=string, method=string, off=boolean, range=float, float, rayScale=float, stream=string):
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
    


def showSelectionInTitle( string ):
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
    


def showWindow( string ):
    """
    showWindow is undoable, NOT queryable, and NOT editable.
    

    
Make a window visible. If no window is specified then the current window (most recently created) is used. See also the window command's vis/visible flag.
If the specified window is iconified, it will be opened.

    """
    pass
    


def simplify( animatedObject , animation=string, attribute=string, controlPoints=boolean, float=floatrange, floatTolerance=float, hierarchy=string, includeUpperBound=boolean, index=uint, shape=boolean, time=timerange, timeTolerance=time, valueTolerance=float):
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
    


def singleProfileBirailSurface( curve curve curve , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, polygon=int, tangentContinuityProfile1=boolean, transformMode=int):
    """
    singleProfileBirailSurface is undoable, queryable, and editable.
    

    
This cmd creates a railed surface by sweeping the profile curve along the two rail curves. One of the requirements for surface creation is the profile curve must intersect the two rail curves. If the profile is a surface curve i.e. isoparm, curve on surface or trimmed edge then tangent continuity across the surface underlying the profile may be enabled using the flag -tp1 true.
The first argument represetns the profile curve, the second and third the rails.

    """
    pass
    


def skeletonEmbed(mergedMesh=boolean, segmentationMethod=uint, segmentationResolution=uint):
    """
    skeletonEmbed is undoable, queryable, and NOT editable.
    

    
This command is used to embed a skeleton inside meshes.

    """
    pass
    


def skinBindCtx( string , about=string, axis=string, colorRamp=string, currentInfluence=int, displayInactiveMode=int, displayNormalized=boolean, exists=boolean, falloffCurve=string, history=boolean, image1=string, image2=string, image3=string, name=string, symmetry=boolean, tolerance=float):
    """
    skinBindCtx is undoable, queryable, and editable.
    

    
This command creates a tool that can be used to edit volumes from an interactive bind.

    """
    pass
    


def skinCluster( objects , addInfluence=string, addToSelection=boolean, after=boolean, afterReference=boolean, baseShape=string, before=boolean, bindMethod=int, deformerTools=boolean, dropoffRate=float, exclusive=string, forceNormalizeWeights=boolean, frontOfChain=boolean, geometry=string, geometryIndices=boolean, heatmapFalloff=float, ignoreBindPose=boolean, ignoreHierarchy=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, influence=string, lockWeights=boolean, maximumInfluences=int, moveJointsMode=boolean, name=string, normalizeWeights=int, nurbsSamples=int, obeyMaxInfluences=boolean, parallel=boolean, polySmoothness=float, prune=boolean, recacheBindMatrices=boolean, remove=boolean, removeFromSelection=boolean, removeInfluence=string, removeUnusedInfluence=boolean, selectInfluenceVerts=string, skinMethod=int, smoothWeights=float, smoothWeightsMaxIterations=int, split=boolean, toSelectedBones=boolean, toSkeletonAndTransforms=boolean, unbind=boolean, unbindKeepHistory=boolean, useGeometry=boolean, volumeBind=float, volumeType=int, weight=float, weightDistribution=int, weightedInfluence=boolean):
    """
    skinCluster is undoable, queryable, and editable.
    

    
The skinCluster command is used for smooth skinning in maya. It binds the selected geometry to the selected joints or skeleton by means of a skinCluster node. Each point of the bound geometry can be affected by any number of joints. The extent to which each joint affects the motion of each point is regulated by a corresponding weight factor. Weight factors can be modified using the skinPercent command. The command returns the name of the new skinCluster.
The skinCluster binds only a single geometry at a time. Thus, to bind multiple geometries, multiple skinCluster commands must be issued.
Upon creation of a new skinCluster, the command can be used to add and remove transforms (not necessarily joints) that influence the motion of the bound skin points.
The skinCluster command can also be used to adjust parameters such as the dropoff, nurbs samples, polygon smoothness on a particular influence object. Note: Any custom weights on a skin point that the influence object affects will be lost after adjusting these parameters.

    """
    pass
    


def skinPercent( object selectionList , ignoreBelow=float, normalize=boolean, pruneWeights=float, relative=boolean, resetToDefault=boolean, transform=string, transformMoveWeights=string, transformValue=string, float, value=boolean, zeroRemainingInfluences=boolean):
    """
    skinPercent is undoable, queryable, and NOT editable.
    

    
This command edits and queries the weight values on members of a skinCluster node, given as the first argument. If no object components are explicitly mentioned in the command line, the current selection list is used.
Note that setting multiple weights in a single invocation of this command is far more efficient than calling it once per weighted vertex.

    """
    pass
    


def smoothCurve( selectionList , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, replaceOriginal=boolean, smoothness=float):
    """
    smoothCurve is undoable, queryable, and editable.
    

    
The smooth command smooths the curve at the given control points.

    """
    pass
    


def smoothTangentSurface( surface , caching=boolean, constructionHistory=boolean, direction=int, name=string, nodeState=int, object=boolean, parameter=float, replaceOriginal=boolean, smoothness=int):
    """
    smoothTangentSurface is undoable, queryable, and editable.
    

    
The smoothTangentSurface command smooths the surface along an isoparm at each parameter value. The name of the surface is returned and if history is on, the name of the resulting dependency node is also returned. This command only applies to parameter values with a multiple knot value. (If the given parameter value has no multiple knot associated with it, then the dependency node is created but the surface doesn't change.)

When would you use this? If you have a surface consisting of a number of Bezier patches or any isoparms with more than a single knot multiplicity, you could get into a situation where a tangent break occurs. So, it only makes sense to do this operation on the knot isoparms, and not anywhere in between, because the surface is already smooth everywhere in between.

If you have a cubic or higher degree surface, asking for the maximal smoothness will give you tangent, curvature, etc. up to the degree-1 continuity. Asking for tangent will just give you tangent continuity.

It should be mentioned that this is "C", not "G" continuity we're talking about, so technically, you can still see visual tangent breaks if the surface is degenerate.
Note: A single smoothTangentSurface command cannot smooth in both directions at once; you must use two separate commands to do this.

    """
    pass
    


def snapKey( animatedObject , animation=string, attribute=string, controlPoints=boolean, float=floatrange, hierarchy=string, includeUpperBound=boolean, index=uint, shape=boolean, time=timerange, timeMultiple=float, valueMultiple=float):
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
    


def snapMode(curve=boolean, distanceIncrement=linear, edgeMagnet=uint, edgeMagnetTolerance=float, grid=boolean, liveFaceCenter=boolean, livePoint=boolean, meshCenter=boolean, pixelCenter=boolean, pixelSnap=boolean, point=boolean, tolerance=uint, useTolerance=boolean, uvTolerance=uint, viewPlane=boolean):
    """
    snapMode is undoable, queryable, and NOT editable.
    

    
The snapMode command is used to control snapping. It toggles the snapping modes in effect and sets information used for snapping.

    """
    pass
    


def snapshot( objects , constructionHistory=boolean, endTime=time, increment=time, motionTrail=boolean, name=string, startTime=time, update=string):
    """
    snapshot is undoable, queryable, and editable.
    

    
This command can be used to create either a series of surfaces evaluated at the times specified by the command flags, or a motion trail displaying the trajectory of the object's pivot point at the times specified.
If the constructionHistory flag is true, the output shapes or motion trail will re-update when modifications are made to the animation or construction history of the original shape. When construction history is used, the forceUpdate flag can be set to false to control when the snapshot recomputes, which will typically improve performance.

    """
    pass
    


def snapshotBeadCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, inTangent=boolean, name=string, outTangent=boolean):
    """
    snapshotBeadCtx is undoable, queryable, and editable.
    

    
Creates a context for manipulating in and/or out tangent beads on the motion trail

    """
    pass
    


def snapshotModifyKeyCtx(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    snapshotModifyKeyCtx is undoable, queryable, and editable.
    

    
Creates a context for inserting/delete keys on an editable motion trail

    """
    pass
    


def snapTogetherCtx( contextName , clearSelection=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, setOrientation=boolean, snapPolygonFace=boolean):
    """
    snapTogetherCtx is undoable, queryable, and editable.
    

    
The snapTogetherCtx command creates a tool for snapping surfaces together.

    """
    pass
    


def soft( selectionList , convert=boolean, duplicate=boolean, duplicateHistory=boolean, goal=float, hideOriginal=boolean, name=string):
    """
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
    


def softMod( objects , after=boolean, afterReference=boolean, before=boolean, bindState=boolean, curveInterpolation=int, curvePoint=float, curveValue=float, deformerTools=boolean, envelope=float, exclusive=string, falloffAroundSelection=boolean, falloffBasedOnX=boolean, falloffBasedOnY=boolean, falloffBasedOnZ=boolean, falloffCenter=float, float, float, falloffMasking=boolean, falloffMode=int, falloffRadius=float, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, name=string, parallel=boolean, prune=boolean, relative=boolean, remove=boolean, resetGeometry=boolean, split=boolean, weightedNode=string, string):
    """
    softMod is undoable, queryable, and editable.
    

    
The softMod command creates a softMod or edits the membership of an existing softMod. The command returns the name of the softMod node upon creation of a new softMod.

    """
    pass
    


def softModCtx( string , dragSlider=string, exists=boolean, falseColor=boolean, image1=string, image2=string, image3=string, reset=boolean):
    """
    softModCtx is undoable, queryable, and editable.
    

    
Controls the softMod context.

    """
    pass
    


def softSelect(compressUndo=int, enableFalseColor=int, softSelectColorCurve=string, softSelectCurve=string, softSelectDistance=float, softSelectEnabled=int, softSelectFalloff=int, softSelectReset=boolean, softSelectUVDistance=float):
    """
    softSelect is undoable, queryable, and editable.
    

    
This command allows you to change the soft modelling options.
Soft modelling is an option that allows for reflection of basic manipulator actions such as move, rotate, and scale.

    """
    pass
    


def soloMaterial(attr=string, last=boolean, node=string, unsolo=boolean):
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
    


def sound( objects , endTime=time, file=string, length=boolean, mute=boolean, name=string, offset=time, sourceEnd=time, sourceStart=time):
    """
    sound is undoable, queryable, and editable.
    

    
Creates an audio node which can be used with UI commands such as soundControl or timeControl which support sound scrubbing and sound during playback.

    """
    pass
    


def soundControl( string , annotation=string, backgroundColor=float, float, float, beginScrub=boolean, defineTemplate=string, displaySound=boolean, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, endScrub=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, maxTime=time, minTime=time, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, pressCommand=string, preventOverride=boolean, releaseCommand=string, repeatChunkSize=float, repeatOnHold=boolean, resample=boolean, sound=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, waveform=string, width=int):
    """
    soundControl is undoable, queryable, and editable.
    

    
This command creates a control used for changing current time and scratching/scrubbing through sound files.

    """
    pass
    


def spaceLocator(absolute=boolean, name=string, position=linear, linear, linear, relative=boolean):
    """
    spaceLocator is undoable, queryable, and editable.
    

    
The command creates a locator at the specified position in space. By default it is created at (0,0,0).

    """
    pass
    


def sphere(axis=linear, linear, linear, caching=boolean, constructionHistory=boolean, degree=int, endSweep=angle, heightRatio=float, name=string, nodeState=int, object=boolean, pivot=linear, linear, linear, polygon=int, radius=linear, sections=int, spans=int, startSweep=angle, tolerance=linear, useTolerance=boolean):
    """
    sphere is undoable, queryable, and editable.
    

    
The sphere command creates a new sphere. The number of spans in the in each direction of the sphere is determined by the useTolerance attribute. If -ut is true then the -tolerance attribute will be used. If -ut is false then the -sections attribute will be used.

    """
    pass
    


def spotLight(coneAngle=angle, decayRate=int, discRadius=linear, dropOff=float, intensity=float, name=string, penumbra=angle, rgb=float, float, float, shadowColor=float, float, float, shadowDither=float, shadowSamples=int, softShadow=boolean, useRayTraceShadows=boolean):
    """
    spotLight is undoable, queryable, and editable.
    

    
The spotLight command is used to edit the parameters of existing spotLights, or to create new ones. The default behaviour is to create a new spotlight.

    """
    pass
    


def spotLightPreviewPort( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, spotLight=name, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int, widthHeight=int, int):
    """
    spotLightPreviewPort is undoable, queryable, and editable.
    

    
This command creates a 3dPort that displays an image representing the illumination provided by the spotLight. It is a picture of a plane being illuminated by a light.
The optional argument is the name of the 3dPort.

    """
    pass
    


def spreadSheetEditor( name , allAttr=boolean, attrRegExp=string, control=boolean, defineTemplate=string, docTag=string, execute=string, exists=boolean, filter=string, fixedAttrList=string,..., forceMainConnection=string, highlightConnection=string, keyableOnly=boolean, lockMainConnection=boolean, longNames=boolean, mainListConnection=string, niceNames=boolean, panel=string, parent=string, precision=int, selectedAttr=boolean, selectionConnection=string, showShapes=boolean, stateString=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useTemplate=string):
    """
    spreadSheetEditor is undoable, queryable, and editable.
    

    
This command creates a new spread sheet editor in the current layout.

    """
    pass
    


def spring( objects , addSprings=boolean, allPoints=boolean, count=boolean, damping=float, dampingPS=float, endForceWeight=float, exclusive=boolean, length=float, maxDistance=float, minDistance=float, minMax=boolean, name=string, noDuplicate=boolean, restLength=float, restLengthPS=float, startForceWeight=float, stiffness=float, stiffnessPS=float, useDampingPS=boolean, useRestLengthPS=boolean, useStiffnessPS=boolean, walkLength=uint, wireframe=boolean):
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
    


def squareSurface( string string string string , caching=boolean, constructionHistory=boolean, continuityType1=int, continuityType2=int, continuityType3=int, continuityType4=int, curveFitCheckpoints=int, endPointTolerance=linear, name=string, nodeState=int, object=boolean, polygon=int, rebuildCurve1=boolean, rebuildCurve2=boolean, rebuildCurve3=boolean, rebuildCurve4=boolean):
    """
    squareSurface is undoable, queryable, and editable.
    

    
This command produces a square surface given 3 or 4 curves. This resulting square surface is created within the intersecting region of the selected curves. The order of selection is important and the curves must intersect or their ends must meet.
You must specify one continuity type flag for each selected curve. If continuity type is 1 (fixed, no tangent continuity) then the curveFitCheckpoints flag (cfc) is not required.

    """
    pass
    


def srtContext(exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string):
    """
    srtContext is undoable, queryable, and editable.
    

    
This command can be used to create a combined transform (translate/scale/rotate) context.

    """
    pass
    


def stereoCameraView( objects , activeComponentsXray=boolean, activeCustomEnvironment=string, activeCustomGeometry=string, activeCustomLighSet=string, activeCustomOverrideGeometry=string, activeCustomRenderer=string, activeOnly=boolean, activeShadingGraph=string, activeSupported=boolean, activeView=boolean, addObjects=string, addSelected=boolean, allObjects=boolean, backfaceCulling=boolean, bufferMode=string, bumpResolution=uint, uint, camera=string, cameraName=string, cameraSetup=boolean, cameras=boolean, centerCamera=string, colorMap=boolean, colorResolution=uint, uint, control=boolean, controlVertices=boolean, cullingOverride=string, default=boolean, defineTemplate=string, deformers=boolean, dimensions=boolean, displayAppearance=string, displayLights=string, displayMode=string, displayTextures=boolean, docTag=string, dynamicConstraints=boolean, dynamics=boolean, editorChanged=script, exists=boolean, filter=string, filteredObjectList=boolean, fluids=boolean, fogColor=float, float, float, float, fogDensity=float, fogEnd=float, fogMode=string, fogSource=string, fogStart=float, fogging=boolean, follicles=boolean, forceMainConnection=string, grid=boolean, hairSystems=boolean, handles=boolean, headsUpDisplay=boolean, height=int, highlightConnection=string, hulls=boolean, ignorePanZoom=boolean, ikHandles=boolean, imagePlane=boolean, interactive=boolean, isFiltered=boolean, jointXray=boolean, joints=boolean, leftCamera=string, lights=boolean, lineWidth=float, locators=boolean, lockMainConnection=boolean, lowQualityLighting=boolean, mainListConnection=string, manipulators=boolean, maxConstantTransparency=float, nCloths=boolean, nParticles=boolean, nRigids=boolean, noUndo=boolean, nurbsCurves=boolean, nurbsSurfaces=boolean, objectFilter=script, objectFilterList=script, objectFilterListUI=script, objectFilterShowInHUD=boolean, objectFilterUI=script, occlusionCulling=boolean, panel=string, parent=string, pivots=boolean, planes=boolean, pluginObjects=string, boolean, pluginShapes=boolean, polymeshes=boolean, queryPluginObjects=string, removeSelected=boolean, rendererDeviceName=boolean, rendererList=boolean, rendererListUI=boolean, rendererName=string, rendererOverrideList=boolean, rendererOverrideListUI=boolean, rendererOverrideName=string, resetCustomCamera=boolean, rigRoot=string, rightCamera=string, sceneRenderFilter=string, selectionConnection=string, selectionHiliteDisplay=boolean, setSelected=boolean, shadows=boolean, smoothWireframe=boolean, sortTransparent=boolean, stateString=boolean, strokes=boolean, subdivSurfaces=boolean, swapEyes=boolean, textureAnisotropic=boolean, textureDisplay=string, textureHilight=boolean, textureMaxSize=int, textureMemoryUsed=boolean, textureSampling=int, textures=boolean, transpInShadows=boolean, transparencyAlgorithm=string, twoSidedLighting=boolean, unParent=boolean, unlockMainConnection=boolean, updateColorMode=boolean, updateMainConnection=boolean, useBaseRenderer=boolean, useColorIndex=boolean, useCustomBackground=boolean, useDefaultMaterial=boolean, useInteractiveMode=boolean, useRGBImagePlane=boolean, useTemplate=string, userNode=string, viewColor=float, float, float, float, viewObjects=boolean, viewSelected=boolean, width=int, wireframeBackingStore=boolean, wireframeOnShaded=boolean, xray=boolean):
    """
    stereoCameraView is undoable, queryable, and editable.
    

    
This is the main command for creating stereo editors. This commands only acts as an interface to the actual viewport. It is derived off of MPxModelEditorCommand. This command manages the set of stereo rig tools.

    """
    pass
    


def stereoRigManager( objects , addRig=string, string, string, cameraSetFunc=string, string, creationProcedure=string, string, defaultRig=string, delete=string, language=string, string, listRigs=boolean, rigDefinition=string):
    """
    stereoRigManager is undoable, queryable, and NOT editable.
    

    
This command manages the set of stereo rig tools.

    """
    pass
    


def stitchSurface( surfaceIsoparm surfaceIsoparm , bias=float, caching=boolean, cascade=boolean, constructionHistory=boolean, cvIthIndex=int, cvJthIndex=int, fixBoundary=boolean, keepG0Continuity=boolean, keepG1Continuity=boolean, name=string, nodeState=int, numberOfSamples=int, object=boolean, parameterU=float, parameterV=float, positionalContinuity=boolean, replaceOriginal=boolean, stepCount=int, tangentialContinuity=boolean, togglePointNormals=boolean, togglePointPosition=boolean, toggleTolerance=boolean, tolerance=linear, weight0=float, weight1=float):
    """
    stitchSurface is undoable, queryable, and editable.
    

    
The stitchSurface command aligns two surfaces together to be G(0) and/or G(1) continuous by ajusting only the Control Vertices of the surfaces. The two surfaces can be stitched by specifying the two isoparm boundary edges that are to stitched together. The edge to which the two surfaces are stitched together is obtained by doing a weighted average of the two edges. The weights for the two edges is specified using the flags -wt0, -wt1 respectively.

    """
    pass
    


def stitchSurfacePoints( selectionList , bias=float, caching=boolean, cascade=boolean, constructionHistory=boolean, cvIthIndex=int, cvJthIndex=int, equalWeight=boolean, fixBoundary=boolean, keepG0Continuity=boolean, keepG1Continuity=boolean, name=string, nodeState=int, object=boolean, parameterU=float, parameterV=float, positionalContinuity=boolean, replaceOriginal=boolean, stepCount=int, tangentialContinuity=boolean, togglePointNormals=boolean, togglePointPosition=boolean, toggleTolerance=boolean, tolerance=linear):
    """
    stitchSurfacePoints is undoable, queryable, and editable.
    

    
The stitchSurfacePoints command aligns two or more surface points along the boundaries together to a single point. In the process, a node to average the points is created. The points are averaged together in a weighted fashion. The points may be control vertices along the boundaries. If the points are CVs then they are stitched together only with positional continuity.
Note: No two points can lie on the same surface.

    """
    pass
    


def stringArrayIntersector( string , allowDuplicates=boolean, defineTemplate=string, exists=boolean, intersect=string,..., reset=boolean, useTemplate=string):
    """
    stringArrayIntersector is undoable, queryable, and editable.
    

    
The stringArrayIntersector command creates and edits an object which is able to efficiently intersect large string arrays. The intersector object maintains a sense of "the intersection so far", and updates the intersection when new string arrays are provided using the -i/intersect flag.
Note that the string intersector object may be deleted using the deleteUI command.

    """
    pass
    


def stroke( string , name=string, pressure=boolean, seed=int):
    """
    stroke is undoable, NOT queryable, and NOT editable.
    

    
The stroke command creates a new Paint Effects stroke node.

    """
    pass
    


def subdAutoProjection( selectionList , constructionHistory=boolean, layout=int, name=string, optimize=int, percentageSpace=float, planes=int, scale=int, skipIntersect=boolean, worldSpace=boolean):
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
    


def subdCollapse( string , caching=boolean, constructionHistory=boolean, level=int, name=string, nodeState=int, object=boolean):
    """
    subdCollapse is undoable, queryable, and editable.
    

    
This command converts a takes a subdivision surface, passed as the argument, and produces a subdivision surface with a number of hierarchy levels "removed". Returns the name of the subdivision surface created and optionally the DG node that does the conversion.

    """
    pass
    


def subdDuplicateAndConnect( object ):
    """
    subdDuplicateAndConnect is undoable, NOT queryable, and NOT editable.
    

    
This command duplicates the input subdivision surface object, connects up the outSubdiv attribute of the original subd shape to the create attribute of the newly created duplicate shape and copies over the shader assignments from the original shape to the new duplicated shape.
The command will fail if no objects are selected or sent as argument or if the object sent as argument is not a subdivision surface object.

    """
    pass
    


def subdEditUV(angle=float, pivotU=float, pivotV=float, relative=boolean, rotation=boolean, scale=boolean, scaleU=float, scaleV=float, uValue=float, uvSetName=string, vValue=float):
    """
    subdEditUV is undoable, queryable, and NOT editable.
    

    
Command edits uvs on subdivision surfaces. When used with the query flag, it returns the uv values associated with the specified components.

    """
    pass
    


def subdiv(currentLevel=boolean, currentSubdLevel=boolean, deepestLevel=int, displayLoad=boolean, edgeStats=boolean, faceStats=boolean, maxPossibleLevel=int, proxyMode=int, smallOffsets=boolean):
    """
    subdiv is undoable, queryable, and NOT editable.
    

    
Provides useful information about the selected subdiv or components, such as the deepest subdivided level, the children or parents of the currently selected components, etc.

    """
    pass
    


def subdivCrease(sharpness=boolean):
    """
    subdivCrease is undoable, NOT queryable, and NOT editable.
    

    
Set the creasing on subdivision mesh edges or mesh points that are on the selection list.

    """
    pass
    


def subdivDisplaySmoothness(all=boolean, smoothness=int):
    """
    subdivDisplaySmoothness is undoable, queryable, and NOT editable.
    

    
Sets or querys the display smoothness of subdivision surfaces on the selection list or of all subdivision surfaces if the -all option is set. Smoothness options are; rough, medium, or fine. Rough is the default.

    """
    pass
    


def subdLayoutUV(flipReversed=boolean, layout=int, layoutMethod=int, percentageSpace=float, rotateForBestFit=int, scale=int, separate=int, worldSpace=boolean):
    """
    subdLayoutUV is undoable, queryable, and editable.
    

    
Move UVs in the texture plane to avoid overlaps.

    """
    pass
    


def subdListComponentConversion( objects... , fromEdge=boolean, fromFace=boolean, fromUV=boolean, fromVertex=boolean, internal=boolean, toEdge=boolean, toFace=boolean, toUV=boolean, toVertex=boolean, uvShell=boolean, uvShellBorder=boolean):
    """
    subdListComponentConversion is undoable, NOT queryable, and NOT editable.
    

    
This command converts subdivision surface components from one or more types to another one or more types, and returns the list of the conversion. It doesn't change the currently selected objects.
Use the "-in/internal" flag to specify conversion to "connected" vs. "contained" components. For example, if the internal flag is specified when converting from subdivision surface vertices to faces, then only faces that are entirely contained by the vertices will be returned. If the internal flag is not specified, then all faces that are connected to the vertices will be returned.

    """
    pass
    


def subdMapCut(constructionHistory=boolean, name=string):
    """
    subdMapCut is undoable, queryable, and editable.
    

    
Cut along edges of the texture mapping. The cut edges become map borders.

    """
    pass
    


def subdMapSewMove( selectionList , constructionHistory=boolean, limitPieceSize=boolean, name=string, numberFaces=int):
    """
    subdMapSewMove is undoable, queryable, and editable.
    

    
This command can be used to Move and Sew together separate UV pieces along geometric edges. UV pieces that correspond to the same geometric edge, are merged together by moving the smaller piece to the larger one.

The argument is a UV selection list.

    """
    pass
    


def subdMatchTopology(frontOfChain=boolean):
    """
    subdMatchTopology is undoable, NOT queryable, and NOT editable.
    

    
Command matches topology across multiple subdiv surfaces - at all levels.

    """
    pass
    


def subdMirror( string , caching=boolean, constructionHistory=boolean, name=string, nodeState=int, object=boolean, xMirror=boolean, yMirror=boolean, zMirror=boolean):
    """
    subdMirror is undoable, queryable, and editable.
    

    
This command takes a subdivision surface, passed as the argument, and produces a subdivision surface that is a mirror. Returns the name of the subdivision surface created and optionally the DG node that does the mirroring.

    """
    pass
    


def subdPlanarProjection(createNewMap=boolean, imageCenter=float, float, imageCenterX=float, imageCenterY=float, imageScale=float, float, imageScaleU=float, imageScaleV=float, insertBeforeDeformers=boolean, mapDirection=string, projectionCenter=linear, linear, linear, projectionCenterX=linear, projectionCenterY=linear, projectionCenterZ=linear, projectionScale=linear, linear, rotate=angle, angle, angle, rotateX=angle, rotateY=angle, rotateZ=angle, rotationAngle=angle, worldSpace=boolean):
    """
    subdPlanarProjection is undoable, queryable, and editable.
    

    
Projects a map onto an object, using an orthogonal projection. The piece of the map defined from isu, isv, icx, icy area, is placed at pcx, pcy, pcz location.

    """
    pass
    


def subdToBlind(absolutePosition=boolean, includeCreases=boolean, includeZeroOffsets=boolean):
    """
    subdToBlind is undoable, NOT queryable, and NOT editable.
    

    
The subdivision surface hierarchical edits will get copied into blind data on the given polygon. The polygon face count and topology must match the subdivision surface base mesh face count and topology. If they don't, the blind data will still appear, but is not guaranteed to produce the same result when converted back to a subdivision surface.

The command takes a single subdivision surface and a single polygonal object. Additional subdivision surfaces or polygonal objects will be ignored.

    """
    pass
    


def subdToPoly( subd , applyMatrixToResult=boolean, caching=boolean, connectShaders=boolean, constructionHistory=boolean, copyUVTopology=boolean, depth=int, extractPointPosition=boolean, format=int, inSubdCVId=int, int, inSubdCVIdLeft=int, inSubdCVIdRight=int, maxPolys=int, name=string, nodeState=int, object=boolean, outSubdCVId=int, int, outSubdCVIdLeft=int, outSubdCVIdRight=int, outv=int, preserveVertexOrdering=boolean, sampleCount=int, shareUVs=boolean, subdNormals=boolean):
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
    


def substituteGeometry(disableNonSkinDeformers=boolean, newGeometryToLayer=boolean, oldGeometryToLayer=boolean, reWeightDistTolerance=float, retainOldGeometry=boolean):
    """
    substituteGeometry is undoable, NOT queryable, and NOT editable.
    

    
This command can be used to replace the geometry which is already connected to deformers with a new geometry. The weights on the old geometry will be retargeted to the new geometry.

    """
    pass
    


def suitePrefs(applyToSuite=string, installedAsSuite=boolean, isCompleteSuite=boolean):
    """
    suitePrefs is undoable, NOT queryable, and NOT editable.
    

    
This command sets the mouse and keyboard interaction mode for Maya and other Suites applications (if Maya is part of a Suites install).

    """
    pass
    


def surface(degreeU=int, degreeV=int, formU=string, formV=string, knotU=float, knotV=float, point=linear, linear, linear, pointWeight=linear, linear, linear, linear):
    """
    surface is undoable, NOT queryable, and NOT editable.
    

    
The cmd creates a NURBS spline surface (rational or non rational). The surface is created by specifying control vertices (CV's) and knot sequences in the U and V direction. You cannot query the properties of the surface using this command. See examples below.

    """
    pass
    


def surfaceSampler(camera=name, fileFormat=string, filename=string, filterSize=float, filterType=uint, flipU=boolean, flipV=boolean, ignoreMirroredFaces=boolean, ignoreTransforms=boolean, mapHeight=uint, mapMaterials=boolean, mapOutput=string, mapSpace=string, mapWidth=uint, maxSearchDistance=linear, maximumValue=linear, overscan=uint, searchCage=string, searchMethod=uint, searchOffset=linear, shadows=boolean, source=string, sourceUVSpace=string, superSampling=uint, target=string, targetUVSpace=string, useGeometryNormals=boolean, uvSet=string):
    """
    surfaceSampler is undoable, NOT queryable, and NOT editable.
    

    
Maps surface detail from a source surface to a new texture map on a target surface. Both objects must be selected when the command is invoked, with the source surface selected first, and the target last.

    """
    pass
    


def surfaceShaderList(add=name, remove=name):
    """
    surfaceShaderList is undoable, queryable, and editable.
    

    
Add/Remove a relationship between an object and the current shading group.

    """
    pass
    


def swatchDisplayPort( string , annotation=string, backgroundColor=float, float, float, borderColor=float, float, float, borderWidth=int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, pressCommand=script, preventOverride=boolean, renderPriority=int, renderSize=int, shadingNode=name, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int, widthHeight=int, int):
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
    


def switchTable( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label1=string, label2=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, selectedRow=boolean, switchNode=name, underPointerRow=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    switchTable is undoable, queryable, and editable.
    

    
This command creates/edits/queries the switch table control.
The optional argument is the name of the control.

    """
    pass
    


def symbolButton( string , annotation=string, backgroundColor=float, float, float, command=script, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    symbolButton is undoable, queryable, and editable.
    

    
This command creates a symbol button. A symbol button behaves like a regular button, the only difference is a symbol button displays an image rather that a text label. A command may be attached to the button which will be executed when the button is pressed.

    """
    pass
    


def symbolCheckBox( string , annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, disableOffImage=string, disableOnImage=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, image=string, innerMargin=boolean, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, offCommand=script, offImage=string, onCommand=script, onImage=string, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, value=boolean, visible=boolean, visibleChangeCommand=script, width=int):
    """
    symbolCheckBox is undoable, queryable, and editable.
    

    
This command creates a symbol check box. A symbol check box is a simple control containing a pixmap and a state of either on or off. Commands can be attached to any or all of the following events: when the symbol check box is turned on, turned off, or simply when it's state is changed.

    """
    pass
    


def symmetricModelling(about=string, allowPartial=boolean, axis=string, preserveSeam=int, seamFalloffCurve=string, seamTolerance=float, symmetry=int, tolerance=float, topoSymmetry=boolean):
    """
    symmetricModelling is undoable, queryable, and editable.
    

    
This command allows you to change the symmetric modelling options.
Symmetric modelling is an option that allows for reflection of basic manipulator actions such as move, rotate, and scale.

    """
    pass
    


def sysFile( string , copy=string, delete=boolean, makeDir=boolean, move=string, removeEmptyDir=boolean, rename=string):
    """
    sysFile is undoable, NOT queryable, and NOT editable.
    

    
This command provides a system independent way to create a directory or to rename or delete a file.

    """
    pass
    


def tabLayout( string , annotation=string, backgroundColor=float, float, float, borderStyle=string, changeCommand=script, childArray=boolean, childResizable=boolean, defineTemplate=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, horizontalScrollBarThickness=int, image=string, imageVisible=boolean, innerMarginHeight=int, innerMarginWidth=int, isObscured=boolean, manage=boolean, minChildWidth=int, moveTab=int, int, newTabCommand=script, noBackground=boolean, numberOfChildren=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preSelectCommand=script, preventOverride=boolean, scrollable=boolean, scrollableTabs=boolean, selectCommand=script, selectTab=string, selectTabIndex=int, showNewTab=boolean, tabLabel=string, string, tabLabelIndex=int, string, tabsClosable=boolean, tabsVisible=boolean, useTemplate=string, verticalScrollBarThickness=int, visible=boolean, visibleChangeCommand=script, width=int):
    """
    tabLayout is undoable, queryable, and editable.
    

    
This command creates a tab group. Tab groups are a specialized form of control layouts that contain only control layouts. Whenever a control layout is added to a tab group it will have a tab provided for it that allows selection of that group from amongst other tabbed control groups. Only one child of a tab layout is visible at a time.

    """
    pass
    


def tangentConstraint( target... object , aimVector=float, float, float, layer=string, name=string, remove=boolean, targetList=boolean, upVector=float, float, float, weight=float, weightAliasList=boolean, worldUpObject=name, worldUpType=string, worldUpVector=float, float, float):
    """
    tangentConstraint is undoable, queryable, and editable.
    

    
Constrain an object's orientation based on the tangent of the target curve[s] at the closest point[s] to the object.
A tangentConstraint takes as input one or more NURBS curves (the targets) and a DAG transform node (the object). The tangentConstraint orients the constrained object such that the aimVector (in the object's local coordinate system) aligns in world space to combined tangent vector. The upVector (again the the object's local coordinate system) is aligned in world space with the worldUpVector. The combined tangent vector is a weighted average of the tangent vector for each target curve at the point closest to the constrained object.

    """
    pass
    


def targetWeldCtx(exists=boolean, image1=string, image2=string, image3=string, mergeToCenter=boolean):
    """
    targetWeldCtx is undoable, queryable, and editable.
    

    
Create a new context to weld vertices together on a poly object.

    """
    pass
    


def texCutContext( contextName , adjustSize=boolean, displayShellBorders=boolean, edgeSelectSensitive=float, exists=boolean, history=boolean, image1=string, image2=string, image3=string, mode=string, moveRatio=float, name=string, size=float, steadyStroke=boolean, steadyStrokeDistance=float, touchToSew=boolean):
    """
    texCutContext is undoable, queryable, and editable.
    

    
This command creates a context for cut uv tool. This context only works in the UV editor.

    """
    pass
    


def texLatticeDeformContext( contextName , envelope=float, exists=boolean, history=boolean, image1=string, image2=string, image3=string, latticeColumns=uint, latticeRows=uint, name=string, snapPixelMode=boolean, useBoundingRect=boolean):
    """
    texLatticeDeformContext is undoable, queryable, and editable.
    

    
This command creates a context which may be used to deform UV maps with lattice manipulator. This context only works in the texture UV editor.

    """
    pass
    


def texManipContext(exists=boolean, image1=string, image2=string, image3=string):
    """
    texManipContext is undoable, queryable, and editable.
    

    
Command used to register the texSelectCtx tool. Command used to register the texManipCtx tool.

    """
    pass
    


def texMoveContext( object , exists=boolean, image1=string, image2=string, image3=string, position=boolean, snapComponentsRelative=boolean, snapPixelMode=int):
    """
    texMoveContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    """
    pass
    


def texMoveUVShellContext( object , exists=boolean, image1=string, image2=string, image3=string, iterations=int, mask=boolean, position=boolean, shellBorder=float):
    """
    texMoveUVShellContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    """
    pass
    


def texRotateContext(exists=boolean, image1=string, image2=string, image3=string, position=boolean, snap=boolean, snapRelative=boolean, snapValue=float):
    """
    texRotateContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a rotate context for the UV Editor. Note that the above flag controls the global behaviour of all texture editor rotate contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flag, will change all existing texture editor rotate contexts.

    """
    pass
    


def texScaleContext(exists=boolean, image1=string, image2=string, image3=string, position=boolean, snap=boolean, snapRelative=boolean, snapValue=float):
    """
    texScaleContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a scale context for the UV Editor. Note that the above flag controls the global behaviour of all texture editor scale contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flag, will change all existing texture editor scale contexts.

    """
    pass
    


def texSculptCacheContext(adjustSize=boolean, adjustStrength=boolean, direction=int, falloffType=int, floodPin=float, grabTwist=boolean, inverted=boolean, mode=string, sculptFalloffCurve=string, showBrushRingDuringStroke=boolean, size=float, strength=float):
    """
    texSculptCacheContext is undoable, queryable, and editable.
    

    
This is a tool context command for uv cache sculpting tool.

    """
    pass
    


def texSelectContext(exists=boolean, image1=string, image2=string, image3=string):
    """
    texSelectContext is undoable, queryable, and editable.
    

    
Command used to register the texSelectCtx tool.

    """
    pass
    


def texSelectShortestPathCtx(exists=boolean, image1=string, image2=string, image3=string):
    """
    texSelectShortestPathCtx is undoable, queryable, and editable.
    

    
Creates a new context to select shortest edge path between two vertices or UVs in the texture editor window.

    """
    pass
    


def texSmudgeUVContext( contextName , dragSlider=string, effectType=string, exists=boolean, functionType=string, history=boolean, image1=string, image2=string, image3=string, name=string, pressure=float, radius=float, smudgeIsMiddle=boolean):
    """
    texSmudgeUVContext is undoable, queryable, and editable.
    

    
This command creates a context for smudge UV tool. This context only works in the texture UV editor.

    """
    pass
    


def text( string , align=string, annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, dropRectCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, hyperlink=boolean, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, recomputeSize=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int, wordWrap=boolean):
    """
    text is undoable, queryable, and editable.
    

    
Create a simple text label control.

    """
    pass
    


def textCurves( string , font=string, name=string, object=boolean, text=string):
    """
    textCurves is undoable, queryable, and editable.
    

    
The textCurves command creates NURBS curves from a text string using the specified font.
A single letter can be made up of more than one NURBS curve. The number of curves per letter varies with the font.

    """
    pass
    


def textField( string , alwaysInvokeEnterCommandOnReturn=boolean, annotation=string, backgroundColor=float, float, float, changeCommand=script, defineTemplate=string, disableButtons=boolean, disableClearButton=boolean, disableHistoryButton=boolean, docTag=string, dragCallback=script, drawInactiveFrame=boolean, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, enterCommand=script, exists=boolean, fileName=string, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, insertText=string, insertionPosition=int, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, placeholderText=string, popupMenuArray=boolean, preventOverride=boolean, receiveFocusCommand=script, searchField=boolean, text=string, textChangedCommand=script, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    textField is undoable, queryable, and editable.
    

    
Create a text field control.

    """
    pass
    


def textFieldButtonGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, buttonCommand=script, buttonLabel=string, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, enableButton=boolean, exists=boolean, fileName=string, forceChangeCommand=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, insertText=string, insertionPosition=int, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, placeholderText=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, text=string, textChangedCommand=script, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    textFieldButtonGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command adds a button to the textFieldGrp command.

    """
    pass
    


def textFieldGrp( groupName , adjustableColumn=int, adjustableColumn2=int, adjustableColumn3=int, adjustableColumn4=int, adjustableColumn5=int, adjustableColumn6=int, annotation=string, backgroundColor=float, float, float, changeCommand=script, columnAlign=int, string, columnAlign2=string, string, columnAlign3=string, string, string, columnAlign4=string, string, string, string, columnAlign5=string, string, string, string, string, columnAlign6=string, string, string, string, string, string, columnAttach=int, string, int, columnAttach2=string, string, columnAttach3=string, string, string, columnAttach4=string, string, string, string, columnAttach5=string, string, string, string, string, columnAttach6=string, string, string, string, string, string, columnOffset2=int, int, columnOffset3=int, int, int, columnOffset4=int, int, int, int, columnOffset5=int, int, int, int, int, columnOffset6=int, int, int, int, int, int, columnWidth=int, int, columnWidth1=int, columnWidth2=int, int, columnWidth3=int, int, int, columnWidth4=int, int, int, int, columnWidth5=int, int, int, int, int, columnWidth6=int, int, int, int, int, int, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, editable=boolean, enable=boolean, enableBackground=boolean, exists=boolean, fileName=string, forceChangeCommand=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, insertText=string, insertionPosition=int, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, placeholderText=string, popupMenuArray=boolean, preventOverride=boolean, rowAttach=int, string, int, text=string, textChangedCommand=script, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    textFieldGrp is undoable, queryable, and editable.
    

    
All of the group commands position their individual controls in columns starting at column 1. The layout of each control (ie. column) can be customized using the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and -adj/adjustableColumn flags. By default, columns are left aligned with no offset and are 100 pixels wide. Only one column in any group can be adjustable.
This command creates a pre-packaged collection of label text and editable text field. The label text is optional.

    """
    pass
    


def textManip(visible=boolean):
    """
    textManip is undoable, queryable, and NOT editable.
    

    
Shows/hides the text manip.

    """
    pass
    


def textScrollList( string , allItems=boolean, allowAutomaticSelection=boolean, allowMultiSelection=boolean, annotation=string, append=string, appendPosition=int, string, backgroundColor=float, float, float, defineTemplate=string, deleteKeyCommand=script, deselectAll=boolean, deselectIndexedItem=int, deselectItem=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, font=string, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, lineFont=int, string, manage=boolean, noBackground=boolean, numberOfItems=boolean, numberOfPopupMenus=boolean, numberOfRows=int, numberOfSelectedItems=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, removeAll=boolean, removeIndexedItem=int, removeItem=string, selectCommand=script, selectIndexedItem=int, selectItem=string, selectUniqueTagItem=string, showIndexedItem=int, uniqueTag=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    textScrollList is undoable, queryable, and editable.
    

    
This command creates/edits/queries a text scrolling list. The list can be in single select mode where only one item at at time is selected, or in multi-select mode where many items may be selected.
Note: The -dgc/dragCallback flag works only on Windows.

    """
    pass
    


def textureDeformer( selectionList , after=boolean, afterReference=boolean, before=boolean, deformerTools=boolean, direction=string, envelope=float, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, ignoreSelected=boolean, includeHiddenSelections=boolean, name=string, offset=float, parallel=boolean, pointSpace=string, prune=boolean, remove=boolean, split=boolean, strength=float, vectorOffset=float, float, float, vectorSpace=string, vectorStrength=float, float, float):
    """
    textureDeformer is undoable, queryable, and editable.
    

    
This command creates a texture deformer for the object. The selected objects are the input geometry objects. The deformer node name will be returned.

    """
    pass
    


def texturePlacementContext(exists=boolean, history=boolean, image1=string, image2=string, image3=string, labelMapping=boolean, name=string):
    """
    texturePlacementContext is undoable, queryable, and editable.
    

    
Create a command for creating new texture placement contexts. By default label mapping is on when the context is created.

    """
    pass
    


def textureWindow( string , backFacingColor=float, float, float, float, capture=string, captureSequenceNumber=int, changeCommand=string, string, string, string, checkerDensity=int, clearImage=boolean, cmEnabled=boolean, control=boolean, defineTemplate=string, displayAxes=boolean, displayCheckered=boolean, displayDistortion=boolean, displayDivisionLines=boolean, displayGridLines=boolean, displayImage=int, displayLabels=boolean, displayPreselection=boolean, displaySolidMap=boolean, displayStyle=string, distortionPerObject=boolean, divisions=int, docTag=string, doubleBuffer=boolean, drawAxis=boolean, drawSubregions=boolean, exists=boolean, exposure=float, filter=string, forceMainConnection=string, forceRebake=boolean, frameAll=boolean, frameSelected=boolean, frontFacingColor=float, float, float, float, gamma=float, highlightConnection=string, imageBaseColor=float, float, float, imageDisplay=boolean, imageNames=boolean, imageNumber=int, imagePixelSnap=boolean, imageRatio=boolean, imageSize=boolean, imageTileRange=float, float, float, float, imageUnfiltered=boolean, internalFaces=boolean, labelPosition=string, loadImage=string, lockMainConnection=boolean, mainListConnection=string, maxResolution=int, nbImages=boolean, numUvSets=boolean, numberOfImages=int, panel=string, parent=string, realSize=boolean, refresh=boolean, relatedFaces=boolean, removeAllImages=boolean, removeImage=boolean, rendererString=string, reset=boolean, saveImage=boolean, scaleBlue=float, scaleGreen=float, scaleRed=float, selectInternalFaces=boolean, selectRelatedFaces=boolean, selectionConnection=string, setUvSet=int, singleBuffer=boolean, size=float, spacing=float, stateString=boolean, style=int, tileLabels=boolean, toggle=boolean, toggleExposure=boolean, toggleGamma=boolean, unParent=boolean, unlockMainConnection=boolean, updateMainConnection=boolean, useFaceGroup=boolean, useTemplate=string, uvSets=boolean, viewPortImage=boolean, viewTransformName=string, writeImage=string):
    """
    textureWindow is undoable, queryable, and editable.
    

    
This command is used to create a UV Editor and to query or edit the texture editor settings.
The UV Editor displays texture mapped polygon objects in 2D texture space. Only active objects are visible in this window.
The UV Editor has the ability to display two types of images. The Texture Image is a visualisation of the current texture and associated placement parameters. The Editor Image is a user specified image loaded from disk.
A UV Editor can be invoked by selecting the "Window -> UV Texture Editor..." menu item from the main maya menu listing that appears at the top of the maya window. It can also be invoked by selecting the "Panel -> UV Editor" item under the "Panels" menu item that appears at the top right hand corner of the view.
As a UV Editor typically exists at start-up time, and as only one of these can exist at any given time, this command is normally used to query and edit the editor settings.

    """
    pass
    


def texTweakUVContext( object , exists=boolean, image1=string, image2=string, image3=string, position=boolean, tolerance=float):
    """
    texTweakUVContext is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts. Changing one context independently is not allowed. Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    """
    pass
    


def texWinToolCtx(alternateContext=boolean, boxzoom=boolean, dolly=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, toolName=string, track=boolean):
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
    


def threePointArcCtx(degree=uint, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, spans=uint):
    """
    threePointArcCtx is undoable, queryable, and editable.
    

    
The threePointArcCtx command creates a new context for creating 3 point arcs

    """
    pass
    


def thumbnailCaptureComponent( string , capture=boolean, capturedFrameCount=boolean, closeCurrentSession=boolean, delete=boolean, endFrame=int, fileDialogCallback=string, isSessionOpened=boolean, launchedFromOptionsBox=boolean, previewPath=boolean, removeProjectThumbnail=string, save=string, startFrame=int):
    """
    thumbnailCaptureComponent is undoable, queryable, and NOT editable.
    

    
This command is used to generate a thumbnail/playblast sequence from the scene.

    """
    pass
    


def timeCode(mayaStartFrame=float, productionStartFrame=float, productionStartHour=float, productionStartMinute=float, productionStartSecond=float):
    """
    timeCode is undoable, queryable, and editable.
    

    
Use this command to query and set the time code information in the file

    """
    pass
    


def timeControl( string , animCurveNames=boolean, animLayerFilterOptions=string, animLayerShowWeight=boolean, annotation=string, backgroundColor=float, float, float, beginScrub=boolean, currentFrameColor=float, float, float, float, defineTemplate=string, displaySound=boolean, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, endScrub=boolean, exists=boolean, forceRedraw=boolean, forceRefresh=boolean, foregroundColor=float, float, float, fullPathName=boolean, globalTime=boolean, greasePencilSequenceNames=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, mainListConnection=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, pressCommand=script, preventOverride=boolean, range=boolean, rangeArray=boolean, rangeVisible=boolean, releaseCommand=script, repeatChunkSize=float, repeatOnHold=boolean, resample=boolean, showGreaseFrames=string, showKeys=string, showKeysCombined=boolean, snap=boolean, sound=string, tickSize=int, tickSpan=int, useTemplate=string, visible=boolean, visibleChangeCommand=script, waveform=string, width=int):
    """
    timeControl is undoable, queryable, and editable.
    

    
This command creates a control that can be used for changing current time, displaying/editing keys, and displaying/scrubbing sound.
Note: only one timeControl may be created. The one Maya creates on startup can be accessed from the global string variable $gPlayBackSlider. Also, it is not a good idea to delete it.

    """
    pass
    


def timePort( name , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, globalTime=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, snap=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    timePort is undoable, queryable, and editable.
    

    
This command creates a simple time control widget. See also the "timeControl" command.

    """
    pass
    


def timer(endTimer=boolean, lapTime=boolean, name=string, startTimer=boolean):
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
    


def timeWarp(deleteFrame=int, frame=float, g=boolean, interpType=int, string, moveFrame=int, float):
    """
    timeWarp is undoable, queryable, and editable.
    

    
This command is used to create a time warp input to a set of animation curves.

    """
    pass
    


def toggle( objects , above=boolean, below=boolean, boundary=boolean, boundingBox=boolean, controlVertex=boolean, doNotWrite=boolean, editPoint=boolean, extent=boolean, facet=boolean, geometry=boolean, gl=boolean, highPrecisionNurbs=boolean, hull=boolean, latticePoint=boolean, latticeShape=boolean, localAxis=boolean, newCurve=boolean, newPolymesh=boolean, newSurface=boolean, normal=boolean, origin=boolean, point=boolean, pointDisplay=boolean, pointFacet=boolean, rotatePivot=boolean, scalePivot=boolean, selectHandle=boolean, state=boolean, surfaceFace=boolean, template=boolean, uvCoords=boolean, vertex=boolean):
    """
    toggle is undoable, queryable, and NOT editable.
    

    
The toggle command is used to toggle the display of various object features for objects which have these components. For example, CV and edit point display may be toggled for those listed NURB curves or surfaces.
Note: This command is not undoable.

    """
    pass
    


def toggleAxis(origin=boolean, view=boolean):
    """
    toggleAxis is undoable, queryable, and NOT editable.
    

    
Toggles the state of the display axis.
Note: the display of the axis in the bottom left corner has been rendered obsolete by the headsUpDisplay command.

    """
    pass
    


def toggleWindowVisibility( string ):
    """
    toggleWindowVisibility is undoable, NOT queryable, and NOT editable.
    

    
Toggle the visibility of a window. If no window is specified then the current window (most recently created) is used. See also the window command's vis/visible flag.

    """
    pass
    


def tolerance(angular=angle, linear=linear):
    """
    tolerance is undoable, queryable, and NOT editable.
    

    
This command sets tolerances used by modelling operations that require a tolerance, such as surface fillet. Linear tolerance is also known as "positional" tolerance. Angular tolerance is also known as "tangential" tolerance.

    """
    pass
    


def toolBar( name , allowedArea=string, annotation=string, area=string, backgroundColor=float, float, float, content=string, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, label=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    toolBar is undoable, queryable, and editable.
    

    
Create a toolbar. Tool bars are movable panel that contains a set of controls. They are placed in the tool bar area around the central control in a main window. Tool bars can be moved inside their current area, moved into new areas and floated.

    """
    pass
    


def toolButton( string , allowMultipleTools=boolean, annotation=string, backgroundColor=float, float, float, changeCommand=script, collection=string, defineTemplate=string, docTag=string, doubleClickCommand=script, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, image1=string, image2=string, image3=string, imageOverlayLabel=string, isObscured=boolean, ltVersion=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, offCommand=script, onCommand=script, parent=string, popupIndicatorVisible=boolean, popupMenuArray=boolean, preventOverride=boolean, select=boolean, style=string, tool=string, toolArray=boolean, toolCount=boolean, toolImage1=string, string, toolImage2=string, string, toolImage3=string, string, useTemplate=string, version=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    toolButton is undoable, queryable, and editable.
    

    
This command creates a toolButton that is added to the most recently created tool button collection unless the cl/collection flag is used. It also attaches the named tool, activating it when this control is selected.
By default, this control only handles one tool at a time. Using the t/tool flag to associate a new tool will simply override the previous attached tool. If you use the amt/allowMultipleTools flag then you will be able to attach more than one tool with this control. Only one tool will be current within the control. To access the other tools press the right mouse button to display a popup menu containing all the tools associated with this control. If you set the piv/popupIndicatorVisible flag then a small arrow will be drawn on the control to indicate that additional tools are attached to this control.

    """
    pass
    


def toolCollection( string , collectionItemArray=boolean, defineTemplate=string, exists=boolean, gl=boolean, numberOfCollectionItems=boolean, parent=string, select=string, useTemplate=string):
    """
    toolCollection is undoable, queryable, and editable.
    

    
This command creates a tool button collection. Collections are parented to the current default layout if no parent is specified with the -p/parent flag. As children of the layout they will be deleted when the layout is deleted. Collections may also span more than one window if the -gl/global flag is used. In this case the collection has no parent and must be explicitly deleted with the 'deleteUI' command when it is no longer wanted.

    """
    pass
    


def toolDropped( string ):
    """
    toolDropped is undoable, NOT queryable, and NOT editable.
    

    
This command builds and executes the commands necessary to recreate the specified tool button. It is invoked when a tool is dropped on the shelf.

    """
    pass
    


def toolHasOptions( string ):
    """
    toolHasOptions is undoable, NOT queryable, and NOT editable.
    

    
This command queries a tool to see if it has options. If it does, it returns true. Otherwise it returns false.

    """
    pass
    


def toolPropertyWindow(field=string, helpButton=string, icon=string, inMainWindow=boolean, location=string, noviceMode=boolean, resetButton=string, selectCommand=string, showCommand=string):
    """
    toolPropertyWindow is undoable, queryable, and editable.
    

    
End users should only call this command as 1. a query (in the custom tool property sheet code) or 2. with no arguments to create the default tool property sheet. The more complex uses of it are internal.

    """
    pass
    


def torus(axis=linear, linear, linear, caching=boolean, constructionHistory=boolean, degree=int, endSweep=angle, heightRatio=float, minorSweep=angle, name=string, nodeState=int, object=boolean, pivot=linear, linear, linear, polygon=int, radius=linear, sections=int, spans=int, startSweep=angle, tolerance=linear, useTolerance=boolean):
    """
    torus is undoable, queryable, and editable.
    

    
The torus command creates a new torus and/or a dependency node that creates one, and returns their names.

    """
    pass
    


def track( camera , down=linear, left=linear, right=linear, upDistance01=linear, upDistance02=linear):
    """
    track is undoable, NOT queryable, and NOT editable.
    

    
The track command translates a camera horizontally or vertically in the world space. The viewing-direction and up-direction of the camera are not altered. There is no translation in the viewing direction.
The track command can be applied to either a perspective or an orthographic camera.
When no camera name is supplied, this command is applied to the camera in the active view.

    """
    pass
    


def trackCtx(alternateContext=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, toolName=string, trackGeometry=boolean, trackScale=float):
    """
    trackCtx is undoable, queryable, and editable.
    

    
This command can be used to create a track context.

    """
    pass
    


def transferAttributes(*args, **kwargs):
    """
    transferAttributes is undoable, queryable, and editable.
    

    
Samples the attributes of a source surface (first argument) and transfers them onto a target surface (second argument).

    """
    pass
    


def transferShadingSets(sampleSpace=uint, searchMethod=uint):
    """
    transferShadingSets is undoable, queryable, and editable.
    

    
Command to transfer shading set assignments between meshes. The last mesh in the list receives the shading assignments from the other meshes.

    """
    pass
    


def transformCompare( dagObject dagObject , root=boolean):
    """
    transformCompare is undoable, NOT queryable, and NOT editable.
    

    
Compares two transforms passed as arguments. If they are the same, returns 0. If they are different, returns 1. If no transforms are specified in the command line, then the transforms from the active list are used.

    """
    pass
    


def transformLimits( object , enableRotationX=boolean, boolean, enableRotationY=boolean, boolean, enableRotationZ=boolean, boolean, enableScaleX=boolean, boolean, enableScaleY=boolean, boolean, enableScaleZ=boolean, boolean, enableTranslationX=boolean, boolean, enableTranslationY=boolean, boolean, enableTranslationZ=boolean, boolean, remove=boolean, rotationX=angle, angle, rotationY=angle, angle, rotationZ=angle, angle, scaleX=float, float, scaleY=float, float, scaleZ=float, float, translationX=linear, linear, translationY=linear, linear, translationZ=linear, linear):
    """
    transformLimits is undoable, queryable, and editable.
    

    
The transformLimits command allows us to set, edit, or query the limits of the transformation that can be applied to objects.
We can also turn any limits off which may have been previously set. When an object is first created, all the transformation limits are off by default.
Transformation limits allow us to control how much an object can be transformed. This is most useful for joints, although it can be used any place we would like to limit the movement of an object.
Default values are:
( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    """
    pass
    


def translator( string , defaultFileRule=boolean, defaultOptions=string, extension=boolean, fileCompression=string, filter=boolean, list=boolean, loaded=boolean, objectType=boolean, optionsScript=boolean, readSupport=boolean, writeSupport=boolean):
    """
    translator is undoable, queryable, and NOT editable.
    

    
Set or query parameters associated with the file translators specified in as the argument.

    """
    pass
    


def treeLister( string , addFavorite=string, addItem=string, string, script, addVnnItem=string, string, string, annotation=string, backgroundColor=float, float, float, clearContents=boolean, collapsePath=string, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, executeItem=string, exists=boolean, expandPath=string, expandToDepth=int, favoritesCallback=script, favoritesList=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, itemScript=string, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, refreshCommand=script, removeFavorite=string, removeItem=string, resultsPathUnderCursor=boolean, selectPath=string, useTemplate=string, visible=boolean, visibleChangeCommand=script, vnnString=boolean, width=int):
    """
    treeLister is undoable, queryable, and editable.
    

    
This command creates/edits/queries the tree lister control. The optional argument is the name of the control.

    """
    pass
    


def treeView( string , addItem=string, string, allowDragAndDrop=boolean, allowHiddenParents=boolean, allowMultiSelection=boolean, allowReparenting=boolean, annotation=string, attachButtonRight=int, backgroundColor=float, float, float, borderHighlite=string, boolean, borderHighliteColor=string, float, float, float, buttonErase=boolean, buttonState=string, int, string, buttonStyle=string, int, string, buttonTextIcon=string, int, string, buttonTooltip=string, int, string, buttonTransparencyColor=string, int, float, float, float, buttonTransparencyOverride=string, int, boolean, buttonVisible=string, int, boolean, children=string, clearSelection=boolean, contextMenuCommand=script, defineTemplate=string, displayLabel=string, string, displayLabelSuffix=string, string, docTag=string, dragAndDropCommand=script, dragCallback=script, dropCallback=script, editLabelCommand=script, enable=boolean, enableBackground=boolean, enableButton=string, int, int, enableKeys=boolean, enableLabel=string, int, exists=boolean, expandCollapseCommand=script, expandItem=string, boolean, font=string, string, fontFace=string, int, fullPathName=boolean, height=int, hideButtons=boolean, highlightColor=float, float, float, highlite=string, boolean, highliteColor=string, float, float, float, ignoreButtonClick=string, int, int, image=string, int, string, isItemExpanded=string, isLeaf=string, isObscured=boolean, item=string, itemAnnotation=string, string, itemDblClickCommand=script, itemDblClickCommand2=script, itemExists=string, itemIndex=string, itemParent=string, itemRenamedCommand=script, itemSelected=string, itemVisible=string, boolean, labelBackgroundColor=string, float, float, float, manage=boolean, noBackground=boolean, numberOfButtons=int, numberOfPopupMenus=boolean, ornament=string, int, int, int, ornamentColor=string, float, float, float, parent=string, popupMenuArray=boolean, pressCommand=int, script, preventOverride=boolean, removeAll=boolean, removeItem=string, reverseTreeOrder=boolean, rightPressCommand=int, script, selectCommand=script, selectItem=string, boolean, selectionChangedCommand=script, selectionColor=string, float, float, float, showItem=string, textColor=string, float, float, float, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    treeView is undoable, queryable, and editable.
    

    
This command creates a custom control.

    """
    pass
    


def trim( objects , caching=boolean, constructionHistory=boolean, locatorU=float, locatorV=float, name=string, nodeState=int, object=boolean, selected=int, shrink=boolean, tolerance=linear):
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
    


def tumble( camera , azimuthAngle=angle, elevationAngle=angle, localTumble=int, pivotPoint=linear, linear, linear, rotationAngles=angle, angle):
    """
    tumble is undoable, NOT queryable, and NOT editable.
    

    
The tumble command revolves the camera(s) by varying the azimuth and elevation angles in the perspective window. When both the azimuth and the elevation angles are supplied on the command line, the camera is firstly tumbled for the azimuth angle, then tumbled for the elevation angle.
When no camera name is supplied, this command is applied to the camera in the active view.
The camera's rotate pivot will override a specified pivot point if the rotate pivot is not at the camera's eye point.

    """
    pass
    


def tumbleCtx(alternateContext=boolean, autoOrthoConstrain=boolean, autoSetPivot=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, localTumble=int, name=string, objectTumble=boolean, orthoLock=boolean, orthoStep=angle, toolName=string, tumbleScale=float):
    """
    tumbleCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a tumble context.

    """
    pass
    


def turbulence( selectionList , attenuation=float, frequency=float, magnitude=float, maxDistance=linear, name=string, noiseLevel=int, noiseRatio=float, perVertex=boolean, phase=float, phaseX=float, phaseY=float, phaseZ=float, position=linear, linear, linear):
    """
    turbulence is undoable, queryable, and editable.
    

    
A turbulence field causes irregularities (also called 'noise' or 'jitter') in the motion of affected objects.
Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def twoPointArcCtx(degree=uint, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, spans=uint):
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
    


def uiTemplate( string , exists=boolean):
    """
    uiTemplate is undoable, queryable, and editable.
    

    
This command creates a new command template object. Template objects can hold default flag arguments for multiple UI commands. The command arguments are specified with the individual commands using the -defineTemplate flag and the desired flags and arguments. See also setUITemplate.

    """
    pass
    


def unassignInputDevice(clutch=string, device=string):
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
    


def undoInfo(chunkName=string, closeChunk=boolean, infinity=boolean, length=uint, openChunk=boolean, printQueue=boolean, redoName=string, redoQueueEmpty=boolean, state=boolean, stateWithoutFlush=boolean, undoName=string, undoQueueEmpty=boolean):
    """
    undoInfo is undoable, queryable, and NOT editable.
    

    
This command controls the undo/redo parameters.
In query mode, if invoked without flags (other than the query flag), this command will return the number of items currently on the undo queue.

    """
    pass
    


def unfold(applyToShell=boolean, areaWeight=float, globalBlend=float, globalMethodBlend=float, iterations=int, optimizeAxis=int, pinSelected=boolean, pinUvBorder=boolean, scale=float, stoppingThreshold=float, useScale=boolean):
    """
    unfold is undoable, NOT queryable, and NOT editable.
    

    
None

    """
    pass
    


def ungroup( objects... , absolute=boolean, parent=string, relative=boolean, world=boolean):
    """
    ungroup is undoable, NOT queryable, and NOT editable.
    

    
This command ungroups the specified objects.
The objects will be placed at the same level in the hierarchy the group node occupied unless the -w flag is specified, in which case they will be placed under the world.
If an object is ungrouped and there is an object in the new group with the same name then this command will rename the ungrouped object.
See also: group, parent, instance, duplicate

    """
    pass
    


def uniform( selectionList , attenuation=float, directionX=float, directionY=float, directionZ=float, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear):
    """
    uniform is undoable, queryable, and editable.
    

    
A uniform field pushes objects in a fixed direction. The field strength, but not the field direction, depends on the distance from the object to the field location.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def unknownNode(plugin=boolean, realClassName=boolean, realClassTag=boolean):
    """
    unknownNode is undoable, queryable, and NOT editable.
    

    
Allows querying of the data stored for unknown nodes (nodes that are defined by a plug-in that Maya could not load when loading a scene file).

    """
    pass
    


def unknownPlugin(dataTypes=boolean, list=boolean, nodeTypes=boolean, remove=boolean, version=boolean):
    """
    unknownPlugin is undoable, queryable, and NOT editable.
    

    
Allows querying of the unknown plug-ins used by the scene, and provides a means to remove them.

    """
    pass
    


def unloadPlugin( string string... , addCallback=script, force=boolean, removeCallback=script):
    """
    unloadPlugin is undoable, NOT queryable, and NOT editable.
    

    
Unload plug-ins from Maya. After the successful execution of this command, plug-in services will no longer be available.

    """
    pass
    


def untangleUV(mapBorder=string, maxRelaxIterations=int, pinBorder=boolean, pinSelected=boolean, pinUnselected=boolean, relax=string, relaxTolerance=float, shapeDetail=float):
    """
    untangleUV is undoable, NOT queryable, and NOT editable.
    

    
This command will aid in the creation of non-overlapping regions (i.e. polygons) in texture space by untangling texture UVs. This is done in two stages:
1) Use this command to map the UV border determined by the current selection or passed component into a shape that is more suitable for subsequent relaxation.
2) Relax all the internal texture UVs by performing a length minimization algorithm on all edges in texture space.

    """
    pass
    


def untrim( surface , caching=boolean, constructionHistory=boolean, curveOnSurface=boolean, name=string, noChanges=boolean, nodeState=int, object=boolean, replaceOriginal=boolean, untrimAll=boolean):
    """
    untrim is undoable, queryable, and editable.
    

    
Untrim the surface.

    """
    pass
    


def upAxis(axis=string, rotateView=boolean):
    """
    upAxis is undoable, queryable, and NOT editable.
    

    
The upAxis command changes the world up direction. Current implementation provides only two choices of axis (the Y-axis or the Z-axis) as the world up direction.
By default, the ground plane in Maya is on the XY plane. Hence, the default up-direction is the direction of the positive Z-axis.
The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag is specified, the camera of currently active view is revolved about the X-axis such that the position of the groundplane in the view will remain the same as before the the up direction is changed.
The screen update is applied to all cameras of all views.

    """
    pass
    


def uvLink( objects , b=boolean, isValid=boolean, make=boolean, queryObject=name, texture=name, uvSet=name):
    """
    uvLink is undoable, queryable, and NOT editable.
    

    
This command is used to make, break and query UV linking relationships between UV sets on objects and textures that use those UV sets.
If no make, break or query flag is specified and both uvSet and texture flags are present, the make flag is assumed to be specified.
If no make, break or query flag is specified and only one of the uvSet and texture flags is present, the query flag is assumed to be specified.
The term "texture" in the context of UV linking is a bit of an oversimplification. In fact, UV sets can be linked to any node which takes UV coordinates as input. However in most cases it will be a texture to which you wish to link a UV set.

    """
    pass
    


def uvSnapshot(antiAliased=boolean, blueColor=int, entireUVRange=boolean, fileFormat=string, greenColor=int, name=string, overwrite=boolean, redColor=int, uMax=float, uMin=float, uvSetName=string, vMax=float, vMin=float, xResolution=int, yResolution=int):
    """
    uvSnapshot is NOT undoable, NOT queryable, and NOT editable.
    

    
Builds an image containg the UVs of the selected objects.

    """
    pass
    


def vectorize(browserView=boolean, byFrame=float, camera=string, combineFillsEdges=boolean, currentFrame=boolean, curveTolerance=float, customExtension=string, detailLevel=int, edgeColor=int, int, int, edgeDetail=boolean, edgeStyle=string, edgeWeight=float, endFrame=float, filenameFormat=string, fillStyle=string, flashVersion=int, frameRate=int, height=int, hiddenEdges=boolean, highlightLevel=int, highlights=boolean, imageFormat=string, layer=name, minEdgeAngle=float, outlinesAtIntersections=boolean, outputFileName=string, pixelAspectRatio=float, reflectionDepth=int, reflections=boolean, renderLayers=boolean, renderOptimization=string, renderView=boolean, secondaryCurveFitting=boolean, shadows=boolean, showBackFaces=boolean, startFrame=float, svgAnimation=string, svgCompression=boolean, width=int):
    """
    vectorize is NOT undoable, NOT queryable, and NOT editable.
    

    
This command renders Maya scenes to various vector and raster formats using the Maya Vector renderer.

    """
    pass
    


def view2dToolCtx(alternateContext=boolean, boxzoom=boolean, dolly=boolean, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, toolName=string, track=boolean):
    """
    view2dToolCtx is undoable, queryable, and editable.
    

    
This class creates a context for the View Tools "track", "dolly", and "box zoom" in the Hypergraph.

    """
    pass
    


def viewCamera( camera , move=name, sideView=boolean, topView=boolean):
    """
    viewCamera is undoable, NOT queryable, and NOT editable.
    

    
The viewCamera command is used to position a camera to look directly at the side or top of another camera. This is primarily useful for the user when he or she is setting depth-of-field and clipping planes, if they are being used.
The default behaviour: If no other flags are specified, the camera in the active panel is moved and the -t is presumed. If there is a camera selected, it is used as the target camera.

    """
    pass
    


def viewClipPlane( camera , autoClipPlane=boolean, farClipPlane=linear, nearClipPlane=linear, surfacesOnly=boolean):
    """
    viewClipPlane is undoable, queryable, and NOT editable.
    

    
The viewClipPlane command can be used to query or set a camera's clip planes. If a camera is not specified, the camera in the active view will be used. The near and far clip plane flags may be used in conjunction with the auto clip plane flag.

    """
    pass
    


def viewFit( camera , allObjects=boolean, animate=boolean, center=boolean, fitFactor=float, namespace=string):
    """
    viewFit is undoable, NOT queryable, and NOT editable.
    

    
The viewFit command positions the specified camera so its point-of-view contains all selected objects other than itself. If no objects are selected, everything is fit to the view (excepting cameras, lights, and sketching plannes). The fit-factor, if specified, determines how much of the view should be filled. If a camera is not specified, the camera in the active view will be used. After the camera is moved, its center of interest is set to the center of the bounding box of the objects.

    """
    pass
    


def viewHeadOn( camera ):
    """
    viewHeadOn is undoable, NOT queryable, and NOT editable.
    

    
The viewHeadOn command positions the specified camera so it is looking "down" the normal of the live object, and fitted to the live object. If the live object is a surface, an arbitrary normal is chosen.

    """
    pass
    


def viewLookAt( camera , position=linear, linear, linear):
    """
    viewLookAt is undoable, NOT queryable, and NOT editable.
    

    
The viewLookAt command positions the specified camera so it is looking at the centroid of all selected objects. If no objects are specified the camera will look at the ground plane.

    """
    pass
    


def viewManip(bottomLeft=boolean, bottomRight=boolean, compassAngle=float, dragSnap=boolean, drawCompass=boolean, fitToView=boolean, levelCamera=boolean, minOpacity=float, restoreCenter=boolean, size=string, topLeft=boolean, topRight=boolean, visible=boolean, zoomToFitScene=boolean):
    """
    viewManip is undoable, queryable, and NOT editable.
    

    
Mel access to the view cube manipulator.

    """
    pass
    


def viewPlace( camera , animate=boolean, eyePoint=linear, linear, linear, fieldOfView=angle, lookAt=linear, linear, linear, ortho=boolean, perspective=boolean, upDirection=linear, linear, linear, viewDirection=linear, linear, linear):
    """
    viewPlace is undoable, NOT queryable, and NOT editable.
    

    
This command positions the camera as specified. The lookAt and viewDirection flags are mutually exclusive, as are the ortho and perspective flags. If this command switches a camera from ortho to perspective or the other way around without specifying a new field of view, then one is calculated based on a heuristic involving the selected objects.
If the camera is not specified on the command line, the command will check to see if there is a camera on the active list.
The user should be aware that some positions will be unattainable. For example, using a new camera located at the origin and specifying a lookAt of [0 0 -5] and an up of [1 1 1]. In these cases, the camera will always aim at the lookAt, and the new up direction will be determined by transforming the specified up into camera space and then projecting this vector onto a plane defined by the camera's up and right vectors. Using the example above, the new up vector will be [1 1 0].

    """
    pass
    


def viewSet( camera , animate=boolean, back=boolean, bottom=boolean, fit=boolean, fitFactor=float, front=boolean, home=boolean, keepRenderSettings=boolean, leftSide=boolean, namespace=string, nextView=boolean, persp=boolean, previousView=boolean, rightSide=boolean, side=boolean, top=boolean, viewNegativeX=boolean, viewNegativeY=boolean, viewNegativeZ=boolean, viewX=boolean, viewY=boolean, viewZ=boolean):
    """
    viewSet is undoable, queryable, and NOT editable.
    

    
This command positions the camera to one of the pre-defined positions. If the fit flag is set in conjunction with persp, top, side, or front, the view is "fit" based on the list of selected objects (if there are any) or on all the objects if nothing is selected. Notice that the fit flag cannot be set in conjunction with view along axis commands like viewX. If a camera is not specified, the camera in the active view will be used. If no flag is specified, the camera is set to the home position.

    """
    pass
    


def visor(addFolder=boolean, addNodes=string, allowPanningInX=boolean, allowPanningInY=boolean, allowZooming=boolean, command=string, deleteFolder=string, editFolder=string, folderList=string, menu=string, name=string, nodeType=string, openDirectories=boolean, openFolder=boolean, parent=string, path=string, popupMenuScript=string, rebuild=boolean, refreshAllSwatches=boolean, refreshSelectedSwatches=boolean, refreshSwatch=string, reset=boolean, restrictPanAndZoom=boolean, saveSwatches=boolean, scrollBar=string, scrollPercent=float, selectedGadgets=string, showDividers=boolean, showFiles=boolean, showFolders=boolean, showNodes=boolean, stateString=boolean, style=string, transform=string, type=string):
    """
    visor is undoable, queryable, and NOT editable.
    

    
Command for the creation and manipulation of a Visor UI element. The Visor is used to display the contents of a scene (rendering related nodes in particular), as well as files on disk which the user may wish to bring into the scene (shader and texture libraries for example).

    """
    pass
    


def vnn(flushProxies=string, libraries=string, listPortTypes=string, nodes=string, string, runTimes=boolean):
    """
    vnn is NOT undoable, queryable, and NOT editable.
    

    
This command is used for operations that apply to a whole VNN runtime, for example Bifrost. The Create Node window uses it to build its list of nodes.

    """
    pass
    


def vnnCompound( string string , addNode=string, addStatePortUI=boolean, canResetToFactory=string, connected=boolean, connectedTo=string, connectedToInput=boolean, connectedToOutput=boolean, create=string, createInputPort=string, string, createOutputPort=string, string, deletePort=string, explode=string, inputPort=boolean, listNodes=boolean, listPortChildren=string, listPorts=boolean, moveNodeIn=string, movePort=string, int, nodeType=string, outputPort=boolean, queryIsReferenced=boolean, queryMetaData=string, queryPortDataType=string, queryPortMetaDataValue=string, string, removeNode=string, renameNode=string, string, renamePort=string, string, resetToFactory=string, saveAs=string, setIsReferenced=boolean, setMetaData=string, string, setPortDataType=string, string, setPortMetaDataValue=string, string, string, specializedTypeName=boolean):
    """
    vnnCompound is undoable, NOT queryable, and NOT editable.
    

    
The vnnCompound command is used to operate compound and its VNN graph. The first parameter is the full name of the DG node that contains the VNN graph. The second parameter is the name of the compound.

    """
    pass
    


def vnnConnect( string string string , disconnect=boolean):
    """
    vnnConnect is undoable, NOT queryable, and NOT editable.
    

    
Makes a connection between two VNN node ports. The first parameter is the full name of the DG node that contains the VNN graph. The next two parameters are the full path of the ports from the root of the VNN container. This command can be used for compound or node connections, and the parameters can be out-of-order.

    """
    pass
    


def vnnCopy( string string , sourceNode=string):
    """
    vnnCopy is NOT undoable, NOT queryable, and NOT editable.
    

    
Copy a set of VNN nodes to clipper board. The first parameter is the full name of the DG node that contains the VNN graph. The second parameter is the full path of the parent VNN compound. The source VNN nodes must be set by the flag "-sourceNode".

    """
    pass
    


def vnnNode( string string , connected=boolean, connectedTo=string, listConnectedNodes=boolean, listPortChildren=string, listPorts=boolean, portDefaultValue=string, string, queryPortDataType=string, queryPortDefaultValue=string):
    """
    vnnNode is undoable, NOT queryable, and NOT editable.
    

    
The vnnNode command is used to operate vnnNode and query its port and connections. The first argument is the full name of the DG node that the VNN node is in. The second argument is the name of the full path of the VNN node.

    """
    pass
    


def vnnPaste( string string ):
    """
    vnnPaste is undoable, NOT queryable, and NOT editable.
    

    
Paste the copied VNN nodes to target VNN compound. The first parameter is the full name of the DG node that contains the VNN graph. The second parameter is the full path of the target VNN compound. A "vnnCopy" must be called before this command is called.

    """
    pass
    


def volumeAxis( selectionList , alongAxis=float, aroundAxis=float, attenuation=float, awayFromAxis=float, awayFromCenter=float, detailTurbulence=float, directionX=float, directionY=float, directionZ=float, directionalSpeed=float, invertAttenuation=boolean, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear, turbulence=float, turbulenceFrequencyX=float, turbulenceFrequencyY=float, turbulenceFrequencyZ=float, turbulenceOffsetX=float, turbulenceOffsetY=float, turbulenceOffsetZ=float, turbulenceSpeed=float):
    """
    volumeAxis is undoable, queryable, and editable.
    

    
A volume axis field can push particles in four directions, defined with respect to a volume: along the axis, away from the axis or center, around the axis, and in a user-specified direction. These are analogous to the emission speed controls of volume emitters. The volume axis field also contains a wind turbulence model (different from the turbulence field) that simulates an evolving flow of liquid or gas. The turbulence has a build in animation that is driven by a connection to a time node.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def volumeBind( objects , influence=string, name=string):
    """
    volumeBind is undoable, queryable, and editable.
    

    
Command for creating and editing volume binding nodes. The node is use for storing volume data to define skin weighting data.

    """
    pass
    


def vortex( selectionList , attenuation=float, axisX=float, axisY=float, axisZ=float, magnitude=float, maxDistance=linear, name=string, perVertex=boolean, position=linear, linear, linear):
    """
    vortex is undoable, queryable, and editable.
    

    
A vortex field pulls objects in a circular direction, like a whirlpool or tornado. Objects affected by the vortex field tend to rotate around the axis specified by -ax, -ay, and -az.
The transform is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object.
If fields are created, this command returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name is returned.
If object names are provided or the active selection list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0.
Setting the -pos flag with objects named on the command line is an error.

    """
    pass
    


def waitCursor(state=boolean):
    """
    waitCursor is undoable, queryable, and NOT editable.
    

    
This command sets/resets a wait cursor for the entire Maya application. This works as a stack, such that for each waitCursor -state on command executed there should be a matching waitCursor -state off command pending.
Warning: If a script fails that has turned the wait cursor on, the wait cursor may be left on. You need to turn it off manually from the command line by entering and executing the command 'waitCursor -state off'.

    """
    pass
    


def walkCtx(alternateContext=boolean, crouchCount=float, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, toolName=string, walkHeight=float, walkSensitivity=float, walkSpeed=float, walkToolHud=boolean):
    """
    walkCtx is undoable, queryable, and editable.
    

    
This command can be used to create, edit, or query a walk context.

    """
    pass
    


def warning(noContext=boolean, showLineNumber=boolean):
    """
    warning is NOT undoable, NOT queryable, and NOT editable.
    

    
The warning command is provided so that the user can issue warning messages from his/her scripts. The string argument is displayed in the command window (or stdout if running in batch mode) after being prefixed with a warning message heading and surrounded by the appropriate language separators (# for Python, // for Mel).

    """
    pass
    


def webBrowser( string , annotation=string, backgroundColor=float, float, float, defineTemplate=string, docTag=string, dragCallback=script, dropCallback=script, enable=boolean, enableBackground=boolean, exists=boolean, fullPathName=boolean, height=int, highlightColor=float, float, float, isObscured=boolean, manage=boolean, noBackground=boolean, numberOfPopupMenus=boolean, parent=string, popupMenuArray=boolean, preventOverride=boolean, useTemplate=string, visible=boolean, visibleChangeCommand=script, width=int):
    """
    webBrowser is undoable, queryable, and editable.
    

    
This command is obsolete and will be removed in next version of Maya. The internal web browser of Maya has been replaced by a plug-in which allows your own browser to connect with Maya. Please refer help for information on how to setup communication of Maya with external web browser application.

    """
    pass
    


def webView(urlAddress=string, windowHeight=int, windowWidth=int):
    """
    webView is undoable, NOT queryable, and NOT editable.
    

    
This command allows the user to bring up a web page view

    """
    pass
    


def whatsNewHighlight(highlightColor=float, float, float, highlightOn=boolean, showStartupDialog=boolean):
    """
    whatsNewHighlight is undoable, queryable, and NOT editable.
    

    
This command is used to toggle the What's New highlighting feature, and the display of the settings dialog for the feature that appears on startup.

    """
    pass
    


def window( string , backgroundColor=float, float, float, closeCommand=script, defineTemplate=string, docTag=string, dockCorner=string, string, dockStation=boolean, dockingLayout=string, exists=boolean, frontWindow=boolean, height=int, iconName=string, iconify=boolean, interactivePlacement=boolean, leftEdge=int, mainWindow=boolean, maximizeButton=boolean, menuArray=boolean, menuBar=boolean, menuBarVisible=boolean, menuIndex=string, uint, minimizeButton=boolean, minimizeCommand=script, nestedDockingEnabled=boolean, numberOfMenus=boolean, parent=string, resizeToFitChildren=boolean, restoreCommand=script, retain=boolean, sizeable=boolean, state=string, title=string, titleBar=boolean, titleBarMenu=boolean, toolbox=boolean, topEdge=int, topLeftCorner=int, int, useTemplate=string, visible=boolean, width=int, widthHeight=int, int):
    """
    window is undoable, queryable, and editable.
    

    
This command creates a new window but leaves it invisible. It is most efficient to add the window's elements and then make it visible with the showWindow command. The window can have an optional menu bar. Also, the title bar and minimize/maximize buttons can be turned on or off. If the title bar is off, then you cannot have minimize or maximize buttons.
Note: The window will require a control layout of some kind to arrange the controls (buttons, sliders, fields, etc.). Examples of control layouts are columnLayout, formLayout, rowLayout, etc.
Note: This command will clear the uiTemplate stack. Templates for a window need to be set after the window cmd.

    """
    pass
    


def windowPref( string , enableAll=boolean, exists=boolean, height=int, leftEdge=int, loadAll=boolean, maximized=boolean, parentMain=boolean, remove=boolean, removeAll=boolean, restoreMainWindowState=string, saveAll=boolean, saveMainWindowState=string, topEdge=int, topLeftCorner=int, int, width=int, widthHeight=int, int):
    """
    windowPref is undoable, queryable, and editable.
    

    
Create or modify preferred window attributes. The size and position of a window is retained during and between application sessions. A default window preference is created when a window is closed. Window preferences must be named and, consequently, only affect the window with a matching name.
Note that window preferences are not applied to the main Maya window nor the Command window.

    """
    pass
    


def wire( objects , after=boolean, afterReference=boolean, before=boolean, crossingEffect=float, deformerTools=boolean, dropoffDistance=uint, linear, envelope=float, exclusive=string, frontOfChain=boolean, geometry=string, geometryIndices=boolean, groupWithBase=boolean, holder=uint, string, ignoreSelected=boolean, includeHiddenSelections=boolean, localInfluence=float, name=string, parallel=boolean, prune=boolean, remove=boolean, split=boolean, wire=string, wireCount=uint):
    """
    wire is undoable, queryable, and editable.
    

    
This command creates a wire deformer.
In the create mode the selection list is treated as the object(s) to be deformed, Wires are specified with the -w flag. Each wire can optionally have a holder which helps define the the regon of the object that is affected by the deformer.

    """
    pass
    


def wireContext( string , crossingEffect=linear, deformationOrder=string, dropoffDistance=linear, envelope=linear, exclusive=boolean, exclusivePartition=string, exists=boolean, groupWithBase=boolean, history=boolean, holder=boolean, image1=string, image2=string, image3=string, localInfluence=linear, name=string):
    """
    wireContext is undoable, queryable, and editable.
    

    
This command creates a tool that can be used to create a wire deformer.

    """
    pass
    


def workspace( string , active=boolean, baseWorkspace=string, create=string, directory=string, expandName=string, fileRule=string, string, fileRuleEntry=string, fileRuleList=boolean, filter=boolean, fullName=boolean, list=boolean, listFullWorkspaces=boolean, listWorkspaces=boolean, newWorkspace=boolean, objectType=string, string, objectTypeEntry=string, objectTypeList=boolean, openWorkspace=boolean, projectPath=string, removeFileRuleEntry=string, removeVariableEntry=string, renderType=string, string, renderTypeEntry=string, renderTypeList=boolean, rootDirectory=boolean, saveWorkspace=boolean, shortName=boolean, update=boolean, updateAll=boolean, variable=string, string, variableEntry=string, variableList=boolean):
    """
    workspace is undoable, queryable, and NOT editable.
    

    
Create, open, or edit a workspace associated with a given workspace file.
The string argument represents the workspace. If no workspace is specified then the current workspace is assumed.
A workspace provides the underlying definition of a Maya Project. Each project has an associated workspace file, named workspace.mel, which is stored in the project root directory. The workspace file defines a set of rules that map file types to their storage, either relative to the project root or as an absolute location. These rules are used when resolving file paths at runtime.
The workspace command operates directly on the low-level definition of the workspace to read, change and store the definition to the underlying file. Use of this command is not generally required, for most purposes it is recommended that project definition changes be done via the Project Window in the User Interface.

    """
    pass
    


def wrinkle( objects , axis=linear, linear, linear, branchCount=uint, branchDepth=uint, center=linear, linear, linear, crease=string, dropoffDistance=linear, envelope=linear, randomness=linear, style=string, thickness=linear, uvSpace=linear, linear, linear, linear, linear, wrinkleCount=uint, wrinkleIntensity=linear):
    """
    wrinkle is undoable, NOT queryable, and NOT editable.
    

    
The wrinkle command is used to create a network of wrinkles on a surface. It automatically creates a network of wrinkle curves that control a wire deformer. The wrinkle curves are attached to a cluster deformer.

    """
    pass
    


def wrinkleContext( string , branchCount=uint, branchDepth=uint, exists=boolean, history=boolean, image1=string, image2=string, image3=string, name=string, randomness=linear, style=string, thickness=linear, wrinkleCount=uint, wrinkleIntensity=linear):
    """
    wrinkleContext is undoable, queryable, and editable.
    

    
This command creates a context that creates wrinkles.

    """
    pass
    


def writeTake(angle=string, device=string, linear=string, noTime=boolean, precision=int, take=string, virtualDevice=string):
    """
    writeTake is undoable, NOT queryable, and NOT editable.
    

    
This action writes a take from a device with recorded data to a take (.mov) file. The writeTake action can also write the virtual definition of a device.
See also: recordDevice, readTake, defineVirtualDevice

    """
    pass
    


def xform( objects... , absolute=boolean, boundingBox=boolean, boundingBoxInvisible=boolean, centerPivots=boolean, centerPivotsOnComponents=boolean, deletePriorHistory=boolean, euler=boolean, matrix=float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, objectSpace=boolean, pivots=linear, linear, linear, preserve=boolean, preserveUV=boolean, reflection=boolean, reflectionAboutBBox=boolean, reflectionAboutOrigin=boolean, reflectionAboutX=boolean, reflectionAboutY=boolean, reflectionAboutZ=boolean, reflectionTolerance=float, relative=boolean, rotateAxis=angle, angle, angle, rotateOrder=string, rotatePivot=linear, linear, linear, rotateTranslation=linear, linear, linear, rotation=angle, angle, angle, scale=float, float, float, scalePivot=linear, linear, linear, scaleTranslation=linear, linear, linear, shear=float, float, float, translation=linear, linear, linear, worldSpace=boolean, worldSpaceDistance=boolean, zeroTransformPivots=boolean):
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
    


def xformConstraint(alongNormal=int, live=boolean, type=string):
    """
    xformConstraint is undoable, queryable, and editable.
    

    
This command allows you to change the transform constraint used by the transform tools during component transforms.

    """
    pass
    


def xpmPicker(fileName=string, parent=string):
    """
    xpmPicker is undoable, NOT queryable, and NOT editable.
    

    
Open a dialog and ask you to choose a xpm file

    """
    pass
    

