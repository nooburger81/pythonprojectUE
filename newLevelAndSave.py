import unreal

levelTools = unreal.Level
editorLevelLibrary = unreal.EditorLevelLibrary
levelSubsys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

newLevel = "myNewLevel"

myNewLevel = levelSubsys.new_level("/Game/Levels/newLevel")

levelSubsys.set_current_level_by_name(newLevel)

levelSubsys.save_current_level()