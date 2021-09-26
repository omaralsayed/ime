#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Email.generated.h"

UCLASS()
class INTERACTIVEMESSAGING_API AEmail : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AEmail();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
