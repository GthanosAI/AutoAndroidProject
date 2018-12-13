from tool.TemplateUtil import template_text


def get_map(key):
    global VIEW_MAP
    VIEW_MAP = {
        'L': layout,
        'i': ImageView,
        't': TextView,
        'R': RecyclerView,
        'l': LinearLayout,
        'r': RelativeLayout,
        'c': ConstrainLayout
    }
    return VIEW_MAP.get(key)


def ImageView(name, scaleType="fitXY"):
    imageview = '''
    <ImageView
            android:id="@+id/${name}"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:scaleType="${scaleType}" />'''

    return template_text(imageview, {
        'name': name,
        "scaleType": scaleType
    })


def TextView(name, textColor="#004c62", textSize="28px"):
    textView = """
    <TextView
                        android:id="@+id/${name}"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:textColor="@{textColor}"
                        android:textSize="@{textSize}"
                        tools:text="demodemo" />
    """

    return template_text(textView, {
        'name': name,
        'textColor': textColor,
        'textSize': textSize
    })


def RecyclerView(name):
    recyclerView = """
     <android.support.v7.widget.RecyclerView
            android:id="@+id/${name}"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"/>
    """

    return template_text(recyclerView, {
        'name': name,
    })


def layout(name, items=[]):
    head = """<?xml version="1.0" encoding="utf-8"?>
    <layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">
    """
    ret = head
    for item in items:
        ret += item

    foot = """
</layout>
    """

    ret += foot
    return ret


def LinearLayout(name, items, orientation="vertical"):
    head = """
    <LinearLayout
            android:id="@+id/${name}"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:orientation="${orientation}">
    """
    foot = """
            </LinearLayout>
        """

    ret = template_text(head, {"name": name, "orientation": orientation})
    for item in items:
        ret += item
    ret += foot
    return ret


def RelativeLayout(name, items):
    head = """
        <RelativeLayout
                android:id="@+id/${name}"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content">
        """
    foot = """
                </RelativeLayout>
            """

    ret = template_text(head, {"name": name})
    for item in items:
        ret += item
    ret += foot
    return ret


def ConstrainLayout(name, items):
    head = """
          <android.support.constraint.ConstraintLayout
            android:id="@+id/${name}"
            android:layout_width="match_parent"
            android:layout_height="match_parent">
        """
    foot = """
                </android.support.constraint.ConstraintLayout>
            """

    ret = template_text(head, {"name": name})
    for item in items:
        ret += item
    ret += foot
    return ret


def make(rule=[], name=""):
    pass


if __name__ == '__main__':
    items = []
    file_name = "fragment_layout.xml"
    title = ImageView("ivTitle")
    back = ImageView("ivBack")
    recycleView = RecyclerView("recyclerView")
    ivOpen = ImageView("ivOpen")
    all = ImageView("ivAll")

    itemsButtons = []
    itemsButtons.append(ivOpen)
    itemsButtons.append(all)
    ll = LinearLayout("llHolder", itemsButtons)

    items.append(title)
    items.append(back)
    items.append(recycleView)
    items.append(back)
    items.append(ll)

    ret = layout(items)

    with open(file_name, 'w') as  tf:
        tf.write(ret)
