using UnrealBuildTool;
using System.Collections.Generic;

public class InteractiveMessagingEditorTarget : TargetRules
{
	public InteractiveMessagingEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V2;

		ExtraModuleNames.AddRange( new string[] { "InteractiveMessaging" } );
	}
}
