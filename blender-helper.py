import bpy

# Global variable to track the clicked object
last_clicked_object = None

# Function to handle the click event
def click_handler(scene, context):
    global last_clicked_object
    
    if not last_clicked_object:
        return
    
    # Get the active object (the one clicked)
    active_object = context.active_object
    
    # Check if the active object is the last clicked object
    if active_object == last_clicked_object and active_object.animation_data:
        # Iterate through the available actions (animations)
        for action in bpy.data.actions:
            # Play the action if it matches the object's name
            if action.name == active_object.name:
                active_object.animation_data.action = action
                break

# Function to set the last clicked object
def set_last_clicked(self, context):
    global last_clicked_object
    if context.active_object:
        last_clicked_object = context.active_object
    else:
        last_clicked_object = None

# Add the click handler to the scene
bpy.app.handlers.scene_update_post.append(click_handler)

# Register the UI panel
def register():
    bpy.types.VIEW3D_PT_tools_object.append(draw_last_clicked)

def unregister():
    bpy.types.VIEW3D_PT_tools_object.remove(draw_last_clicked)

def draw_last_clicked(self, context):
    layout = self.layout
    if last_clicked_object:
        layout.label(text="Last Clicked: " + last_clicked_object.name)
    else:
        layout.label(text="Last Clicked: None")

# Add properties to the scene
bpy.types.Scene.last_clicked_object = bpy.props.PointerProperty(
    type=bpy.types.Object,
    name="Last Clicked Object",
    description="Last object clicked in the 3D view",
    update=set_last_clicked
)

register()
print("Click-to-animate script with last clicked object tracking is active.")
