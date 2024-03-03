# Qt QML

## QML
QML is a language that sits on top of C++ (Qt-> a library in C++ layer)

QML is a declarative programming language.
You declare what your UI looks like


QML (UI)
Qt (C++ Library) -> Business Logic

## 02: History

Was used in Nokia for cross platform native app development. Nokia used it to unify their UI stacks. Used in their old phones. 

Design criteria for QML
- Intuitive UI
- Design Oriented language
- Rapid prototyping and production
- Easy deployment

## 03: Element and Properties

```
Item {
    width: 400;
    height: 200;

    Rectangle {
        x:100;
        y:50;
        height:100;
        width:height*2;
        color:"lightblue";
    }

    Rectangle {
        x:100;
        y:170;
        height:100;
        width:height*2;
        color:"lightblue";
    }
}
```
Set order of elements overlapping, the earlier elements in the file will be lower in the stack, so the later elements in the file appear on top in the UI
This is if `z` is not mentioned.
if `z` mentioned, it will arange based on its values.

## 04: Understanding Properties

Property Bindings
```
Rectangle {
    id: RectangleId;
    x:100;
    y:50;
    width:height*2;
    height:100;
    color:"lightblue";
}
```
Positions of properties do not matter. Width is twice the height no matter what the value of height is at any point of time, which makes it dynamic in nature.

We can reference any element using its `id` property which is set

## 05: Exercise

Q) Can items overlap?
A) Yes

Q) Can child items be displayed outside their parents?
A) Yes

set `clip: true` to avoid child elements being displayed outside the parent

## 07: Images

```
Rectangle {
    x:100;
    y:50;
    width:height*2;
    height:100;
    color:"lightblue";

    Image {
        source: "../images/image.png";
        id: image
        x: 150;
        y: 150;
        Component.onCompleted:console.log("hello");
        onStatusChanged: console.log("status changed");

        Rectangle{
            visible: image.progress!=1
        }
    }
}
```

`sourceSize`: gives the actual size of the image
Images are loaded asynchorounsly
`progress` tells progress of image being loaded

`Scale` has 3 modes
- Stretch
- Repeat
- Round

## 08: Transformations

Can be applied to any items
Its applied on an element and all its childrens

Control properties
- opacity: 0-1
- scaling: size mutliplcation factor
- rotation: clockwise roattion in degrees

## 10: Anchor Layout

4 Different Layouts
3 layout managers and manual positioning
- Anchor
- Positioners
- QtQuick Controls Layout
- Manual Positioning

Anchors and QtQuick Layouts prefered

Anchor layout has
- left
- right
- top
- bottom
- horizontalCenter
- verticalCenter

using these, we can attach multiple elements

```
Rectangle {
    id:dad
    x:100;
    y:50;
    width:height*2;
    height:100;
    color:"lightblue";

    Rectangle {
        width:height*2;
        height:100;
        anchors: {
            right: dad.right;
            top: parent.top; //you can directly reference parent
        }
    }
}
```

`anchors.centerIn:parent`
`anchors.fill:parent`

## 11: Binding Loops

```
Rectangle {
    width:child.width;
    height:child.height;
    color:"black";

    Image {
        id: child;
        source: "../images/grad.png";
        acnhors.fill: parent;
        anchors.margin: 5
    }
}
```
This code causes a binding loop.
The parent's size depends on child
Child is filling the parent
This leads to a loop

To avoid this, use implicitWidth and implicitHeight instead of width, height in Reactangle
```
implicitWidth:child.implicitWidth;
implicitHeight:child.implicitHeight;
```

## 13: Mouse and Touch Handling

```
MouseArea {
    anchors.fill: parent
    onPressed: parent.color = "green"
    onReleased: parent.color = "black"
}
MouseArea {
    anchors.fill: parent
    onClicked: parent.font.bold = !parent.font.bold
}

```

By default size of mouseArea is 0 so always do `anchors.fill:parent`
`porpagateComposeEvents: true` propagates it to children or overlapping elements

## 15 Keyboard Input

`TextInput` (single iline input) and `TextEdit`  (multi iline input)

```
Rectangle{
    TextInput {
        text: "Field 1";
        focus:true;
        color: activeFocus? "black":"grey";
        activeFocusOnTab: true;
    }
    TextInput {
        text: "Field 2";
        activeFocusOnTab: true;
    }
}
```

`KeyNavigation.right: <id of element>`
`KeyNavigation.left: <id of element>`
`KeyNavigation.top: <id of element>`
`KeyNavigation.bottom: <id of element>`
This helps in moving focus to another element with keyboard

`Keys.onLeftPressed:`
To trigger something in an element after pressing left key

```
Keys.onPressed: {
    if(event.key == Qt.Key.Left)
    {
        Do Something
    }
}
```
To handle any key

Only one element at a time can have active focus

## 16: Custom Components

Create custom properties
`property string product: 'Qt Quick'`
`readonly property string product: 'Qt Quick'`

Place qml code in a file and file name must start with capital letter
eg: LineEdit.qml
```
Rectangle{
    property alias text: TextInput.text;
    clip: true

    TextInput {
        anchors.fill: parent;
        text: "Enter text...";
    }
}
```
Only the properties in the highest element is accessible

In another file, just use it
```
LineEdit {
    text: "Sample Text";
}
```

## 17: Methods and Signals + Declarative

Signals
`signal <name>[<type> <name>,...]`

Handler
`on<name>: `

eg:
```
signal clicked;
onClicked:<>;

signal checked(bool checkValue);
onChecked:<>;
```

```
LineEdit {
    signal sendData(string text);
    onReturnPressed: sendData(text);
}
```
`onSendData` is the handler for this signal

## 21: Loader Element

Makes UI faster
Load only the necessary element when required
Loader element helps for this

```
Loader {
    source: visible? "<file.qml>":""
    visible: false
    active: visible
    anchors.fill: parent
}
```
`active`: loads or unloads element based on its value (true/false)
from a different file

```
Component {
    id: home component
    Item {...}
}

Loader {
    id: homescreen;
    sourceComponent: homeComponent;
}
```
from the same file

`onLoaded` signal handler goes off whenever element is loaded

## 22: FocusScope

Distributing focus between elements
Send focus down to child elements via FocusScope

`FocusScope` will always have focus but not active focus
when it gets active focus it will pass it down to its child element which has `focus:true`

## 29: ListView

```
ListView {
    model: nameModel
    delegate: nameDelegate
    clip: true
}
```
example: 
```
Rectangle {

    ListModel {
        id: nameModel;
        ListElement {name: "1"}
        ListElement {name: "1"}
        ListElement {name: "1"}
        ListElement {name: "1"}
    }

    Component {
        id: nameDelegate
        Text {
            text: model.name
        }
    }

    ListView {
        anchors.fill: parent;
        model: nameModel
        delegate: nameDelegate
    }
}
```

`cacheBuffer` property determines whether delegates are retained outside the visible area of the view.


`cacheBuffer:40`, 40 pixel lines worth of data is retained outside the view of the screen in listview

## 38: Qt Meta Object System

QObject is heart of Qt's object mode
QObject has no visual represention

C++ object have no info on the methods its class has
This is required in Qt

QObject sits on top of class hierarcy in Qt
It adds facilities for 
- Signal, Slots
- Properties
- Event Handling
- Memory Management

Qobjects organize in object trees

QObject (QObject *parent = 0)
- Parent adds object to its list of children
- parent owns children
<br>
Construction
- Tree can be constructed in any order
- Tree can be destructed in any order
    - If object has parent, object is first removed from parent
    - If object has children, each child is deleted first
    - No object is deleted twice.

Parent Child Relationship is not inheritance.
<br>
It is forbidden to copy QObject instances.
Anything that inherits from QObject has to be allocated on heap using `new`
QTimer *timer = new QTimer(parent);

Value Types
- QString
- QStringList
- QColor

Value types are not QObject subclasses
These can be created on stack
```
QString name;
QStringList list;
QColor color;
```

## 39: Signals and Slots (Qt Widgets)

C++ does not have mechanism for objects to communicate with each other
Qt fixed that using Signals and slots

For a singal slot connection
`QObject::connect()`

Signal should be a notification mechanism, you should not look whether it has received or not(not a communication mechanism).

You can have:
- One signal to many slots
- Many signals to one slot
- One signal to another signal

## 40: Connecting Signals to Slots

Three ways to make a signal slot connection:

### Function Pointers
```
connect(const QObject* sender, PointerToMemberFunction signal, 
    const QObject* receiver, PointerToMemberFunction method)
```

Example:
```
QSlider *slider = new QSlider(Qt::Horizontal);
QSpinBox *spin = new QSpinBox;
QObject::connect(slider, &QSlider::valueChanged, spin, &QSpinBox::setValue);
```

### SIGNAL/SLOT Macros
```
connect(const QObject* sender, const char* signal, 
    const QObject* receiver, const char* method)
```

Example: 
```
QSlider *slider = new QSlider(Qt::Horizontal);
QSpinBox *spin = new QSpinBox;
QObject::connect(slider, SIGNAL(valueChanged(int)), spin, SLOT(setValue(int)));
```

NOTE: Not allowed to name the parameters inside the MACROS

### Function Objects (Lambda)

## 42: Custom Signals and Slots (Qt Widgets)

Skipped

## 44: QVariant

union Data {
    int i;
    double d;
    char* name;
}

Q) When to use union?
A) A function where return value can be different

Q) Disadvantages of Union?
A) 

- QVariant is used for common Qt value types
- Supports implicit sharing

```
//For QtCore Types
QVariant variant(42);
int value = variant.toInt();
qDebug() << variant.typeName(); //int

//For NonCor and custom types
QVariant variant = QVariant::fromValue(QColor(Qt::red));
int value = variant.value<QColor>();
qDebug() << variant.typeName(); //QColor
```

## 45: Properties in QML

```
Text {
    text:"Hello World";
}
```

Whenever QML Parser sees the text element, it will instantiate a new object in C++ (QQuickText).
text is converted to a QVariant. (basically any property)


QObject has two helper functions
- `QVariant property(const char* name) const;`
- `void setProperty(const char* name, const QVariant &va;ue);`

In the QQuickText class in C++, you would find code liek this
```
Q_PORPERTY( type name
(READ getFunction [WRITE setFunction] | MEMBER memberName)
(NOTIFY notifySignal | CONSTANT) [FINAL][...])
```

Moc will read this file and setup a table, and will link a property (in this case text) to the appropriate functions like setText, etc

## 46: Exporting Values from C++ to QML

```
QQuickView view;
QQmlContext* context = view.engine()->rootContext();
context->setContextProperty("_aSize", QSize(800,600));
context->setContextProperty("_aBackground", QColor(Qt::lighGray));
```
root conetxt is like the global namespace in qml

```
import QtQuick 2.0

Rectangle {
    width: _aSize.width
    height: _aSize.height
    background: _aBackground
}
```

Gadgets in C++?
They are not QObjects
They can't participate in property bindings
A copy is sent from C++ to QML, QML can even update it. But if you need it in C++, you have to implement a setter

Q_INVOKAABLE - Adding this to the function declaration will allow it to be called from QML.


## 47: Exporting QObjects from C++ to QML

```
class User: public QObject {
    Q_OBJECT
    Q_PROPERTY(QString name READ getName WRITE setName NOTIFY nameChanged);
    Q_PROPERTY(int age READ getAge WRITE setAge NOTIFY ageChanged);

public:
User(constr QString& name, int age);
QString getName() const;
void setName(const QString &name);
    
}
```

```
int main() {
    User* currentUser = new User("Alice", 29);
    QQuickView* view = new QQuickView;
    QQmlContext* context = view->engine.rooContext();
    context->setContextProperty("_currentUser",currentUser);
}
```

What is exported from C++ to QML if we do the above?
- Properties
- Signale
- Slots
- Methods marked with Q_INVOKABLE
- Enums registered with Q_ENUM


## 48: QObject Ownership

QObjects are owned by C++ or JS Engine

Changeable through QQmlEngine::setObjectOwnership()
- QQmlEngine::CppOwnership
- QQmlEngine::JavaScriptOwnership

Automatically chosen based on heuristics
- QObjects created in cpp: Cpp Ownership
- QObjects created in QML: JavaScript Ownership

Excpetion
- Parent-less QObjects returned by Q_INVOKABLE methods: JavaScript Ownership

## 49: Creating new elements from C++

Steps to define a new type in QML:
1. In C++: Subclass either QObject or QQuickItem
2. In C++: Register the type for QML Environment
3. In QML: Import the module containing the new item
4. in QML: Use the item like any other standard item

Step 1: Implementing the element
```
#include <QObject>

class QTimer;
class RandomTimer: public QObject {
    Q_OBJECT
public:
    RandomTimer(QObject* parent = 0);

private:
    QTimer* m_timer;
}
```

Step 2: Registering the element
```
int main(){
    QGUIApplication app(argc, argv);
    qmlRegisterType<RandomTimer>("CustomComponents",1,0,"RandomTimer");

    QQuickView view;
    view.setSource(QUrl("qrc:///main.qml"));
    view.show();
    return app.exec();
}
```
RandomTimer registered as an element in module CustomComponents
RandomTimer automcatically available to the main.qml file

Step 3&4: Importing and using the element
```
import QtQuick 2.0
import CustomComponents 1.0

Rectangle {
    RandomTimer {
        id: random_timer_id
    }
}
```

Q) Why doing composition (having a object QTimer) and not inheritance(inheriting from QTimer) in CPP?
A) Composition is the more eneric way of doing this (creating new components). It is possible to inherit, add new properties, signals, slots, etc, but you can only inheirt from classes that have inherited from QOBject. Sometimes it may be required to make objects avaiable in QML which are not inheriting from QML. In such cases, composition is the go-to approach.

## 50: Creating new GUI Elements from C++

- Painted items (potentially slower)
    - Subclass QQuickPaintedItem
    - Implement paint (...)

(Scene Graph and Raw OpenGL too advanced, skipped)

- Scene Graph items (hardware accelerated)
    - Subclass QQuickItem
    - Iplement updatePaintNode(...)

- Raw OpenGL items
    - Subclass QQuickFrameBufferObject
    - Implement createRenderer(...)

- Similar to non GUI Classes
    - Export object from C++
    - Import and use in QML
    - Properties, signals/slotsm Q_INVOKABLE

```
#include <QQuickPaintedItem>

class EllipseIem: public QQuickPaintedItem {
    Q_OBJECT;
    Q_PROPERTY(QColor color READ color WRITE setColor NOTIFY colorChanged);

public:
    explicit EllipseItem(QQuickItem* parent = nullptr);
    void paint(QPainter* painter) override;
}
```
Implementation of the paint() method in the video
```
qmlRegisterType<EllipseItem>("Shapes", 1, 0, "Ellipse");
```

```
Rectangle {
    Ellipse{ 
        id: custom_item;
    }
}
```

Event handling can be done in C++ side instead of QML
- `QQuickItem::event(QEvent *ev)` is the entry point for events
- Delegates to mousePressEvent(), mouseReleaseEvent(), touchEvent(), etc

## 51: Models Provided from C++

Read-Only List Model
- Inherits from QAbstractListMode
- Reimplements the following
```
int rowCount(const QModelIndex &parent = QModelIndex()) const;
QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const;
```

- Subclass of QAbstractItemModel can be used in QML
- Item roles must be mapped to properties on the C++ side
- Reimplement the roleNames method to add new roles
```
QHash<int, QByteArray> MyModel::roleNames() const
{
    static QHash<int, QByteArray> mapping {
        {NameRole, "name"},
        {FlagRole, "flag"},
        {PopulationRole, "population"}
    };

    return mapping;
}
```
- Mapped roles can be used as properties
```
ListView{ 
    model: myModel,
    delegate: Image {
        source: model.flag
    }
}
```