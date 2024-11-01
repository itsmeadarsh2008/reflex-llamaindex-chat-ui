"""Reflex custom component LlamaindexChatUi."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/
import reflex as rx
from typing import Any


version = "@llamaindex/chat-ui@0.0.4"

class Button(rx.Component):
    library = version
    tag = "Button"

class Collapsible(rx.Component):
    library = version
    tag = "TextInput"

class CollapsibleContent(rx.Component):
    library = version
    tag = "CollapsibleContent"

class CollapsibleTrigger(rx.Component):
    library = version
    tag = "CollapsibleTrigger"

class Drawer(rx.Component):
    library = version
    tag = "Drawer"

class DrawerClose(rx.Component):
    library = version
    tag = "DrawerClose"

class DrawerContent(rx.Component):
    library = version
    tag = "DrawerContent"

class DrawerDescription(rx.Component):
    library = version
    tag = "DrawerDescription"

class DrawerFooter(rx.Component):
    library = version
    tag = "DrawerFooter"

class DrawerHeader(rx.Component):
    library = version
    tag = "DrawerHeader"

class DrawerOverlay(rx.Component):
    library = version
    tag = "DrawerOverlay"

class DrawerPortal(rx.Component):
    library = version
    tag = "DrawerPortal"

class DrawerTitle(rx.Component):
    library = version
    tag = "DrawerTitle"

class DrawerTrigger(rx.Component):
    library = version
    tag = "DrawerTrigger"

class HoverCard(rx.Component):
    library = version
    tag = "HoverCard"

class HoverCardContent(rx.Component):
    library = version
    tag = "HoverCardContent"

class HoverCardTrigger(rx.Component):
    library = version
    tag = "HoverCardTrigger"

class Input(rx.Component):
    library = version
    tag = "Input"

class Select(rx.Component):
    library = version
    tag = "Select"

class SelectContent(rx.Component):
    library = version
    tag = "SelectContent"

class SelectGroup(rx.Component):
    library = version
    tag = "SelectGroup"

class SelectItem(rx.Component):
    library = version
    tag = "SelectItem"

class SelectLabel(rx.Component):
    library = version
    tag = "SelectLabel"

class SelectScrollDownButton(rx.Component):
    library = version
    tag = "SelectScrollDownButton"

class SelectScrollUpButton(rx.Component):
    library = version
    tag = "SelectScrollUpButton"

class SelectSeparator(rx.Component):
    library = version
    tag = "SelectSeparator"

class SelectTrigger(rx.Component):
    library = version
    tag = "SelectTrigger"

class SelectValue(rx.Component):
    library = version
    tag = "SelectValue"

class Tabs(rx.Component):
    library = version
    tag = "Tabs"

class TabsContent(rx.Component):
    library = version
    tag = "TabsContent"

class TabsList(rx.Component):
    library = version
    tag = "TabsList"

class TabsTrigger(rx.Component):
    library = version
    tag = "TabsTrigger"

class Textarea(rx.Component):
    library = version
    tag = "Textarea"

class ChatInput(rx.Component):
    library = version
    tag = "ChatInput"
    is_default = True

class ChatInputForm(rx.Component):
    library = version
    tag = "ChatInput.Form"

class ChatInputField(rx.Component):
    library = version
    tag = "ChatInput.Field"

class ChatInputUpload(rx.Component):
    library = version
    tag = "ChatInput.Upload"

class ChatInputSubmit(rx.Component):
    library = version
    tag = "ChatInput.Submit"

class PrimiviteChatMessage(rx.Component):
    library = version
    tag = "PrimiviteChatMessage"
    is_default = True

class PrimiviteChatMessageAvatar(rx.Component):
    library = version
    tag = "PrimiviteChatMessage.Avatar"

class PrimiviteChatMessageContent(rx.Component):
    library = version
    tag = "PrimiviteChatMessage.Content"

class PrimiviteChatMessageActions(rx.Component):
    library = version
    tag = "PrimiviteChatMessage.Actions"

class ChatMessages(rx.Component):
    library = version
    tag = "ChatMessages"
    is_default = True

class ChatMessagesList(rx.Component):
    library = version
    tag = "ChatMessages.List"

class ChatMessagesLoading(rx.Component):
    library = version
    tag = "ChatMessages.Loading"

class ChatMessagesActions(rx.Component):
    library = version
    tag = "ChatMessages.Actions"

class ChatSection(rx.Component):
    library = version
    tag = "ChatSection"
    is_default = True
    handler: rx.Var[Any]

# Set value .create to their lowercases class names 
# to be used in the frontend
button = Button.create
collapsible = Collapsible.create
collapsible_content = CollapsibleContent.create
collapsible_trigger = CollapsibleTrigger.create
drawer = Drawer.create
drawer_close = DrawerClose.create
drawer_content = DrawerContent.create
drawer_description = DrawerDescription.create
drawer_footer = DrawerFooter.create
drawer_header = DrawerHeader.create
drawer_overlay = DrawerOverlay.create
drawer_portal = DrawerPortal.create
drawer_title = DrawerTitle.create
drawer_trigger = DrawerTrigger.create
hover_card = HoverCard.create
hover_card_content = HoverCardContent.create
hover_card_trigger = HoverCardTrigger.create
input = Input.create
select = Select.create
select_content = SelectContent.create
select_group = SelectGroup.create
select_item = SelectItem.create
select_label = SelectLabel.create
select_scroll_down_button = SelectScrollDownButton.create
select_scroll_up_button = SelectScrollUpButton.create
select_separator = SelectSeparator.create
select_trigger = SelectTrigger.create
select_value = SelectValue.create
tabs = Tabs.create
tabs_content = TabsContent.create
tabs_list = TabsList.create
tabs_trigger = TabsTrigger.create
textarea = Textarea.create
chat_input = ChatInput.create
chat_input_form = ChatInputForm.create
chat_input_field = ChatInputField.create
chat_input_upload = ChatInputUpload.create
chat_input_submit = ChatInputSubmit.create
primivite_chat_message = PrimiviteChatMessage.create
primivite_chat_message_avatar = PrimiviteChatMessageAvatar.create
primivite_chat_message_content = PrimiviteChatMessageContent.create
primivite_chat_message_actions = PrimiviteChatMessageActions.create
chat_messages = ChatMessages.create
chat_messages_list = ChatMessagesList.create
chat_messages_loading = ChatMessagesLoading.create
chat_messages_actions = ChatMessagesActions.create
chat_section = ChatSection.create